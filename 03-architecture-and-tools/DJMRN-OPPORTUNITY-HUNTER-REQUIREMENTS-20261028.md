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
