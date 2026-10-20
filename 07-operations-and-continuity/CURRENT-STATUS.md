# DJMRN — CANONICAL CURRENT STATUS (2026-10-20)
**Repo:** `mohammadrezanabizadeh41-png/DJMRN-Intelligent-Assistant` / `main` — exact repo verification is mandatory.  
**For exhaustive handoff read:** [PROJECT-STATE-HANDOFF-20261020.md](PROJECT-STATE-HANDOFF-20261020.md); [rules](../PROJECT-RULES.md); [TASKS](../02-project-management/TASK-REGISTER.md); [DECISIONS](../02-project-management/DECISION-REGISTER.md).

## What's done and adopted
- User-approved D-009: **minimum logical task/permission/result contract → first deterministic useful no-Agent capability; full central RAM manager only after specific workload evidence**. D-004 full P0–P6 roadmap remains a PROPOSAL.
- User-approved D-012: **CAP-006 V0 source + isolated synthetic tests**; Python stdlib (D-011) chosen **only for V0**.
- CAP-006 code under [document_search_v0](../05-assistants-and-capabilities/src/document_search_v0/README.md): user-specified UTF-8 file allowlist, Persian/Arabic normalized lexical matches with source SHA/line. No Agent/LLM/daemon/queue/database/remote connection.
- 16/16 **OFF-DEVICE synthetic tests PASS** in assistant's Python 3.13.5 Linux container [NEW-V0001](../06-tests-and-evidence/logs/NEW-V0001-20261020.md); [source GitHub commit 4d2b9801](https://github.com/mohammadrezanabizadeh41-png/DJMRN-Intelligent-Assistant/commit/4d2b9801e3a985fb34462ee912f89d41363a6115) with verified original code/test blobs. **No tests yet on user's Windows** and no real personal-file usage.
- 01 device historical baseline: Lenovo 81W1 / Ryzen5 3500U / Vega8 / **8GiB physical RAM**, ~5.88GiB OS visible and ~2–3GiB typically free historically, Windows11Pro. See [inventory](../01-system-inventory/hardware-baseline.md); do not request complete D0 again.
- GitHub Work T0001 transport PASS. WQ0001/WA0001 research **verified / ACCEPTED-PARTIAL**, with two misleading internal source SHA receipts identified in [review](../04-work-research-bridge/reviews/WQ0001.md); KB-0010 extracted. D-010 [repo lock](../04-work-research-bridge/REPOSITORY-LOCK.md) applies to all future Work outputs.
- [Project KB INDEX](../08-project-knowledge-base/INDEX.md) has 10 entries and user's [SRC-0001](../08-project-knowledge-base/inbox/SRC-0001-djmrn-assistant-architecture-research-20261020.md) full 607 lines. Notion Applied/General are external research catalogs; no need to copy entire library.

## Exact next action: WINDOWS SYNTHETIC SMOKE
- **User has NOW authorized this bounded synthetic-only Windows test** (2026-10-20), after asking for comprehensive repo handoff first.
- [PowerShell procedure](../05-assistants-and-capabilities/src/document_search_v0/WINDOWS-SMOKE-PROTOCOL.md), package 5 files, ZIP SHA256 `f6228e06b9efc565c971e08f6404e05f8fc9dbc4e625879d420130a9f0026af4`.
- User manually downloads package to Downloads, pastes a non-admin PowerShell block; it checks archive/file SHA, extracts into a fresh folder, invokes existing Python `py -3`/fallback and runs 16 dummy unittest cases + one dummy JSON search.
- **NEW-V0002 USER WINDOWS ATTEMPT BLOCKED before Python:** error `STOP: File hash mismatch: fixtures/sample_alpha.txt`. [Incident receipt](../06-tests-and-evidence/logs/NEW-V0002-20261020.md). Original ZIP and ZIP-contained sample hash match expected in assistant container; **actual extracted file hash unknown**. Next: read-only hash/size diagnostic, no reinstall/overwrite. After screenshot/log, check Windows/Python/result and persist test receipt & CURRENT in GitHub; then consider specifically approved *real non-sensitive* files.

## Not done/not approved
No Windows installation or benchmark, no model/engine/Agent resource manager/UI/remote host, no live website/email/customer data or payments, no Notion modification; no project-wide language or DB selected. PowerShell smoke must not inspect real folders or install software. If Python absent/hash wrong, STOP and report.

**Always:** verify exact repo fullname and HEAD; preserve Work other repository separation, source status and user permissions; update CURRENT/HANDOFF/CHANGELOG with evidence only.

## Latest UPDATE after NEW-V0002 read-only diagnostic (2026-10-20)
- User's PowerShell ZIP and extracted file check returned **4/4 MATCH=True**, correct lengths/hashes and ZIP SHA256, no exception. [Observed evidence](../06-tests-and-evidence/logs/NEW-V0002-20261020.md). The earlier `sample_alpha.txt` discrepancy cause is **UNKNOWN** but current files match; no modifications made.
- **Next now: run existing Python against the already-extracted, checked dummy-file directory** (no new extraction, install or Administrator). Await exact 16-unit-test and CLI console result; do not mark CAP-006 Windows PASS prematurely.
