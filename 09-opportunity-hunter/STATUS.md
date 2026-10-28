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
