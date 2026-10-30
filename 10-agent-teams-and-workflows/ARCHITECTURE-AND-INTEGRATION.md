# معماری هدف و اتصال OpenClaw ↔ OpenAgents — DJMRN-AGTEAM-001

**Status: PROPOSED / NOT DEPLOYED — 2026-10-30**

## 1. مدل مفهومی (نه دیاگرام اجراشده)

```text
USER (web/desktop/mobile)
  |
  v
OpenAgents Workspace [collaboration UI, Threads, Tasks, Files, Inbox, Routines]
  |            ^       ROLE: collaboration / projection; NOT DJMRN source-of-truth
  |  agent messages, results and limited shared artifacts
  v            |
OpenAgents Launcher / agn node / supported OpenClaw connector
  |     [node/device pairing, agent runtime online/offline; compatibility TO TEST]
  v
OpenClaw Gateway  [ONE candidate local runtime service]
  |-- PM-01        independent workspace, persona, sessions, tool policy
  |-- ARCH-01      independent workspace, persona, sessions, tool policy
  |-- RESEARCH-01  independent workspace, persona, sessions, tool policy
  |-- REVIEW-01    OPTIONAL after need proven
  |      <------ sessions_send / allowed peer consultation ------>
  |
  +--> OmniRoute (existing local API gateway) --> approved FREE models ONLY
  +--> approved read-only GitHub/Notion/web tools and evidence
  +--> runtime scheduler (exactly ONE owner per scheduled job)
  
GitHub authoritative CODE/CI/approved project records; Notion authoritative cross-project decisions;
runtime session stores = ephemeral/persistent operational transcript, NEVER replacement authority.
```

## 2. نقش‌ها/Ownership
| Component | Defined role | May own | Must NOT own |
|---|---|---|---|
| OpenClaw | Agent runtime / orchestrated execution | agent identities, session state, tool restrictions, approved schedules, direct messaging | canonical GitHub code/decisions without project authorization |
| OpenAgents Workspace | collaborative GUI / projection | Threads, Inbox, task presentation, shared workspace artifacts | second canonical agent registry or silent duplicate schedules |
| Launcher / agn node | runtime-to-workspace connection | connection health/agent registration on node | independent AI model authority or second PM |
| OmniRoute | model API routing candidate | allowed provider/model gateway only | user authorization, task identity or guaranteed zero price |
| GitHub main repo | project docs/code/CI source of truth | user-approved current/project records | unsanitized secrets or live full conversation transcript |
| Notion canonical | approved general architecture/governance | org-level policy | automatically replicated routine status |

OpenAgents server holds messages and shared artifacts in hosted deployment. Gate: redact sensitive prompts/source material or prefer evaluated self-hosted option before sensitive operational workflows.

## 3. اتصال پیشنهادی مرحله به مرحله (NOT EXECUTED)
A. Validate Windows 11 baseline (8 GB physical RAM), network, exact target versions and signed installer/supply chain.
B. Test Workspace in browser **with synthetic non-sensitive data** (free terms / geo / privacy verified).
C. After explicit approval, install ONE OpenAgents Launcher (or CLI if official connector demands it). Confirm supported OpenClaw integration. Avoid separate duplicate daemon.
D. After approval, install/configure ONE OpenClaw Gateway; create two independent personas with distinct agent IDs, agentDirs, workspaces and scoped tools.
E. Pair node using documented "Connect this computer" workflow; add OpenClaw runtime/agent to Workspace; verify authentication and online status.
F. **Critical P0 question:** Can PM and ARCH hosted in one OpenClaw Gateway register as TWO distinct, selectable Workspace participants, with separate targeting, history and permissions? Confirm through UI trace + actual messages. If no, evaluate officially supported per-agent instance, connector mapping, or narrower separate bridge. **Do not duplicate full business state or claim success from one generic OpenClaw bot.**
G. Only then trial three-agent consultation and PM review; inspect messages, trace IDs and duplicate behavior.
H. Integrate OmniRoute OpenAI-compatible endpoint only after local Tool Calling, streaming, model role and quota verification. Do not assume endpoint or model identifiers from historical screenshot; no API secret stored in repo.
I. Select schedule owner for each job (OpenClaw Automations OR Workspace Routines). Never schedule the same job twice without dedup ownership.

## 4. Two viable communication planes
- **Primary internal:** OpenClaw `sessions_send` from one agent session to another, restricted by `tools.agentToAgent` and session visibility/send-only permissions; no UI needed for peer consultation.
- **Visible collaborative:** agents invited to OpenAgents thread, `@mentions`, proactive Doer/Reviewer work; shared thread human-visible but not proof of independent internal sessions.
- For a traceable decision, both routes may produce task IDs and summaries; **do not mirror every private transcript**. Implement explicit event mapping only after proof of connector capability.

## 5. Separation questions (test before acceptance)
- Workspace user/agent relationship is by node runtime vs by OpenClaw internal agent ID? Can one Gateway publish N distinct participants?
- Can Workspace task/Stop/Pause/Approval target precisely one agent and preserve authority on OpenClaw?
- Do OpenAgents Routines trigger OpenClaw session by agent ID or simply connected launcher instance? If not, keep schedule only in OpenClaw.
- Does OpenAgents Launcher support custom OmniRoute OpenAI-compatible base URL and per-agent model selections in installed current version?
- What is the exact cache/queue/ACK/resume behavior after disconnect? Avoid exactly-once claims without evidence.
- Is hosted Workspace permissible for user code and prompts? Default is **NO private client payloads** until privacy approval.
- Official Launcher self-hosted endpoint GUI currently not guaranteed; CLI may be required; revalidate docs on actual version.

## 6. Alternatives and fallback
1. OpenClaw-only pilot with direct agent-to-agent messaging and its Control UI: smallest feasible test, no Workspace duplication.
2. OpenClaw + OpenAgents if independent agent registration + review collaboration passes.
3. OpenAgents with separately connected native agent runtimes if one OpenClaw Gateway cannot expose multiple personalities; heavier, requires measuring RAM and model costs.
4. Other workflow-first engines (Flowise / LangGraph / comparable) only after gap/benefit established; no framework accumulation.
5. AGNT historical experiment preserved; no deletion or migration until pass.

## Official references (checked 2026-10-30)
- https://docs.openclaw.ai/concepts/multi-agent
- https://docs.openclaw.ai/gateway/config-tools/sessions-and-subagents
- https://docs.openclaw.ai/concepts/session-tool
- https://docs.openclaw.ai/automation/cron-jobs
- https://openagents.org/docs/en/getting-started/overview
- https://openagents.org/docs/en/getting-started/workspace-vs-launcher
- https://openagents.org/docs/en/tutorials/connect-an-agent
- https://openagents.org/docs/en/launcher/what-is-launcher
- https://openagents.org/docs/en/self-hosting/connecting-agents
- https://github.com/openagents-org/openagents
