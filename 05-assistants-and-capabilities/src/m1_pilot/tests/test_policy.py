"""Permission state tests: mock Windows metadata, never use real files."""
import unittest

from core.manifest import ApprovedFile, Manifest
from core.approval import LocalApprovalControl, PermissionDenied


def fake_manifest(revision=1, digest_a="a" * 64):
    return Manifest(revision, "S-1-5-21-1000", (
        ApprovedFile("doc-alpha", "alpha.md", r"C:\Fixtures\alpha.md",
                     digest_a, 123, 101, 1),
        ApprovedFile("doc-beta", "beta.md", r"C:\Fixtures\beta.md",
                     "b" * 64, 234, 101, 2)
    ))


class ApprovalTests(unittest.TestCase):
    def setUp(self):
        self.control = LocalApprovalControl()
        self.manifest = fake_manifest()

    def test_default_no_grant(self):
        with self.assertRaises(PermissionDenied) as ctx:
            self.control.require(self.manifest, "local-connection",
                                 ("doc-alpha",), 1)
        self.assertEqual(ctx.exception.code, "NO_GRANT")

    def test_local_grant_and_revoke(self):
        self.control.grant_by_operator(self.manifest, "local-connection")
        gen = self.control.require(self.manifest, "local-connection",
                                   ("doc-alpha", "doc-beta"), 1)
        self.assertTrue(self.control.still_valid(gen))
        self.control.revoke()
        self.assertFalse(self.control.still_valid(gen))

    def test_third_id_rejected(self):
        self.control.grant_by_operator(self.manifest, "local-connection")
        with self.assertRaises(PermissionDenied):
            self.control.require(self.manifest, "local-connection",
                                 ("doc-third",), 1)

    def test_connection_and_revision_binding(self):
        self.control.grant_by_operator(self.manifest, "local-connection")
        with self.assertRaises(PermissionDenied):
            self.control.require(self.manifest, "other", ("doc-alpha",), 1)
        with self.assertRaises(PermissionDenied):
            self.control.require(self.manifest, "local-connection",
                                 ("doc-alpha",), 2)
        with self.assertRaises(PermissionDenied):
            self.control.require(fake_manifest(revision=1, digest_a="c"*64),
                                 "local-connection", ("doc-alpha",), 1)

    def test_expiration_rejected(self):
        self.control.grant_by_operator(self.manifest, "local-connection", 1)
        grant = self.control._grant  # deliberately test-only direct fixture
        object.__setattr__(grant, "expires_at", -1)
        with self.assertRaises(PermissionDenied) as ctx:
            self.control.require(self.manifest, "local-connection",
                                 ("doc-alpha",), 1)
        self.assertEqual(ctx.exception.code, "EXPIRED")


if __name__ == "__main__":
    unittest.main()
