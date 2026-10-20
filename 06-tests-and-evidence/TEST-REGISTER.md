# Test Register — historical vs new
| ID | تاریخ | موضوع | وضعیت | اعتماد/فاصلهٔ شاهد |
|---|---|---|---|---|
| HIST-T01 | 2026-10-17 | Python/pip/Git/SQLite CLI smoke | HISTORICAL PASS | user-executed/Journal; not modern stack validation |
| HIST-T02 | 2026-10-17 | Jan Desktop API catalog | HISTORICAL PASS | localhost catalog request; not reliable tool calling |
| HIST-T03 | 2026-10-18 | Gemma 3 1B basic local inference/stream | HISTORICAL PARTIAL PASS | basic model response; not safe Agent proof |
| HIST-T04 | 2026-10-18 | Gemma 3 4B Vulkan/Jinja | HISTORICAL FAIL IN SELECTED CASES | OOM/role template error; later basic direct reply success |
| HIST-T05 | 2026-10-18 | Jan Agent read-only file pilot | HISTORICAL LIMITED PASS | user screenshot/tool reported read + file unchanged hash; sandbox permissions not proven |
| HIST-T06 | 2026-10-19 | P1-A synthetic receipt/dedup/crash | USER-REPORTED PASS / NOT INDEPENDENT FILE AUDIT | 15 accepted +5 duplicates, replay before/after commit; no real agent/account/web |
| NEW-T0001 | 2026-10-20 | GitHub Work transport | **PASS / VERIFIED** | Request/response marker `DJMRN-ASSISTANT-BRIDGE-T0001-20261020-8F31` matched, [response](https://github.com/mohammadrezanabizadeh41-png/DJMRN-Intelligent-Assistant/blob/main/04-work-research-bridge/responses/T0001.md) blob `8094f76e732305fcc8d22a48639cb0e347325874`, [commit](https://github.com/mohammadrezanabizadeh41-png/DJMRN-Intelligent-Assistant/commit/d70a9a406a7057a7b40e11ad99e70d2574536e5c); not a research/agent performance test |
| NEW-P1 | TBD | limited *user-Windows* real smoke and source I/O | **NOT AUTHORIZED / NOT TESTED ON DEVICE** | separate approval with only benign fixtures; do not confuse with synthetic CAP-006 pass |

| NEW-V0001 | 2026-10-20 | CAP-006 no-Agent deterministic text search with synthetic Persian/UTF-8 data | **16/16 PASS / ISOLATED ASSISTANT CONTAINER PYTHON 3.13.5 / TESTED-SYNTHETIC** | [test receipt](logs/NEW-V0001-20261020.md), exact code/fixtures SHA + CLI demo; not Windows/user data or resource benchmark |

**No current Windows benchmark or operational assistant execution was performed during repo setup.** CAP-006 synthetic tests were executed later in an isolated environment; still **no Windows device test**.

| NEW-V0002 | user-authorized 2026-10-20 | CAP-006 synthetic-only Windows smoke | **FIRST USER WINDOWS ATTEMPT BLOCKED: EXTRACTED FIXTURE HASH MISMATCH; PYTHON NOT RUN** | [incident NEW-V0002](logs/NEW-V0002-20261020.md); read-only hash diagnostics of existing extracted file next; do not mark Windows PASS |

**NEW-V0002 update, 2026-10-20:** read-only Windows user PowerShell diagnostic shows ZIP SHA and **all four ZIP-entry/extracted-file SHA256 and byte sizes match (True)**. [Details](logs/NEW-V0002-20261020.md). The first reported SHA mismatch remains unexplained; **Python/unittests/CLI on Windows STILL PENDING**. Status: `INTEGRITY VERIFIED / AWAITING PYTHON TEST RESULTS`.

**NEW-V0002 second attempt (2026-10-20):** original expected-hash PowerShell run again stopped at `STOP: Hash changed: fixtures/sample_alpha.txt` **before Python started**, despite prior direct ZIP/disk comparison 4/4 MATCH. Cause UNKNOWN. Use the [pinned-ZIP-derived hash and safe Python script](../05-assistants-and-capabilities/src/document_search_v0/WINDOWS-SMOKE-VERIFIED-ZIP.ps1); no bypass, install, re-extraction or file deletion. **Windows unit tests still PENDING.**

## Latest evidence superseding older NEW-V0002 pending notes — 2026-10-20
**[NEW-V0002](logs/NEW-V0002-20261020.md): WINDOWS SYNTHETIC SMOKE PASS**, user-provided actual PowerShell result: original ZIP + four file hashes match; Python 3.14.7; `Ran 16 tests in 0.992s — OK (skipped=1)` = **15 pass / 1 skipped (symlink unavailable)**; synthetic search returns 2 correct source-linked matches. Prior `BLOCKED/PENDING` entries above are **earlier attempts only**, not the current result. No real data or production validation.