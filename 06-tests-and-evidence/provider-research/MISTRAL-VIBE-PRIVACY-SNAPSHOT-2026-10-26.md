# Mistral Vibe Privacy snapshot
Date: 2026-10-26. Evidence: user screenshot of Vibe → Privacy. Screenshot observations only; no settings were changed by assistant.

## Observed
- `Sensitive data in Knowledge`: ON (green). Description: organization users may choose whether Knowledge saves sensitive personal information they explicitly ask it to remember; some highly sensitive information never saved.
- `Allow user feedback on model responses`: ON (green). Description: users may submit thumbs up/down and free-text feedback.
- `Chat Retention Policy`: `No expiration`. Description: choosing a period automatically deletes chats and their artifacts; applies to existing and new chats.

## Recommended decisions, not yet applied
- Consider disabling sensitive-data saving in Vibe Knowledge to reduce duplication of DJMRN canonical memory, and confirm resulting behavior.
- Feedback toggle can remain on; avoid sharing sensitive information in feedback.
- Leave retention unchanged until archive/export implications are assessed. No-expiration is not a backup policy.
- Audit data-retention/feedback terms separately if needed.
- Distinguish Vibe Privacy from API Privacy; API training opt-out and Labs OFF were confirmed in prior evidence.
