#!/usr/bin/env python3
"""Discover, install and update Project Keeper instructions. Python 3.9+."""
import argparse
import hashlib
import json
import os
from pathlib import Path
import stat
import subprocess
import sys
import tempfile
import uuid
from datetime import datetime, timezone

ROOT = Path(__file__).resolve().parents[1]
START = '<!-- Project Keeper: start -->'
END = '<!-- Project Keeper: end -->'


def digest(text):
    return hashlib.sha256(text.encode('utf-8')).hexdigest()


def read(path):
    # Preserve the original newlines in unrelated content.
    with path.open(encoding='utf-8', newline='') as stream:
        return stream.read()


def git(*args):
    return subprocess.run(['git', '-C', str(ROOT), *args], text=True,
                          stdout=subprocess.PIPE, stderr=subprocess.PIPE)


def version():
    result = git('rev-parse', 'HEAD') if (ROOT / '.git').exists() else None
    commit = result.stdout.strip() if result and result.returncode == 0 else 'local-copy'
    return {'commit': commit, 'policy_sha256': digest(read(ROOT / 'PROJECT_KEEPER.md'))}


def atomic_write(path, text):
    if path.is_symlink():
        raise ValueError(f'Refusing to replace a symbolic link: {path}')
    path.parent.mkdir(parents=True, exist_ok=True)
    mode = stat.S_IMODE(path.stat().st_mode) if path.exists() else 0o600
    fd, temporary = tempfile.mkstemp(prefix='.project-keeper-', dir=str(path.parent))
    try:
        with os.fdopen(fd, 'w', encoding='utf-8', newline='') as stream:
            stream.write(text)
        os.chmod(temporary, mode)
        os.replace(temporary, path)
    finally:
        if os.path.exists(temporary):
            os.unlink(temporary)


def target(name, path, adapter, kind='shared', found=False):
    return dict(name=name, path=str(path.absolute()), adapter=adapter, kind=kind, found=found)


def candidates(home, project=None, workspace=None):
    codex = Path(os.environ.get('CODEX_HOME', str(home / '.codex'))).expanduser()
    override = codex / 'AGENTS.override.md'
    active = override if override.exists() and override.stat().st_size else codex / 'AGENTS.md'
    items = [
        target('claude', home / '.claude/CLAUDE.md', 'claude/CLAUDE.md', found=(home / '.claude').is_dir()),
        target('kiro', home / '.kiro/steering/project-keeper.md', 'kiro/project-keeper.md', 'dedicated', (home / '.kiro').is_dir()),
        target('codex', active, 'codex/AGENTS.md', found=codex.is_dir()),
        target('copilot-global', home / '.copilot/copilot-instructions.md', 'copilot/copilot-instructions.md', found=(home / '.copilot').is_dir()),
    ]
    if project:
        items += [
            target('copilot-project', project / '.github/copilot-instructions.md', 'copilot/copilot-instructions.md', found=True),
            target('cursor', project / '.cursor/rules/project-keeper.mdc', 'cursor/project-keeper.mdc', 'dedicated', (project / '.cursor').is_dir()),
            target('windsurf', project / ('.devin/rules/project-keeper.md' if (project / '.devin').is_dir() else '.windsurf/rules/project-keeper.md'), 'windsurf/project-keeper.md', 'dedicated', (project / '.windsurf').is_dir() or (project / '.devin').is_dir()),
        ]
    if workspace:
        items.append(target('openclaw', workspace / 'AGENTS.md', 'openclaw/AGENTS.md', found=True))
    return items


def load_state(state_dir):
    file = state_dir / 'installations.json'
    if not file.exists():
        return {'schema': 1, 'installations': {}}
    data = json.loads(read(file))
    if data.get('schema') != 1 or not isinstance(data.get('installations'), dict):
        raise ValueError('Unsupported or invalid installation manifest; no changes made.')
    return data


def save_state(state_dir, state):
    atomic_write(state_dir / 'installations.json', json.dumps(state, indent=2) + '\n')


def known_copies(adapter, desired):
    """Recognize exact complete manual copies; never guess where an unmarked block ends."""
    copies = {desired}
    if not (ROOT / '.git').exists():
        return copies
    result = git('log', '-40', '--format=%H', '--', 'adapters/' + adapter)
    if result.returncode == 0:
        for commit in result.stdout.splitlines():
            old = git('show', commit + ':adapters/' + adapter)
            if old.returncode == 0:
                copies.add(old.stdout)
    return copies


def managed_block(text):
    if text.count(START) != 1 or text.count(END) != 1:
        raise ValueError('Expected exactly one complete Project Keeper marker pair.')
    start, end = text.index(START), text.index(END) + len(END)
    if end <= start:
        raise ValueError('Project Keeper markers are out of order.')
    return start, end, text[start:end]


def prepare(item, record, adopt=False):
    path = Path(item['path'])
    if path.is_symlink():
        raise ValueError('Destination is a symbolic link; use the manual guide.')
    if item['name'] == 'codex' and path.name == 'AGENTS.md':
        override = path.with_name('AGENTS.override.md')
        if override.exists() and override.stat().st_size:
            raise ValueError('A Codex override now hides this destination. Review the active file before updating.')
    desired = read(ROOT / 'adapters' / item['adapter'])
    old = read(path) if path.exists() else ''
    if record:
        if not path.exists():
            raise ValueError('Registered destination is missing; inspect before reinstalling.')
        if item['kind'] == 'shared':
            start, end, managed = managed_block(old)
        else:
            managed = old
        if digest(managed) != record['managed_sha256']:
            raise ValueError('Managed instructions changed locally; preserve/reconcile edits before updating.')
    elif old:
        # Unregistered marked sections require explicit adoption, including exact current copies.
        if item['kind'] == 'shared' and (START in old or END in old):
            start, end, managed = managed_block(old)
            body = managed[len(START):-len(END)].strip()
            matches = any(body.replace('\r\n', '\n') == copy.replace('\r\n', '\n').strip()
                          for copy in known_copies(item['adapter'], desired))
            if not adopt or not matches:
                raise ValueError('Unregistered marked block: use --adopt-existing only for an exact known policy copy.')
        elif any(old.replace('\r\n', '\n').strip() == copy.replace('\r\n', '\n').strip()
                 for copy in known_copies(item['adapter'], desired)):
            if not adopt:
                raise ValueError('Exact manual policy copy found. Re-run with --adopt-existing to manage it.')
            if item['kind'] == 'shared':
                start, end = 0, len(old)
        elif item['kind'] == 'dedicated':
            raise ValueError('Dedicated rule file contains unrecognized content; leaving it intact.')
        elif '# Project Keeper' in old or 'PROJECT_KEEPER.md' in old:
            raise ValueError('Possible unmarked policy or import found. Use the manual migration guide; no duplicate added.')
        else:
            start = end = len(old)
    elif item['kind'] == 'shared':
        start = end = 0
    if item['kind'] == 'shared':
        managed = START + '\n' + desired.rstrip('\n') + '\n' + END
        separator = '\n\n' if start == end and old and not old.endswith('\n\n') else ''
        new = old[:start] + separator + managed + old[end:]
        if not old:
            new += '\n'
    else:
        managed = new = desired
    return old, new, digest(managed)


def apply_items(items, state, state_dir, dry_run=False, adopt=False):
    prepared = []
    for item in items:
        record = state['installations'].get(item['path'])
        old, new, fingerprint = prepare(item, record, adopt)
        action = 'unchanged' if old == new else 'write'
        print(f'{action}: {item["name"]} -> {item["path"]}')
        prepared.append((item, old, new, fingerprint))
    # Preflight every destination before writing any of them.
    if dry_run:
        print('Preview only. No files, backups or registration records changed.')
        return
    installed_version = version()
    for item, old, new, fingerprint in prepared:
        path = Path(item['path'])
        exists = path.exists()
        # Recheck just before mutation to avoid overwriting concurrent edits.
        if path.is_symlink() or (read(path) if exists else '') != old:
            raise ValueError(f'Destination changed after preview: {path}')
        backup = None
        if old != new:
            if exists:
                stamp = datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')
                backup = state_dir / 'backups' / (stamp + '-' + uuid.uuid4().hex + '.bak')
                atomic_write(backup, old)
            atomic_write(path, new)
            if read(path) != new:
                raise ValueError(f'Post-write verification failed: {path}')
        state['installations'][item['path']] = {
            **{k: item[k] for k in ('name', 'path', 'adapter', 'kind')},
            'managed_sha256': fingerprint, 'version': installed_version,
            'backup': str(backup) if backup else state['installations'].get(item['path'], {}).get('backup'),
        }
        save_state(state_dir, state)
        if backup:
            print(f'Backup: {backup}')
    print('Saved installation records. Start a new assistant session to load the instructions.')


def refresh():
    if not (ROOT / '.git').exists():
        raise ValueError('Automatic update needs a Git clone. Download a new copy and use update --no-pull instead.')
    clean = git('status', '--porcelain')
    if clean.returncode or clean.stdout.strip():
        raise ValueError('The Project Keeper checkout has local changes. Resolve them before updating, or use --no-pull.')
    branch = git('symbolic-ref', '--quiet', '--short', 'HEAD')
    if branch.returncode:
        raise ValueError('Detached checkout; select the intended branch before updating.')
    result = git('pull', '--ff-only')
    if result.returncode:
        raise ValueError('Could not fast-forward the configured upstream. No installed instructions changed.\n' + result.stderr.strip())
    print(result.stdout.strip(), flush=True)


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('command', choices=['discover', 'install', 'update', 'status'])
    parser.add_argument('--targets', help='Comma-separated names shown by discover; explicitly selects them')
    parser.add_argument('--project', type=Path, help='Target project root; enables project-scoped destinations')
    parser.add_argument('--workspace', type=Path, help='Explicit OpenClaw agent workspace')
    parser.add_argument('--home', type=Path, default=Path.home(), help='Home to inspect (use a temporary directory for tests)')
    parser.add_argument('--state-dir', type=Path, help='Manifest/backups directory; default: HOME/.config/project-keeper')
    parser.add_argument('--dry-run', action='store_true', help='Preview writes; never pulls or modifies files')
    parser.add_argument('--adopt-existing', action='store_true', help='Adopt only exact recognized manual policy copies')
    parser.add_argument('--no-pull', action='store_true', help='Update registered targets from this local copy without fetching')
    args = parser.parse_args(argv)
    home = args.home.expanduser().absolute()
    state_dir = (args.state_dir or home / '.config/project-keeper').expanduser().absolute()
    project = args.project.expanduser().absolute() if args.project else None
    workspace = args.workspace.expanduser().absolute() if args.workspace else None
    for directory in (project, workspace):
        if directory and not directory.is_dir():
            raise ValueError(f'Target directory does not exist: {directory}')
    if args.command != 'install' and (args.targets or args.adopt_existing):
        raise ValueError('--targets and --adopt-existing apply to install only.')
    state = load_state(state_dir)
    if args.command == 'status':
        for record in state['installations'].values():
            try:
                prepare(record, record)
                condition = 'intact'
            except (ValueError, OSError) as exc:
                condition = str(exc)
            print(f'{record["name"]}: {record["path"]}\n  installed: {record["version"]["commit"]}; {condition}')
        if not state['installations']:
            print('No registered installations.')
        return 0
    if args.command == 'update':
        if not state['installations']:
            print('No registered installations. Run install first.')
            return 0
        if not args.no_pull and not args.dry_run:
            refresh()
            # Re-run the possibly updated installer, without pulling a second time.
            return subprocess.call([sys.executable, str(ROOT / 'scripts/project_keeper.py'),
                                    *(argv if argv is not None else sys.argv[1:]), '--no-pull'])
        if args.dry_run and not args.no_pull:
            print('Preview uses the current local version; no Git pull is performed.')
        apply_items(list(state['installations'].values()), state, state_dir, args.dry_run)
        return 0
    options = candidates(home, project, workspace)
    if args.command == 'discover':
        for item in options:
            print(f'{item["name"]}: {"found" if item["found"] else "not detected (explicit install allowed)"} -> {item["path"]}')
        print('Discovery does not prove the tool is installed and changes nothing.')
        return 0
    if args.targets:
        names = args.targets.split(',')
        if len(names) != len(set(names)):
            raise ValueError('Duplicate target names are not allowed.')
        selected = [item for item in options if item['name'] in names]
        missing = set(names) - {item['name'] for item in selected}
        if missing:
            raise ValueError('Unknown/unavailable targets: ' + ', '.join(sorted(missing)) + '. Check --project or --workspace.')
    else:
        found = [item for item in options if item['found']]
        if not found:
            raise ValueError('No destinations detected. Use discover, then explicitly select --targets if appropriate.')
        for index, item in enumerate(found, 1):
            print(f'{index}. {item["name"]}: {item["path"]}')
        if not sys.stdin.isatty():
            raise ValueError('No interactive terminal; use --targets to explicitly select destinations.')
        answer = input('Install into which destinations? Enter numbers separated by commas, or Enter to cancel: ').strip()
        if not answer:
            print('Cancelled; no changes made.')
            return 0
        numbers = [int(part.strip()) for part in answer.split(',')]
        if len(numbers) != len(set(numbers)) or any(n < 1 or n > len(found) for n in numbers):
            raise ValueError('Invalid selection; no changes made.')
        selected = [found[n - 1] for n in numbers]
    apply_items(selected, state, state_dir, args.dry_run, args.adopt_existing)
    return 0


if __name__ == '__main__':
    try:
        raise SystemExit(main())
    except (ValueError, OSError, EOFError, json.JSONDecodeError) as error:
        print(f'Error: {error}', file=sys.stderr)
        raise SystemExit(1)
