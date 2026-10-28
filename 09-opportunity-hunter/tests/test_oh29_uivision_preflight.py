"""OH-29 synthetic offline tests. Does not launch Ui.Vision or write live DB."""
import importlib.util
import tempfile
import sqlite3
import pathlib
import unittest
import hashlib

spec = importlib.util.spec_from_file_location('oh29', pathlib.Path(__file__).with_name('oh29_uivision_preflight.py'))
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)


class PreflightTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = pathlib.Path(self.temp.name)
        self.home = self.root / 'user'
        self.local = self.root / 'local'
        self.program = self.root / 'program'
        self.home.mkdir()
        self.local.mkdir()
        self.program.mkdir()
        self.db = self.root / 'opportunities.sqlite3'
        with sqlite3.connect(self.db) as db:
            db.execute('CREATE TABLE metadata (key TEXT, value TEXT)')
            db.execute("INSERT INTO metadata VALUES ('schema_version','djmrn.oh.local.v1')")
            for name in m.EXPECTED_TABLES:
                db.execute(f'CREATE TABLE {name} (id INTEGER)')
            for table, count in (('opportunities',44),('opportunity_history',44),('opportunity_details',4)):
                db.executemany('INSERT INTO '+table+' VALUES (?)', [(i,) for i in range(count)])
        self.env={'USERPROFILE':str(self.home),'LOCALAPPDATA':str(self.local),'PROGRAMFILES':str(self.program),'PROGRAMFILES(X86)':str(self.root / '86'),'PATH':''}
    def checksum(self):
        return hashlib.sha256(self.db.read_bytes()).hexdigest()
    def test_missing_browser_and_page_no_mutations(self):
        before=self.checksum()
        r=m.inspect_local(self.env,self.db)
        self.assertFalse(r['chrome_found'])
        self.assertFalse(r['cli_launch_page_found'])
        self.assertEqual(r['next_gate'],'VERIFY_CHROME_EXECUTABLE')
        self.assertEqual(before,self.checksum())
    def test_chrome_without_page(self):
        chrome=self.program/'Google/Chrome/Application/chrome.exe'
        chrome.parent.mkdir(parents=True)
        chrome.write_bytes(b'fixture')
        r=m.inspect_local(self.env,self.db)
        self.assertTrue(r['chrome_found'])
        self.assertEqual(r['next_gate'],'GENERATE_UIVISION_API_HTML_ONCE')
    def test_launch_page_in_immediate_subfolder(self):
        chrome=self.program/'Google/Chrome/Application/chrome.exe'
        chrome.parent.mkdir(parents=True)
        chrome.write_bytes(b'fixture')
        folder=self.home/'Downloads'/'ui-vision-api'
        folder.mkdir(parents=True)
        (folder/'ui.vision.html').write_text('fixture',encoding='utf-8')
        before=self.checksum()
        r=m.inspect_local(self.env,self.db)
        self.assertEqual(r['next_gate'],'CLI_LAUNCH_SMOKE_PILOT')
        self.assertEqual(len(r['cli_launch_page_paths']),1)
        self.assertFalse(r['cli_run_tested'])
        self.assertEqual(before,self.checksum())
    def test_macro_detection_local_only(self):
        folder=self.home/'uivision'/'macros';folder.mkdir(parents=True)
        name=m.MACRO_NAMES[0]
        (folder/name).write_text('{}',encoding='utf-8')
        r=m.inspect_local(self.env,self.db)
        self.assertEqual(len(r['local_macro_files'][name]),1)
        self.assertEqual(r['macro_in_browser_storage'],'UNVERIFIED')
    def test_changed_db_count_fails_closed(self):
        with sqlite3.connect(self.db) as db:
            db.execute('INSERT INTO opportunities VALUES (100)')
        before=self.checksum()
        with self.assertRaisesRegex(RuntimeError,'DB_COUNTS_CHANGED_REVIEW_REQUIRED'):
            m.inspect_local(self.env,self.db)
        self.assertEqual(before,self.checksum())
    def test_missing_db_fails_closed(self):
        with self.assertRaisesRegex(RuntimeError,'PRODUCTION_DB_MISSING'):
            m.inspect_local(self.env,self.root/'absent.sqlite3')
    def test_unexpected_schema_fails_closed(self):
        with sqlite3.connect(self.db) as db:
            db.execute("UPDATE metadata SET value='broken' WHERE key='schema_version'")
        with self.assertRaisesRegex(RuntimeError,'DB_SCHEMA_UNEXPECTED'):
            m.inspect_local(self.env,self.db)

if __name__=='__main__':
    unittest.main(verbosity=2)
