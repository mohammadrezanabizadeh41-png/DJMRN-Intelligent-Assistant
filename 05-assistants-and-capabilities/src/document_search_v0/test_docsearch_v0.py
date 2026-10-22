"""Disposable synthetic tests. Do not touch user's Windows files."""
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

from docsearch_v0 import InputRejected, normalize, search


class V0SearchTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        self.alpha = self.root / "alpha.txt"
        self.beta = self.root / "beta.md"
        self.alpha.write_text("سلام\nاين يك كتاب است.\nمی‌رود تا سند ۱۲ را بخواند.\n", encoding="utf-8")
        self.beta.write_text("گزارش نسخه ١٢\nکتاب و متن\n", encoding="utf-8")

    def test_normalization_arabic_letters(self):
        self.assertEqual(normalize("كـتاب"), "کتاب")
        self.assertEqual(normalize("كتاب"), "کتاب")
        self.assertEqual(normalize("ي ی ى"), "ی ی ی")

    def test_normalization_digits(self):
        self.assertEqual(normalize("۱۲ ١٢ 12"), "12 12 12")

    def test_zwnj_forms(self):
        self.assertEqual(normalize("می‌رود"), normalize("میرود"))
        result = search(self.root, ["alpha.txt"], "می رود")
        self.assertEqual(result["matches"][0]["line"], 3)
        self.assertEqual(result["matches"][0]["match_mode"], "relaxed-whitespace")

    def test_sources_sha_and_line(self):
        before = self.alpha.read_bytes()
        found = search(self.root, ["beta.md", "alpha.txt"], "کتاب")
        self.assertEqual([m["file"] for m in found["matches"]], ["alpha.txt", "beta.md"])
        self.assertEqual(found["matches"][0]["line"], 2)
        self.assertEqual(found["matches"][0]["text"], "اين يك كتاب است.")
        self.assertEqual(found["matches"][0]["source_sha256"], hashlib.sha256(before).hexdigest())
        self.assertEqual(self.alpha.read_bytes(), before)

    def test_deterministic_id_independent_of_order(self):
        a = search(self.root, ["alpha.txt", "beta.md"], "گزارش")
        b = search(self.root, ["beta.md", "alpha.txt"], "گزارش")
        self.assertEqual(a, b)

    def test_no_match_is_success(self):
        result = search(self.root, ["alpha.txt"], "بیابان")
        self.assertEqual(result["status"], "succeeded")
        self.assertEqual(result["matches"], [])

    def test_reject_parent_and_absolute(self):
        for unsafe in ["../bad.txt", "/tmp/a.txt", "..\\bad.txt", "C:\\Secret\\bad.txt", ".\\alpha.txt"]:
            with self.subTest(unsafe=unsafe), self.assertRaises(InputRejected):
                search(self.root, [unsafe], "سلام")

    def test_reject_symlink(self):
        link = self.root / "link.txt"
        try:
            link.symlink_to(self.alpha)
        except (OSError, NotImplementedError):
            self.skipTest("Symbolic links unavailable")
        with self.assertRaises(InputRejected):
            search(self.root, ["link.txt"], "سلام")

    def test_reject_duplicate_files(self):
        with self.assertRaises(InputRejected):
            search(self.root, ["alpha.txt", "alpha.txt"], "سلام")

    def test_reject_missing_file(self):
        with self.assertRaises(InputRejected):
            search(self.root, ["missing.txt"], "سلام")

    def test_reject_binary_utf8(self):
        (self.root / "bad.txt").write_bytes(b"\xff\xfe")
        with self.assertRaises(InputRejected):
            search(self.root, ["bad.txt"], "سلام")

    def test_reject_file_too_large(self):
        (self.root / "big.txt").write_bytes(b"x" * (1024 * 1024 + 1))
        with self.assertRaises(InputRejected):
            search(self.root, ["big.txt"], "x")

    def test_reject_empty_query_and_unsupported_suffix(self):
        for query in ("", "\u200c  "):
            with self.assertRaises(InputRejected):
                search(self.root, ["alpha.txt"], query)
        (self.root / "exec.py").write_text("pass", encoding="utf-8")
        with self.assertRaises(InputRejected):
            search(self.root, ["exec.py"], "pass")

    def test_match_limit(self):
        self.alpha.write_text("نص\n" * 10, encoding="utf-8")
        result = search(self.root, ["alpha.txt"], "نص", limit=3)
        self.assertEqual(result["match_count_returned"], 3)
        self.assertTrue(result["truncated"])

    def test_exact_limit_is_not_truncated(self):
        self.alpha.write_text("نص\n" * 3, encoding="utf-8")
        result = search(self.root, ["alpha.txt"], "نص", limit=3)
        self.assertFalse(result["truncated"])

    def test_cli_success_and_bad_path(self):
        script = str(Path(__file__).with_name("docsearch_v0.py"))
        proc = subprocess.run([sys.executable, script, "--root", str(self.root), "--file", "alpha.txt", "--query", "کتاب"], capture_output=True, text=True, encoding="utf-8")
        self.assertEqual(proc.returncode, 0, proc.stderr)
        obj = json.loads(proc.stdout)
        self.assertEqual(obj["matches"][0]["line"], 2)
        bad = subprocess.run([sys.executable, script, "--root", str(self.root), "--file", "../private.txt", "--query", "کتاب"], capture_output=True, text=True, encoding="utf-8")
        self.assertEqual(bad.returncode, 2)
        self.assertEqual(json.loads(bad.stdout)["status"], "rejected")



    def test_preloaded_bytes_parity_with_legacy_without_second_open(self):
        from unittest.mock import patch
        from docsearch_v0 import search_preloaded_bytes
        original = search(self.root, ["beta.md"], "كتاب", limit=8)
        payload = self.beta.read_bytes()
        with patch.object(Path, "read_bytes", side_effect=AssertionError("NO_FILE_OPEN")):
            new = search_preloaded_bytes([("beta.md", payload)], "كتاب", limit=8)
        for field in ("task_id", "searched", "matches", "truncated",
                      "normalized_query", "match_count_returned", "status"):
            self.assertEqual(new[field], original[field], field)
        self.assertEqual(new["permission_scope"],
                         "caller-supplied-bytes/NOT-OS-authorized")

    def test_preloaded_untrusted_bytes_no_filesystem(self):
        from unittest.mock import patch
        from docsearch_v0 import search_preloaded_bytes
        raw = "اين يك كتاب است.\n".encode("utf-8")
        with patch.object(Path, "read_bytes", side_effect=AssertionError("READ")):
            out = search_preloaded_bytes([("alpha.md", raw)], "کتاب")
        self.assertEqual(out["matches"][0]["line"], 1)
        self.assertEqual(out["matches"][0]["source_sha256"],
                         hashlib.sha256(raw).hexdigest())

    def test_preloaded_fail_closed_inputs(self):
        from docsearch_v0 import search_preloaded_bytes
        variants = (
            [("../bad.md", b"bad")],
            [(r"C:\secret.md", b"bad")],
            [("third.txt", b"bad")],
            [("alpha.md", b"\xff")],
            [("alpha.md", b"a"), ("alpha.md", b"b")],
            [("alpha.md", b"a"), ("beta.md", b"b"), ("gamma.md", b"c")],
            [("alpha.md", "text-not-bytes")],
            [("alpha.md", b"x" * (1024 * 1024 + 1))],
        )
        for candidate in variants:
            with self.subTest(candidate=repr(candidate)[:90]):
                with self.assertRaises(InputRejected):
                    search_preloaded_bytes(candidate, "کتاب")

    def test_preloaded_limit_and_normalization(self):
        from docsearch_v0 import search_preloaded_bytes
        raw = "كتاب\nکتاب\nگزارش ١٢\n".encode("utf-8")
        result = search_preloaded_bytes([("alpha.md", raw)], "كتاب", limit=1)
        self.assertEqual(result["matches"][0]["text"], "كتاب")
        self.assertTrue(result["truncated"])
        digits = search_preloaded_bytes([("alpha.md", raw)], "۱۲")
        self.assertEqual(digits["matches"][0]["line"], 3)
        with self.assertRaises(InputRejected):
            search_preloaded_bytes([("alpha.md", raw)], "کتاب", limit=True)


if __name__ == "__main__":
    unittest.main()
