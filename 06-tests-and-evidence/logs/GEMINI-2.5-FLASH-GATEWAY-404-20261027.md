# DJMRN OmniRoute: Gemini 2.5 Flash, model 9, first text-only test

Date: 2026-10-27. Source: user-provided PowerShell terminal output, actual local execution.

- Model `gemini/gemini-2.5-flash`, existing OmniRoute Gemini provider, local gateway `http://127.0.0.1:20128/v1/chat/completions`.
- Test: one text-only Chat Completions POST, no image, user prompt "Reply with exactly READY.", `max_tokens=128`, `stream=false`, client timeout 35 sec. Existing Gateway API key entered via secure prompt; key not recorded.
- Observed: `IMAGE_ATTACHED=False`, `HTTP_STATUS=404`, `NETWORK_STATUS=ProtocolError`, `ERROR_CLASS=UNKNOWN`, `ERROR_TYPE=WebException`, `SECONDS=0.61`, `TEXT_TEST=FAILED`.
- Interpretation: the gateway returned HTTP 404; the client script did not expose the provider error payload. Root cause is **UNCONFIRMED**. The separate Gemma/Gemini routes remain unchanged. The previous Gemini 2.5 Flash-Lite test independently showed a Google upstream "no longer available to new users" restriction, which is suggestive for this model but does not prove its own error cause.
- Operational state: `MODEL9_TEXT_GATEWAY_404`, `MODEL9_VISION_NOT_TESTED`, `MODEL9_NOT_ADMITTED`. Neither global retirement nor account-specific new-user restriction confirmed for this exact model from this output.
- Next: read-only authenticated OmniRoute Management GET `/api/usage/call-logs?model=gemini-2.5-flash&limit=8`, print only sanitized status, duration, error. No need to re-run inference. If provider error says restricted to new users, preserve it and defer. No changes to existing model config, proxy, keys, billing, Combo, Agno, or installations. User requested text-only tests.


## MODEL9-GOOGLE-NEW-USER-RESTRICTION-VERIFIED-20261027 — provider denial confirmed by actual OmniRoute call logs

The user performed **read-only** authenticated GET `http://127.0.0.1:20128/api/usage/call-logs?model=gemini-2.5-flash&limit=8`. No new inference call was performed and no secrets were shared. The response `LOG_MATCHES=8` contains both `gemini-2.5-flash` and `gemini-2.5-flash-lite` records; a model substring-match appears to admit Flash-Lite. **Do NOT attribute all eight logs to Flash.**

Exact relevant Flash row:
- `STATUS=404`
- `DURATION_MS=447`
- `ERROR=[404]: This model models/gemini-2.5-flash is no longer available to new users. Please update your code to use models/gemini-3.8-flash for the latest features and improvements. We recommend you to use the Interactions API ([REDACTED_URL]` (user script truncated/redacted URL; do not reconstruct).

Other displayed rows, distinct model or historical:
- `gemini-2.5-flash-lite`, `STATUS=404`, `DURATION_MS=541`: Google says no longer available to new users, recommends `gemini-3.5-flash-lite` (known previously passed text + inline-JPEG Vision).
- Historical `403` HTML_ERROR rows with durations `25002`, `562`, `525` ms.

**Finding:** upstream Google access for stable `gemini-2.5-flash` on this current Gateway/project is **RESTRICTED_FOR_NEW_USERS**. This model is not necessarily globally shut down or deprecated for all existing users. The related 2.5 Flash-Lite denial was separately verified; no point retesting either model from this same account absent eligibility change.
**Important caveat:** Google suggests `gemini-3.8-flash` as successor, but this user's same-model connection had repeated Gateway timeouts (110.02s Vision; 40.05s text) and proxy ECONNRESET/high-demand logs. Do **NOT** silently use that suggestion as an agent-routing fallback; prefer already functional Gemini 3.5 Flash-Lite, Gemini 3.6 Flash, Gemini 3.1 Flash-Lite, Gemma 4 26B/31B or the text-only tested Gemini 3 Flash Preview depending on task and validated capabilities.

**Operational disposition:** `gemini/gemini-2.5-flash = RESTRICTED_FOR_NEW_USERS / CURRENT_ACCOUNT_UNAVAILABLE / NOT_ADMITTED_TO_AGENT_ROUTING`. Historical entry retained, no config or proxy modifications. All five previously image+text-passed candidates and Gemini 3 Flash Preview's text pass retained. Do not test images in the current user-selected workflow. Next specialty research/tests should match modality: embeddings endpoint, speech synthesis endpoint, live transcription, robotics, agents. Do not automatically add models into Combos or Agno until QA/cost gates. 
