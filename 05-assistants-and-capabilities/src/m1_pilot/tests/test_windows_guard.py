"""Pure fail-closed guard tests; these are NOT actual Windows negative tests."""
import unittest
from core.windows_guard import WindowsGuardHold, require_verified_read


class GuardHoldTests(unittest.TestCase):
    def test_unguarded_cap_reads_never_allowed(self):
        with self.assertRaises(WindowsGuardHold) as ctx:
            require_verified_read("simulated-valid-path")
        self.assertEqual(ctx.exception.code, "FILE_BOUNDARY_UNPROVEN")

    def test_cannot_bypass_with_flag(self):
        with self.assertRaises(WindowsGuardHold):
            require_verified_read(verified=True, path=r"C:\Fixtures\alpha.md")

    @unittest.skip("G3 NOT AUTHORIZED: no actual Windows link/race/locking tests")
    def test_windows_reparse_hardlink_rename(self):
        raise AssertionError("run only after explicit G3 approval")


if __name__ == "__main__":
    unittest.main()
