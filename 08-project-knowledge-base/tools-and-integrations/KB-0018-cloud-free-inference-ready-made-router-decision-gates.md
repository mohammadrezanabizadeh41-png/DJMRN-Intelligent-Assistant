# KB-0018 — Ready-made Cloud-First LLM routers, legal free quotas and decision gates

**Date:** 2026-10-23 | **Status:** CURATED / RESEARCH ACCEPTED-PARTIAL / NO ADOPTED STACK OR PROVIDER / D-005 OPEN / G3B CLOSED.
**Evidence:** [WA0011](../../04-work-research-bridge/responses/WA0011.md), [coordinator WQ0011 review](../../04-work-research-bridge/reviews/WQ0011.md), [WA0012](../../04-work-research-bridge/responses/WA0012.md), [coordinator WQ0012 review](../../04-work-research-bridge/reviews/WQ0012.md), [WQ0012 request](../../04-work-research-bridge/requests/WQ0012.md); source pointer SRC-0020/SRC-0021 in [Source Register](../SOURCE-REGISTER.md). This is a selective synthesis, not an independent full vendor/source, regional or security audit.

## User's practical goal
Persian chat-first DJMRN on Windows 11 with 8GiB RAM (historically ~5.88 GiB OS usable), heavy reasoning in permitted cloud APIs, light local data/control/trusted executor. Shared stable loopback endpoint eventually for more than one real client; no need to use heavy local models simultaneously, but preserve existing weights/engines and CAP-006 file-access boundaries. **Cloud-First is the user's direction for evaluation, not approval to activate a provider or install a gateway.**

## Verified distinction vs unverified implementation

| Finding | Evidence and uncertainty | Consequence |
|---|---|---|
| WA0012 delivered 26 candidate rows/10 deeper source audits | Work original 73,960-char response; commit `58ee256e09f19b1a286150bc07692f0d9b827ce3`, blob `a3ccd0d76539a7655fdcb3fd5aa839b8b92fa851` independently matched; third-party behavior not run | useful source atlas, not an installed tested product |
| Two different Bifrost owners | separate real GitHub `maximhq/bifrost` and `boelabs/bifrost`; Work source comparison | never merge codebase/release/role/dependencies |
| SDK/gateway/model registry/hosted provider are different layers | WA0011 & WA0012 products | a list of free models doesn't grant account usage or quota |
| Publisher quota/budget/free claims | WA0012 provider region delta, FREE_MODEL_AUTO_DISCOVERY_AUDIT; user account not inspected | renewable free/remaining/reset/true hard spending cap UNKNOWN/DENY |
| Regional use and upstream legality | no complete provider+upstream entitlement for user Iran confirmed | no VPN/account rotation or unapproved activation |

## Conditional ready-made shortlist (NOT winners)
- **NO_NEW_GATEWAY / STOP NOW:** provider/model entitlement must be proven first. If it is, a single existing GUI with one model pinned may be enough for the first synthetic chat pilot; require separate approval and enforce zero spend.
- **Maxim Bifrost (general gateway):** broad HTTP compatibility and routing in source/docs, but exact OSS release edition, security, Windows RAM/background lifecycle, quota truth and user region remain HOLD. Different from BoeLabs Bifrost, whose Bun/Postgres/Redis footprint adds complexity.
- **freelm (light SDK/optional local server):** reduced dependency candidate; must prevent keyless use, simultaneous hedged calls, unsafe auto-fallback, paid charges and unauthenticated endpoint. Durable per-client quota reservations unproven.
- **freellmpool (catalog + SDK/proxy):** distinguishes free/trial/disabled groups in catalog, not proof of legal recurring grant for a real account. Restrict to explicit verified allowlist, don't auto-admit everything marked free.
- LiteLLM Proxy, Portkey, Arbiter, New API/One API, Ficelle, Hadrian, Kaiser free-llm-proxy-router and others remain possible comparator leads with edition/license/state/security/Windows holds.

## Hard acceptance gates before selection (all NOT PASSED)
1. **G1 law/regional rights:** terms and upstream Iran availability, actual commercial/account/card/KYC eligibility; UNKNOWN → DENY.
2. **G2 recurring API free and hard-zero liability:** exact model ID, quota scope (account/org/model), authoritative reset, true spend cap including auto top-up/overage; a spending dashboard alone is not hard stop.
3. **G3 privacy/security:** loopback authentication, narrow egress/secret and logs, per-client access, prompt/tool safety; no raw prompts/API secrets exported or collected in project.
4. **G4 capability/quality:** Persian, programming, tool-call schema, structured output, context/streaming actually fit; no fallback to an unqualified weaker or paid route.
5. **G5 resource/recovery:** Windows actual RAM idle/peak, startup/reboot, durable quota ledger and two-client concurrency; never infer from Go/Python binary size.

**Failure behavior:** distinguish 429 minute throttle from exhausted daily quota; 401 account/auth; 403 territory/rights; 402 money/budget; 5xx/timeout; disconnected stream/unknown cost; provider reset from authoritative timestamps only; safe stop with no routes. Inference replay must NOT re-execute filesystem/PowerShell/Gmail actions. Future mock-only tests need separate authorization.

## Next evidence with highest value
Acquire official public account/provider eligibility and hard-zero free renewal evidence for one exact model/user situation; if impossible, remain STOP. Only after that compare direct single-client against one lightweight localhost proxy/gateway with pinned release and measured Windows test proposal. User next requested a platform-neutral copyable third-party research brief; the result must be independently reviewed before registering project data. Do not create WQ0013 or install a service just because research exists.

**Evidence strength:** Git artifact identity VERIFIED; product implementation claims source-verified only where reported; actual user account/provider entitlement and Windows gateway runtime UNKNOWN. No architecture decision D-005 taken.
