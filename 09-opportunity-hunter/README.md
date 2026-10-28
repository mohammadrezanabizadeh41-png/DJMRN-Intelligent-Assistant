# DJMRN Opportunity Hunter — dedicated project home
**Project ID:** DJMRN-OH-001
**Created:** 2026-10-28
**State:** PLANNING COMPLETE / IMPLEMENTATION NOT STARTED
**Owner:** DJMRN
**Canonical location:** this directory, within DJMRN-Intelligent-Assistant. No second repository.

## Purpose
Find suitable freelance projects and eligible employment opportunities across registered international and Iranian platforms, evaluate actual fit and economics, prepare personalized first contact, track employer replies, and hand positive replies to the user for negotiation. Avoid claiming unavailable skills or committing to binding contracts.

## Start here
1. [ROADMAP.md](ROADMAP.md): phased work, testable exit gates, estimated effort, next action.
2. [POLICY-AND-DECISIONS.md](POLICY-AND-DECISIONS.md): current requirements, policy precedence, open approvals.
3. [STATUS.md](STATUS.md): authoritative status and next checkpoint for this vertical.
4. [Original discussion requirements](../03-architecture-and-tools/DJMRN-OPPORTUNITY-HUNTER-REQUIREMENTS-20261028.md): chronological decision history; latest approved refinements take precedence over earlier open questions.

## Existing project components to inspect before coding
- [Global project rules](../PROJECT-RULES.md)
- [Project-wide task register](../02-project-management/TASK-REGISTER.md): don't reuse TASK IDs or silently alter unrelated task statuses.
- [Coordination hub P1](../05-assistants-and-capabilities/src/coordination_hub_p1/README.md): experimental, synthetic, SQLite and idempotency reference; NOT proven production-ready.
- [Document search V0](../05-assistants-and-capabilities/src/document_search_v0/README.md): bounded Python stdlib reference.
- [Current status](../07-operations-and-continuity/CURRENT-STATUS.md): historical wider system state; this folder tracks this vertical.

## Architecture
Chrome + Ui.Vision (read) -> normalized listing -> SQLite dedup -> market/site policy -> AI structured extraction via AGNT/OmniRoute -> deterministic gate -> project/employment economic gate -> personalized draft -> site-authorized outbound action -> delivery receipt -> reply classification -> user handoff.
Prefer Python stdlib/SQLite/JSON, no always-on additional engines, no local LLM. Keep all site-specific credentials out of GitHub.

## Evidence and completion rules
Never mark a phase DONE without runnable test, receipt, code revision and explicit result. Bridge connected != AGNT macro execution. A simulated send != a real delivered message. A posted message != a confirmed reply. An archived plan != running software.
