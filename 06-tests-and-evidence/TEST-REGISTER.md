# Test Register — historical vs new
| ID | تاریخ | موضوع | وضعیت | اعتماد/فاصلهٔ شاهد |
|---|---|---|---|---|
| HIST-T01 | 2026-10-17 | Python/pip/Git/SQLite CLI smoke | HISTORICAL PASS | user-executed/Journal; not modern stack validation |
| HIST-T02 | 2026-10-17 | Jan Desktop API catalog | HISTORICAL PASS | localhost catalog request; not reliable tool calling |
| HIST-T03 | 2026-10-18 | Gemma 3 1B basic local inference/stream | HISTORICAL PARTIAL PASS | basic model response; not safe Agent proof |
| HIST-T04 | 2026-10-18 | Gemma 3 4B Vulkan/Jinja | HISTORICAL FAIL IN SELECTED CASES | OOM/role template error; later basic direct reply success |
| HIST-T05 | 2026-10-18 | Jan Agent read-only file pilot | HISTORICAL LIMITED PASS | user screenshot/tool reported read + file unchanged hash; sandbox permissions not proven |
| HIST-T06 | 2026-10-19 | P1-A synthetic receipt/dedup/crash | USER-REPORTED PASS / NOT INDEPENDENT FILE AUDIT | 15 accepted +5 duplicates, replay before/after commit; no real agent/account/web |
| NEW-T0001 | TBD | GitHub Work transport | READY NOT EXECUTED | Work reply none; no success claim |
| NEW-P1 | TBD | minimal real I/O | NOT AUTHORIZED | first use case + acceptance needed |

**No current Windows benchmark or operational assistant execution was performed during repo setup.**
