# OpenRouter — API Keys list verification
Date: 2026-10-26
Source: user screenshot, Personal / Default Workspace → API Keys.

## Directly observed
- 2 keys displayed.
- `DJMRN-OmniRoute` (suffix shown `1e0`): Guardrails `No guardrails`; Expires `Never`; Last Used `Never`; Key usage `$0.000`; Key limit `$0.000` (`TOTAL`).
- `Default key` (suffix shown `142`): Guardrails `No guardrails`; expiration shown `Apr 21, 2027, 1:11 PM G...` (timezone truncated); Last Used `Never`; Key usage `$0.000`; Key limit `$100` (`TOTAL`).
- The `$100` is a **key limit**, not evidence of free account credit. Do not use the default key in DJMRN or infer a funded balance.
- Screenshot shows no actual secret key values.

## Status
- `DJMRN-OmniRoute` key creation and zero-dollar lifetime cap CONFIRMED from UI.
- Free-model `:free` calls under zero cap: **NOT TESTED**; potential rejection because UI warns requests are rejected once `$0.000` usage is reached.
- OpenRouter account billing/credits and actual free-model catalog: NOT VERIFIED.
- OmniRoute upstream integration: PENDING.
- No paid use authorized.

## Next
Continue provider onboarding (Mistral next). Later perform a single zero-cost model test with this key, then register in OmniRoute only if working.
