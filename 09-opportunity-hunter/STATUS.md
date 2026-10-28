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
