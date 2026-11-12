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

---

## ایجنت‌های کلود یا ابری — Cloud Agents (Free Renewable Tiers, 2026-11-12)

**Mission scope:** Research-only comparison for a DJMRN cloud + Windows hybrid agent team. **Research date:** 2026-11-12. **Requested by owner:** preserve these findings in the existing agent-team research section. **Status:** RESEARCH / PROPOSAL ONLY — no deployment, account creation, plugin installation, API-key change, data migration, scheduler enablement, purchase, or security change authorized. This dated note supplements older 2026-10-30 baselines, which contain outdated "not installed" statements; use the current operational record for actual agent/runtime state.

### 1. Actual requirement and architectural distinction

- Owner's Windows laptop is **not always on**; VPN/proxy switching interrupts some local calls to previously registered model API providers (Gemini, Groq, OpenRouter, etc.). Owner needs small *unattended cloud tasks* that can fetch/triage/analyze public opportunities and deposit results for later review and collaboration with Windows agents (OpenMausBot/MausBot / existing DJMRN agent-team environment).
- Separate three independent costs/capabilities: **(a) cloud workflow/agent builder**, **(b) hosting/execution/scheduling**, **(c) model inference quota**. A free editor or open-source agent runtime does not itself provide a free always-on cloud server or free LLM usage. Likewise, a high "requests/day" number is not "AI-agent jobs/day".
- **Preferred simplest viable approach:** Scheduled/stateless cloud functions + externally supplied permitted free API models + durable job/result store + occasional Windows sync. This is an evaluated *candidate*, NOT a migration or implementation decision.
- Cloud runs avoid requiring the laptop to be online, but **do not guarantee** that the provider, account, or region is authorized/available. Check each provider's geographic eligibility, terms and live account rate limits; do not use identity/region evasion.

### 2. Platform comparison: renewable free tier vs trial vs one-time credit

| Platform | Renewal / official plan facts (checked 2026-11-12) | Models bundled? | Agent-team fit / limitation | Status |
|---|---|---|---|---|
| **n8n Cloud** | Standard trial **14 days**, not a renewable free cloud hosting plan; trial ends and hosted instance stops/deletes on schedule. | Trial advertises AI credits; not permanent free inference. | Strong workflow orchestration; not free forever when n8n hosts it. | DO NOT select as enduring free runtime |
| **n8n Community self-hosted** | Free-to-use software without a 14-day license expiry; **hosting is separate**. Sustainable Use License: personal/own-organization workflows and certain client-output arrangements allowed; hosted workflow editor/white-label for clients may require commercial license. | Bring your own model endpoint/key, no permanent included LLM quota. | Good optional workflow layer if a compatible stable-free host exists and cost/RAM/license are verified. | OPTIONAL / NO HOST CHOSEN |
| **Activepieces Cloud Free** | **100 credits per day** on the current official pricing page, $0 forever, no card; unlimited flows and Flow/Agent/Table features. AI steps consume extra credits. | Built-in AI credits can be used within plan limits; **bring-your-own AI keys is advertised on Plus**, not Free. | Closest ready-made GUI cloud Agent/Flow candidate; quota cost per AI step/tool call matters; custom HTTP/API route needs separate free-plan/security verification. | FIRST HOSTED-GUI CANDIDATE, UNTESTED |
| **Make Free** | **1,000 credits/month**, no time limit; scheduled scenario minimum interval **15 minutes** on Free. | Do not presume independent bundled free inference. | Very practical for simple integration/scheduling; credits count actions/modules, not full autonomous "agent sessions". | ALTERNATIVE |
| **Neon Free Functions + Postgres** | Official Free: **1M Function invocations/month, 10 active and 400 waiting capacity-hours/month;** Postgres **1 GB/project**, **100 CU-hours/month/project**. Scheduled Node.js Functions and scale-to-zero, with limits. | **No free AI inference implicitly bundled**. Neon AI Gateway is separately priced/prepaid; requires explicit review/approval, not automatically free. | Best reuse/low-sprawl candidate for bounded scheduled cloud work + durable state in DJMRN; not a full always-running VM or ready-made graphical multi-agent platform. | EXISTING DJMRN CANDIDATE |
| **Cloudflare Workers Free** | **100,000 Worker requests/day**, **10 ms CPU/invocation**, 5 cron triggers/account on Free (CPU excludes network waiting). | **Workers AI** has a separate **10,000 Neurons/day** allocation for eligible models; some models demand paid plan. | Lightweight HTTP/scheduled tasks, API dispatch, webhook bridge; heavy parsing / multi-agent local inference unsuitable under 10-ms CPU. | ALTERNATIVE |
| **Google Apps Script (consumer)** | **90 min total trigger runtime/day**, max **6 min per execution**, URL Fetch quota also applies; time-limited execution. | No free LLM embedded; may call separately allowed Gemini APIs. | Good for simple Workspace / Sheets / Gmail automation with proper permissions. | SPECIALIST ALTERNATIVE |
| **GitHub Actions (GitHub Free)** | **2,000 hosted-runner minutes/month for private repos** (plan allowance; public-repo eligible behavior differs), possible schedule delay/drop. Exceeding allowance can generate charges unless budget blocks paid usage. | No LLM embedded. | Useful fallback CI/small jobs; not a guaranteed exact-time production agent scheduler. | CI CORE / SCHEDULER FALLBACK |
| **Dify Cloud Sandbox** | Free account with **200 message credits** and 5 apps, but page does **not establish a recurring free monthly/daily refresh** of those 200; don't treat them as renewable. | Initial credits for supported models; per-response consumption depends on model. | UI prototype/testing, not a confirmed permanent free scheduled agent runtime at useful volume. | EXPERIMENTAL / NOT RENEWABLE-PROVEN |
| **Google ADK** | Free/open agent *framework*, **not a cloud host**; Gemini Free Tier is a separate inference service. Cloud deployment (e.g., Cloud Run) has distinct terms and may require billing. | Model supplied by Gemini or another provider under that provider's eligibility/quotas. | Code-first multi-agent development if demonstrably needed; higher implementation overhead. | FUTURE ALTERNATIVE |

**Important correction of prior chat summary:** Activepieces Free is currently shown as **100 credits/day**, **not 1,000 credits/month**. The previous 1,000/month claim should be treated as SUPERSEDED by the official current pricing page. GitHub Actions allowance is verified as **2,000 minutes/month** for GitHub Free private repositories; do not substitute an unsupported general $12-credit value. Dify's initial 200 message credits must NOT be presented as monthly renewable without proof.

### 3. Free model supply (independent of cloud execution platform)

- **Gemini API:** selected Free-tier models have free input/output tokens with per-model/project quotas and region restrictions; exact remaining quotas are **account-specific** and only AI Studio dashboard / API response can establish actual usable daily limits. Some Free-tier data may be used to improve Google's products — avoid customer confidential input absent rights/privacy review. Source: https://ai.google.dev/gemini-api/docs/pricing
- **OpenRouter:** models with suffix ':free' are $0/token under advertised limits; a free account typically has **50 free requests/day and 20/min** (including failed attempts), shared account limits; account-specific balance and actual model availability still need a check. Source: https://openrouter.ai/collections/free-models
- **Cloudflare Workers AI:** **10,000 Neurons/day** for eligible models in Workers Free; does not imply 10,000 prompts. Source: https://developers.cloudflare.com/workers-ai/platform/pricing/
- **Groq / AI Horde / OmniRoute:** previously mentioned/connected in DJMRN history; their exact current free entitlement, region, per-model limits, and whether remote cloud IPs work are **UNVERIFIED here**. OmniRoute running on a local Windows gateway is **not** remotely available while laptop is off. Do not route cloud traffic through local loopback or publicly expose local gateway.
- **DeepSeek API:** free chat UI is not equivalent to free official API. A provider-specific free-hosted DeepSeek model may exist but inherits that provider's separate rate limits and service terms.
- External execution may avoid local VPN proxy switching, but is **not proof** that service legal eligibility, IP policy, platform account, or provider ToS permits the call; use only authorized routes.

### 4. Current DJMRN status / live evidence vs archival

- Existing project 'djmrn-intelligence-v0' in connected Neon was observed on **Free (free_v3)** in read-only checks on 2026-11-12; its listed production/test branches showed **Archived** state. Three observed Scheduled Function triggers across the inspected branches were **disabled**, including the production-named ones. **No active unattended Neon job was proven**; the cloud team is NOT OPERATIONAL.
- Earlier canonical research/experiments proved a bounded **non-production source fetch -> durable Postgres write** path; this does **not** prove successful free-model inference, Windows-to-cloud agent messaging, Cloud-to-Windows sync, production backup/recovery, or cross-provider free eligibility.
- Existing Windows OpenClaw/OpenMausBot / agent team and OmniRoute are distinct local agent/coordination/inference roles. Do not create a second source-of-truth, alternate task coordinator, or uncontrolled always-on cloud gateway.
- Repository/privacy risk: treat any GitHub document as potentially public; **no secrets, personal identifiers, customer data, private endpoint values, credentials, raw emails, session tokens, or API key material in this research record**.

### 5. Proposed hybrid integration (NOT approved or deployed)

Cloud scheduler / worker (one bounded task) -> eligible free model API when reasoning is needed -> **single existing durable operational store** (e.g. Neon Postgres) -> outbound-authenticated sync from Windows when laptop reconnects -> existing MausBot team validates, codes, tests, prepares user-reviewed output.

Separate responsibilities:
- **Cloud Executor:** scheduled data gathering, deterministic dedup/triage, *optional* model analysis; no direct edit of user's local PC; minimal permissions.
- **Model Provider / Router:** use pre-approved free models with rate/cost caps and fallback. Remote cloud component must not depend on local Windows OmniRoute when PC is off.
- **State Authority:** one selected DB holding job ID, result, source/provenance, model version, cost usage, status, last run, retries and errors.
- **Windows Agent Team:** pull pending results upon reconnection, acknowledge job receipt with idempotent updates, perform local-only jobs; no inbound firewall opening/public Windows port required for pull sync.
- **Notion/GitHub:** Notion is governance/architecture decision authority; GitHub is source/tests and explicitly requested research artifact; research note is not evidence of an approved architectural decision.

**Reliability/security:** bounded timeouts, no paid overage, disabled auto-top-up, job-level retries/backoff and idempotency, audit trail, secret-manager/env binding, least-privilege scopes, owner approval for sending messages/applying changes, and a deliberate offline-to-online sync protocol. Avoid permanent network tunneling to laptop.

### 6. Smallest operational acceptance test before choosing platform

1. Select **one actual read-only job**, e.g. public freelance listings/RSS -> timestamped dedup + short Persian summary. Prefer deterministic extraction first; only one model call if necessary. Define daily budget (< free limits) before testing.
2. Read-only assess existing Neon plan, archived branches, triggers and retention; evaluate access to existing nonproduction branch. Do not wake/modify/migrate/enable anything yet without separate owner approval.
3. Separately compare a Free Activepieces sample workflow and a Neon scheduled Node.js function on **same tiny synthetic input**, with no customer data, and measure task success, per-run credit/model consumption, scheduling, reliable persistence and region eligibility. No signup/paid add-ons without consent.
4. Confirm cloud job can complete with laptop powered off, persist result, then test Windows *pull and acknowledgment* when online. Deduplicate/handle retry, lost request, quota 429, timeout, provider outage, cloud workflow failure, partial state, and duplicate delivery.
5. Measure quality/latency/time/cost and operational effort; select **one** default scheduler/executor, avoid adding n8n unless an actual unsupported flow complexity is proven. Deploy/production enablement requires explicit proposal + impact + approval.

### 7. Source links checked in this research round (official)

- n8n cloud trial: https://support.n8n.io/article/how-do-i-cancel-my-trial ; pricing: https://n8n.io/pricing/
- n8n self-host license boundary: https://support.n8n.io/article/can-i-use-your-license-for-my-use-case
- Activepieces Free/Plus and credit refresh: https://www.activepieces.com/pricing ; AI cost/key separation: https://www.activepieces.com/product/ai-agent-builder ; keys: https://www.activepieces.com/docs/admin-guide/guides/setup-ai-providers
- Make Free: https://www.make.com/en/pricing
- Neon Free (Functions/Postgres): https://neon.com/blog/neon-free-plan-1-gb-per-project ; AI Gateway separate from free Functions: https://neon.com/blog/neon-backend-is-ga
- Cloudflare Workers Free & cron limits: https://developers.cloudflare.com/workers/platform/limits/ ; Workers AI pricing: https://developers.cloudflare.com/workers-ai/platform/pricing/
- Google Apps Script quotas: https://developers.google.com/apps-script/guides/services/quotas
- GitHub Actions allowance: https://docs.github.com/en/billing/reference/product-usage-included
- Dify Sandbox: https://dify.ai/pricing
- Google ADK: https://codelabs.developers.google.com/multi-agent-app-with-adk ; Gemini API Free: https://ai.google.dev/gemini-api/docs/pricing
- OpenRouter Free: https://openrouter.ai/collections/free-models

**Decision gate / next step:** Preserve current Windows agent team and previously-tested infrastructure. Investigate only **Neon (reuse-first)** and **Activepieces Cloud Free (hosted no-code comparator)** for the first small offline-laptop pilot. This is a comparison priority, **not** authorization to create an agent, sign up, activate a provider, spend credits, enable cloud triggers, or publish/deploy. Current actual account quota, service accessibility, data/region terms and incident handling must be verified at implementation time.
