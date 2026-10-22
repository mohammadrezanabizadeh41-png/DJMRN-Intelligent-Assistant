"""Off-device pure protocol tests; no files or operating-system permissions."""
import json
import unittest
from uuid import uuid4

from core.contract import ContractError, parse_model_args, parse_envelope


def envelope(**override):
    o = {
        "schema_version": "djmrn.m1.search.v1",
        "operation": "search_approved_documents",
        "manifest_revision": 1,
        "request_id": str(uuid4()),
        "arguments": {"query": "كتاب", "file_ids": ["doc-alpha"]}
    }
    o.update(override)
    return json.dumps(o, ensure_ascii=False)


class ContractTests(unittest.TestCase):
    def test_good_envelope(self):
        parsed = parse_envelope(envelope())
        self.assertEqual(parsed.args.max_matches, 8)

    def test_no_grant_from_model_arguments(self):
        for name in ("root", "path", "command", "approval", "url", "owner_sid"):
            with self.subTest(name=name):
                with self.assertRaises(ContractError):
                    parse_model_args({"query": "کتاب", "file_ids": ["doc-alpha"],
                                      name: True})

    def test_deduplicate_file_ids(self):
        with self.assertRaises(ContractError):
            parse_model_args({"query": "کتاب",
                              "file_ids": ["doc-alpha", "doc-alpha"]})

    def test_third_file_denied_at_schema(self):
        with self.assertRaises(ContractError):
            parse_model_args({"query": "کتاب",
                              "file_ids": ["doc-alpha", "doc-beta", "doc-three"]})

    def test_bool_integer_rejected(self):
        with self.assertRaises(ContractError):
            parse_model_args({"query": "کتاب", "file_ids": ["doc-alpha"],
                              "max_matches": True})

    def test_duplicate_json_key_denied(self):
        with self.assertRaises(ContractError) as ctx:
            parse_envelope(envelope().replace('"manifest_revision": 1',
                                               '"manifest_revision": 1, "manifest_revision": 2'))
        self.assertEqual(ctx.exception.code, "DUPLICATE_JSON_KEY")

    def test_path_like_file_id_denied(self):
        for value in ("../alpha.md", r"C:\alpha.md", "https://x", "foo/bar"):
            with self.subTest(value=value):
                with self.assertRaises(ContractError):
                    parse_model_args({"query": "کتاب", "file_ids": [value]})

    def test_unknown_tool_denied(self):
        with self.assertRaises(ContractError):
            parse_envelope(envelope(operation="execute_shell"))

    def test_invalid_utf8_surrogate_in_query(self):
        with self.assertRaises(ContractError):
            parse_model_args({"query": "a\ud800", "file_ids": ["doc-alpha"]})


if __name__ == "__main__":
    unittest.main()
