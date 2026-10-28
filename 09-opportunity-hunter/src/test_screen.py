"""OH-02 screening smoke tests, standard library only."""
import json
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from screen import screen

POLICY = json.loads((Path(__file__).resolve().parent.parent / "config" / "policy.v1.json").read_text(encoding="utf-8"))

class ScreeningTests(unittest.TestCase):
    def base(self, **updates):
        item = dict(site="freelancermap", kind="project", estimated_hours=30,
                    calendar_days=5, net_effective_hourly_rate=6)
        item.update(updates)
        return item

    def test_accepted(self):
        self.assertEqual(screen(self.base(), POLICY)["decision"], "ACCEPT_FOR_REVIEW")

    def test_hours_exceeded(self):
        self.assertEqual(screen(self.base(estimated_hours=101), POLICY)["decision"], "REJECT")

    def test_days_exceeded(self):
        self.assertEqual(screen(self.base(calendar_days=11), POLICY)["decision"], "REJECT")

    def test_low_net_rate(self):
        self.assertEqual(screen(self.base(net_effective_hourly_rate=4), POLICY)["decision"], "REJECT")

    def test_missing_rate(self):
        self.assertEqual(screen(self.base(net_effective_hourly_rate=None), POLICY)["decision"], "HOLD_FOR_REVIEW")

    def test_explicit_incompatibility(self):
        self.assertEqual(screen(self.base(explicit_incompatible=True), POLICY)["decision"], "REJECT")

    def test_unpaid(self):
        self.assertEqual(screen(self.base(unpaid=True), POLICY)["decision"], "REJECT")

    def test_freelancermap_employment(self):
        self.assertEqual(screen(self.base(kind="employment"), POLICY)["decision"], "REJECT")

    def test_linkedin_employment(self):
        self.assertEqual(screen(self.base(site="linkedin", kind="employment"), POLICY)["decision"], "HOLD_FOR_REVIEW")

    def test_unknown_site(self):
        self.assertEqual(screen(self.base(site="unknown"), POLICY)["decision"], "HOLD_FOR_REVIEW")

    def test_iranian_floor_undefined(self):
        p = json.loads(json.dumps(POLICY))
        p["sites"]["iranian_test"] = dict(p["sites"]["iranian_template"], market="IR")
        self.assertEqual(screen(self.base(site="iranian_test"), p)["decision"], "HOLD_FOR_REVIEW")

    def test_invalid_hours(self):
        self.assertEqual(screen(self.base(estimated_hours=-2), POLICY)["decision"], "HOLD_FOR_REVIEW")

if __name__ == "__main__":
    unittest.main(verbosity=2)
