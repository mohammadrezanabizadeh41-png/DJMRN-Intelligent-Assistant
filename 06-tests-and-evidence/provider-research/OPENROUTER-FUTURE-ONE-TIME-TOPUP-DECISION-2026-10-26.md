# DJMRN future option — OpenRouter one-time $10 purchase
Date researched: 2026-10-26
Status: **DEFERRED — NO PURCHASE AUTHORIZED**

## Official published rule
- Without $10+ cumulative purchased credits: free models limited to 50 requests/day and 20 requests/minute.
- Once an account has **purchased at least $10 in credits**, free model allowance rises to **1,000 requests/day**, while the 20 requests/minute limit remains.
- Official OpenRouter tutorial describes this as a **one-time purchase**, not monthly subscription. It does **not** require repeated monthly deposits under current policy.
- The quota applies at account/free-model level, **not per model**.
- Official sources: https://openrouter.ai/pricing ; https://openrouter.ai/blog/tutorials/how-to-get-the-lowest-cost-llm-inference-on-openrouter/ ; https://openrouter.ai/blog/tutorials/sillytavern-openrouter/

## Permanence caveat
- Do **not** describe the increase as guaranteed forever. Service policies and limits can change.
- OpenRouter Terms section 4.2 reserves the right to expire unused credits 365 days after purchase: https://openrouter.ai/terms ; support https://openrouter.ai/support/ .
- Whether the free-tier quota uplift persists after the *purchased balance itself* expires is **NOT EXPLICITLY GUARANTEED** by the reviewed documentation; reconfirm before purchase, ideally with provider support.
- One OpenRouter tutorial says the deposit 'never expires', but the formal Terms reserve the right to expire unused credits; **terms take precedence for planning**.

## Costs / governance
- Nominal purchase threshold **$10 of credits**; transaction fees/taxes/payment method must be verified at checkout before approval. Platform purchase fee may apply.
- Free model token prices are $0, but paid model calls or paid fallback may spend credits; enforce free-only model slugs and failover, spend controls and per-key cap.
- Existing `DJMRN-OmniRoute` API key has $0 total limit; test free requests first, and investigate whether key limit needs adjusting for free calls. No automatic adjustment.
- User account screenshot showed $0 balance, 0 transactions on 2026-10-26.
- Do not add payment method, enable auto-top-up, buy credits, change key limits, or activate paid models without **explicit user approval**.

## Future follow-up checklist
1. Reconfirm pricing and eligibility rule from official docs on purchase date.
2. Ask OpenRouter whether uplift persists after unused credits expire, balance reaches zero, or account changes plan.
3. Check exact all-in price, fees, tax, card/crypto availability, refund policy.
4. Compare benefit against other free providers (Groq, Gemini, Mistral, Cloudflare, NVIDIA, Cohere).
5. Verify zero-cost free-model routing and prevent paid fallbacks.
6. Present recommendation and request explicit user approval before any payment.

## Decision
**Park for later**. Potential 20x increase in daily free request capacity for one-time minimum $10 purchase under current published policy; permanence not guaranteed.
