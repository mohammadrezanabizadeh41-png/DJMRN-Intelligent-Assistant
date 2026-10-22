"""Pure result mapping checks, no live CAP search and no disk access."""
import unittest
from core.cap006_adapter import map_legacy_result, InvalidLegacyResult
from test_policy import fake_manifest


class CapAdapterTests(unittest.TestCase):
    def good_result(self):
        return {"status": "succeeded", "searched": [
            {"file": "alpha.md", "sha256": "a"*64, "bytes": 123}
        ], "matches": [{"file": "alpha.md", "line": 2,
                        "source_sha256": "a"*64, "text": "كتاب",
                        "match_mode": "normalized"}], "truncated": False}

    def test_pure_map(self):
        out = map_legacy_result(self.good_result(), fake_manifest(), ("doc-alpha",))
        self.assertEqual(out["matches"][0]["file_id"], "doc-alpha")
        self.assertEqual(out["matches"][0]["line"], 2)

    def test_wrong_digest_denied(self):
        source = self.good_result()
        source["searched"][0]["sha256"] = "c"*64
        with self.assertRaises(InvalidLegacyResult):
            map_legacy_result(source, fake_manifest(), ("doc-alpha",))

    def test_unlisted_file_denied(self):
        source = self.good_result()
        source["searched"][0]["file"] = "forbidden-third.md"
        with self.assertRaises(InvalidLegacyResult):
            map_legacy_result(source, fake_manifest(), ("doc-alpha",))


if __name__ == "__main__":
    unittest.main()
