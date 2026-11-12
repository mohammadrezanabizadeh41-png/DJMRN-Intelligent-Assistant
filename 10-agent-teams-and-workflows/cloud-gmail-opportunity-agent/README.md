# DJMRN — ایجنت ابری پیگیری کارها، Gmail و فرصت‌های فریلنسری

**Project ID:** DJMRN-CLOUD-GMAIL-OPPORTUNITY-001
**Registered:** 2026-11-12
**Priority:** NEXT PROJECT — next planned execution workstream, not an automatically running service.
**Status:** PROJECT CREATED / SPECIFICATION & RESEARCH REGISTERED / IMPLEMENTATION NOT STARTED.
**Owner:** DJMRN; approval authority: the user.
**Repository:** DJMRN-Intelligent-Assistant, main.
**Scope:** Cloud-first monitoring, triage, draft preparation, reply-follow-up and later permitted job-site opportunity collection; integrates eventually with existing Windows agent team while laptop is offline.
**Safety/privacy:** This repository has been observed PUBLIC. No Gmail address, employer email, customer record, email body, personal identity, API key, OAuth token, secret, resume private details, browser session or credential is stored here.

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
