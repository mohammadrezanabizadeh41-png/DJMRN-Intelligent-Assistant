# Capability/Implementation Register — 2026-10-20 INITIAL
| Capability | هدف | Status | Implemented artifact | Observation |
|---|---|---|---|---|
| CAP-001 | کنترل منابع Windows و نوبت‌دهی | RESEARCH CANDIDATE | **NONE** | مقایسه ابزار آماده / lightweight controller؛ صرفاً پژوهش Applied A0011 |
| CAP-002 | همیار فارسی اسناد و پژوهش | FUTURE BROADER ASSISTANT | **NONE as an Agent** | CAP-006 is a standalone no-Agent subcapability, not a full document assistant |
| CAP-003 | Freelance web-platform copilot | FUTURE | **NONE** | email notification ≠ full website message؛ authorized platform reply+receipt approval |
| CAP-004 | Research Curator | FUTURE | **NONE** | source provenance, independent official research, draft/approval for catalog |
| CAP-005 | code/data/media specialists | FUTURE | **NONE** | اول تأیید نیاز؛ shared host ممکن، multiple agent servers اجباری نیست |

| CAP-006 | جست‌وجوی مجاز و محدود اسناد محلی با تطبیق فارسی، خط و SHA256 | **TESTED-SYNTHETIC / NOT VERIFIED ON USER WINDOWS** | [V0 source](src/document_search_v0/README.md), Python stdlib / no third-party, [test NEW-V0001](../06-tests-and-evidence/logs/NEW-V0001-20261020.md) | approved D-012 for repo+off-device; no Agent/LLM/index/server/real deployment |

**قانون ثبت اجرا:** capability ID → I/O → ownership & authorization → tool/engine/model/host version + installation status → source commit → command to reproduce (sanitize) → test result + resources + safe rollback → integration contract → security review → user approval → deployment/use → monitoring.
هر خطای test، نصب، config، crash و recovery باید در TEST-REGISTER نیز cross-link شود. `OPERATIONAL` فقط وقتی value واقعی و durability مشاهده شد.

## CAP-006 stage update (2026-10-20)
**SCOPED WINDOWS SYNTHETIC SMOKE PASS** (user-reported console, [NEW-V0002](../06-tests-and-evidence/logs/NEW-V0002-20261020.md)): Python 3.14.7, archive and 4 extracted SHA matching, 15 successful unit tests and 1 skipped symlink case, 2 correct synthetic Persian search matches with file/line/SHA. This **does not** qualify as `OPERATIONAL` on real work or justify an Agent/LLM/central manager. Next gate: user-consented non-sensitive real-file read-only assessment; Windows symlink behavior remains untested.