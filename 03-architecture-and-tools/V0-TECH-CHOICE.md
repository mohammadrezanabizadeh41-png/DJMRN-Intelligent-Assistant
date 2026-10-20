# V0 technology choice — narrow scope, not DJMRN system stack

**Decision date:** 2026-10-20. **User authorization:** sequencing D-009 and source-only V0 approved in the same conversation. **Implementation scope:** only CAP-006 document-search-v0. No other language, model, manager, framework or architecture is adopted.

## Minimal competing approaches considered
| Approach | Pros | Limitation for first V0 | Status |
|---|---|---|---|
| PowerShell built-in `Get-Content` + `Select-String` | Native Windows, no new interpreter; quick basic grep | Handling Arabic/Persian normalization, reproducible machine-readable provenance, encoding behavior across Windows PowerShell 5.1 vs 7.x and test harness need more glue; more brittle than simple pure code for this exact scope | REJECT FOR V0 ONLY / valid fallback |
| **Python standard library CLI** (`pathlib`, `argparse`, `unicodedata`, `hashlib`, `json`, `unittest`) | Small standalone read-only functionality, no third-party dependency or ongoing service; repeatable tests and JSON source receipts | Requires a Python interpreter; **real Windows runtime and footprint not tested** | **SELECTED FOR CAP-006 V0 ONLY** |
| C#/.NET or Go small CLI | Windows-native or single-binary shipping may matter later | Packaging/build toolchain and native API add work before proven V0 benefit; actual RAM/latency not measured | DEFER |
| Off-the-shelf file search / SQLite FTS | Good full-text indexing when many documents need recurring queries | Need scoped Persian normalization, precise source-byte hash and very small manual allowlist; DB/index persistence premature | DEFER UNTIL REPEATED VOLUME/NEED |
| Agent, LLM, inference engine | Might help semantic analysis later | Not needed for deterministic exact/normalized text search; RAM and permissions overhead not justified | NOT NOW |

**Sources, checked as implementation-method guidance 2026-10-20:** [Python argparse](https://docs.python.org/3/library/argparse.html), [Python pathlib](https://docs.python.org/3/library/pathlib.html), [Python Unicode data](https://docs.python.org/3/library/unicodedata.html), [Python unittest](https://docs.python.org/3/library/unittest.html), [PowerShell encoding differences](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_character_encoding) and [Get-Content](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.management/get-content).

## Implementation constraints and exit criteria
- All source explicitly selected, no recursive crawl, no subprocess except synthetic tests, no network, no persistent background worker, no system config changes.
- UTF-8 files only; relative selected paths under a supplied root, reject traversal and symlink/junction; max 20 files, 1MiB each; returned matches max 100.
- V0 uses Unicode NFKC + Persian/Arabic form mapping and relaxed whitespace match only as clearly marked. **This is not Persian morphological/semantic search** and may produce false positives for relaxed matches; original line and SHA are returned for manual confirmation.
- Source is read-only; JSON goes to stdout; no output file or hidden database. CLI `task_id` is a deterministic fingerprint **not a durable run ledger or globally unique execution ID**.
- Stop or change language/tool if real Windows source/encoding tests fail, manual workload expands beyond bounded files, throughput insufficient, or future requirements necessitate a service/UI/index.
- No adoption of Python for the DJMRN host, resource manager or inference engine. Reassess when those needs appear.

**Evidence:** [V0 source](../05-assistants-and-capabilities/src/document_search_v0/README.md), [synthetic test](../06-tests-and-evidence/logs/NEW-V0001-20261020.md), [approved scope](../02-project-management/V0-BUILD-DECISION.md).
