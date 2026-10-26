# Mistral API Privacy — Opt-out confirmed

Date: 2026-10-26
Evidence: user screenshot of Admin → API → Privacy following earlier recommendation.

## Verified UI state
- `Allow the use of your API calls to train Mistral’s AI models`: OFF (gray toggle). Previously ON in earlier screenshot.
- `Enable Labs models`: OFF (gray toggle), unchanged.
- UI states that new interactions are not used to train Mistral models when first toggle is disabled.
- Labs text explicitly warns that Labs data may be used for model training regardless of opt-out if Labs is enabled.

## Qualifications / follow-up
- UI opt-out does not establish deletion of earlier interactions or zero retention for other purposes.
- Impact of API training opt-out on Free plan availability, monthly allowance and accessible model set not yet verified.
- Audit Vibe → Privacy separately.
- No API keys, payment information or other secrets stored.
