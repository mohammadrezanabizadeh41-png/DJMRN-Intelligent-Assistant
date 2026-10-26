# OpenRouter — DJMRN Account and Key Onboarding
Date: 2026-10-26

## Confirmed by user
- OpenRouter API key **created and saved privately by user**.
- Key display name shown: `DJMRN-OmniRoute`.
- Expiration shown: `No expiration`.
- Credit limit: custom **USD 0**, reset `N/A`.
- UI warning: “Requests are rejected once this key has used $0.000 in total, until you raise its credit limit.”
- It is **UNKNOWN** whether zero-credit-cap keys can make successful `:free` model requests. Must test before classifying as working.
- No actual API secret in repository; no billing/top-up authorized.

## DJMRN integration plan
- Do not use optional OpenRouter 'Connect to Tools' setup at this stage.
- Configure OpenRouter as upstream provider inside OmniRoute; connect DJMRN agents to OmniRoute gateway rather than independently to OpenRouter.
- Verify live `:free` model IDs, quotas, request status, and whether zero-dollar credit limit blocks even free requests.
- Never silently change credit limit or enable paid models.

## Pending
1. Verify account free tier and actual quota in OpenRouter account.
2. Test one free model with the zero-cap key; record response/error without disclosing secret.
3. Register key locally in OmniRoute → OmniProxy → Providers.
4. Map verified free model IDs and integrate with shared routing/failover.
