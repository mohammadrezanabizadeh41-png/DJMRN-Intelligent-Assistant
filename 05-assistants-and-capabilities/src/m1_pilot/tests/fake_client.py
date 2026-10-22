"""Synthetic-only protocol demo: no file reads, model, network or Windows actions.

Optional to run off-device AFTER a separate test approval; not an actual user GUI.
"""
import json
from uuid import uuid4

from core.session import SearchSession
from core.approval import LocalApprovalControl
from test_policy import fake_manifest


def fake_denial_receipt():
    connection = "fake-test-connection"
    manifest = fake_manifest()
    controller = LocalApprovalControl()  # default inactive
    session = SearchSession(manifest, controller, connection)
    request = {"schema_version": "djmrn.m1.search.v1",
               "request_id": str(uuid4()), "operation": "search_approved_documents",
               "manifest_revision": 1,
               "arguments": {"query": "کتاب", "file_ids": ["doc-alpha"]}}
    receipt = session.dispatch(json.dumps(request, ensure_ascii=False))
    assert receipt["status"] == "BLOCKED"
    session.close()
    return receipt


if __name__ == "__main__":
    print(json.dumps(fake_denial_receipt(), ensure_ascii=False, indent=2))
