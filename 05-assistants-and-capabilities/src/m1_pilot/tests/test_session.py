"""Mocks cannot validate OS reads; they verify the dispatcher never fails open."""
import json
import unittest
from uuid import uuid4
from core.approval import LocalApprovalControl
from core.session import SearchSession
from test_policy import fake_manifest


def call(rid=None, file_ids=None):
    return json.dumps({
        "schema_version": "djmrn.m1.search.v1",
        "request_id": rid or str(uuid4()),
        "operation": "search_approved_documents",
        "manifest_revision": 1,
        "arguments": {"query": "کتاب",
                      "file_ids": ["doc-alpha"] if file_ids is None else file_ids}
    }, ensure_ascii=False)


class SessionTests(unittest.TestCase):
    def test_no_grant_and_no_reads(self):
        session = SearchSession(fake_manifest(), LocalApprovalControl(), "local")
        self.assertEqual(session.dispatch(call())["error"]["code"], "NO_GRANT")

    def test_even_with_mock_grant_os_read_is_blocked(self):
        manifest = fake_manifest()
        permission = LocalApprovalControl()
        permission.grant_by_operator(manifest, "local")
        session = SearchSession(manifest, permission, "local")
        result = session.dispatch(call())
        self.assertEqual(result["status"], "BLOCKED")
        self.assertEqual(result["error"]["code"], "FILE_BOUNDARY_UNPROVEN")
        self.assertEqual(result["matches"], [])

    def test_replay_denied(self):
        manifest = fake_manifest()
        permission = LocalApprovalControl()
        session = SearchSession(manifest, permission, "local")
        rid = str(uuid4())
        session.dispatch(call(rid))
        self.assertEqual(session.dispatch(call(rid))["error"]["code"], "REPLAY")

    def test_third_file_rejected_before_permission(self):
        session = SearchSession(fake_manifest(), LocalApprovalControl(), "local")
        result = session.dispatch(call(file_ids=["doc-alpha", "doc-beta", "doc-third"]))
        self.assertEqual(result["status"], "INVALID")

    def test_closed_session_blocked(self):
        session = SearchSession(fake_manifest(), LocalApprovalControl(), "local")
        session.close()
        self.assertEqual(session.dispatch(call())["error"]["code"], "SESSION_CLOSED")


if __name__ == "__main__":
    unittest.main()
