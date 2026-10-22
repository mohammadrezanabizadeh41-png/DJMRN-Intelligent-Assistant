"""Test the G3B opt-in harness using no real Win32 or personal files."""
from __future__ import annotations
import contextlib
import hashlib
import io
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch
import g3b_synthetic_probe as mod

class ProbeHarnessOfflineTests(unittest.TestCase):
    def test_01_default_no_run(self):
        with contextlib.redirect_stdout(io.StringIO()) as s:
            self.assertEqual(mod.main([]), 0)
        self.assertIn("PLAN ONLY", s.getvalue())

    def test_02_optin_does_not_run_off_windows(self):
        with patch.object(mod.sys,"platform","linux"), contextlib.redirect_stdout(io.StringIO()) as s:
            self.assertEqual(mod.main(["--run-synthetic"]), 2)
        self.assertIn("WINDOWS_ONLY", s.getvalue())

    def test_03_git_blob_math(self):
        self.assertEqual(mod.git_blob_id(b"a"), hashlib.sha1(b"blob 1\0a").hexdigest())

    def test_04_valid_pins(self):
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            (root/"one.py").write_bytes(b"one")
            with patch.object(mod,"PINNED",{"one.py":mod.git_blob_id(b"one")}):
                mod.verify_pinned_sources(root)

    def test_05_bad_pin_denied(self):
        with tempfile.TemporaryDirectory() as d:
            root=Path(d); (root/"one.py").write_bytes(b"other")
            with patch.object(mod,"PINNED",{"one.py":mod.git_blob_id(b"one")}):
                with self.assertRaisesRegex(mod.ProbeHold,"SOURCE_BLOB_MISMATCH"):
                    mod.verify_pinned_sources(root)

    def test_06_pre_revocation(self):
        gate=mod.DeliveryFence(); gate.revoke(); called=[]
        with self.assertRaisesRegex(mod.ProbeHold,"REVOKED_BEFORE_READ"):
            gate.call(lambda: called.append(1))
        self.assertFalse(called)

    def test_07_revocation_during_callback(self):
        gate=mod.DeliveryFence()
        def fake_read(): gate.revoke(); return b"secret"
        with self.assertRaisesRegex(mod.ProbeHold,"REVOKED_BEFORE_DELIVERY"):
            gate.call(fake_read)

    def test_08_no_revoke_accepted_test_only(self):
        self.assertEqual(mod.DeliveryFence().call(lambda: b"fixture"),b"fixture")

    def test_09_network_audit_blocked(self):
        with self.assertRaisesRegex(mod.ProbeHold,"PYTHON_NETWORK_OR_PROCESS_DENIED"):
            mod.no_network_audit("socket.connect",())

    def test_10_process_audit_blocked(self):
        with self.assertRaisesRegex(mod.ProbeHold,"PYTHON_NETWORK_OR_PROCESS_DENIED"):
            mod.no_network_audit("subprocess.Popen",())

    def test_11_unrelated_audit_allowed(self):
        self.assertIsNone(mod.no_network_audit("open",()))

    def test_12_cleanup_two_fixtures(self):
        with tempfile.TemporaryDirectory() as parent:
            folder=Path(parent)/"fixture"; folder.mkdir()
            paths=[folder/"alpha.md",folder/"beta.md"]
            for p in paths: p.write_bytes(b"synthetic")
            self.assertEqual(mod.fixture_cleanup(folder,paths),"OWN_FIXTURES_REMOVED")
            self.assertFalse(folder.exists())

    def test_13_cleanup_refuses_symlinks(self):
        with tempfile.TemporaryDirectory() as parent:
            root=Path(parent)
            folder=root/"fixture";folder.mkdir()
            (root/"target.txt").write_bytes(b"safe")
            symlink=folder/"alpha.md"
            symlink.symlink_to(root/"target.txt")
            self.assertEqual(mod.fixture_cleanup(folder,[symlink]),"MANUAL_CLEANUP_REQUIRED")
            self.assertEqual((root/"target.txt").read_bytes(),b"safe")

    def test_14_no_fixture_cleanup_is_noop(self):
        self.assertEqual(mod.fixture_cleanup(None,[]),"NO_FIXTURE_CREATED")

    def test_15_uses_only_two_fixture_names(self):
        import ast
        tree=ast.parse(Path(mod.__file__).read_text(encoding="utf-8"))
        self.assertTrue(any(isinstance(n,ast.FunctionDef) and n.name=="execute_synthetic" for n in tree.body))
        s=Path(mod.__file__).read_text(encoding="utf-8")
        self.assertIn('folder / "alpha.md", folder / "beta.md"',s)
        self.assertNotIn("shutil.rmtree",s)
        self.assertNotIn("os.symlink(",s)

    def test_16_cleanup_refuses_unexpected_filename(self):
        with tempfile.TemporaryDirectory() as d:
            folder=Path(d)/"fixture";folder.mkdir()
            third=folder/"third.md";third.write_bytes(b"fake")
            self.assertEqual(mod.fixture_cleanup(folder,[third]),"MANUAL_CLEANUP_REQUIRED")
            self.assertTrue(third.is_file())

    def test_17_cleanup_refuses_symlinked_directory(self):
        with tempfile.TemporaryDirectory() as d:
            actual=Path(d)/"actual";actual.mkdir()
            linked=Path(d)/"linked";linked.symlink_to(actual,target_is_directory=True)
            self.assertEqual(mod.fixture_cleanup(linked,[]),"MANUAL_CLEANUP_REQUIRED")
            self.assertTrue(actual.exists())

    def test_18_verify_source_does_not_run_device(self):
        with patch.object(mod,'verify_pinned_sources') as verify, contextlib.redirect_stdout(io.StringIO()) as s:
            self.assertEqual(mod.main(["--verify-source"]),0)
        verify.assert_called_once()
        self.assertIn("SOURCE PREFLIGHT PASS",s.getvalue())

    def test_19_verify_source_bad_pin_holds(self):
        with patch.object(mod,'verify_pinned_sources',side_effect=mod.ProbeHold('SOURCE_BLOB_MISMATCH')), contextlib.redirect_stdout(io.StringIO()) as s:
            self.assertEqual(mod.main(["--verify-source"]),2)
        self.assertIn("HOLD",s.getvalue())

if __name__ == "__main__": unittest.main()
