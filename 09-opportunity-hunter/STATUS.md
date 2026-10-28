# DJMRN-OH-001 — live vertical status
Date: 2026-10-28
Overall: PROJECT SPACE CREATED / ROADMAP DOCUMENTED / NO CODE IMPLEMENTED
Current gate: **OH-00 — repo reuse and contract audit**.
Next exact action: inspect `coordination_hub_p1/hub_p1.py`, its tests, JSON coordination contracts and current Task Register IDs. Produce a small reuse map and then start OH-01 site-profile resolver with synthetic tests.
Completed today: requirements consolidated in original architecture document; new dedicated project README, policy, roadmap and status files created.
Not completed: no actual browser macro invocation, no real listing extraction, no project eligibility code, no pricing calculator, no live send or reply watcher.
User approvals still needed for domestic pricing floor, employment pay floor, outreach message and notification, and each live site capability.
Status update rule: only change a gate to DONE after evidence, tests and readback. Keep project-specific status here and link to global registers; avoid conflicting authoritative states.


## 2026-10-28 15:59:36 Windows OH-W0 read-only inventory — USER-REPORTED, NOT INDEPENDENTLY VERIFIED
- Windows user local appdata: `C:\Users\Mrn7206\AppData\Local`; user profile: `C:\Users\Mrn7206`.
- C: free space: **134.58 GB**; no other filesystem PSDrive shown.
- Commands found: python WindowsApps alias, `py` at Python Launcher, Node `C:\Program Files\nodejs\node.exe`, npm, Git and VS Code.
- Running process groups (WorkingSet64 sum): AGNT 10 processes / 687.9 MB; Chrome 14 / 1524.9 MB; OmniRoute 5 / 565.2 MB; Ui.Vision Desktop 5 / 267.8 MB. Total **3045.8 MB**, not whole-system RAM.
- Existing directory `%LOCALAPPDATA%\DJMRN` = TRUE; Documents\DJMRN, profile\DJMRN, C:\DJMRN and D:\DJMRN = FALSE.
- **Next action**: inspect contents of existing `%LOCALAPPDATA%\DJMRN` without mutation; verify `py --version` and optionally check active install locations. Only then approve and create `%LOCALAPPDATA%\DJMRN\OpportunityHunter`.
- **OH-W0 status:** initial inventory RECEIVED; full installation/path audit still IN PROGRESS. No local OpportunityHunter directory or executable verified created. Do not treat a GitHub commit as Windows deployment.


## 2026-10-28 — OH-W0 follow-up verified from user PowerShell output
Read-only first-level enumeration of `C:\Users\Mrn7206\AppData\Local\DJMRN` reported directories: `agent-foundation`, `Bifrost`, `Downloads`. `py --version` = Python 3.14.7. `Test-Path %LOCALAPPDATA%\DJMRN\OpportunityHunter` = False.
**Decision:** use sibling `%LOCALAPPDATA%\DJMRN\OpportunityHunter` as the proposed Windows operational root; do not modify existing sibling directories. **OH-W0 inventory complete for path selection; OH-W1 creation command prepared, execution awaiting user output.** No directory creation has yet been verified.


## 2026-10-28 — OH-W1 WINDOWS DIRECTORY CREATION: PASS (user PowerShell evidence)
User executed the approved local PowerShell setup and reported:
- `PROJECT_ROOT=C:\Users\Mrn7206\AppData\Local\DJMRN\OpportunityHunter`
- Created immediate directories: `app`, `backups`, `config`, `data`, `exports`, `logs`.
- `DIRECTORY_COUNT=6`
- `OH_W1_RESULT=CREATED`
**Status:** OH-W1 COMPLETE on user Windows per console output. No executable, configuration, SQLite database, automation, or live integrations have yet been installed or tested. Next OH-W2: audit existing hub interfaces and prepare a minimal versioned local bootstrap/test, then execute on Windows and record receipts. Do not confuse source commits with local deployment.


## OH-W2 initial implementation (2026-10-28)
- Inspected `05-assistants-and-capabilities/src/coordination_hub_p1/README.md` and `hub_p1.py`: P1 is a synthetic-only in-process CAP-006 reference, not a production coordinator, and cannot yet execute Opportunity Hunter.
- Committed and read-back verified `09-opportunity-hunter/src/bootstrap.py` at commit `ac2b59592937785b106eb43f38fcf5757cd222e2`; Python stdlib only, no browser, network or send. Creates local `data/opportunities.sqlite3`, metadata version, deduplicated opportunity table and quick-check; refuses missing directories and mismatched schema version.
- Supplied user a PowerShell download/install and run command pinned to commit; **Windows execution result PENDING USER OUTPUT**. No claim of local SQLite success yet.
- Follow-up after local PASS: add tests for bootstrap repeatability/duplicate rejection, then versioned site policies and deterministic screening.


## OH-W2 Windows bootstrap execution receipt — PASS (user console, 2026-10-28)
- Installed `app/bootstrap.py` from pinned commit `ac2b59592937785b106eb43f38fcf5757cd222e2` at `C:\Users\Mrn7206\AppData\Local\DJMRN\OpportunityHunter\app\bootstrap.py`.
- File length **2342 bytes**; reported SHA256 `9D6C3A02E676CCB696991119C8CAC63FC3A9A88147598FAE86B28AFF517BCF2F`.
- `py -I bootstrap.py --root ...` returned `result=PASS`, `schema_version=djmrn.oh.local.v0`, `sqlite_quick_check=ok`, `opportunities=0`, `outbound_actions=0`.
- SQLite file reported at `data/opportunities.sqlite3`. `OH_W2_BOOTSTRAP_COMMAND=COMPLETED`.
- **OH-W2 initial deployment PASS**, not full OH-W2 acceptance until persistence/dedup tests. No site or model integration tested; no external messages sent.


## OH-W2 SQLite read-only validation — PASS (user PowerShell receipt)
- `PRAGMA integrity_check` = `ok`.
- `metadata.schema_version` = `djmrn.oh.local.v0`.
- `opportunities` row count = 0.
- `PRAGMA index_list(opportunities)` = `[(0, 'sqlite_autoindex_opportunities_1', 1, 'u', 0)]`: unique index exists.
- `OH_W2_READONLY_CHECK=COMPLETE`.
**Interpretation:** actual Windows database integrity/schema/unique index verified. This is NOT yet an insert/dedup or reopen-persistence test. Next: isolated temporary SQLite synthetic insert/reopen/duplicate test without modifying operational database.


## OH-W2 synthetic SQLite test — PARTIAL PASS / CLEANUP FAIL (user Windows receipt)
- Synthetic temporary SQLite: `REOPEN_PERSISTENCE=PASS`, `DUPLICATE_REJECTION=PASS`, `FINAL_SYNTHETIC_COUNT=1`.
- Then `tempfile.TemporaryDirectory` cleanup raised `PermissionError [WinError 32]` deleting `synthetic-test.sqlite3`; thus `OH_W2_SYNTHETIC_TEST=PASS` was **not** printed and end-to-end test is NOT PASS.
- Root cause in supplied test script: `with sqlite3.connect(...) as db` commits/rolls back but does not close connection. On Windows open file handle blocks temporary directory deletion.
- Corrective action: explicit `db.close()` in `finally` or `contextlib.closing` around connection, then rerun; separately verify cleanup. Do not claim operational DB was modified by this synthetic test. No real DB write in script.


## OH-W2 corrected synthetic SQLite test — FULL PASS (user Windows receipt)
- `REOPEN_PERSISTENCE=PASS`
- `DUPLICATE_REJECTION=PASS`
- `FINAL_SYNTHETIC_COUNT=1`
- `TEMP_CLEANUP=PASS`
- `REAL_DATABASE_MODIFIED=NO`
- `OH_W2_SYNTHETIC_TEST=PASS`
Correction used `contextlib.closing(sqlite3.connect(...))` for both test connections; Windows temporary file handles released before cleanup. **OH-W2 local bootstrap and synthetic persistence/dedup smoke gate COMPLETE**. Scope: isolated synthetic DB and real operational DB integrity check; not yet production opportunity ingestion or site integration. Next OH-01 policy configuration and OH-02 deterministic filtering.


## OH-01 configuration started
Committed and readback parsed `09-opportunity-hunter/config/policy.v1.json` (schema `djmrn.oh.policy.v1`), commit `9aa947de908ba93212fb9ae9f71339e9ffefeb3e`. Contains INTL $5/hour independent-project floor, IR floor null, 100h/10d project bounds, freelancermap employment denied, LinkedIn employment allowed, IR template pending, and SEND disabled for all. **Status: GitHub source ready; Windows local deployment and resolver/tests pending.**

## OH-01 Windows test PASS
User PowerShell output: OH_01_POLICY_VALIDATION=PASS; SITE_PROFILES=freelancermap,linkedin,iranian_template; AUTOMATIC_SEND=DISABLED. Local policy installed in OpportunityHunter/config/policy.v1.json. Initial deployment verified; advanced override tests pending.

## OH-02 deterministic screening source prepared
Created src/screen.py commit b5abcaa2f1c75e67959b2220f6892912bf1b7224 and src/test_screen.py commit 75e6d2092a4c4bf7b7e02f769a4deedace143f1e. 12 unit tests authored, not yet executed on Windows. No site connections, sends or real opportunity ingestion. OH-02 pending Windows download, test output, and verification.

## OH-02 Windows unit-test receipt — PASS
User installed app/screen.py SHA256 5697B4198AFB69AEAA63AF55CA59E6AD30CC0F8CD203948FACCE3C54F4349BA6 and app/test_screen.py SHA256 755C5134A305C01385D26BA197514931381F79DBD7E609DAFF96358F05395B2F. Python unit tests: Ran 12 tests in 0.003s, OK, OH_02_WINDOWS_TESTS=PASS. Scope: deterministic synthetic unit tests only; no live-site read, external send, production ingestion, or integration acceptance. Next: CLI sample inputs and edge-case hardening.

## OH-02 CLI Windows BOM failure and patch
Windows CLI synthetic sample execution FAILED before screening first sample: json.decoder.JSONDecodeError Unexpected UTF-8 BOM in PowerShell Set-Content -Encoding utf8 output. Unit tests 12/12 previously passed, but did not cover BOM input. Fixed src/screen.py input decoding to utf-8-sig at commit 7e41c2f2a10d326cb79f7fde12c75dfeb0eb50eb. Windows patch deployment and 3-case CLI rerun PENDING; do not mark CLI pass.

## OH-02 CLI BOM patch Windows retest PASS
Windows patch installed: app/screen.py SHA256 7F2DBE5CEE460C359863602F1A3898CE916EBD7386825D13F06013C3494DACA7. Three synthetic CLI scenarios matched: ACCEPT_FOR_REVIEW, REJECT, HOLD_FOR_REVIEW. Receipt OH_02_CLI_RETEST=PASS. Combined with earlier 12/12 unit tests, OH-02 initial deterministic screening gate PASS. Still no real listings or browser integration.

## OH-03 initial Windows calculator test — PASS
User installed app/quote.py from pinned commit 04763eeec30d31ca07441abd715fdd66f9f1766c and ran JSON CLI test. Result CALCULATED, USD, net_amount 250.00, net_effective_hourly_rate 6.25, effective_hours 40, outbound_actions 0; OH_03_INITIAL_TEST=PASS. This is one happy-path test only; invalid/missing costs and screening integration still pending.

## OH-03 Windows edge-case receipt — PASS
User executed five quote.py CLI cases: LOW_RATE CALCULATED (2.00 USD/h); MISSING_COST HOLD_FOR_REVIEW; ZERO_HOURS HOLD_FOR_REVIEW; INVALID_FEE (150%) HOLD_FOR_REVIEW; IRANIAN_PROJECT CALCULATED (62500.00 TOMAN/h). Output OH_03_EDGE_TESTS=PASS. Combined with earlier happy path, calculator has six verified Windows scenarios. Calculator-to-screen integration still pending; Iranian rate floor remains unset.

## OH-03 Windows integration test failure and import fix
User attempted integrated CLI test; first GOOD case failed before evaluation: ModuleNotFoundError: No module named 'quote' from evaluate.py when invoked via py -I. Cause: Python isolated mode excludes script directory from sys.path. Patch in src/evaluate.py adds resolved application script directory to sys.path before importing quote and screen, commit d70cf1155b3f10deb61091b0615944b921856f9d. Windows deployment/retest PENDING; do not claim integration PASS.

## OH-03 integrated Windows retest — PASS
User installed patched app/evaluate.py (SHA256 2A4D0601C7C49BFD3F3F7BC4906C633888C5BBDBB539D44019F43DD1832D9299). Three CLI cases: GOOD ACCEPT_FOR_REVIEW, LOW REJECT, UNKNOWN HOLD_FOR_REVIEW, all matched; OH_03_INTEGRATION_RETEST=PASS. OH-03 initial calculator+screen integration verified on Windows using synthetic inputs. No live sites or outbound actions. Next OH-04 durable opportunity ledger with safe idempotent upsert and tests.

## OH-04 initial Windows synthetic test — IMPORT FAILURE
User downloaded ledger.py and test_ledger.py successfully, but `py -I test_ledger.py` failed before any database operations with ModuleNotFoundError: No module named 'ledger'. Root cause Python isolated mode omits script directory from import path. Patched test_ledger.py to add its own resolved directory to sys.path, commit 8ebe2e2977a0e6af7dbee6a883c2cfbbbc0dc2d9. Windows retest pending; OH-04 NOT PASS. Test only references temporary database, not operational DB.

## OH-04 Windows retest partial logic PASS, cleanup FAIL
User test output: NEW/SEEN/UPDATED, final count 1, REAL_DATABASE_MODIFIED=NO; then TemporaryDirectory cleanup failed with Windows WinError 32 on open SQLite file. Therefore full OH-04 gate remains FAIL/PENDING. Cause: sqlite3 connection context manager does not close handle. Both ledger.py and test_ledger.py patched to use contextlib.closing with transaction context, commits 3553f5a944b950a3893f42105535480ac13f89ce and fbfebbe27bf1da065ba3e3a72065a1289c35ad48. Windows retest pending.

## OH-04 Windows synthetic ledger full retest — PASS
User updated ledger.py SHA256 D796014B3ED5369CEB05867BB320B3989BAD91BA5AB3C6CDEDBF589F6E9AEE22 and test_ledger.py SHA256 B135F00BCBC5F6BEC84A3DD7D1B5C22A4D1E64719C87ECE8DB623259F5CF4FBC. Reported OH_04_SYNTHETIC_LEDGER_TEST=PASS, EVENTS=NEW,SEEN,UPDATED, FINAL_COUNT=1, REAL_DATABASE_MODIFIED=NO, OH_04_FULL_RETEST=PASS. Synthetic basic dedup gate passed including Windows cleanup. Full OH-04 state history, delivery-state preservation and operational DB integration remain pending.

## OH-04 history synthetic prototype prepared
Added src/ledger_history.py commit 583183d7bd303f76e58ee69159684f31c1a03ee9 and src/test_ledger_history.py commit 4381ed9846140f831cf26227c5afcbe5b3f11aa5. Tests designed for NEW/SEEN/UPDATED, history NEW+UPDATED, preserve SENT status, single record, temporary DB. NOT YET RUN ON WINDOWS. Important: prototype writes ledger update and history in separate transactions; not atomic, must harden before operational DB use. Do not migrate real DB yet.

## OH-04 history Windows synthetic test — PASS
User ran test_ledger_history.py: OH_04_HISTORY_SYNTHETIC=PASS; STATUS_PRESERVED=SENT; HISTORY_EVENTS=NEW,UPDATED; FINAL_COUNT=1; REAL_DATABASE_MODIFIED=NO; OH_04_HISTORY_TEST_COMMAND=COMPLETED. This validates happy-path synthetic history and status preservation, NOT atomicity or failure recovery. Operational DB unchanged. Next implement atomic single-transaction history and rollback test.

## OH-04 atomic rollback Windows synthetic test — PASS
User output: OH_04_ATOMIC_ROLLBACK=PASS; STATUS_PRESERVED=SENT; HISTORY_EVENTS=NEW,UPDATED; FINAL_COUNT=1; REAL_DATABASE_MODIFIED=NO; OH_04_ATOMIC_TEST_COMMAND=COMPLETED. This verifies injected history insert failure rolls back opportunity title change in synthetic SQLite DB. Does not establish operational DB schema compatibility or authorize migration. Next: read-only operational schema inspection and explicit backup/migration plan.

## OH-04 operational migration verified by Windows output
User reported SCHEMA_VERSION=djmrn.oh.local.v1, OPPORTUNITIES=0, HISTORY_ROWS=0, INTEGRITY=ok, OH_04_MIGRATION=PASS. Pre-migration backup previously validated. Next test engine against temporary SQLite copy, without modifying live database.

## OH-04 COMPLETED — Windows v1 compatibility verified
User reported OH_04_V1_COMPATIBILITY=PASS; EVENTS=NEW,SEEN,UPDATED; HISTORY=NEW,UPDATED; TEST_COPY_RECORDS=1; REAL_DATABASE_MODIFIED=NO; TEMPORARY_COPY_CLEANUP=PASS. Test used a temporary SQLite backup copy of operational v1 database, not the live DB. Prior gates: synthetic dedup, status preservation, injected failure rollback, operational v1 migration and integrity passed. OH-04 baseline completed. OH-05 site ingestion/read-only adapter remains pending; no live website actions or outbound messages authorized.

## OH-05 sample JSON parse test passed
Windows output confirmed OH_05_SAMPLE_PARSE=PASS, NORMALIZED_RECORDS=2, UNIQUE_RECORDS=2, NETWORK_ACTIONS=0, REAL_DATABASE_MODIFIED=NO. This was inline Python on a synthetic Freelancermap sample, not a reusable ingest module. Next: offline parser with validation and synthetic tests.

## OH-05 offline validator code ready; Windows test pending
Created src/ingest.py commit 4407dd6a7d49940486a7ebffc67bb1ed68845f21 and src/test_ingest.py commit 94588fc06e6e24ab012614532cbdd045203b7aa4. Validation: Freelancermap only, required ID/title, HTTPS URL, duplicate IDs, max 1000 entries. No network or DB writes. NOT YET TESTED ON WINDOWS.

## OH-05 Windows offline validation — PASS
User output: OH_05_VALIDATION=PASS, NORMALIZED_RECORDS=2, INVALID_CASES_REJECTED=5, NETWORK_ACTIONS=0, REAL_DATABASE_MODIFIED=NO, OH_05_VALIDATION_COMMAND=COMPLETED. Offline Freelancermap import validator passed. Next: validate ingest-to-ledger integration on temporary copy of operational v1 database.

## OH-05 Windows ingest-to-ledger integration — PASS
User output: OH_05_LEDGER_INTEGRATION=PASS; EVENTS=NEW,SEEN,UPDATED; HISTORY_ROWS=3; FINAL_COUNT=2; STATUS_PRESERVED=SENT; REAL_DATABASE_MODIFIED=NO; TEMP_COPY_CLEANUP=PASS; OH_05_INTEGRATION_COMMAND=COMPLETED. Test used temporary SQLite copy of operational v1 database. Live website ingestion not yet tested; no outbound messages.

## OH-05 Freelancermap real page structure — visual inspection only
User screenshots show project detail overlay at /projects?id=3066230. Visible: ID 3066230, title IT Cost Optimisation/Cost-Out Specialist, employer Dns Info Ltd, London UK, On-site, Freelance, publication displayed 2026-10-28 17:33, description and skills, and application form requiring email, UK work qualification, CV, name, telephone, availability, salary expectation. Budget and duration not visible. This is visual evidence only; selectors and automated extraction remain UNVERIFIED. No application submitted. Prior synthetic ledger integration PASS.

## OH-05 Freelancermap URL variants observed
User Chrome Console evidence: 22 loaded title anchors; 12 URLs end with numeric project IDs; 10 URLs have descriptive slugs only, e.g. /project/middleware-weblogic-lead-developer. The 10 are not extraction errors. Proposed fallback is namespaced URL-path key (not an official site ID), with collision/URL-change risk and explicit provenance. No production DB import or automatic messaging yet. Next: browser-side read-only validation of all 22 unique keys.

## OH-05 real browser DOM identity pilot — PASS (read-only)
User screenshot confirms DJMRN_TOTAL=22, DJMRN_UNIQUE=22, DJMRN_NUMERIC=12, DJMRN_FALLBACK=10 for loaded Freelancermap project title anchors. 931 is UI total search results, NOT number scanned. Fallback keys are URL-path-derived and are NOT official IDs; slug changes may cause duplicates. No real database writes or applications. Next: persist read-only extraction format, test identity collision/slug-change behavior, then controlled import.

## OH-05 Ui.Vision macro download — Windows verified
User PowerShell output: OH_05_MACRO_DOWNLOAD=PASS; file C:\Users\Mrn7206\AppData\Local\DJMRN\OpportunityHunter\exports\DJMRN-OH05-Freelancermap-ReadOnly-Pilot.json; COMMANDS=2. JSON downloaded and parsed; macro import and execution NOT YET TESTED. No SQLite changes reported.

## OH-05 Ui.Vision first execution
User screenshot: imported macro visible, executeScript and echo both green, Ui.Vision displays '[info] Macro completed (Runtime 0.69s...)'. Execution completed without reported error. Extracted record counts not yet verified from log; awaiting log screenshot. No claim of SQLite import.

## OH-05 Ui.Vision real browser execution — VERIFIED PASS
User screenshots of Ui.Vision Logs show echo JSON total=22, numeric=12, fallback=10, unique=22, with two example records containing source_site/external_id/title/canonical_url. Macro completed in 0.69 seconds with '100% local execution, no cloud used'. This validates read-only DOM extraction and identity uniqueness on loaded results, not full 931 listings. Macro only logs summary and two samples; it does NOT export all rows, persist to SQLite, or send messages. Next deliverable: safe complete JSON export and local validation before controlled DB ingestion.

## OH-05 export macro Windows download — verified
User PowerShell: OH_05_EXPORT_MACRO_DOWNLOAD=PASS; local file C:\Users\Mrn7206\AppData\Local\DJMRN\OpportunityHunter\exports\DJMRN-OH05-Freelancermap-Export-Pilot.json; COMMANDS=2. Import into Ui.Vision and local browser JSON download still pending verification. Source pinned at GitHub commit 8903cf0c2464d5a307a9f27a920d476772bd11f6.

## OH-05 export macro failure — observed
User supplied Ui.Vision log: Export-Pilot first executeScript failed in 0.25s with 'Could not establish connection to tab 555978241. Receiving end does not exist'. No echo, no verified JSON export. This is a browser extension-to-tab messaging failure; not evidence of a JSON schema or extraction logic error. Next: refresh Freelancermap tab, reselect Export-Pilot, retry once; if persistent, inspect extension connection and reload Ui.Vision. Do not mark export PASS.

## OH-05 real export uploaded and independently inspected — PASS
User uploaded DJMRN-OH05-freelancermap-2026-10-28T15-12-39-243Z.json. Parsed successfully: schema_version djmrn.oh.export.v1, 22 rows, 22 unique site/external_id keys, 12 numeric, 10 URL fallback, 5712 bytes. Offline field/URL validation PASS. Independent ephemeral SQLite dedup simulation PASS: first pass NEW=22/SEEN=0, second NEW=0/SEEN=22, final 22; temporary database destroyed. This is a schema-compatible simulation, NOT yet a test against the repo's actual ingest.py + ledger_history.py implementation. No operational Windows DB changes. Next: Windows validation via existing ingest.py and actual ledger_history on temporary copy, then consider controlled production import only after approval.

## OH-05 real export + actual ledger integration — WINDOWS VERIFIED PASS
User PowerShell output on 2026-10-28: EXPORT_FILE=DJMRN-OH05-freelancermap-2026-10-28T15-12-39-243Z.json; OH_05_REAL_EXPORT_LEDGER=PASS; VALIDATED_ROWS=22; FIRST_NEW=22; SECOND_SEEN=22; TEMP_DB_COUNT=22; TEMP_DB_INITIAL=0; INTEGRITY=ok; OPERATIONAL_DATABASE_MODIFIED=NO; TEMP_COPY_CLEANUP=PASS. Tested real exported JSON through repo ingest.py and ledger_history.py against disposable SQLite backup copy. Production ingestion NOT performed; automation and outbound messaging remain disabled. Next: production import with explicit approval and backup/rollback guard, or extend metadata/filters before importing.

## OH-05 approved production import — WINDOWS VERIFIED PASS (2026-10-28)
User explicitly approved storing 22 real Freelancermap ads. Windows PowerShell output: IMPORT_SOURCE=DJMRN-OH05-freelancermap-2026-10-28T15-12-39-243Z.json; OH_05_BACKUP=PASS; BACKUP_FILE=C:\Users\Mrn7206\AppData\Local\DJMRN\OpportunityHunter\backups\opportunities-pre-oh05-20261028T151853Z.sqlite3; IMPORT_ROWS=22; OH_05_PRODUCTION_IMPORT=PASS; EVENTS_NEW=22; EVENTS_SEEN=0; EVENTS_UPDATED=0; BEFORE=0; AFTER=22; HISTORY_BEFORE=0; HISTORY_AFTER=22; VERIFIED_STORED=22; INTEGRITY=ok; OUTBOUND_ACTIONS=0; BACKUP_RETAINED=YES. Production SQLite now has 22 discovered records and 22 history events. No outbound contact, no automatic recurring execution. Next: read-only reporting and evaluation/filtering; separately design repeat-run monitoring with backups, stable IDs and explicit action gates.

## OH-06 title-only triage — WINDOWS VERIFIED PASS (2026-10-28)
User executed src/report_title_triage.py against production SQLite in read-only mode. OH_06_READ_ONLY_REPORT=PASS; TOTAL_RECORDS=22; PRIORITY_REVIEW=0; NEEDS_DETAILS=2 (id 18 Engineering Practice Lead, id 20 E2E Solution Architect (Market Services)); LIKELY_UNRELATED=20; DATABASE_WRITES=0; OUTBOUND_ACTIONS=0. All 22 remained DISCOVERED. Categories are heuristic and provisional, based solely on titles; no permanent rejection. Next: obtain full description and constraints via read-only browser extraction; improve saved-search relevance, avoiding organizational engineering jobs outside DJMRN scope.

## OH-07 second detail export (2026-10-28)
User-provided read-only JSON export for E2E Solution Architect (Market Services): site freelancermap; URL /project/e2e-solution-architect-market-services; exported external_id=url:/project/e2e-solution-architect-market-services; visible page text reveals numeric project id 3066185. Employer Eolas Recruitment, Ireland/Dublin, On-site, Freelance, duration six months with potential extension, architecture experience 7-8+ years; no numeric rate shown. Provisional suitability: not a short independent DJMRN project. Crucial: slug-based IDs can be reconciled with official numeric IDs from detail pages without creating duplicate records. Captured application form text should be separated from job description; no application submitted, no database detail write. Second distinct page successfully exported. 

## OH-08 structured offline parsing — WINDOWS VERIFIED PASS (2026-10-28)
User executed src/parse_details.py against three OH-07 JSON exports. Output: OH_08_OFFLINE_PARSE=PASS; UNIQUE_PROJECTS=2; DATABASE_WRITES=0; NETWORK_ACTIONS=0; DUPLICATE_CAPTURE=3066213. Project 3066213 Engineering Practice Lead: Caspian One Ltd, United Kingdom, header On-site vs description Hybrid (WORK_MODE_CONFLICT), duration 6 months, budget unspecified, description_chars=2356, application_form_chars=441. Project 3066185 E2E Solution Architect (Market Services): Eolas Recruitment, Ireland, On-site, 6 months, budget unspecified, 7 explicit skill tags, description_chars=2876, application_form_chars=230; export_external_id is url:/project/e2e-solution-architect-market-services. Both exceed 10-day project limit. Next: add safe read-only reconciliation preview, test temporary SQLite schema for details, backup and require explicit approval before production schema migration or writes. Do not insert duplicate opportunity for URL fallback vs official numeric ID.

## OH-09 disposable detail SQLite test — WINDOWS VERIFIED PASS (2026-10-28)
User ran src/test_detail_store.py with live DB as read-only source and three OH-07 exports. Output: OH_09_TEMP_DETAIL_STORE=PASS; FIRST_NEW=2; SECOND_SEEN=2; DETAIL_ROWS=2; OPPORTUNITIES_BEFORE=22; OPPORTUNITIES_AFTER=22; OFFICIAL_ID_3066185_LINKED_TO_EXISTING_ID=20; INTEGRITY=ok; FOREIGN_KEYS=ok; OPERATIONAL_DB_WRITES=0; OUTBOUND_ACTIONS=0; TEMP_CLEANUP=PASS. Next: separate explicit approval for production DB backup/schema migration/detail writes; preserve existing statuses and history.

## OH-10 production detail migration — WINDOWS VERIFIED PASS (2026-10-28)
User ran approved src/apply_detail_store.py. Output OH_10_BACKUP=PASS; backup C:\\Users\\Mrn7206\\AppData\\Local\\DJMRN\\OpportunityHunter\\backups\\opportunities-pre-oh10-20261028T161003058827Z.sqlite3; OH_10_PRODUCTION_IMPORT=PASS; EVENTS=NEW,NEW; DETAIL_ROWS=2; OPPORTUNITIES=22; HISTORY=22; ID_3066185=20; ORIGINAL_ROWS_UNCHANGED=YES; BACKUP_RETAINED=YES; OUTBOUND_ACTIONS=0. Next OH-11 site-specific quota and approval-only outbound gate; do not enable auto sending.

## OH-11 outbound gate — WINDOWS VERIFIED PASS (2026-10-28)
User ran src/outbound_gate.py --self-test against config/outbound-policy.v1.json. Output OH_11_GATE_SELF_TEST=PASS; CASES=4; GLOBAL_COOLDOWN_SECONDS=300; FREELANCEMAP_MONTHLY_LIMIT=10; SENDS=0; DB_WRITES=0. All four scenarios HOLD: unknown quota and permission; 10/month cap; unknown site; missing approval plus cross-site cooldown. Five-minute minimum is global across sites; 10/month applies only to Freelancermap Basic. Next OH-12 read-only usage ledger test on temporary SQLite; no outbound actions.

## OH-12 outbound ledger disposable test — WINDOWS VERIFIED PASS (2026-10-28)
User ran src/test_outbound_ledger.py: OH_12_LEDGER_TEST=PASS; MONTHLY_COUNT=10; DAILY_COUNT=10; GLOBAL_LAST_EVENT_FROM_OTHER_SITE=YES; RESERVED_AND_UNKNOWN_COUNTED=YES; CONFIRMED_FAILURE_EXCLUDED=YES; DUPLICATE_PREVENTED=YES; TEMP_DATABASE_ONLY=YES; PRODUCTION_WRITES=0; SENDS=0. Counts are synthetic test fixtures, NOT real Freelancermap account usage. Next OH-13 production migration needs backup, explicit approval, and read-only preparation first.

## OH-13 production outbound ledger migration — WINDOWS VERIFIED PASS (2026-10-28)
User executed src/migrate_outbound_ledger.py with explicit production-write approval. Output OH_13_BACKUP=PASS; backup C:\\Users\\Mrn7206\\AppData\\Local\\DJMRN\\OpportunityHunter\\backups\\opportunities-pre-oh13-20261028T162727531987Z.sqlite3; OH_13_PRODUCTION_MIGRATION=PASS; OPPORTUNITIES=22; HISTORY=22; DETAILS=2; OUTBOUND_ATTEMPTS=0; ORIGINAL_DATA_UNCHANGED=YES; INTEGRITY=ok; FOREIGN_KEYS=ok; BACKUP_RETAINED=YES; SENDS=0. Next OH-14 read-only actual-ledger gate; never infer external account quota from empty local ledger.

## OH-14 operational read-only ledger audit — WINDOWS VERIFIED PASS (2026-10-28)
User ran src/audit_outbound_ledger.py on production SQLite: OH_14_READ_ONLY_AUDIT=PASS; LEDGER_ROWS=0; LOCAL_MONTH_COUNT=0; LOCAL_DAY_COUNT=0; ACCOUNT_QUOTA_FROM_SITE=UNVERIFIED; LOCAL_LEDGER_NOT_AUTHORITATIVE_FOR_SITE_BALANCE=YES; DECISION=HOLD; REASONS=PROJECT_MESSAGE_APPROVAL_MISSING,SEND_DISABLED,AUTOMATION_PERMISSION_UNVERIFIED,QUOTA_UNKNOWN; PRODUCTION_WRITES=0; OUTBOUND_ACTIONS=0. Next: verify actual site/account plan and quota before any proposed outbound operation.

## OH-15 Freelancermap account plan confirmation (2026-10-28)
User explicitly confirmed Freelancermap plan = Basic (free). Config updated: plan_verified_by_user=true, plan_verified_date=2026-10-28, monthly_application_limit=10; account_remaining_quota=null and quota_reset_rule=UNVERIFIED pending site-account evidence. Global 300-second cross-site cooldown unchanged. Sending disabled, per-project approval required. No production DB mutation or outbound actions.

## OH-15 Freelancermap user-reported quota (2026-10-28)
User reports Basic account has 10 of 10 applications remaining, membership began ~10 days ago, and next reset expected in ~20 days (estimated 2026-11-17). Recorded in outbound-policy.v1.json as USER_REPORTED; reset rule UNVERIFIED_USER_ESTIMATE, not verified against site. Local outbound_attempts remains empty as of OH-14. Global cooldown 300 seconds applies across all sites. send_enabled=false, automation_permission=UNVERIFIED, per-project approval remains mandatory. No sends or local DB changes.
