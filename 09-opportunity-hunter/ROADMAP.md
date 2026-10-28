# DJMRN-OH-001 — implementation roadmap
Created 2026-10-28. Goal: deliver a bounded, measurable vertical first, then extend across sites. Estimates are engineering effort, not guarantees.

| Gate | Deliverable | Exit proof | Estimate | Status |
|---|---|---|---:|---|
| OH-00 | Audit existing repo contracts, source, user constraints and integrations | documented reuse map; no duplicate authoritative hub/ledger | 2–4 h | NEXT |
| OH-01 | Versioned policy schema, site profiles for freelancermap/LinkedIn plus IR template, category economics config | valid JSON and override/precedence tests | 3–6 h | TODO |
| OH-02 | Deterministic eligibility and engagement classifier, compact reasons | >=25 tests incl. explicit vs missing restrictions, 100/101h, 10/11d, employment site overrides | 4–8 h | TODO |
| OH-03 | Project fixed/hourly quote and employment effective-hourly evaluator | USD 4.99/5.00 boundary, IR without USD inheritance, fees/hours and no fabricated quote | 6–12 h | TODO |
| OH-04 | SQLite opportunity ledger, source evidence, dedup and state machine | reopen-safe storage, duplicate tests, UNKNOWN_SEND handling | 4–8 h | TODO |
| OH-05 | Ui.Vision read-only integration with one permitted platform | 10 real listings with canonical URLs/full text and RAM snapshot; bridge-to-macro invocation verified | 4–12 h | TODO |
| OH-06 | AGNT/OmniRoute extraction and personalized draft | schema-validated structured results, 429/retry/fallback tests, prompt-injection fixture | 4–10 h | TODO |
| OH-07 | Dry-run submission and reply classification | zero external sends, receipts, quotas, state transitions, positive handoff | 4–8 h | TODO |
| OH-08 | Controlled live pilot, then additional sites | permission checked, approved template and economic floors, one confirmed send/receipt/reply check, rollback | variable | BLOCKED |
| OH-09 | One-click/Task Scheduler operation, monitoring, backup and performance | on-demand run, failure recovery, low-memory measurement, no secrets in repo | variable | TODO |

**Estimated offline/core build (OH-00..OH-04): 19–38 engineering hours.** First integration and dry run (OH-05..OH-07): additional 12–30 hours, site-dependent. Full production not promised in one week. Prior 24–53h rough estimate was preliminary; these expanded gates include persistence and integration explicitly.

## Dependencies
OH-00 -> OH-01 -> OH-02; OH-01 -> OH-03; OH-02 + OH-03 -> OH-04; OH-04 -> OH-05/OH-06 -> OH-07 -> OH-08 -> OH-09. A standalone local test harness may precede Hub adapter; do not block all work on unverified AGNT MCP integration.

## First coding slice after OH-00
- Place code under this folder's future `src/`, tests under `tests/`, site profiles under `config/sites/` (directories materialize when files are created).
- Start with Python standard library `json`, `sqlite3`, `unittest`; no new installer. Implement profile resolver + pure eligibility function before browser actions.
- Create synthetic fixtures: freelancermap monthly job REJECT; LinkedIn monthly job ELIGIBLE_FOR_REVIEW; USD $4.99/h REJECT, $5/h PASS; Iranian toman listing must not inherit USD floor; 101h project REJECT; 11d REJECT; missing nationality nonblocking; explicit on-site-only REJECT; unknown cost -> pricing review.
- Only after local tests pass connect the authorized read-only Ui.Vision pilot.

## Risk register
1. AGNT-to-MCP bridge and macro invocation not yet demonstrated.
2. Ui.Vision per-site DOM changes, authentication, quota and platform restrictions.
3. LLM structured extraction errors, malicious instructions embedded in listings, and provider 429/rate limits.
4. Price market evidence insufficient; unknown fees and scope.
5. User's limited available RAM and Chrome processes; measure actual process peaks.
6. Duplicate or uncertain delivery, privacy of employer/user data, API keys in logs.
7. Per-site Iranian and foreign payment rules and employer negotiation constraints.

## Definition of done
A controlled, user-configured site profile can ingest a permitted listing, deduplicate it, correctly classify and price or flag it, generate a truthful tailored draft, respect permissions/quotas, send only where enabled and allowed, store receipt, track response, and notify user. All acceptance tests and measured RAM must be logged. No autonomous final contract.


## Deployment clarification — Windows-first (2026-10-28)
**Authoritative operational environment: user's Windows 11 PC, NOT GitHub.** Repo holds source, design, reproducible tests and installer instructions. Live SQLite, site sessions, browser state, local logs and secrets remain on Windows. Proposed root `%LOCALAPPDATA%\DJMRN\OpportunityHunter\` is pending local path approval/inventory and has NOT been created.

Insert operational subgates ahead of OH-01/OH-05:
- **OH-W0:** Inspect existing Windows installations, program paths, disk space, user permissions and any DJMRN working roots; avoid duplicate installations.
- **OH-W1:** User confirms local project root/drive; create app/config/data/logs/exports/backups directories locally and record actual paths (do not assume).
- **OH-W2:** Deploy versioned source from GitHub to Windows, create SQLite and local settings, run synthetic tests on the user's machine; no secrets in repo.
- **OH-W3:** Verify local Ui.Vision macro invocation and AGNT/OmniRoute integration using read-only inputs before outbound actions; measure actual RAM and capture receipts.
- **OH-W4:** Implement one-click/Task Scheduler launcher, controlled restart, backup and recovery after safe pilot.

Keep GitHub test fixtures and operational Windows files separate. A GitHub commit is not a Windows installation or working app. First next practical action: local inventory and path selection, not more GitHub-only design.
