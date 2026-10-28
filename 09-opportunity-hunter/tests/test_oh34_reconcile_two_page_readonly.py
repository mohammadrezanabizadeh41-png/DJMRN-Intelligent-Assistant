"""OH-34 reproducible offline-only tests; no real browser, network or DB access."""
import importlib.util
import json
import pathlib
import sqlite3
import tempfile
import unittest

p = pathlib.Path(__file__).resolve().parent.parent / 'src' / 'oh34_reconcile_two_page_readonly.py'
if not p.exists():
    p = pathlib.Path(__file__).with_name('oh34_reconcile_two_page_readonly.py')
spec = importlib.util.spec_from_file_location('oh34', p)
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)


def fixture(n):
    out = []
    for i in range(22):
        number = n*10000+i
        path = '/project/oh34-test-' + str(number) if i < (6 if n==1 else 8) else '/project/oh34-test-fallback-%d-%d' % (n,i)
        ident = str(number) if i < (6 if n==1 else 8) else 'url:' + path
        out.append(dict(site='freelancermap', external_id=ident, title='Test '+str(number),
                        url='https://www.freelancermap.com'+path))
    return out


class OH34Offline(unittest.TestCase):
    def setUp(self):
        self.folder=tempfile.TemporaryDirectory()
        self.addCleanup(self.folder.cleanup)
        self.root=pathlib.Path(self.folder.name)
        self.page1=fixture(1)
        self.page2=fixture(2)
        self.a=self.root / m.EXPECTED[0][0]
        self.b=self.root / m.EXPECTED[1][0]
        self.db=self.root / 'fixture.sqlite3'
        self.write(self.a,self.page1,m.EXPECTED[0][1])
        self.write(self.b,self.page2,m.EXPECTED[1][1])
        with sqlite3.connect(self.db) as con:
            con.execute('CREATE TABLE metadata (key TEXT, value TEXT)')
            con.execute("INSERT INTO metadata VALUES ('schema_version','djmrn.oh.local.v1')")
            for key in m.EXPECTED_COUNTS:
                con.execute('CREATE TABLE '+key+' (id INTEGER,source_site TEXT,external_id TEXT,title TEXT,canonical_url TEXT)')
            for i in range(44):
                con.execute('INSERT INTO opportunities VALUES (?,?,?,?,?)',(i,'freelancermap',
                    'old'+str(i),'Old '+str(i),'https://www.freelancermap.com/project/old-'+str(i)))
                con.execute('INSERT INTO opportunity_history VALUES (?,NULL,NULL,NULL,NULL)',(i,))
            for i in range(4):
                con.execute('INSERT INTO opportunity_details VALUES (?,NULL,NULL,NULL,NULL)',(i,))

    def write(self,path,rows,size):
        data=json.dumps(dict(schema_version=m.SCHEMA,opportunities=rows))
        self.assertLessEqual(len(data),size)
        path.write_text(data+' '*(size-len(data)),encoding='utf-8')

    def test_valid_22_each(self):
        self.assertEqual(len(m.load_export(self.a,m.EXPECTED[0])),22)
        self.assertEqual(len(m.load_export(self.b,m.EXPECTED[1])),22)

    def test_bad_receipt_size(self):
        self.a.write_bytes(self.a.read_bytes()+b' ')
        with self.assertRaisesRegex(RuntimeError,'SIZE_MISMATCH'):
            m.load_export(self.a,m.EXPECTED[0])

    def test_wrong_site(self):
        self.page1[0]['site']='evil'
        self.write(self.a,self.page1,m.EXPECTED[0][1])
        with self.assertRaisesRegex(RuntimeError,'ROW_SITE_INVALID'):
            m.load_export(self.a,m.EXPECTED[0])

    def test_wrong_hostname(self):
        self.page1[0]['url']='https://notfreelancermap.com/project/oh34-test-10000'
        self.write(self.a,self.page1,m.EXPECTED[0][1])
        with self.assertRaisesRegex(RuntimeError,'INVALID_PROJECT_URL'):
            m.load_export(self.a,m.EXPECTED[0])

    def test_duplicate_in_page(self):
        self.page1[1]=dict(self.page1[0])
        self.write(self.a,self.page1,m.EXPECTED[0][1])
        with self.assertRaisesRegex(RuntimeError,'PAGE_DUPLICATE'):
            m.load_export(self.a,m.EXPECTED[0])

    def test_invalid_numeric_id(self):
        self.page1[0]['external_id']='99999'
        self.write(self.a,self.page1,m.EXPECTED[0][1])
        with self.assertRaisesRegex(RuntimeError,'ROW_NUMERIC_ID_URL_MISMATCH'):
            m.load_export(self.a,m.EXPECTED[0])

    def test_fallback_mismatch(self):
        self.page1[12]['external_id']='url:/project/wrong'
        self.write(self.a,self.page1,m.EXPECTED[0][1])
        with self.assertRaisesRegex(RuntimeError,'ROW_FALLBACK_ID_URL_MISMATCH'):
            m.load_export(self.a,m.EXPECTED[0])

    def test_unique_44(self):
        a=m.load_export(self.a,m.EXPECTED[0])
        b=m.load_export(self.b,m.EXPECTED[1])
        report=m.reconcile(a,b,m.database_rows(self.db))
        self.assertEqual(report['unique_across_two_pages'],44)
        self.assertEqual(report['cross_page_overlaps'],0)

    def test_duplicate_across_pages(self):
        a=m.load_export(self.a,m.EXPECTED[0])
        b=m.load_export(self.b,m.EXPECTED[1])
        b[0]=dict(a[0])
        report=m.reconcile(a,b,m.database_rows(self.db))
        self.assertEqual(report['unique_across_two_pages'],43)

    def test_db_readonly(self):
        before=m.sha256(self.db)
        m.run(self.a,self.b,self.db)
        self.assertEqual(m.sha256(self.db),before)

    def test_db_baseline_drift(self):
        with sqlite3.connect(self.db) as con:
            con.execute('DELETE FROM opportunities WHERE id=0')
        with self.assertRaisesRegex(RuntimeError,'COUNTS_CHANGED'):
            m.database_rows(self.db)

    def test_same_page_fails_closed(self):
        a=m.load_export(self.a,m.EXPECTED[0])
        with self.assertRaisesRegex(RuntimeError,'PAGE_2_HAS_NO_UNIQUE_LISTINGS'):
            m.reconcile(a,a,m.database_rows(self.db))

    def test_cross_page_id_conflict(self):
        a=m.load_export(self.a,m.EXPECTED[0])
        b=m.load_export(self.b,m.EXPECTED[1])
        b[0]['id']=a[0]['id']
        with self.assertRaisesRegex(RuntimeError,'CROSS_PAGE_ID_CONFLICT'):
            m.reconcile(a,b,m.database_rows(self.db))

    def test_local_db_overlap(self):
        a=m.load_export(self.a,m.EXPECTED[0])
        b=m.load_export(self.b,m.EXPECTED[1])
        old=m.database_rows(self.db)
        old[0]=(a[0]['id'],a[0]['title'],a[0]['url'])
        report=m.reconcile(a,b,old)
        self.assertEqual(report['local_db']['SEEN'],1)


if __name__ == '__main__':
    unittest.main(verbosity=2)
