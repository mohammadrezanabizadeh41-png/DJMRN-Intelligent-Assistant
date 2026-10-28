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
