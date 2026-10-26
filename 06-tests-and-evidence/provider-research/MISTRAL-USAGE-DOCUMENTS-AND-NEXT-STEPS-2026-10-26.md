# Mistral onboarding — Usage, document controls, and handoff

Date: 2026-10-26. Evidence: user screenshots in chat. No API secret stored.

## Confirmed API usage (Admin → API → Usage)
- Selected date range: 2026-10-01 00:00 through 2026-10-26 15:17 (UI indicates UTC+3:30).
- Total API requests: **0**.
- Total estimated cost: **$0.00**.
- Charts: `No API requests for this period` and `No model usage for the selected filters`.
- This proves no recorded usage in selected period, **not** that model access has been tested.

## Document controls (Admin settings screenshot)
- Current effective maximum file size: **100 MB**. Slider indicates configurable range 1–250 MB; no change applied.
- `Disable file downloads`: **OFF** in screenshot, so document downloads not disabled. Recommend leave OFF for current export-heavy DJMRN workflows; consider ON later only for tightly controlled shared document libraries. Does not alter model quotas.

## Account audit references
- Dedicated key `DJMRN-OmniRoute` created, saved privately; prior key retained. See `MISTRAL-DJMRN-OMNIROUTE-KEY-CREATED-2026-10-26.md`.
- Free plan and $10/month API/Studio allowance plus separate $10/month Vibe Code allowance; per-model rate limits recorded in `MISTRAL-FREE-PLAN-AND-23-MODEL-LIMITS-2026-10-26.md`.
- API model-training opt-out **OFF** and Labs **OFF** confirmed in `MISTRAL-API-PRIVACY-OPT-OUT-CONFIRMED-2026-10-26.md`.
- Vibe Privacy last screenshot: `Sensitive data in Knowledge` **ON**, feedback **ON**, retention `No expiration`. Recommendation to disable sensitive-data option was issued, but **no confirmation screenshot** of change received. See `MISTRAL-VIBE-PRIVACY-SNAPSHOT-2026-10-26.md`.
- Billing: no payment method, €0 purchased credits, auto-recharge disabled. Do not enable pay-as-you-go or add payment method without explicit approval.

## Remaining before operational integration
1. Confirm Vibe sensitive-data toggle after user changes it, if desired.
2. Verify actual authenticated model catalog and free-allowance eligibility per endpoint/model, not just rate-limit cards.
3. Test dedicated key against a known eligible model with minimal tokens; monitor Usage and allowance after test.
4. Inspect other organization/workspace settings later as user requested.
5. Continue provider onboarding queue: Cloudflare Workers AI next, then NVIDIA API Catalog, Cohere, Hugging Face as appropriate.

## Status
**Research snapshot captured; operational connection to OmniRoute not yet validated.**
