# Mistral Studio — existing API key snapshot
Date: 2026-10-26
Source: user screenshot, Organization API keys.

## Observed
- One visible active key, name `API Key`, type `Studio`.
- Key secret masked; trailing characters visible but not stored here.
- Principal is user; key created **17 days ago** according to UI.
- Expires: **Never**.
- Last used: truncated **October 9t...** (year/time not fully visible).
- Workspace: `Default ...` truncated.
- Access scope: **Shared only**.
- Organization API key expiration policy: **Not required**.
- `New key` button exists.

## Interpretation
- An API key already exists, but its secret may not be recoverable from UI. Do not assume it can be reused without checking whether the user securely retained it.
- Do not assume this key is currently usable for free API requests or that it accesses all resources; verify active plan, limits and models.
- Prior Billing screenshot: €0.00 credits, no payment method, auto recharge disabled.
- No new key created in this step; no secret exposed.

## Next
1. Check whether existing key is securely available; if not, create dedicated `DJMRN-OmniRoute` key without deleting the existing one.
2. Inspect plan/usage/rate limits and model availability.
3. Test free API model call before OmniRoute integration.
4. Later review complete organization/workspace/security settings.
