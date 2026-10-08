import importlib.util
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

SOURCE = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('installer', SOURCE / 'scripts/project_keeper.py')
installer = importlib.util.module_from_spec(spec)
spec.loader.exec_module(installer)


class InstallerTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        self.repo = self.root / 'repo'
        (self.repo / 'adapters/claude').mkdir(parents=True)
        (self.repo / 'adapters/kiro').mkdir(parents=True)
        self.policy = '# Project Keeper\n\nTest policy.\n'
        (self.repo / 'PROJECT_KEEPER.md').write_text(self.policy)
        (self.repo / 'adapters/claude/CLAUDE.md').write_text(self.policy)
        (self.repo / 'adapters/kiro/project-keeper.md').write_text('---\ninclusion: always\n---\n' + self.policy)
        self.home = self.root / 'home'
        self.home.mkdir()
        self.state_dir = self.root / 'state'
        self.state = {'schema': 1, 'installations': {}}
        self.addCleanup(patch.stopall)
        patch.object(installer, 'ROOT', self.repo).start()
        patch.dict(os.environ, {}, clear=False).start()
        os.environ.pop('CODEX_HOME', None)

    def item(self, name='claude'):
        return next(i for i in installer.candidates(self.home) if i['name'] == name)

    def apply(self, items=None, **kwargs):
        installer.apply_items(items or [self.item()], self.state, self.state_dir, **kwargs)

    def test_discover_and_preview_write_nothing(self):
        self.assertEqual(installer.main(['discover', '--home', str(self.home)]), 0)
        self.apply(dry_run=True)
        self.assertEqual(list(self.home.iterdir()), [])
        self.assertFalse(self.state_dir.exists())

    def test_preserves_unrelated_text_and_permissions_and_backs_up(self):
        path = Path(self.item()['path']); path.parent.mkdir()
        original = 'Existing instruction.\r\nKeep this.\r\n'
        with path.open('w', newline='') as f: f.write(original)
        path.chmod(0o640)
        self.apply()
        self.assertTrue(installer.read(path).startswith(original))
        record = self.state['installations'][str(path)]
        self.assertEqual(installer.read(Path(record['backup'])), original)
        if os.name != 'nt': self.assertEqual(path.stat().st_mode & 0o777, 0o640)
        self.assertEqual(json.loads(installer.read(self.state_dir / 'installations.json'))['schema'], 1)

    def test_repeated_install_is_idempotent(self):
        self.apply(); path=Path(self.item()['path']); first=installer.read(path)
        self.apply()
        self.assertEqual(first, installer.read(path))
        self.assertEqual(first.count(installer.START), 1)
        self.assertFalse((self.state_dir / 'backups').exists())

    def test_update_preserves_edits_outside_managed_block(self):
        self.apply(); path=Path(self.item()['path'])
        path.write_text('New user instruction\n' + installer.read(path) + '\nAnother user instruction')
        (self.repo / 'adapters/claude/CLAUDE.md').write_text(self.policy + 'New rule\n')
        self.apply()
        result=installer.read(path)
        self.assertTrue(result.startswith('New user instruction\n'))
        self.assertTrue(result.endswith('\nAnother user instruction'))
        self.assertIn('New rule', result)

    def test_local_managed_edit_aborts_before_other_target_write(self):
        self.apply(); path=Path(self.item()['path'])
        path.write_text(installer.read(path).replace('Test policy.', 'Local edit.'))
        with self.assertRaisesRegex(ValueError, 'changed locally'):
            self.apply([self.item('kiro'),self.item()])
        self.assertFalse(Path(self.item('kiro')['path']).exists())
        self.assertIn('Local edit.', installer.read(path))

    def test_explicit_manual_adoption(self):
        path=Path(self.item()['path']);path.parent.mkdir();path.write_text(self.policy)
        with self.assertRaisesRegex(ValueError, 'adopt-existing'):self.apply()
        self.apply(adopt=True)
        self.assertEqual(installer.read(path).count('# Project Keeper'),1)
        self.assertIn(installer.START,installer.read(path))

    def test_manual_copy_with_windows_newlines(self):
        path=Path(self.item()['path']);path.parent.mkdir()
        with path.open('w',newline='') as stream:stream.write(self.policy.replace('\n','\r\n'))
        self.apply(adopt=True)
        self.assertEqual(installer.read(path).count('# Project Keeper'),1)

    def test_new_codex_override_blocks_old_registration(self):
        (self.repo/'adapters/codex').mkdir()
        (self.repo/'adapters/codex/AGENTS.md').write_text(self.policy)
        item=self.item('codex');self.apply([item])
        Path(item['path']).with_name('AGENTS.override.md').write_text('New override')
        with self.assertRaisesRegex(ValueError,'override now hides'):self.apply([item])

    def test_unknown_manual_text_is_not_replaced_even_with_adopt(self):
        path=Path(self.item()['path']);path.parent.mkdir();path.write_text(self.policy+'My custom rule')
        with self.assertRaises(ValueError):self.apply(adopt=True)
        self.assertTrue(installer.read(path).endswith('My custom rule'))
        self.assertFalse(self.state_dir.exists())

    def test_marked_adoption_preserves_surrounding_text(self):
        path=Path(self.item()['path']);path.parent.mkdir()
        with path.open('w',newline='') as stream:
            stream.write('Before\n'+installer.START+'\r\n'+self.policy.replace('\n','\r\n')+installer.END+'\nAfter')
        self.apply(adopt=True)
        self.assertTrue(installer.read(path).startswith('Before\n'))
        self.assertTrue(installer.read(path).endswith('\nAfter'))

    def test_malformed_markers_rejected(self):
        path=Path(self.item()['path']);path.parent.mkdir();path.write_text(installer.START+'\nOther text')
        with self.assertRaisesRegex(ValueError, 'marker pair'):self.apply(adopt=True)

    def test_dedicated_file_conflict_and_symlink(self):
        item=self.item('kiro');path=Path(item['path']);path.parent.mkdir(parents=True)
        path.write_text('Unrelated rules')
        with self.assertRaises(ValueError):self.apply([item])
        if os.name != 'nt':
            path.unlink(); destination=self.root/'actual';destination.write_text('Keep')
            path.symlink_to(destination)
            with self.assertRaisesRegex(ValueError,'symbolic link'):self.apply([item])
            self.assertEqual(destination.read_text(),'Keep')

    def test_codex_override_and_explicit_project_path(self):
        (self.home/'.codex').mkdir();(self.home/'.codex/AGENTS.override.md').write_text('Existing override')
        self.assertTrue(self.item('codex')['path'].endswith('AGENTS.override.md'))
        project=self.root/'target';project.mkdir()
        items=installer.candidates(self.home,project)
        self.assertEqual(next(i for i in items if i['name']=='copilot-project')['path'],str(project/'.github/copilot-instructions.md'))

    def test_update_only_registered_paths(self):
        self.apply()
        (self.home/'.kiro').mkdir()
        self.assertEqual(installer.main(['update','--no-pull','--home',str(self.home),'--state-dir',str(self.state_dir)]),0)
        self.assertFalse(Path(self.item('kiro')['path']).exists())


@unittest.skipUnless(shutil.which('git'), 'Git integration tests require Git')
class GitUpdateTests(unittest.TestCase):
    def test_fast_forward_refresh_reexec_and_historical_adoption(self):
        with tempfile.TemporaryDirectory() as temp:
            root=Path(temp); upstream=root/'upstream'; clone=root/'clone'; home=root/'home';home.mkdir()
            upstream.mkdir();shutil.copytree(SOURCE/'scripts',upstream/'scripts',ignore=shutil.ignore_patterns('__pycache__'))
            (upstream/'adapters/claude').mkdir(parents=True)
            old='# Project Keeper\nOld policy\n'
            (upstream/'PROJECT_KEEPER.md').write_text(old)
            (upstream/'adapters/claude/CLAUDE.md').write_text(old)
            env={**os.environ};env.pop('CODEX_HOME',None)
            def cmd(*args,cwd=upstream):
                return subprocess.run(args,cwd=cwd,env=env,text=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,check=True)
            cmd('git','init');cmd('git','config','user.name','Test');cmd('git','config','user.email','test@example.invalid')
            cmd('git','add','.');cmd('git','commit','-m','Initial fixture')
            cmd('git','clone',str(upstream),str(clone),cwd=root)
            path=home/'.claude/CLAUDE.md';path.parent.mkdir();path.write_text(old)
            def cli(*args):
                return cmd(sys.executable,str(clone/'scripts/project_keeper.py'),*args,'--home',str(home),cwd=root)
            cli('install','--targets','claude','--adopt-existing')
            new='# Project Keeper\nNew policy\n'
            (upstream/'PROJECT_KEEPER.md').write_text(new);(upstream/'adapters/claude/CLAUDE.md').write_text(new)
            cmd('git','add','.');cmd('git','commit','-m','Updated fixture')
            cli('update')
            self.assertIn('New policy',path.read_text())
            # Recognize an older exact manual copy from history after updating the clone.
            other=root/'other';(other/'.claude').mkdir(parents=True);(other/'.claude/CLAUDE.md').write_text(old)
            cmd(sys.executable,str(clone/'scripts/project_keeper.py'),'install','--targets','claude','--adopt-existing','--home',str(other),cwd=root)
            self.assertIn('New policy',(other/'.claude/CLAUDE.md').read_text())
            (clone/'untracked.txt').write_text('Do not delete')
            result=subprocess.run([sys.executable,str(clone/'scripts/project_keeper.py'),'update','--home',str(home)],text=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,env=env)
            self.assertNotEqual(result.returncode,0)
            self.assertIn('local changes',result.stderr)
            self.assertEqual((clone/'untracked.txt').read_text(),'Do not delete')


if __name__ == '__main__':
    unittest.main()
