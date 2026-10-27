# DJMRN P1 synthetic/off-device test report — 2026-10-27

Scope: **Hub standalone Python reference**, test-only local CAP-006 stand-in, no external network or model.

Executed: `python -m unittest discover -q -s .../coordination_hub_p1 -p 'test_*.py'`.

Result: **11 tests PASS** (read-only path; deterministic Persian text matched; SHA receipts checked; unique durable Hub UUID; idempotency and conflict; unknown resource and web capability denied; invalid version/extras rejected; no duplicate execution; SQLite restart/readback; bounded read-only reconcile; retry-limit failure; deleted file failure).

Existing `schemas/hub-record.schema.json` v1.0 was used to validate the JSON emitted by `example_request()`; **PASS** under `jsonschema.Draft202012Validator` on sandbox.

**Critical scope limit:** The offline test sandbox could not fetch the main repository's actual CAP-006 Python file. A temporary stand-in implementing the same Python function signature and synthetic result shape was used exclusively for these unit tests. It is **not** included among files to publish to the GitHub repository. Real CAP-006 test, A2A/MCP/AG-UI conformance, cross-language worker interoperability, Windows execution, file authorization hardening, Crash mid-transaction, genuine remote network retries, model calls, and RAM measurement are **NOT VERIFIED**. No Docker, model, email, accounts or policies modified. An integration run from a complete repo checkout is the required next gate.