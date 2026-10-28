"""OH-31 offline-only tests: navigation wrapper CLI parser; no browser or live database."""
import importlib.util
import json
import pathlib
import sqlite3
import tempfile
import unittest
from contextlib import closing

p = pathlib.Path(__file__).resolve().with_name('oh31_cli_onepage_readonly.py')
if not p.exists():
    p = pathlib.Path(__file__).resolve().parent.parent / 'src' / 'oh31_cli_onepage_readonly.py'
spec = importlib.util.spec_from_file_location('oh31_tested', p)
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)


def rows_fixture():
    return [{'site': 'freelancermap', 'external_id': '3066480',
             'title': 'IDAM Infrastructure Engineer',
             'url': 'https://www.freelancermap.com/project/idam-infrastructure-engineer-3066480'},
            {'site': 'freelancermap', 'external_id': 'url:/project/test-engineer-analyst-dv-cleared',
             'title': 'Test Engineer/Analyst - DV Cleared',
             'url': 'https://www.freelancermap.com/project/test-engineer-analyst-dv-cleared'}]


class OH31ReadOnly(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = pathlib.Path(self.temp.name)
        self.export = self.root/'export.json'
        self.db = self.root/'temp.sqlite3'
        with closing(sqlite3.connect(self.db)) as con:
            with con:
                con.execute('CREATE TABLE metadata (key TEXT, value TEXT)')
                con.execute("INSERT INTO metadata VALUES ('schema_version','djmrn.oh.local.v1')")
                for name in m.EXPECTED_COUNTS:
                    con.execute('CREATE TABLE '+name+' (id INTEGER,source_site TEXT, external_id TEXT, title TEXT, canonical_url TEXT)')
                for i in range(44):
                    con.execute('INSERT INTO opportunities VALUES(?,?,?,?,?)', (i, 'freelancermap', 'x'+str(i), 'Title'+str(i), 'https://www.freelancermap.com/project/test-'+str(i)))
                    con.execute('INSERT INTO opportunity_history VALUES (?,NULL,NULL,NULL,NULL)', (i,))
                for i in range(4):
                    con.execute('INSERT INTO opportunity_details VALUES (?,NULL,NULL,NULL,NULL)', (i,))

    def write_export(self, rows):
        self.export.write_text(json.dumps({'schema_version':'djmrn.oh.export.v1','opportunities':rows}), encoding='utf-8')

    def test_valid_offline_export(self):
        self.write_export(rows_fixture())
        self.assertEqual(len(m.validate_export(self.export)), 2)

    def test_reject_wrong_domain(self):
        rows = rows_fixture()
        rows[0]['url'] = 'https://notfreelancermap.com/project/x'
        self.write_export(rows)
        with self.assertRaisesRegex(RuntimeError, 'INVALID_PROJECT_URL'):
            m.validate_export(self.export)

    def test_reject_duplicate(self):
        rows = rows_fixture()
        rows.append(dict(rows[0]))
        self.write_export(rows)
        with self.assertRaisesRegex(RuntimeError, 'DUPLICATE_ID_OR_URL'):
            m.validate_export(self.export)

    def test_reject_empty_rows(self):
        self.write_export([])
        with self.assertRaisesRegex(RuntimeError, 'INVALID_EXPORT_COUNT'):
            m.validate_export(self.export)

    def test_log_success(self):
        log = 'Status=OK\n[status] Playing macro ' + m.MACRO+'\n[status] Finished running DJMRN-OH05-Freelancermap-Export-Pilot, returning to '+m.MACRO+'\n[echo] DJMRN_OH05_EXPORT={"rows":22}\n[info] Macro completed (Runtime 0.8s)\n'
        self.assertTrue(m.validate_log(log))

    def test_log_fail_closed(self):
        for log in ('Status=ERROR\n', 'Status=OK\n[status] Playing macro OTHER\n',
                    'Status=OK\n[status] Playing macro '+m.MACRO+'\n', ''):
            with self.assertRaises(RuntimeError):
                m.validate_log(log)

    def test_log_success_real_browser_storage_parent(self):
        parent = '/macros/' + m.MACRO + '.json'
        log = ('Status=OK\n'
               '[status] Playing macro ' + parent + '\n'
               '[info] Executing:  | open | https://www.freelancermap.com/projects |  | \n'
               "[status] Running 'DJMRN-OH05-Freelancermap-Export-Pilot', called by '" + parent + "'\n"
               '[status] Playing macro DJMRN-OH05-Freelancermap-Export-Pilot\n'
               '[echo] DJMRN_OH05_EXPORT={"rows":22}\n'
               "[status] Finished running 'DJMRN-OH05-Freelancermap-Export-Pilot', returning to '" + parent + "'\n"
               '[status] Playing macro ' + parent + '\n'
               '[info] Macro completed (Runtime 4.38s, 100% local execution, no cloud used)\n')
        self.assertTrue(m.validate_log(log))

    def test_no_acceptance_of_other_macro_path(self):
        log = ('Status=OK\n[status] Playing macro /macros/OTHER.json\n'
               "[status] Finished running 'DJMRN-OH05-Freelancermap-Export-Pilot', returning to '/macros/OTHER.json'\n"
               '[echo] DJMRN_OH05_EXPORT={"rows":22}\n'
               '[info] Macro completed\n')
        with self.assertRaisesRegex(RuntimeError, 'WRONG_MACRO_IN_LOG'):
            m.validate_log(log)

    def test_verify_prior_log_and_json_without_browser(self):
        name = 'DJMRN-OH05-freelancermap-2026-10-28T21-20-30-626Z.json'
        export = self.root / name
        rows = rows_fixture()
        export.write_text(json.dumps({'schema_version':'djmrn.oh.export.v1', 'opportunities':rows}),encoding='utf-8')
        info = {'rows':2,'numeric':1,'fallback':1,'download':name,
                'bytes':export.stat().st_size,'network_actions':0,'database_writes':0}
        parent = '/macros/' + m.MACRO + '.json'
        log = self.root / 'actual-receipt.txt'
        log.write_text('Status=OK\n[status] Playing macro '+parent+'\n'
                       "[status] Finished running 'DJMRN-OH05-Freelancermap-Export-Pilot', returning to '"+parent+"'\n"
                       '[echo] DJMRN_OH05_EXPORT='+json.dumps(info)+'\n'
                       '[info] Macro completed (Runtime 4.38s)\n',encoding='utf-8')
        before = m.sha256(self.db)
        m.verify_existing(log,self.root,self.db)
        self.assertEqual(m.sha256(self.db),before)

    def test_verify_missing_real_export_fail_closed(self):
        parent='/macros/'+m.MACRO+'.json'
        log=self.root/'receipt.txt'
        log.write_text('Status=OK\n[status] Playing macro '+parent+'\n'
                       "[status] Finished running 'DJMRN-OH05-Freelancermap-Export-Pilot', returning to '"+parent+"'\n"
                       '[echo] DJMRN_OH05_EXPORT={"download":"DJMRN-OH05-freelancermap-2026-10-28T21-20-30-626Z.json","rows":22}\n'
                       '[info] Macro completed\n',encoding='utf-8')
        with self.assertRaisesRegex(RuntimeError,'EXPORT_FILE_MISSING_OR_SIZE_CHANGED'):
            m.verify_existing(log,self.root,self.db)

    def test_existing_reconciliation(self):
        rows = rows_fixture()
        old = [('3066480','IDAM Infrastructure Engineer',rows[0]['url'])]
        counts, samples = m.reconcile(rows,old)
        self.assertEqual(counts, {'NEW_TO_LOCAL_DB':1,'SEEN':1,'UPDATED_TITLE':0})
        self.assertEqual(len(samples),1)

    def test_readonly_database_hash_unchanged(self):
        before=m.sha256(self.db)
        old=m.check_database(self.db)
        self.assertEqual(len(old),44)
        self.assertEqual(before,m.sha256(self.db))

    def test_changed_database_fails_closed(self):
        with closing(sqlite3.connect(self.db)) as con:
            with con:
                con.execute('DELETE FROM opportunities WHERE id = 1')
        with self.assertRaisesRegex(RuntimeError, 'DB_BASELINE_CHANGED'):
            m.check_database(self.db)

if __name__ == '__main__':
    unittest.main(verbosity=2)
