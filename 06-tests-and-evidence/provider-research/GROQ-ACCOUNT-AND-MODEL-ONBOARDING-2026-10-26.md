# GroqCloud — DJMRN Provider Onboarding
Date: 2026-10-26
Status: API KEY CREATED AND SAVED BY USER; OmniRoute integration pending.

## Verified from user
- User completed GroqCloud API key creation and reports having saved the key.
- Suggested display name during setup: `DJMRN-OmniRoute`; actual saved display name not independently confirmed.
- Expiration option shown in preceding screenshot: `No expiration`; final choice not independently confirmed.
- No secret key values, screenshots containing secrets, or credentials are stored here.
- Rate limits, free-tier model catalog, organization/project identity, billing state, and actual API success are **not yet verified**.

## Evidence requested (screenshots or redacted text)
1. Groq Console → Settings → Limits: model-level RPM, RPD, TPM, TPD and any account-level restrictions; capture full model list and date.
2. Groq Console → Models: exact model IDs, context lengths, tool calling/JSON/vision/audio capability where displayed, model availability and status.
3. Groq Console → Billing/Plan: whether free plan, zero spend, payment method required, credits and trial expiry; redact personal details.
4. Groq Console → API Keys: key entry exists (name, creation and expiry metadata only); do not show key value.
5. Later, OmniRoute provider configuration and actual test request (model ID, HTTP status, latency, observed error, without key).

## Intended DJMRN routing
Classify only after live evidence: quick low-cost tasks, coding, complex reasoning, structured extraction, multilingual, long context, and fallback suitability. Prefer free-first, verify quotas from the actual account; do not assume provider-wide published limits apply to user account.

## Next step
Inspect the account's Limits page first; then Models; then plan/billing status. Store screenshots' observed values with source/date and preserve unknowns as UNKNOWN.
