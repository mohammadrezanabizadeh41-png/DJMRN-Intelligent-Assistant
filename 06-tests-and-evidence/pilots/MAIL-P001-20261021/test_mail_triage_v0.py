"""Synthetic fixture and safety tests, no network or account access."""
import json
import unittest
from pathlib import Path
from mail_triage_v0 import analyze, classify, report_md

ROOT = Path(__file__).resolve().parent
RECORDS = json.loads((ROOT/'synthetic_inbox.json').read_text(encoding='utf-8'))

class SyntheticMailTest(unittest.TestCase):
    def test_expected_labels(self):
        for row in RECORDS:
            with self.subTest(row=row['id']):
                self.assertEqual(classify(row)[0], row['expected_category'])

    def test_untrusted_content_cannot_grant_actions(self):
        flagged=next(r for r in analyze(RECORDS)['observations'] if r['id']=='E12')
        self.assertIn('UNTRUSTED_INSTRUCTION',flagged['flags'])
        self.assertNotIn('send', analyze(RECORDS))

    def test_duplicate_merge_and_portal_priority(self):
        r=analyze(RECORDS)
        self.assertEqual(r['input_count'],26)
        self.assertEqual(r['unique_offers'],22)
        self.assertEqual(r['source_counts'], {'email':20,'portal':6})
        self.assertEqual(next(x for x in r['canonical'] if x['offer_id']=='A18')['selected_source'],'P04')
        self.assertEqual(next(x for x in r['canonical'] if x['offer_id']=='A18')['category'],'BLOCKED_OR_VERIFY')

    def test_budget_from_body_and_portal_not_subject(self):
        r=analyze(RECORDS)
        for key,expected in [('A01',400),('A04',350),('A08',480),('A18',500)]:
            with self.subTest(offer=key):
                selected=next(x for x in r['canonical'] if x['offer_id']==key)
                self.assertEqual(selected['budget']['amount'],expected)
        self.assertIsNone(next(x for x in r['canonical'] if x['offer_id']=='A06')['budget'])

    def test_rejects_non_fixture_url(self):
        rows=[dict(RECORDS[0],url='https://gmail.com/mail/u/0/')]
        with self.assertRaisesRegex(ValueError,'Non-fixture URL'):
            analyze(rows)

    def test_rejects_duplicate_ids(self):
        with self.assertRaisesRegex(ValueError,'Duplicate fixture id'):
            analyze(RECORDS+[RECORDS[0]])

    def test_persian_report_and_no_send(self):
        a=analyze(RECORDS)
        self.assertTrue(a['no_real_account_access'])
        self.assertTrue(a['no_send_capability'])
        text=report_md(a)
        self.assertIn('کاملاً ساختگی',text)
        self.assertIn('P05',text)

if __name__=='__main__':
    unittest.main(verbosity=2)
