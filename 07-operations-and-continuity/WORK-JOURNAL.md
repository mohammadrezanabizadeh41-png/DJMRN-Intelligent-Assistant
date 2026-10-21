# DJMRN — Project Work Journal / دفتر وقایع اجرای واقعی

**Purpose:** append-only chronological, evidence-oriented account of WHAT was requested, WHAT was actually performed, WHERE artifacts live, WHETHER tests/commits succeeded, and WHAT remains. It supplements, but does not supersede, `07-operations-and-continuity/CURRENT-STATUS.md` (canonical CURRENT), `TASK-REGISTER.md` and GitHub commit history. Future assistants should read CURRENT first, then latest journal entry and linked files; never treat a plan as an implemented result.

## Entry format for future work

`date/time | context/request | intended scope | inputs and permissions | actual step and affected paths | evidence/test environment + PASS/FAIL/NOT_RUN | Git commit/blob/readback | blockers/uncertainty | precise next step`. Mark **NOT VERIFIED** for missing independent proof, and never invent background work. For non-sensitive data, link original WQ/WA, KB, test log and source version. Never store Gmail credentials, OTPs, browser cookies, raw private inbox/customer contents or API keys.

## 2026-10-21 — MAIL-P001 synthetic-only minimum triage baseline (new, TESTED-SYNTHETIC)

**User goal:** start the first useful Gmail and freelance opportunity assistant, with a persistent record of *every* research/build/test action in the canonical private GitHub project. Do not prematurely choose Jan, browser agent or paid API. Earlier official research WQ0005/WA0005 and coordinator KB-0012 are the starting knowledge. Existing V0 CAP-006 (document lookup) is NOT this mail assistant.

**Authorized scope interpreted:** proceed with isolated research/demo and non-sensitive synthetic-only Python experiment in the model's container; **not** installing on user's Windows, connecting real Gmail, browser sessions or sending external messages.

**Actions actually executed in isolated container:** created local `mail_triage_v0.py`, `synthetic_inbox.json`, `test_mail_triage_v0.py`, generated a real Persian synthetic report. Seven standard-library test cases passed; 26 sample records grouped to 22 keys including four email/portal duplicate pairs; final category split 8 opportunities, 4 follow-ups, 4 routine, 4 blocked/verify and 2 other-needs-review. Environment **Linux Python 3.13.5**, not the user's laptop. Other two comparison routes — current ChatGPT/Gmail and Email Triage demo — **NOT TESTED**. No email/service/browser/API/real account accessed and no third-party code installed.

**Actual artifact:** `06-tests-and-evidence/pilots/MAIL-P001-20261021/` containing code, fixture, tests, reports and comparison matrix. Refer to `EVIDENCE.md` and `FILE-SHA256.json` for reproducibility and provenance. Journal itself is a new dedicated continuity record, not a rewrite of WA0005 or changing historical WQ/WA.

**GitHub write status:** Pending while GitHub connector returns `The tool failed internally.` during this conversation. Do not declare commit/readback success until the exact contents have been written and fetched from `mohammadrezanabizadeh41-png/DJMRN-Intelligent-Assistant` main. A local artifact package can be handed to the user in meantime. If committed later, record exact commit and changed path list in a later journal entry rather than rewriting this honest historical status.

**Next:** after GitHub is available, upload complete synthetic test/evidence under agreed paths; update `CURRENT-STATUS`, existing task register and changelog without falsely claiming ChatGPT/Email Triage/Windows tests. Then compare other two approaches on the SAME fixture with specific permissions; continue toward one read-only real account only with separate consent. No new local agent runtime or permanent architecture chosen.
