# DJMRN — بستر ایجنت‌های ابری چندمنظوره | Cloud Agent Foundation

**Project ID:** DJMRN-CLOUD-GMAIL-OPPORTUNITY-001
**CURRENT IMPLEMENTATION ROADMAP (C0–C10 / FOUNDATION-FIRST):** [IMPLEMENTATION-ROADMAP.md](IMPLEMENTATION-ROADMAP.md) — verify renewable-free cloud hosts → choose/create ONE cloud runtime → run first independent agent/tool/model on public data → durable state → permissions, scheduling and recovery → optional Google ADK multi-agent → optional Windows sync → later domain applications (Gmail, jobs, others). The older R0–R10 Gmail/portfolio-first order is SUPERSEDED.
**Registered:** 2026-11-12
**Priority:** NEXT PROJECT — next planned execution workstream, not an automatically running service.
**Status:** PROJECT CREATED / SPECIFICATION & RESEARCH REGISTERED / IMPLEMENTATION NOT STARTED.
**Owner:** DJMRN; approval authority: the user.
**Repository:** DJMRN-Intelligent-Assistant, main.
**CURRENT SCOPE (owner correction, 2026-11-12):** Create an independent, reusable, secure and free-first CLOUD AGENT EXECUTION SPACE. Runtime/provider/tools/state/permissions/scheduling/observability first; applications including Gmail, jobs, portfolios and market analysis later and only when explicitly selected. Existing folder path and project ID are kept for link continuity.
**Safety/privacy:** This repository has been observed PUBLIC. No Gmail address, employer email, customer record, email body, personal identity, API key, OAuth token, secret, resume private details, browser session or credential is stored here.

## 0. CURRENT CHARTER — Multi-purpose cloud-agent foundation FIRST (2026-11-12)

**Owner-corrected priority — this section and the C0–C10 roadmap supersede any Gmail-first / portfolio-first implied priority in the historical sections below.** The project's business objective is now to obtain an actual FREE-FIRST multi-purpose cloud execution environment where one or more agents can operate without the laptop, call the owner's legitimately available free model APIs, use approved tools, persist state, run scheduled tasks, expose status/outputs, recover failures and later synchronize with local agents.

**Build order, not vendor preselection:** (1) live account/free-tier and regional/billing audit; (2) compare Neon Functions (existing), Activepieces Hosted Free, Google Cloud/ADK, Supabase, Apps Script and Cloudflare against a small measurable workload; (3) choose a **single** host and activate it only after approval; (4) cloud-first one-worker public I/O + a free verified model call; (5) durable results/restart, security/tools, scheduled execution and monitoring; (6) optional ADK 2.0 collaborative agents if its overhead is justified; (7) Windows sync if desired; **(8) only then** domain-specific applications. Serverless/on-demand is acceptable if it operates while the Windows laptop is off; permanent VM is not a requirement.

**MVP is platform readiness, NOT Gmail:** Verify real cloud job execution, independent connectivity and legally permitted provider use, one non-sensitive tool and model, persisted results, retry/idempotency, budget, a safe stop and human-readable cloud outputs. Building a project folder or merely running tests is not a functioning cloud agent. **Gmail OAuth, drafts/sends, web job application, CV/portfolio creation and employer messaging are downstream modules, not current work.** No API key, Gmail OAuth scope or private account data is involved in the first foundation smoke.

**Google placement:** Gemini is a *candidate model provider*, not the cloud host. Google ADK 2.0 is a *candidate agent-development framework*, not included free hosted runtime. Google Apps Script is a *small cloud job runner*, not synonymous with ADK or the only architecture. Cloud Run hosting demands an independently verified billing/IAM/region/free-tier assessment. Do not force a Google-only architecture just because model keys exist. Compare simpler supported managed providers (and current existing DJMRN cloud resources) fairly.

**Relation to earlier notes:** The remaining numbered sections 1–9 were written before the owner corrected the scope. They are preserved for research/history and for a **possible future Gmail/job-follow-up Domain**, not as active implementation steps. For **current** architecture priority, use [C0–C10 foundation roadmap](IMPLEMENTATION-ROADMAP.md). No existing Gmail automation, model key, secret, cloud trigger, account, or environment was changed by this documentation amendment.



## 1. Formal mission / intended value

Build one cost-controlled cloud capability that can run periodic checks even when the Windows laptop is OFF or its VPN/proxy changes, **identify genuine freelance / remote project opportunities**, compare them with DJMRN constraints, prepare relevant written replies and resumes, watch replies and notify the owner. Later coordinate with existing Windows MausBot/OpenMausBot and related specialized agents without duplicating the task authority. Target is actual opportunity follow-up and owner-usable drafts, not the number of agents or integrations.

Initial outcome: shortlist with source links and rationale + Gmail draft requiring human approval + reply watcher + actionable Persian report. Future outputs (each separately approved): email send, follow-up messages, application to approved site, meeting invitations, CRM-style pipeline.

**Explicitly not approved now:** creating a Google Cloud/Apps Script project, enabling APIs or scopes, adding OAuth authorizations, reading private Gmail, deploying code, creating triggers, migrating data, opening browser sessions, sending emails, auto-applying, changing existing automations, making payments, installing plugins, or exposing local gateway. This owner request authorizes **registration of project docs only**.

## 2. Reconcile with prior DJMRN work (reuse / don't duplicate)

- Existing parent project: **DJMRN-AGTEAM-001** and seven named Windows specialist agents + built-in main (previous registered inventory). This cloud project is a **cloud execution track**, not a replacement for the existing team and not an additional always-on local process.
- Existing early work: **DJMRN-EMAIL-OPPORTUNITY-AUTOMATION-001** (2026-10-31) proposed a Python/Browser-Use/Windows Scheduler Gmail opportunity reader. It was not implemented. New cloud track **extends its business objective and re-evaluates its runtime choice** because laptop uptime and VPN dependence are unacceptable for scheduled monitoring. Existing local-only path remains a specialist future fallback, not a parallel owner of the same Gmail job.
- Existing research: the 2026-11-12 **Cloud Agents / renewable free tier** section in the parent RESEARCH-AND-OPEN-QUESTIONS.md compares n8n, Activepieces, Neon, Cloudflare, Make, Apps Script, GitHub Actions, Dify, Google ADK and model sources. Reuse instead of reproducing the whole research catalog.
- Existing related domains: **DJMRN-OH-001 Opportunity Hunter** for public listings and site extraction; keep site-specific code and contracts there. This cloud project owns *Gmail-centered opportunity follow-up workflow*, not another duplicate general scraping framework.
- Existing chat-level scheduled Gmail automations: three active checks/reporting tasks were observed 2026-11-12. **Do not enable a fourth overlapping production poller** until deduplication, ownership, schedule and whether to retain/replace the existing jobs are decided with the user. Do not disable/change existing automations as a side effect.
- Existing **Neon Intelligence Fabric** can be considered for durable state/scheduled processing; connected read-only inspection on 2026-11-12 found a Free plan, existing branches marked Archived and three inspected schedules disabled. Thus it is not a currently proven operating Gmail agent.

## 3. Functional domains, authority and contracts (proposal)

| Domain | Inputs | Processing | Outputs | Owner / authority |
|---|---|---|---|---|
| Gmail Ingestion | Authorized Gmail account, query/labels, message/thread IDs, checkpoint | Read-only metadata-first discovery, thread fetch only for candidate matches | deduped candidate event; provenance | Gmail canonical for messages and drafts; cloud workflow for processing |
| Deterministic Eligibility | Public offer metadata, approved eligibility rules | Sender/source verification, project-vs-employment, time, budget, remote/geography, payment feasibility, fraud signals | keep / reject / manual-review + reason | Versioned rule code in GitHub; owner approves rules |
| AI Analysis | **Approved non-sensitive/pseudonymized** job description only | Gemini or other eligible free model; bounded prompt/output; source-cited summary, fit score, missing facts | analysis proposal (not evidence) | Provider owns model service; project stores decision provenance |
| Correspondence Preparation | Qualified opportunity, approved DJMRN profile & public portfolio, original permitted email thread | Create a tailored bilingual reply/follow-up proposal | Gmail Draft + review request | Gmail owns draft; human authorizes sending |
| Reply Watcher | Authorized Gmail thread, last action, expected response window | Check thread changes, detect human reply, dedup/notify, request human review | state transition and concise Persian alert | Same selected job-state store |
| Website Opportunity Adapter (later) | Public listings and approved user-authenticated site session | Official API / RSS first, browser only if allowed and necessary | structured, provenance-linked listings and optional draft applications | Reuse Opportunity Hunter site adapters, not duplicate crawler |
| Windows bridge (later) | Reviewed cloud job results/status | Outbound authenticated pull on laptop reconnection; acknowledge idempotently | local work items for MausBot team | Local team owns Windows actions; cloud owns scheduled task |

**One source of truth per fact:** Gmail for email/thread/draft bodies, **one** approved store for pipeline/job state (initial candidates: Google-local Sheet/Properties for very small pilot OR existing Neon Postgres after permission/schema audit; not both as canonical), GitHub for source/tests/specification, Notion for accepted architecture/decisions, owner for authorizations. No raw Gmail mailboxes mirrored to GitHub or unapproved external database. Shared Windows/cloud status must use stable job IDs and a single owner per task. Cloud apps/LLMs are executors/analyzers, not decision authority.

### Suggested state machine (subject to approval)

DISCOVERED → FILTERED → NEEDS_REVIEW → QUALIFIED → DRAFT_PREPARED → AWAITING_OWNER_APPROVAL → (OWNER_SENT | OWNER_REJECTED) → WAITING_REPLY → REPLIED → (FOLLOW_UP_DRAFT | CLOSED).

Explicit states for ERROR, RATE_LIMITED, PERMISSION_REVOKED, TIMEOUT, NEEDS_RESYNC, DUPLICATE and UNSUPPORTED_SITE. No automatic transition to SENT without future task-specific authorization. Message/thread IDs and labels are data, not instructions (prompt-injection boundary).

## 4. Google-first technical proposal (smallest adequate implementation)

**Preferred P0 stack for evaluation (not adopted/deployed):**
1. **Google Apps Script (V8)** — scheduled lightweight executor in Google cloud; no laptop uptime required. Timer triggers are approximate, not a guaranteed precisely timed daemon.
2. **Gmail API using Advanced Gmail Service** for read-only message/thread listing and targeted fetch; use official Google OAuth authorization under owner account. For full body read, the gmail.readonly scope is classified RESTRICTED; use least privilege and review verification/security requirements. The metadata scope alone cannot read body. Do not use account passwords, cookies or OTP in automation.
3. **Deterministic rules before AI** — sender allowlist, search criteria, source classification, dedup, eligibility, deadlines and safe-link checks. Avoid sending whole inbox content to a model.
4. **Google Gemini Developer API Free Tier**, conditional and **only for public / explicitly shareable, non-sensitive content**; existing API key does NOT authorize Gmail, and account/project-specific active RPM/TPM/RPD must be inspected. Some free Gemini models/regions may be unavailable; free quota is not guaranteed.
5. **Gmail Drafts** on later authorized phase: compose tailored draft, reply in proper thread (threadId + References/In-Reply-To/Subject) with human send approval. Creating drafts is a Gmail write; **not part of first read-only pilot** and requires scope review and owner approval.
6. **Minimal durable state** after existing Neon/Google data-location decision: idempotency key, cursor/checkpoint, job status, source link, selection reason, next review date, prompt/model and quota metadata (never raw secrets). If task-state store is Google Sheets, avoid duplicate state in Neon; decide later.
7. **Notifications**: summary/report via existing authorized ChatGPT/Gmail pathways first; avoid self-emailing and excessive notifications. Notification route and receiving account permissions need verification.

**Why not adopt n8n Cloud now?** n8n hosted plan is time-limited trial, while n8n Community is software-only and needs independently free hosting. **Why not Google ADK first?** ADK is a free code-first agent framework, not a free cloud host; it adds complexity before one short Gmail workflow is proven. **Why not Activepieces as default?** It is a renewable Free hosted-GUI alternative, but separate API key compatibility, AI credit model, metadata/privacy/OAuth and job-state ownership must be validated. Keep Activepieces/Neon as comparators, not default second production executors.

### Google official free quota snapshot (consumer Gmail, 2026-11-12)

Google Apps Script documentation currently lists **90 minutes/day aggregate trigger runtime**, **6 minutes/execution**, **20,000 email read/write (excluding send)/day**, **20,000 URL Fetch/day**, and up to **20 triggers per user per script**. Recipient quotas and Gmail API quotas are separate; no authorization to send. The reset and quota semantics must be read from official docs and re-verified at execution. This quota is NOT a number of agent tasks or Gemini inference requests.

Gemini quotas: **per project, not per API key**; model-specific RPM/TPM/RPD, RPD reset at midnight Pacific; view actual limits in AI Studio. Model free credits are conditional on the current project/tier, geographic and privacy terms. No inferred "messages per day" from token quotas.

**CRITICAL PRIVACY GATE:** Google's Gemini API **Unpaid Services** terms say submitted input and generated responses can be used to improve products and human reviewers may inspect them; they say **do not submit sensitive, confidential or personal information**. Therefore **do not send raw personal Gmail, private hiring correspondence, identifying employer/person data, CV personal fields, tokens or attachments to unpaid Gemini**. Co-locating Gmail and Gemini under Google does NOT waive this transfer risk. In P0 use metadata and deterministic rules; use Gemini only for public job-ad descriptions after sanitization and review of redistribution rights. Full private-mail AI analysis remains BLOCKED until an appropriate privacy-compliant processing path is chosen.

**OAuth/security gate:** Gmail API read/compose scopes are RESTRICTED; send scope is SENSITIVE. A public OAuth app can require verification and, if restricted-scope data is stored or transmitted to servers, a security assessment. Exact obligation for a private single-user Apps Script setup needs verification. No scope expansion, script trigger creation, cloud export, automatic email send, or provider billing activation is authorized by this README.

## 5. Site scope and progression

Previously owner-identified **email-triggered site follow-up set**, only when permitted: **Creativepool; Joberz (exact platform identity/domain to verify); Voice123; LinkedIn; iEstekhdam**. Do not silently widen this exact five-source flow. Existing other sites such as freelancermap, 404Works, LaborX or Jobbers.io belong to a *separate future public-listing discovery* workflow with its own approved eligibility/site constraints. Check terms for scraping, account automation and proposal sending per site; never bypass CAPTCHA, KYC or restrictions.

For target opportunities record: link, timestamp, employer source, freelance/contract vs employment, remote/country/visa eligibility, verifiable ability to work and receive payment, estimated budget, required skills, deadline, risks, match confidence and clearly cited facts. Human verifies employer-specific commitments, portfolio claims, proposal pricing, delivery promises and visa/legal conditions.

## 6. Phased development plan / approval checkpoints

**P0 — REGISTER & RESEARCH (THIS COMMIT: DOCS ONLY).**
- Write this project home and a one-line current-status pointer; retain earlier research and existing running Gmail automations unchanged.
- Next scoped check: actual Google Apps Script / Gmail OAuth / Gemini API account-specific free eligibility & permissions, and existing task overlap. No new account access.

**P1 — Synthetic workflow prototype (only after approval).**
- Deterministic mock email threads; zero private Gmail content, external calls or SMTP sends; prove labeling, dedup, classification, audit, resume from cursor, zero sends.
- Acceptance: identical synthetic message processed once; unsafe/unmatched items held/rejected; no real contact affected; all state transitions attributable.

**P2 — Bounded Gmail read-only pilot (requires separate OAuth and read approval).**
- Small allowlist + time window + limit of real messages, metadata-first; read only owner-approved candidate threads; no draft, send, mark-read, move, delete or site login; use exact approved scopes.
- Acceptance: correct identification, no side effects, stop on permission/quota/errors, readable Persian evidence report with source links and data-minimized logging.

**P3 — Qualification and draft preparation (new approval).**
- Public offer sanitization and optional Gemini free call, measurable quality and quota; create Gmail draft after owner review of scope. Dedupe across sources and existing ChatGPT automations.
- Acceptance: draft pertains to right sender/thread, no invented skills/payment/commitment, no external send.

**P4 — Reply/follow-up automation (new approval).**
- Read reply threads, flag human replies, suggest follow-up date, create follow-up drafts, notify user. Confirm whether existing ChatGPT automations are replaced or remain distinct. Send operations stay human-reviewed by default.
- Acceptance: no duplicate chasers, no spam, correct reply-thread linking, clear reminders and exception logs.

**P5 — Controlled outreach/site workflows (new independent approval per account/site/action).**
- Official APIs/RSS first; browser session use only if allowed. Prepare tailored resume/proposal; automatic submission or outbound email restricted to exact user-approved action templates/campaign bounds and revocable emergency stop.
- Acceptance: proof of permissions, human audit, no CAPTCHA/KYC circumvention, 0 unauthorized sends, correct site confirmation and reply detection.

**P6 — Hybrid Windows integration (new approval).**
- On laptop reconnection Windows MausBot agent pulls relevant accepted cloud task outcomes via least-privilege API, acknowledges with idempotency; no public inbound port, no local-gateway exposure, no assumption that local OmniRoute is online while laptop off.
- Acceptance: cloud completes while laptop off, later sync correct, no duplicate execution, clear owner of every task.

### Tests, observability, stopping

- Test expired OAuth, revoked scope, Gmail historyId expired HTTP 404 (full resync), 429 quota, 5xx network, changed source content, duplicate notifications, malicious prompt-injection in email, missing data, model unavailability, API cost threshold, VPN/local disconnect, reply with ambiguous identity, failed draft, partial completion and overlapping schedules.
- Record only sanitized run IDs, timestamps, source classification, decisions, model IDs/quota consumption, errors/retries and human approval receipt. No email bodies or secrets in logs.
- Default all write paths and outbound communication to **DENY** until separately approved; unexpected paid quota/overage → STOP, never auto-upgrade/charge; no speculative accounts or infra. Budget cap per day first; model call count and cost measured in pilot.
- Production DONE only with real authorized I/O, durable state, documented failure behavior, test evidence, security, rollback, alerts, quota checks and owner-usable value; a design file alone is NOT OPERATIONAL.

## 7. Decisions taken now vs NOT decided

**Owner-approved now:** make this Gmail-centered cloud agent the **NEXT DJMRN PROJECT**; preserve full scope in GitHub; prefer Google-first investigation with existing free-provider accounts and eventual Windows team cooperation.

**Proposals, not decisions:** Apps Script as initial scheduler, Advanced Gmail API + least privilege OAuth, Gemini public-only analysis, Google Sheets vs existing Neon as job-state authority, 3-hour recurrence, any model/rule threshold, automatic send policy, site integrations, chosen notification channel. Choose after test and explicit authorization.

**Unknown/blocked:** whether existing Gemini free access is allowed for current project and location; if Gmail restricted scopes require verification/security assessment in proposed usage; account-specific free quota and active scripts; best authorized processing for sensitive email; site permissions; whether local agent UI can consume cloud results; one canonical state store; any billing/overage. Unknown cost or data rights = DENY action.

## 8. Official evidence and existing project links

**Google:**
- Apps Script installable time triggers: https://developers.google.com/apps-script/guides/triggers/installable
- Apps Script quotas: https://developers.google.com/apps-script/guides/services/quotas
- Apps Script advanced Gmail API: https://developers.google.com/apps-script/advanced/gmail
- Apps Script scope authorization: https://developers.google.com/apps-script/guides/services/authorization
- Gmail API OAuth scopes / restricted data: https://developers.google.com/workspace/gmail/api/auth/scopes
- Gmail API synchronization/history: https://developers.google.com/workspace/gmail/api/guides/sync
- Gmail threads/headers: https://developers.google.com/workspace/gmail/api/guides/threads
- Gmail drafts and send: https://developers.google.com/workspace/gmail/api/guides/drafts
- Gemini API Free pricing: https://ai.google.dev/gemini-api/docs/pricing
- Gemini per-project rate limits: https://ai.google.dev/gemini-api/docs/rate-limits
- Gemini unpaid data terms: https://ai.google.dev/gemini-api/terms

**DJMRN internal references:**
- Existing cloud/free comparisons: ../RESEARCH-AND-OPEN-QUESTIONS.md
- Existing Windows agent team: ../README.md
- Single canonical ongoing project status: ../../07-operations-and-continuity/CURRENT-STATUS.md
- Existing opportunity hunter: ../../09-opportunity-hunter/STATUS.md
- Existing model quota policy: ../../02-project-management/FREE-CLOUD-MODEL-QUOTA-AND-ROLE-ROUTING-POLICY-20261025.md

**Next user-approvable action:** Read-only P0 verification of account-specific Google quotas/rights and compatibility, conflict/dedup review of existing three scheduled Gmail reports, and design of the smallest safe synthetic test. Do NOT deploy or request secrets in chat.

**Continuity rule:** This README is project charter/research/specification. All future daily execution progress and most-current state must live only in the single canonical CURRENT-STATUS.md when owner explicitly asks for saving. Other documents remain supporting artifacts; no parallel state authorities.
---

## 9. Google Agent Development Kit (ADK 2.0) — Cloud Multi-Agent Extension

**Research date: 2026-11-12.** Owner explicitly directed including ADK in this exact cloud Gmail opportunity project. **Status: DOCUMENTED / EVALUATION CANDIDATE / NOT DEPLOYED.** This is a part of DJMRN-CLOUD-GMAIL-OPPORTUNITY-001, not a second project or new running agent. No installation, model activation, IAM/Google account permission, OAuth grant, deployment or fee has been authorized.

### 9.1 Identity, version, licensing and purpose

- **Google Agent Development Kit (ADK)** is Google's modular, code-first, open-source framework for building, evaluating and running AI agents, including multi-agent coordination. License: **Apache-2.0**. Official source: https://github.com/google/adk-python ; documentation: https://adk.dev/ .
- **ADK 2.0 is now current**. Official GA dates: Python 2.0 **May 19, 2026**; Go 2.0 **June 30, 2026**; TypeScript 2.0 **August 21, 2026**. Docs: https://adk.dev/2.0/ . Existing old ADK 1.x examples require compatibility review.
- Official Python package: google-adk, with Python **3.11+** in the current pyproject metadata. Current project machine/package compatibility, installed version and running state are **UNVERIFIED**. Source: https://github.com/google/adk-python/blob/main/pyproject.toml .
- **ADK software is free, but it is NOT itself free cloud hosting, an always-on server, an OAuth grant, a Gmail mailbox account, a scheduler or free Gemini inference.** All external model/host/identity/privacy quotas and terms are separate.

### 9.2 ADK 2.0 capabilities relevant to this project

| Capability | Value for the DJMRN job-follow-up project | Important limit |
|---|---|---|
| Multi-agent coordinator and subagents | Intake, opportunity review, proposal composing, QA, reply tracking | Roles do not justify deploying all agents at once |
| Graph / dynamic workflow execution | Conditional task routing, loops, deterministic decisions, retries | Use plain deterministic code if sufficient |
| Agent-as-tool and delegation | Specialist can return a review to coordinator, or receive handoff | Explicit ownership and approval rules needed |
| Tool calls: functions, OpenAPI, MCP and integrations | Reuse Google and other approved tools | Tool availability is not an authorization grant |
| Tool confirmation / human-in-the-loop | Gate Gmail sends, site application, meeting invitations and financial commitments | Actual approval is user's decision, not a model instruction |
| Evaluation / tracing / sessions | Compare failures, quality, workload and costs | Do not store credentials, private mail or tokens in insecure session state |
| Model-agnostic design | Gemini primarily; other providers may be possible | Groq/OpenRouter and tool-calling compatibilities need separate real tests |

Evidence: https://adk.dev/2.0/ ; https://github.com/google/adk-python ; https://adk.dev/tools-custom/function-tools/ ; https://adk.dev/integrations/ .

### 9.3 Critical native integration: Google Apps Toolsets with Gmail OAuth

Google now provides **official Google Apps Toolsets** for ADK, supporting **Gmail, Google Calendar, Docs, Sheets, Slides and YouTube**. The toolsets are built from the respective Google API discovery definitions and handle OAuth 2.0 authentication. Documentation says **Python supported starting v1.0.0** and **TypeScript supported starting v2.4.0, experimental in TypeScript**. Official: https://adk.dev/integrations/google-api-toolsets/ .

**DJMRN use case:** a future ADK agent could locate/read appropriate Gmail threads, extract public opportunity details, coordinate an analyst and an independent reviewer, prepare an owner-reviewable response, watch for a reply and update selected durable job status. Calendar/Sheets integration might support approved appointment preparation and status reporting. This is only a conceptual capability until OAuth scopes, API methods and actual data handling are tested.

**Security boundary:** Automatically generated toolsets can expose APIs that mutate accounts. **Do not provide the model with a full write-capable Gmail/Calendar toolset.** Start with explicitly allowlisted Gmail read-only methods and least-privilege OAuth; use independent owner approval for Gmail Drafts, sending/replying, labeling/deleting, account changes, Calendar invitations or employer-site submissions. The Gmail body-reading scopes are restricted; relevant verification and security assessment requirements are account/use-case dependent and need a dedicated review. **Gemini API keys cannot authenticate Gmail**. Never pass credentials, passwords, cookies, OTPs or refresh tokens into GitHub, prompts or unsecured agent session states. ADK docs warn explicitly about token security. References: https://adk.dev/tools-custom/authentication/ ; https://developers.google.com/workspace/gmail/api/auth/scopes .

### 9.4 Logical roles, not necessarily independent cloud processes

1. **Cloud Gmail Observer (Read only):** identify new message/thread IDs, check sender and trusted source; do not change mailbox state.
2. **Deterministic Eligibility Checker:** contract/freelance classification, location, remote, payout feasibility, fit, deadline, fraud signals and duplicate checks.
3. **Opportunity Analyst:** use only approved public/non-sensitive job information for optional Gemini calls; no raw private email in unpaid Gemini.
4. **Research Verifier:** validate public job listing link, company evidence, working conditions and policy conflicts before recommendation.
5. **Proposal Composer:** draft Persian/English reply using an approved public portfolio and verified facts; cannot invent skills, cost, deliverables or availability.
6. **Quality/Safety Reviewer:** spot hallucinations, privacy issues, duplicate outreach, policy violations and unfair/wrong matching.
7. **Follow-up Tracker / Coordinator:** monitor actual replies and create reminders; maintain one authoritative task ID/state; escalate sending/meeting/application to human.

**Initial pilot = one small workflow, not seven running agents.** Only grow into coordinator/specialist ADK calls if their benefit is measured. The Windows MausBot/OpenMausBot team stays the owner of local Windows tasks, with outbound pull/sync when laptop reconnects.

### 9.5 Decision: Apps Script first, ADK as the advanced agent layer

**Option A — Minimal Google-first deployment candidate:**

Gmail API (owner-authorized read-only) -> Google Apps Script time-trigger -> rule-based filter / source IDs / dedup -> optional privacy-safe Gemini API -> one chosen durable store -> owner notification -> separately approved Gmail drafts.

- This is smaller, simpler, time-triggered and needs no long-lived ADK server.
- Google Apps Script has consumer quotas (90 minutes/day aggregate trigger time; 6 min/execution; 20,000 email read/write operations and 20,000 URL Fetch calls per day) that do NOT equal Gemini model quotas. Official: https://developers.google.com/apps-script/guides/services/quotas .
- If this covers real use, do not build additional runtime/agents.

**Option B — Advanced multi-agent upgrade if evidence requires:**

An approved scheduler (Apps Script or other existing capability) -> **one ADK service/worker** -> specialized agent and tool calls -> **one** canonical job-state store + Gmail-owned messages/drafts -> gated, human-reviewed outgoing action -> optional Windows sync.

- ADK = agent semantics and tool orchestration; scheduler = clock/event trigger; Gmail = message authority; selected DB = job-state authority; Gemini/other approved API = model inference; Windows team = local executor.
- Do not build second scheduler/queue/DB just because ADK supports multiple agents.
- Cloud service must remain **authenticated and private**. ADK Cloud Run docs describe deployments, service accounts, secrets, build permissions and multiple-agent services; an unauthenticated endpoint connected to Gmail is unacceptable. Source: https://adk.dev/deploy/cloud-run/ .

### 9.6 Cloud hosting, free limits and cost caution

**ADK != free unlimited 24/7 cloud processing.** Google Cloud Run offers a measurable **monthly free allowance** but can bill beyond free limits and depends on region, billing and resource configuration. Request-based Cloud Run pricing currently describes up to **2 million free requests per month** plus vCPU/RAM free allowances; a call is not equivalent to a completed AI-agent task. Cloud Build, Artifact Registry, Secret Manager, networking, Cloud Scheduler and model calls have distinct quota/cost conditions. **Billing account and overage handling must be verified; do not enable billing or deploy without explicit approval.** Source: https://cloud.google.com/run/pricing .

Google-managed Agent Engine / Agent Runtime is another possible ADK deployment target; current personal-account free eligibility, sessions/memory pricing and total cost are **UNVERIFIED**. Under FREE-FIRST, unknown cost = **DENY activation**. Gemini free inference has its own project/model RPM/TPM/RPD and geographical restrictions. The Google **Unpaid Services data terms** may allow submitted data to be used for product improvements and human review: **do not send raw private Gmail or confidential employer correspondence, personal CV fields, account identifiers or secrets to unpaid Gemini**. Source: https://ai.google.dev/gemini-api/terms .

### 9.7 Proof gates before ADK adoption

- Compare **the same synthetic 10 email threads** in deterministic Apps Script and a minimal 1-coordinator/1-specialist ADK workflow, only after independent future approval. Measure output accuracy, false positives, missing requirements, token costs, CPU/time, operational complexity and maintenance.
- Verify read-only Gmail method allowlists and simulate prompt injection from malicious email body that requests sending email, exfiltrating secrets, downloading files or bypassing approval: expected result = **DENY**.
- Validate owner review for every draft/send action, thread ID correctness, retries, idempotency, Gmail history cursor expiry, OAuth revocation, 429/5xx, deployment cold-start and outage, notifications and immutable audit.
- Prove the cloud job can execute while laptop is off, save durable state, then synchronize by authenticated outbound Windows pull without opening the Windows PC to the public internet.
- Before cloud deployment require an explicit cost report including Gemini and runtime quota limits, hard non-paid stopping policy, account-region eligibility, IAM scopes, security and rollback.
- **Promotion criterion:** ADK must deliver a demonstrated, meaningful benefit over the smallest Apps Script pipeline (e.g. superior multi-stage verification / structured delegation) while meeting Free-first, privacy, security and reliability criteria.

### 9.8 Official references and final classification

- ADK 2.0 GA releases/workflows: https://adk.dev/2.0/
- Apache-2.0 / Python package / README: https://github.com/google/adk-python
- Python dependency requirements: https://github.com/google/adk-python/blob/main/pyproject.toml
- Direct ADK Gmail/Google Apps tools: https://adk.dev/integrations/google-api-toolsets/
- OAuth tool authentication and token safety: https://adk.dev/tools-custom/authentication/
- Agent-as-a-tool / delegation: https://adk.dev/tools-custom/function-tools/
- Cloud Run deployment: https://adk.dev/deploy/cloud-run/
- Cloud Run allowance and pricing: https://cloud.google.com/run/pricing
- Apps Script quotas: https://developers.google.com/apps-script/guides/services/quotas
- Gmail OAuth scope classes: https://developers.google.com/workspace/gmail/api/auth/scopes
- Gemini Unpaid Services terms: https://ai.google.dev/gemini-api/terms

**PROJECT DECISION STATUS:** ADK 2.0 is **explicitly retained as a FIRST-CLASS, ON-DEMAND candidate for future cloud multi-agent logic**; Apps Script remains the smaller P0 candidate. No software deployed, no OAuth grant added, no new application or model paid for, no unrelated documents changed and no authorization to send messages granted by this registration.
