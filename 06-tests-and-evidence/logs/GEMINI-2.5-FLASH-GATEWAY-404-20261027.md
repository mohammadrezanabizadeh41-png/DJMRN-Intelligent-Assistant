# DJMRN OmniRoute: Gemini 2.5 Flash, model 9, first text-only test

Date: 2026-10-27. Source: user-provided PowerShell terminal output, actual local execution.

- Model `gemini/gemini-2.5-flash`, existing OmniRoute Gemini provider, local gateway `http://127.0.0.1:20128/v1/chat/completions`.
- Test: one text-only Chat Completions POST, no image, user prompt "Reply with exactly READY.", `max_tokens=128`, `stream=false`, client timeout 35 sec. Existing Gateway API key entered via secure prompt; key not recorded.
- Observed: `IMAGE_ATTACHED=False`, `HTTP_STATUS=404`, `NETWORK_STATUS=ProtocolError`, `ERROR_CLASS=UNKNOWN`, `ERROR_TYPE=WebException`, `SECONDS=0.61`, `TEXT_TEST=FAILED`.
- Interpretation: the gateway returned HTTP 404; the client script did not expose the provider error payload. Root cause is **UNCONFIRMED**. The separate Gemma/Gemini routes remain unchanged. The previous Gemini 2.5 Flash-Lite test independently showed a Google upstream "no longer available to new users" restriction, which is suggestive for this model but does not prove its own error cause.
- Operational state: `MODEL9_TEXT_GATEWAY_404`, `MODEL9_VISION_NOT_TESTED`, `MODEL9_NOT_ADMITTED`. Neither global retirement nor account-specific new-user restriction confirmed for this exact model from this output.
- Next: read-only authenticated OmniRoute Management GET `/api/usage/call-logs?model=gemini-2.5-flash&limit=8`, print only sanitized status, duration, error. No need to re-run inference. If provider error says restricted to new users, preserve it and defer. No changes to existing model config, proxy, keys, billing, Combo, Agno, or installations. User requested text-only tests.
