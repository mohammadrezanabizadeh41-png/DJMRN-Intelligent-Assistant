# DJMRN Opportunity Hunter — requirements snapshot (2026-10-28)

Status: user requirements captured; implementation and live integrations not yet validated.

## Confirmed requirements
- Discover opportunities across video/media, Persian voice, AI automation, Windows support, tourism, and other feasible AI-assisted work; include skill-development opportunities separately.
- Human handles professional negotiations and final contracts after an interested employer replies. Initial outreach should explain relevant experience, remote written communication, Iranian nationality, requested USDT payment, and possible later advance-payment discussion.
- USDT need not appear in an advertisement; it is a term to propose. Unknown payment methods should not cause rejection. Explicitly unpaid jobs are rejected.
- Missing information about nationality, language, phone, or credentials does not automatically disqualify a listing. Explicit incompatible mandatory requirements do.
- Reject independent projects estimated over 100 working hours or over 10 days, as well as unreasonably complex or unscopable work. Monthly employment is a distinct category; a fixed-deliverable project labeled contract is not exempt.
- No minimum advertised budget. For negotiable prices, user requests an evidence-based low competitive quote. Discounts of 30–50% were discussed as possible; no final discount policy or economic floor has been approved.
- Track positive, negative, ambiguous and absent employer replies separately; notify user for human review of positive replies.
- Preserve all previously registered sites as research candidates. Assess each site's permitted automation options separately; use compliant methods and account quotas for live actions.

## Proposed architecture, not yet built
Chrome / Ui.Vision -> extraction -> Python / SQLite ledger and dedup -> deterministic screening -> AGNT / OmniRoute analysis -> workload and pricing estimates -> personalized draft -> authorized send gate -> reply tracking -> human review. Keep low RAM use and on-demand processes.

## Verified local setup versus unverified features
User screenshots confirmed Ui.Vision MCP bridge connection on port 50888. Python with SQLite, Node, Chrome, AGNT, OmniRoute, and Task Scheduler are available. AGNT-to-MCP integration, real macro invocation, end-to-end automated submission, reply monitoring and pricing engine have NOT been tested.

## Open decisions
Geography/languages; actual written communication abilities; monthly employment schedule; whether five days is preferred and ten days maximum; pricing floor, discount algorithm, pricing currency, market sources and fee treatment; final outreach templates; permitted site-specific automation; response notification channel; duplicate and retry rules.

## Corrections
USDT is a negotiation term, not a search filter. Unmentioned restrictions are nonblocking, not known absent. The 100h/10d cap applies to standalone projects, not monthly employment. Assistant-suggested adaptive discount up to 50% is NOT approved.


## Architecture decision and reconciled roadmap — 2026-10-28
Decision: prioritize a small modular Python stdlib + SQLite implementation, reusing existing Chrome/Ui.Vision, AGNT and cloud models via OmniRoute, rather than installing three heavyweight engines. Treat this as a development direction, NOT evidence that integrations work. No extra permanent background processes. Three bounded modules:
1. Deterministic policy gate: explicit mandatory incompatibilities, unpaid requests, standalone project limits (>100 estimated hours OR >10 days), unknown/missing restriction is nonblocking, but insufficient evidence for time/cost estimates is review not invented certainty. AI extracts structured facts and estimates, Python validates rules. Distinguish "not mentioned" from "known compatible".
2. Per-site profiles: common baseline + site-specific overrides; confirmed user example: freelancermap reject employment/monthly roles even one month; LinkedIn allow employment roles for screening. Project-vs-employment classification based on obligations, not a 'contract' tag. Per-site access permission, quotas, message formats and response tracking stored separately. User example was expressed as desired behavior; do not assume all other sites inherit it.
3. Pricing prototype: estimate task decomposition/hours, collect grounded comparables, scope deliverables/revisions, compute proposal using a user-approved discount and economic floor. Suggested 30–50% discount is a possibility, NOT final authorization. No reliable comparable/floor => review, no invented quote. Employment salary proposals require separate policy.

External library audit: Python json-logic-py is available but old; evaluate only if complexity warrants it. Python stdlib json + explicit conditions likely sufficient for MVP. Ui.Vision officially documents macro CLI, JSON macros, and Task Scheduler workflows (https://ui.vision/rpa/docs/); exact installed feature licensing and bridge invocation must be verified locally. No Docker/WSL, local LLM, new rule daemon or pricing scraper required for initial prototype.

Execution order / acceptance gates:
P0 (now): requirements, exceptions, per-site profiles, pricing decision ledger in GitHub; no live outbound action.
P1: inspect current repo tree and existing Hub contracts, avoid duplicate ledger; define JSON schemas/SQLite schema and a site profile for freelancermap and LinkedIn.
P2: implement stdlib deterministic screening and 20+ synthetic tests: missing restrictions, explicit incompatible, unpaid, 99/100/101h, 9/10/11 days, uncertain scope, project labeled contract, genuine monthly employment, site overrides.
P3: implement simple time estimate + price calculation with explicit evidence, low-price floor and confidence; simulate, do not send.
P4: run Ui.Vision authorized read-only 10-listing pilot, capture URL/id/full details and SQLite dedup; measure RAM/CPU; bridge connection alone does not prove AGNT or macro control.
P5: AGNT/OmniRoute structured JSON extraction and draft handoff; validate output, quotas and error handling. Prevent prompt injection from listings.
P6: simulate initial proposals, message receipts, duplicate prevention and reply states (positive/negative/ambiguous/no reply); verify SEND_UNKNOWN handling.
P7: enable live site-specific permitted operations only after access/automation policy, quota, exact templates, quote floor and notification channel are settled; monitor and stop on unexpected behavior. No autonomous binding contract.

Estimated *engineering effort* for three offline modules and tests: roughly 14–26 hours, or 20–40 with basic integration; estimates are not measured and exclude real-site automation/debugging. One-week offline MVP is a target, not a guaranteed fully autonomous production launch. Do not force three independent services or models.

New recommendations:
- Rule precedence: platform-specific hard prohibitions/permissions > user safety and truthfulness constraints > site preferences > general preferences; keep a decision explanation and versioned policy for every record.
- Separate READ, DRAFT, QUOTE, SEND permissions and evidence receipts per site; keep site in research inventory even if automated SEND not allowed.
- Never automatically re-send when delivery status unknown. Keep per-site counters and human-visible audit log.
- Source/quote provenance and confidence fields; route ambiguous employment/project classification or uncertain estimate for review.
- Start with synthetic fixtures and a single permitted site, not mass messaging.

Open decisions needing explicit user input: 5-day target vs 10-day ceiling; economic floor and discount authority; employment hours/schedule, languages and geography; portfolio and actual skill evidence; initial message style; per-site permission and quotas; notification method. Do not make these choices silently.


## 2026-10-28 — User refinements: concise audit, permissions, employment economics
**Status:** user-confirmed requirements, not deployed. This section refines previous roadmap without deleting historical decisions.

### Decision logging — minimal, actionable
- For rejected opportunities store compact reason codes (e.g., UNPAID, EXPLICIT_LOCATION, HOURS_GT_100, DAYS_GT_10, SITE_EMPLOYMENT_BLOCK) and source listing ID; avoid verbose reasoning for every rejection.
- For selected opportunities intended for outreach store a short human-readable justification, relevant user capability evidence, proposed scope, estimated hours and deadline, proposed price with evidence and uncertainty, policy/profile version, draft/target, send state and receipt. Record positive/negative/ambiguous responses and status transitions.
- Keep storage minimal, inspectable and SQLite-based. No unrestricted model chain-of-thought logging.

### Separate permissions and website handling
- User expressly requests continuing to evaluate sites even when site warns against automation, arguing personal use; preserve sites in research inventory and don't conflate research eligibility with automation eligibility.
- However, the system must record actual platform restrictions and cannot treat personal intent as authorization to bypass access controls or site rules. Separate discovery/manual/alerts/API/read/draft/quote/send capabilities per site. If automated interaction is not permitted, use permitted methods and mark automatic action blocked rather than evading restrictions.
- READ, ANALYZE, DRAFT, QUOTE and SEND are distinct capabilities; only enable site-specific live SEND after a successful authorized test. Never retry uncertain sends without reconciliation.

### Employment-specific financial feasibility gate
- Distinguish standalone fixed-deliverable project from genuine monthly/part-time/full-time employment. Site override: freelancermap employment (even one month) rejected; LinkedIn employment allowed for evaluation. Other sites TBD.
- Employment economic analysis: effective hourly compensation = net realistically receivable monthly compensation / expected total hours (including meetings, admin, revisions, onboarding and unpaid overhead); assess weekly/monthly workload, schedule/timezone, fixed availability, task complexity, difficulty, learning, software/cloud fees, payment feasibility and sustainability.
- Project economic analysis: scoped fixed price vs estimated effective hours, direct costs, risk and revision allowance; standalone project caps 100 hours AND 10 days still apply.
- Different categories (e.g., video editing vs website engineering) require distinct skill/complexity multipliers, time baselines and reference-rate evidence. Do NOT hardcode unsupported market rates or assume all work is equally difficult. Price floor is category- and user-cost-sensitive, not a single arbitrary universal amount.
- Build a configurable category table (video, web, automation, voice, Windows, tourism, other) with verified skill evidence, effort baseline, uncertainty, minimum acceptable net hourly rate (user to approve), reference price source/date, and risk/overhead factor.
- For negotiable project prices, calculate competitive quote from grounded comparables, net hourly floor and scope. 30–50% below market is an option only, not an approved automatic discount. Employment monthly/hourly quotes are separate and require approved floor.
- If key compensation, hours, category or market evidence is missing, classify as NEEDS_REVIEW for pricing rather than invent numbers; missing *listing restrictions* remain nonblocking for initial eligibility screening.

### Updated implementation order and estimates
1. Inspect existing GitHub Hub, contracts and schemas; avoid duplicate authoritative database/queue (1–3 engineering hours).
2. Build minimal JSON per-site profiles + category economics config and SQLite audit schema (3–6h).
3. Implement deterministic eligibility engine with compact reason codes and test fixtures (4–8h).
4. Implement project estimate/quote and employment net-hourly feasibility calculations with tests (6–12h).
5. Run 10-record authorized read-only Ui.Vision pilot, measure memory, dedup and capture provenance (4–10h, depends on site).
6. Validate actual AGNT/OmniRoute structured extraction, drafts, outbound simulation, receipt and reply workflow (6–14h, depends on integration).
Total rough engineering effort 24–53h; a one-week offline MVP may be possible with focused work but full live site automation is not guaranteed. These are estimates, not measured durations.

### Open user decisions before production quoting/sending
Minimum net hourly rate per work category or initial shared floor, currency and fee assumptions; acceptable employment hours/week and schedules; 5-day preference vs 10-day cap; automatic discount maximum; languages and portfolio evidence; exact initial message; response notifications; per-site access and sending permissions. Start offline modules without blocking on all decisions.
