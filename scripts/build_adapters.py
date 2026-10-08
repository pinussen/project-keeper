#!/usr/bin/env python3
"""Generate instruction copies from PROJECT_KEEPER.md; never install them."""
import argparse
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PREFIXES = {
    'codex/AGENTS.md': '',
    'claude/CLAUDE.md': '',
    'kiro/project-keeper.md': '---\ninclusion: always\n---\n\n',
    'copilot/copilot-instructions.md': '',
    'copilot/project-keeper.instructions.md': '---\napplyTo: "**"\ndescription: "Manage multi-step projects, plans, work logs and delivery; exempt small standalone tasks."\n---\n\n',
    'openclaw/AGENTS.md': '',
}

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true', help='Check generated files without writing')
    args = parser.parse_args()
    source = (ROOT / 'PROJECT_KEEPER.md').read_text(encoding='utf-8')
    mismatches = []
    for name, prefix in PREFIXES.items():
        path = ROOT / 'adapters' / name
        expected = prefix + source
        if args.check:
            if not path.exists() or path.read_text(encoding='utf-8') != expected:
                mismatches.append(name)
        else:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(expected, encoding='utf-8')
    if mismatches:
        print('Missing or stale adapters: ' + ', '.join(mismatches))
        return 1
    print(f'{len(PREFIXES)} adapters ' + ('verified.' if args.check else 'generated. No app configuration changed.'))
    return 0

if __name__ == '__main__':
    raise SystemExit(main())
