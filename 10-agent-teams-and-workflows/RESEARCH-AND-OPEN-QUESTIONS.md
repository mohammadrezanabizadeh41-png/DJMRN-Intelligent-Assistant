# Research baseline, evidence grades, and unresolved questions — DJMRN-AGTEAM-001

**Research checked:** 2026-10-30, official vendor documentation and GitHub; this is a dated snapshot, not permission to activate or a guarantee of future features. Research-only means **NO live integration executed**.

## Verified in PUBLIC documentation (not locally tested)
| Fact | Source | Confidence/scope |
|---|---|---|
| OpenClaw can host multiple agents in one Gateway with separate workspace, agentDir and SQLite session store | [official multi-agent](https://docs.openclaw.ai/concepts/multi-agent) | DOCUMENTED; Windows execution not tested |
| Peer session calls, `sessions_send` and scopes/agentToAgent policy available | [session tools](https://docs.openclaw.ai/concepts/session-tool), [access config](https://docs.openclaw.ai/gateway/config-tools/sessions-and-subagents) | DOCUMENTED; isolated targeted test needed |
| Built-in OpenClaw Automations schedules require live Gateway; jobs/history persist, startup recovery has conditions | [automations](https://docs.openclaw.ai/automation/cron-jobs), [runtime](https://docs.openclaw.ai/automation/cron-jobs/how-it-works) | DOCUMENTED; no claim of exactly-once |
| OpenAgents Workspace provides Threads, Files, Tasks, Workflows, Routines, Inbox, collaborative members | [workspace docs](https://openagents.org/docs/en/workspace/what-is-workspace) | DOCUMENTED |
| OpenAgents Launcher supports local agent installation, status, connection to Workspace; OpenClaw is listed supported in official repo/gallery | [Launcher](https://openagents.org/docs/en/launcher/what-is-launcher), [repo](https://github.com/openagents-org/openagents), [connect](https://openagents.org/connect) | DOCUMENTED; exact per-persona mapping unverified |
| Pair a local device then add agent instances; connecting device alone is insufficient | [Connect Agent tutorial](https://openagents.org/docs/en/tutorials/connect-an-agent) | DOCUMENTED |
| Hosted Workspace stores messages/shared artifacts while local agent code stays on the machine | [workspace docs](https://openagents.org/docs/en/workspace/what-is-workspace) | DOCUMENTED; privacy/retention review pending |
| Launcher GUI self-hosted endpoint has a stated limitation; CLI supports custom endpoint | [self-hosted agents](https://openagents.org/docs/en/self-hosting/connecting-agents) | DOCUMENTED; verify current version |
| Cross-agent history access on OpenClaw defaults broader than desired, sandbox off in default personal setup | [trust model](https://docs.openclaw.ai/gateway/security/trust-model), [tool permissions](https://docs.openclaw.ai/gateway/security/tool-permissions) | DOCUMENTED; mandatory hardening before real data |
| OpenAgents Workspace and Launcher advertised free/open source; model API consumption external | [FAQ](https://openagents.org/faq), [Launcher](https://openagents.org/docs/en/launcher/what-is-launcher) | PUBLIC TERMS; region/account/privacy to verify |

## Critical unknowns (do not turn into claims)
- **U01 / BLOCKER:** One OpenClaw Gateway with N internal agents -> N separate Workspace member cards/direct addresses? How are agent IDs mapped?
- **U02:** Does Launcher create independent OpenClaw instances or expose internal agents natively? Is per-agent config editable from both apps without drift?
- **U03:** Is workspace STOP/approval applied to remote runtime tool actions or only Workspace work item?
- **U04:** Real OmniRoute endpoint, authentication, free model IDs, Tool Calling behavior and usage ledger across OpenClaw/OpenAgents.
- **U05:** Exact current pricing/geographic eligibility and provider privacy for user's connection; no paid fallback.
- **U06:** Windows 11 8GB measured idle/load RAM, CPU, daemon/process count for combined stack; impact of running Chrome.
- **U07:** Real security restrictions for access to local files, GitHub private repo and model prompts; cloud Workspace message retention.
- **U08:** Autonomous Workspace proactive threads vs internal `sessions_send`: event attribution, duplication, depth limits, independent critique, delivery.
- **U09:** Clock/cron ownership, restarts, missed runs, Windows sleep, outage recovery, idempotency and alerting.
- **U10:** Tool/skills compatibility and whether Windows install requires WSL/Docker/Node and whether existing runtime can be reused.

## Alternatives considered
- **OpenClaw standalone:** best minimal read-only autonomy/peer messaging baseline; lacks desired unified collaboration UX unless sufficient internal UI is found.
- **OpenClaw + OpenAgents:** research-led primary candidate if U01 and cost/privacy tests pass.
- **OpenAgents with separate runtime instances:** fallback if one Gateway cannot expose multiple distinct roles in Workspace; heavier footprint.
- **SillyTavern:** character/group-chat UI; not equivalent to structured tool execution, durable responsibility and review.
- **Flowise:** structured supervisor/worker workflow alternative; less direct independent-persona operations unless configured.
- **AGNT:** earlier user test failed to meet expected independent A2A behavior; preserve and compare, do not uninstall now.
- **Other code-first frameworks:** postpone until a demonstrated gap; do not combine many frameworks prematurely.

## Design decisions explicitly NOT made
No OpenClaw/OpenAgents installs or account registrations; no AGNT deletion, no Workspace sign-in, no cloud uploading, no new scheduler, no running peer messages, no token/config creation, no chosen model endpoint, no database migration, no workflow activation, no permanent architectural adoption. The project is **PROPOSED**.

## Continuation instructions
Before R1, re-read the official docs live and reconcile release versions with current repo/runtime. Use explicit test evidence before qualifying an operational status. Keep future progress in the ONE user-authorized CURRENT-STATUS file when explicitly asked, while these thematic design docs remain stable unless specifically revised.
