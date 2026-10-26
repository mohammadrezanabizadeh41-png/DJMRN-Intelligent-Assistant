# DJMRN — Gemini 3.1 Flash-Lite: live OmniRoute text + vision PASS

Date: 2026-10-27
Evidence: user's actual Windows 11 PowerShell stdout, received in chat on 2026-10-27.
Target model: `gemini/gemini-3.1-flash-lite`
Existing gateway: OmniRoute Desktop v3.8.52, `http://127.0.0.1:20128/v1/chat/completions`.
Credentials: the user entered the private OmniRoute *Gateway API key* locally. No token values were captured or stored.

## Exact test evidence
1. Text via OpenAI-style Chat Completions POST. User prompt `Reply with exactly READY.`, `max_tokens=384`, `stream=false`.
   - `HTTP_STATUS=200`
   - `SECONDS=11.95`
   - `RESPONSE=READY.`
   - `TEXT_TEST=PASS`
2. One-image test on same model via Chat Completions: Wikimedia Commons public JPEG of cat, JPEG magic checked, embedded as `image_url.url="data:image/jpeg;base64,..."`; prompt to classify CAT or OTHER.
   - `HTTP_STATUS=200`
   - `SECONDS=8.38`
   - `RESPONSE=CAT`
   - `VISION_TEST=PASS`
   - `MODEL_STATUS=TEXT_AND_VISION_OPERATIONAL`

## Why significant
- This same model's OmniRoute Gateway route had previously returned HTTP 403 before the Gemini connection-level proxy configuration was corrected on this machine. The successful post-fix tests confirm that, as of this run, this **specific** route works for text and inline-JPEG image understanding. The previous 403 root cause across all models remains an inference, not proof for each individual model.
- Fifth independently confirmed text+image smoke-tested route after `gemini/gemma-4-26b-a4b-it`, `gemini/gemma-4-31b-it`, `gemini/gemini-3.5-flash-lite`, and `gemini/gemini-3.6-flash`.
- No new Custom model entry was created, no local weights installed, no proxy/provider/configuration modification, no model groups or Agno integration performed.
- Free-tier labeling and positive account rate-limit entries are **not** spending control; hard zero-overage/availability/long-term reliability are unverified. Only the one-off text and image types above were tested.

## Next action — proposed only
Candidate 6: existing built-in `gemini/gemini-3.8-flash` under the same Gemini provider, user account previously showed 5 RPM / 250K TPM / 20 RPD for that exact identifier (historical screenshot; may change). Check official/current account access and reuse existing gateway model; no Custom duplication. One text test, then one inline JPEG vision test only on text success. Do not test TTS/embedding/robotics as chat; specialist routes need separate adapter scrutiny and verified user consent for any changes.

Reference: `07-operations-and-continuity/CURRENT-STATUS.md` for Gemini proxy troubleshooting and operational evidence; other model-specific test logs in this directory.
