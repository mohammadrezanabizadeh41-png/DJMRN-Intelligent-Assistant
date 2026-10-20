# CAP-006 — Option A User-Useful Document Lookup: Minimal Pilot Plan

**Prepared 2026-10-21 | Status: USER SELECTED A; PILOT SCOPED / NOT YET AUTHORIZED TO RUN OR WRITE CODE**

**Owner / location:** main project `mohammadrezanabizadeh41-png/DJMRN-Intelligent-Assistant`, `main`.  
**Tracking:** [TASK-0016](TASK-REGISTER.md), [D-013](DECISION-REGISTER.md), [WQ0002](../04-work-research-bridge/requests/WQ0002.md), [Work response WA0002](../04-work-research-bridge/responses/WA0002.md), [independent review](../04-work-research-bridge/reviews/WQ0002.md).  
**Existing evidence:** [NEW-V0002](../06-tests-and-evidence/logs/NEW-V0002-20261020.md), [NEW-V0003 real-document and UTF-8 evidence](../06-tests-and-evidence/logs/NEW-V0003-20261021.md).

## User's actual choice and approval boundary

- The user explicitly selected **"A"** (next practical use case: simple, Persian-readable, source-grounded CAP-006 document lookup) instead of C two-source official research evidence or B CSV validation. This **selects the direction, not authorization for any new Windows execution, downloaded package, code change, installation, generated file, account/API operation, or security exception**.
- Use the **existing Python standard-library search program**; the code already supports 1–20 exact relative paths via repeated `--file` and presents `contract_version/task_id/status/searched/matches/truncated/error` in JSON. Do **not** re-implement multi-file capability or build a new host/Agent, GUI, FTS/indexer, scheduler, manager, model or database based on this choice.
- Objective: answer one **real, user-chosen literal/normalized keyword need** across a small explicit list of already authorized non-sensitive text files, present results legibly in Persian, identify which source copy and line the user should open and independently check. This is **not** semantic question answering, whole-repository search, "latest" project-state determination, or a claim that the user will automatically have saved time.

## Proposed first bounded setup — reuse old real-document copies, but obtain NEW PILOT APPROVAL

Historical user Windows environment observed during NEW-V0003:
- Installed interpreter: `%LOCALAPPDATA%\Programs\Python\Python314\python.exe` (observed `Python 3.14.7`; bare `python` may resolve to WindowsApps alias).
- Existing extracted package: `%USERPROFILE%\Downloads\DJMRN-CAP006-Windows-Smoke`; locate **exactly one** `docsearch_v0.py` inside that approved existing package, do not fetch an unverified replacement.
- Explicit root: `%USERPROFILE%\Downloads\DJMRN-CAP006-Real-Docs`.
- Explicit filenames, as downloaded (do not rename them, even with flattened/doubled extension):
  1. `02-project-managementPROJECT-CHARTER.md.md`
  2. `03-architecture-and-toolsRESOURCE-MANAGEMENT.md.md`
- The original NEW-V0003 verified both local copies with pre/post SHA256, query `هوشمند` → charter line 3, query `منابع` → resources line 1. These are **historical proofs for those exact separate single-file queries**, not proof of a new cross-file query or a recurring user's information need.
- **Next query:** request a user-relevant keyword/phrase or let the user expressly approve a harmless example `Windows` (present in both historically observed documents). It must be clearly represented as lexical keyword search, not a free-form semantic question. No third document, arbitrary glob or directory scan unless separately authorized.
- **Output default:** terminal only; readable short Persian table with `file / line / original raw text / match_mode / original file SHA256`, number of matches, explicit `truncated` and errors, plus raw source JSON available. **No output file writes, GitHub/Notion upload or copy of customer data** in initial pilot.
- **PowerShell display:** in a temporary block, set `[Console]::OutputEncoding = [System.Text.UTF8Encoding]::new($false)` and `PYTHONIOENCODING=utf-8`; restore previous PowerShell console encoding in a `finally` block and restore any previously-set process env values. User's previous `PERSIAN UTF8 ROUND-TRIP: PASS` is already proven for one source query; do not misrepresent it as a new multi-file pilot result.
- Before execution verify literal root/file existence, no symlink/junction for supplied components (within current non-adversarial scope), known suffix, small sizes (1 MiB per file), non-sensitive content and expected script location; use direct installed interpreter. No system-wide policy, permissions/BIOS/pagefile modification, installation or network request.
- No new model, Agent, inference, Browser, Cloud, Notion catalog write or other deferred REQ-OBS-001/REQ-MPA-001/REQ-TDR-001 action.

## Test gates for the FIRST separately approved user-run pilot

**P0 — user authorizes** the two exact local files and program execution and picks a search phrase. If denied/ambiguous → STOP; document-only scope remains. Historical NEW-V0003 consent to different queries does not authorize an automatically repeated pilot.

**P1 — technical:** one `docsearch_v0.py` from previously verified package; Python 3.14 installed and accessible by absolute path; exactly two named files exist within explicit root; reject symlink, unsupported, inaccessible or oversize input.

**P2 — output and integrity:** run a single **two-file** query using repeated `--file`, only after P0. Check exit code and JSON `status=succeeded`, two entries in `searched`, each source SHA256 agrees with an independent before/after file hash; compare all returned file/line/text locations to actual originals or targeted `Select-String` for suitable literal examples (normalized matches require normalization-aware/manual inspection). Check `truncated`; display Persian text without mojibake; indicate none/invalid/error honestly. File content not modified.

**P3 — actual usability:** user identifies a source-relevant passage via the display and can open/check the cited original line, without the assistant claiming an unearned semantic answer. Record whether bare CLI+simple PowerShell formatting is sufficient or a small persistent one-click wrapper would materially help; **do not build a wrapper unless there is an observed need and new explicit user approval**.

**P4 — fail/rollback:** on rejection, mismatch, stale/changed SHA, surprising output, broken UTF-8 or 0 useful results, stop and label accurately; do not alter/delete documents or silently rerun with broader paths. With stdout-only there is no generated artifact to undo; restore temporary encoding settings. If the current CLI already satisfies user experience, **the correct next build may be NONE**, not mandatory feature creep.

**Review:** user supplies PowerShell console output. Coordinator evaluates and records a *new* bounded pilot log if run, separately from historic NEW-V0003 (do not falsify passing results in advance).

## Next user-facing authorization question

"برای مرحلهٔ A، اجازه می‌دهی **فقط یک جست‌وجوی دستی و فقط‌خواندنی** با Python موجود روی همین **دو کپی غیرحساس قبلی** انجام دهیم و نتیجه را در PowerShell به‌صورت فارسی خوانا ببینیم؟ به‌صورت پیش‌فرض عبارت `Windows` را استفاده می‌کنیم؛ اگر عبارت دیگری مدنظر داری، همان را بگو. هیچ نصب یا تغییری در فایل‌ها انجام نمی‌شود."

**Status at plan creation:** **NO USER APPROVAL TO RUN RECEIVED; NO PILOT EXECUTED; NO CODE IMPLEMENTED.** This file is a proposal/fixture for fresh approval, not a passed test.

## 2026-10-21 USER APPROVAL UPDATE — bounded pilot now authorized, not yet run

**User explicitly replied «بله» to the exact preceding consent question.** This authorizes **one manually user-executed read-only pilot** using the **two already approved non-sensitive Windows downloaded Markdown copies**, **query `Windows`**, existing Python 3.14.7 interpreter and existing extracted CAP-006 `docsearch_v0.py` program. Scope: ONE call with two explicit `--file` arguments; stdout-only human-readable Persian original lines, line numbers, file names and source SHA256; independent before/after SHA256 validation; PowerShell session-only temporary UTF-8 output encoding with restoration. No installation, network/cloud/API, account, GitHub/Notion write from test, saved report, original-file modifications, new dependency, elevated permissions, script changes or broader filesystem traversal approved.

**Execution status: AUTHORIZED / NOT YET EXECUTED; awaiting user PowerShell console output.** This consent supersedes prior "not authorized to run" statements *for precisely this narrow one-off run only*. All other tests, code changes and future tasks still require separate authorization.

## 2026-10-21 EXECUTION UPDATE — actual user Windows two-file technical PASS; daily usefulness OPEN

The user subsequently executed the exact approved PowerShell block once and supplied the real console output. **The planned pilot has now run**; prior "NOT YET EXECUTED" lines above are **historical pre-execution states**, not current facts.

Actual stdout: Python **3.14.7**, query `Windows`, `status=succeeded`, **2 searched files**, **4 results**: `02-project-managementPROJECT-CHARTER.md.md` line 3 (1) and `03-architecture-and-toolsRESOURCE-MANAGEMENT.md.md` lines 1, 5, 8 (3). All results had `match_mode=normalized`; an independent `Select-String -SimpleMatch -CaseSensitive -Encoding UTF8` source comparison checked file, exact line and original text and per-hit SHA; original pre/post SHA256 unchanged:
- Charter: `EC5B75577768F12285B8FCEFD6E1E827CC977F676763F052715882DDE2D2D180`.
- Resource-management: `71C41C864C251C2A027DFDED24112296821E706612BDA0733582F689DAD0D066`.

PowerShell displayed original Persian text legibly. Final banner explicitly: `TECHNICAL VALIDATION: PASS` and `Independent line and SHA256 checks passed.` The user output ended `User-value evaluation is still pending.` The standalone evidence and limitations are [NEW-V0004](../06-tests-and-evidence/logs/NEW-V0004-20261021.md) (created and GitHub readback-verified, commit `eba223fac1ed24ecf5bafb065ae211d30b341786`, blob `f341687509ef819d196d32a8c4241193b049ef03`).

**Current verdict: TWO-FILE PRACTICAL-LOOKUP TECHNICAL PILOT PASS / USER DAILY WORKFLOW & UX ACCEPTANCE PENDING.** No broader corpus/semantic/Agent/performance/Windows security proof and no approval to build wrapper or run new pilot. Next ask whether the output is personally useful and whether current manual PowerShell is good enough. A wrapper is optional only after a demonstrated user need and separately approved scope.

## USER UX CORRECTION — 2026-10-21 (supersedes earlier CLI/wrapper UX proposal)
After the [NEW-V0004 technical pilot](../06-tests-and-evidence/logs/NEW-V0004-20261021.md), the user expressly explained they ran PowerShell **only for the technical experiment**. **Manual shell commands are NOT an acceptable ordinary-use UX**, even if shortened to one line; the end-user experience must be **message-based assistant collaboration**, with future automated task handling and authorized manager Agents. The prior suggestion to select between long/short CLI and a simple GUI was a mismatch with the user's goal, **not a pending question to repeat**.

The correct meaning of **Option A:** CAP-006 is the *first proven background capability*, not a finished user-facing assistant. User's goal also includes capabilities B and C as composable functions, not three separate manual applications or obligatory sequential stages. See core [REQ-012](CHAT-FIRST-ASSISTANT-INTERACTION-REQUIREMENT.md), adopted user UX directive [D-014](DECISION-REGISTER.md), scoped integration research/design [TASK-0017](TASK-REGISTER.md).

**Next meaningful acceptance is not another PowerShell query**: one authorized natural-language message → actual tool invocation from an assistant/chat UI → reliable cited Persian answer + clear failure/approval. The exact interface and trusted Windows bridge/runtime need technology-neutral design and fresh explicit approval before any development, installation or network access. Keep the prior numerical/hash PASS intact, but UX/user-value status for conversational use is **NOT BUILT / NOT VERIFIED**. Do not label CAP-006 operational on the basis of a standalone shell script.
