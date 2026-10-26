# Gemma 4 31B operational verification — 27 Oct 2026

Evidence from user's Windows PowerShell, model `gemini/gemma-4-31b-it`.

- Direct Google metadata: `models/gemma-4-31b-it`, supported methods `generateContent,countTokens`.
- Direct Google text: HTTP 200, 8.42s, nonempty response.
- OmniRoute Gateway text: HTTP 200, 35.93s, nonempty response.
- OmniRoute Gateway vision: HTTP 200, 7.53s, correct answer `CAT` for a known cat JPEG, 279603 bytes, sent as inline Base64 in `image_url`.
- Earlier Google and Gateway HTTP 500 attempts remain historical. Exact cause unknown; do not claim that a model ID or token limit change fixed the issue.
- Verified scope: text and one inline-JPEG vision input through OmniRoute. Other modalities, reliability and free-only billing enforcement not verified.
- No new model registration, local weight download, proxy changes, billing changes or group creation.
- Next: choose and test one next existing Custom model at a time; separately verify account-level free-only limits.
