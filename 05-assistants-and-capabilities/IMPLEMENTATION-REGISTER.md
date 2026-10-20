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

## CAP-006 limited real-file gate — 2026-10-21
**VERIFIED-REAL (BOUNDED)** on two user-authorized non-sensitive copied DJMRN Markdown files in Windows 11 / Python 3.14.7. Both Persian queries returned one correct cited line each (charter line 3, resources line 1); independent line search confirmed; pre/post source SHA256 unchanged. [NEW-V0003](../06-tests-and-evidence/logs/NEW-V0003-20261021.md). **NOT OPERATIONAL** / no general host/Agent/LLM. Unicode output is visibly mojibake when the JSON is captured through Windows PowerShell; fix and recheck that presentation. Earlier `TESTED-SYNTHETIC` row is historical and superseded for this narrow capability, not for unverified security/use cases.

## CAP-006 UTF-8 display follow-up — 2026-10-21
The user independently verified readable Persian query and source line after setting session-local PowerShell `[Console]::OutputEncoding` to UTF-8 and `PYTHONIOENCODING=utf-8`: `PERSIAN UTF8 ROUND-TRIP: PASS`, charter line 3. [NEW-V0003](../06-tests-and-evidence/logs/NEW-V0003-20261021.md). Treat this as a **shell-output presentation fix**, not a new Python source version or security/production validation. CAP-006 status: **VERIFIED-REAL (TWO AUTHORIZED PROJECT TEXT FILES) / NOT OPERATIONAL**. No repeated test or new install needed.

## Future multi-persona capability requirement — 2026-10-21
[REQ-MPA-001](../02-project-management/MULTI-PERSONA-SPECIALIST-ASSISTANTS-REQUIREMENT.md) records a **user-requested, deferred, unimplemented** logical specialist-persona environment (with existing CAP-002/003/004/005 specialist goals in view). It **does not assign a new implemented CAP ID** or imply multiple Agents/models/daemons. Raw source [SRC-0004](../08-project-knowledge-base/inbox/SRC-0004-djmrn-multi-persona-logical-assistants-future-20261020.md); future work TASK-0014. Selection/testing requires separate explicit user approval; CAP-006 bounded real search remains current completed test evidence.

## Technology Discovery Radar — future complement to CAP-004 / 2026-10-21
[REQ-TDR-001](../02-project-management/TECHNOLOGY-DISCOVERY-RADAR-REQUIREMENT.md) / [verbatim SRC-0005](../08-project-knowledge-base/inbox/SRC-0005-djmrn-technology-discovery-innovation-radar-future-20261020.md) / `TASK-0015` archive a **deferred future cross-cutting capability** to discover and watch technology signals, distinguish primary verified evidence vs community buzz, filter/deduplicate and hand off curated candidates to existing `CAP-004 Research Curator` and existing Applied/General research procedures. Separate from actual CAP-004 implementation, currently **NONE**, and from still-future REQ-MPA-001/REQ-OBS-001; no second research authority/new CAP implementation ID, workflow daemon, provider, monitoring schedule or deployment. Continue CAP-006 until user reprioritizes.
