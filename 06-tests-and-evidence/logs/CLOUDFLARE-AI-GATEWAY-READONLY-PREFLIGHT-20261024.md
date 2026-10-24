# DJMRN — Cloudflare AI Gateway account read-only preflight (2026-10-24)

**Evidence type:** Public official documentation only (not account proof). **Status:** RESEARCHED / NEXT_WEB_PILOT_PENDING_ACCESS_CHECK / NO_ACTION. **Main repo:** `mohammadrezanabizadeh41-png/DJMRN-Intelligent-Assistant`, `main`, public.

## Cross-window continuation
The existing [full router handoff](../../07-operations-and-continuity/ROUTER-WINDOW-RESTART-HANDOFF-20261024.md) and canonical `CURRENT-STATUS.md` remain authoritative. OmniRoute Windows Setup 3.8.52 was user-reported blocked without a diagnostic log (HOLD, not product rejection). Bifrost 2.3.2 Windows ran SQLite migration, then exited on pricing-catalog timeout (no real cloud inference); synthetic GitHub CI tests are not provider entitlement evidence. D-017 orders Cloudflare AI Gateway second, then New API third. Twenty-seven candidates are retained; D-005 OPEN, G3B/M1 CLOSED.

**Goal:** hosted or GUI central OpenAI-compatible gateway for High/Medium/Light model tiers, per-assistant quotas, protected strong-model allowance, auditable free-only routing and fallback, new free-model discovery, ease of transfer, and no manual daily PowerShell. These capabilities are *acceptance requirements*, not implementation claims.

## Vendor facts checked 2026-10-24
1. Core AI Gateway features (analytics, caching, rate limiting) available on all plans for free; this does **NOT** make upstream inference free. Official pricing: https://developers.cloudflare.com/ai-gateway/reference/pricing/
2. Dynamic Routing (Beta) offers visual condition nodes, rate/budget limit and model/fallback nodes; deployed per-gateway routes. Account-level entitlement and true free-only fail-closed behavior are **UNVERIFIED**. https://developers.cloudflare.com/ai-gateway/features/dynamic-routing/
3. Dynamic routes take OpenAI-shaped chat completion requests. The dynamic-route use of legacy compatibility endpoint requires confirmation because standard single-model compatibility endpoint is marked deprecated; integration with user's assistants is **NOT TESTED**. https://developers.cloudflare.com/ai-gateway/features/dynamic-routing/usage/
4. **Important cost trap:** an authenticated request can auto-create a default gateway with **Workers AI Standard billing**, logging ON, rate-limit OFF and "Require provider credentials" OFF. **Do not create or test the gateway with an API request** before billing review. https://developers.cloudflare.com/ai-gateway/configuration/manage-gateway/
5. For external providers, "Require provider credentials" (`byok_only=true`) is documented to block fallback to Cloudflare Unified Billing if no matching BYOK key is available. This **does not protect Workers AI from its separate billing mode**. Unified Billing requires purchased credit (5% fee) and may charge negative balances; deny. https://developers.cloudflare.com/ai-gateway/features/unified-billing/
6. Workers AI Free allocation published as **10,000 Neurons per day**, resetting at 00:00 UTC; a number of high-end models require paid access. Workers Paid bills usage exceeding Free. Account plan/model eligibility NOT checked. https://developers.cloudflare.com/workers-ai/platform/pricing/
7. No independent confirmation of *automatic discovery of new cross-provider free models*, or *per-account exact remaining free tier quota*, from docs alone. Both are mandatory tests, not claimed PASS.

## Immediate approved scope: read-only GUI inspection
- User opens https://dash.cloudflare.com/ and, only if already registered, signs in normally. Navigate **AI > AI Gateway**.
- Inspect whether Gateway and Dynamic Routes appear, plus visible plan/billing status. No new account, no **Create Gateway** click, no keys, no paid routing or tokens, no provider calls, no secret transfer.
- A screenshot may show page navigation and availability only; redact account IDs, email, billing details, API keys and any personal identifiers.
- Mark result as ACCOUNT_UI_VERIFIED or BLOCKED after evidence. If required functionality/free-only constraints fail, move sequentially to **New API** according to the existing queue.
- Separate explicit user permission is needed for any gateway creation, billing config, account connection, API/inference test, deployment or rights/security change.

**Conclusion:** Cloudflare is a plausible hosted next candidate, **not selected architecture and not proven to meet automatic free discovery or hard cost-zero**. No Windows or cloud action was carried out by this documentation step.
