# KB-0020 — مسیریابی بر اساس توان مدل و حفاظت از سهمیه رایگان | Capability-Tiered Cloud Model Routing
**Recorded:** 2026-10-23 | **Status:** USER-REQUESTED FEATURE / CURATED DESIGN / NOT BUILT / NOT TESTED | **Aliases:** smart tier routing, model intelligence tier, reasoning levels, quota reserve, cloud-first, cost-free fallback, capability routing, LLM routing policy, سه سطح هوش، سهمیه روزانه.
**Context:** User requested a central router serving all downstream DJMRN programs with free cloud models, then explicitly asked if it can assign light/medium/reasoning-intensive tasks to different model levels so scarce high-capability free allowances remain available. **Yes as an architectural policy, not a completed Maxim Bifrost feature/test**.
**Authority:** [Scoped D-016 Maxim Bifrost router choice](../../02-project-management/DECISION-REGISTER.md), [routing evidence/guardrails](../../03-architecture-and-tools/CLOUD-FIRST-BIFROST-ROUTER-CANDIDATE-20261023.md); [WA0011](../../04-work-research-bridge/responses/WA0011.md), [WA0012](../../04-work-research-bridge/responses/WA0012.md), [KB-0019](../tools-and-integrations/KB-0019-six-external-cloud-gateway-reports-reconciliation.md); user request 2026-10-23. Notion Applied/General/Tool Governance consulted 2026-10-23. Independent official source: [Maxim Bifrost v1.5.0 routing/governance/model aliases](https://docs.getbifrost.ai/changelogs/v1.5.0), [Bifrost gateway README](https://github.com/maximhq/bifrost). **Edition, OSS availability, behavior, and Windows performance need pinned checks.**

## Functional objective — preserve actual task quality while reducing precious free quota consumption
Many client programs -> one authenticated localhost API endpoint (preferred Bifrost, not installed) -> **DJMRN routing policy** -> free-approved provider/model pool, with alternative members **within the same capability floor**. Clients can send a reliable explicit `task_class`/logical alias instead of assuming the router understands all Persian text. Prioritize deterministic mapping based on client task metadata; low-cost classifier or quality-based adaptive routing only if the deterministic rules demonstrably fail. An LLM classifier itself consumes quota and may misroute.

| Logical lane / proposed alias | Example workload | Minimum verified capability | Quota use recommendation |
|---|---|---|---|
| `djmrn-lite` | simple chat, short categorization, metadata extraction, elementary rewrite | Persian adequacy, schema if requested, low latency | prefer abundant/cheap free allowance; **never** use reserved advanced-tier quota automatically |
| `djmrn-standard` | emails summarization, document explanation, translation, simple coding | moderate reasoning + sufficient context; tools when required | fallback only among equal-or-better capability routes, monitor daily use |
| `djmrn-reasoning` | multi-file coding, architecture, debugging, deep planning/research | strong measured reasoning/coding and context/tool compatibility | reserve scarce free high-tier allowance for explicitly approved complex tasks; lower-tier downgrade only if explicitly authorized, otherwise fail honestly |
| `djmrn-specialist` | OCR/vision/audio/structured tools and restricted agent actions | exact modality, tool schema, privacy/legal rights | independent pool; never silently route vision/audio to text-only, or tool calls to non-tool-capable model |

**Model power is not a single scalar/B-parameter count.** Use evidence by task: Persian language, instruction fidelity, code tasks, function/tool calls, JSON schema, context window, image/audio and latency/reliability. A model can rank strongly at code but weakly at Persian. Classification policy must be explainable and overrideable.

## Quota accounting and admission — minimum routing policy
- Catalog for each provider credential+model: model ID, `tier`, capabilities and measured evaluation score, free API price type (recurring / temporary promotion / trial credits / unknown), exact provider terms, request RPM/RPD or quota units, reset timezone, service health and retry-after, model/context caps, last observation, verified evidence and expiry.
- A finite **protected reserve** (e.g., policy percentage chosen later, not an empirical quota) for high-reasoning routes; `available_balance` only counts locally observed or authoritative provider capacity; **unknown != unlimited**. Atomic/concurrent reservations matter if two or more programs share the account. Bifrost virtual key budgets/rate limits are **not proof of accurate upstream daily-free entitlement**. `freellmpool_sandbox` contains source-observed atomic allowance ledger, but is an **alternative**, not an automatically installed second gateway.
- Reject before inference if price is unknown/nonzero, provider not enabled/verified, request exceeds model capabilities, or no eligible free route left. No paid/intro-credit fallback without a new explicit separate approval.
- Handling: 429 with `Retry-After` does not identify minute versus day by itself; log cooldown and seek eligible *same-tier* alternate, distinguish auth 401/403, payment 402, provider 5xx/timeout, 400 incompatibility; controlled retry budget. No automatic account rotation/consumer subscription bridging to evade limits.
- Streaming after the first emitted token, side-effectful tools, and exhausted whole pool cannot guarantee transparent continuity. Report clean `UNAVAILABLE_FREE_POOL` rather than promise permanent uptime. Existing local CAP-006 tool authorization and file guards MUST remain separate from gateway model switching.
- Classifier and model selection **MUST NOT** silently grant filesystem/PowerShell/web/email permissions; inference route != tool permission.

## Example acceptance tests — DESIGN ONLY
TIER-01 lite+standard request routed without reducing protected high-tier reserve.
TIER-02 reasoning request goes to a capable reserved route; response reports actual serving model.
TIER-03 lite 429 fails over only to approved compatible lite/standard (not protected reasoning).
TIER-04 advanced 429 -> another verified high-tier or clear unavailable; no silent downgrade.
TIER-05 global provider quota shared between two client identities with no oversubscription; restart retains reservations if chosen build supports it.
TIER-06 zero-cost-deny: unknown price, promo expiry, paid provider, 402, exhausted free budget => no bill and explicit stop.
TIER-07 tool-required request never selects text-only; failed stream cannot replay tool side effects.
TIER-08 account quota periodic reset re-enables a route **only after proven refresh and correct period**.
TIER-09 classify ambiguous Persian requests with deterministic client metadata before invoking a classifier; verify override and failure behavior.
TIER-10 restart/low-RAM Windows and exact OSS build tested later after separate approval.

## Decisions and open questions
**KEEP D-016** Maxim Bifrost evaluation preference; **new project functional requirement:** task tiers + provider-safe reserve + dynamic same-tier fallback + zero-overage. Not a claim Bifrost ships a free-tier inference-ranking model out of the box. Before design implementation choose policy placement (small deterministic local function before Bifrost vs approved native Bifrost routing rules), exact version/OSS limits, model score method and provider evidence. **D-005 overall system not chosen; G3B CLOSED; no installation, external API, account or automated windows action authorized.**
