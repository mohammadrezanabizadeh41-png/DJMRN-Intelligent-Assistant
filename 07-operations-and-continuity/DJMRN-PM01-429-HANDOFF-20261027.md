# DJMRN PM-01 — 2026-10-27 AGNT 429 Handoff

**State: NOT RESOLVED.** This records user-observed screenshot evidence, no changes to computer or OmniRoute.

## Current architecture and status
- OmniRoute Desktop v3.8.52 localhost:20128 runs LLM Gateway; AGNT Desktop v0.6.7 localhost:3333 is the agent/chat app.
- Existing, saved PRIORITY Combo: DJMRN-PM-Standard; target 1 gemini/gemma-4-26b-a4b-it; target 2 gemini/gemma-4-31b-it; both use the same pinned Google connection DJMRN-OmniRoute-Gemini.
- User screenshot Combo Create and Combos list: Combo saved successfully. Independent Test now: 26B OK in 2951ms; 31B ERROR in 21326ms with Internal error encountered. This does not validate routing/fallback.
- AGNT Custom Provider test succeeded and found 485 model names at http://127.0.0.1:20128/v1, existing private Gateway API Key, model DJMRN-PM-Standard. AGNT Main Chat screenshot selected that Combo but real Persian first-turn chat returned [429] You exceeded your current quota, reset after 58s. No successful Persian AGNT chat and no dedicated PM-01 Persona yet.
- 58s reset suggests a short rate window; status 429 alone can represent RPM, TPM or RPD exhaustion. Historical Gemma account observed limits: 30 RPM, 16000 input TPM, 14400 RPD; these are previous screenshots, not fixed or additive entitlement. Both Combo models share one upstream Gemini connection. No rapid retries.

## Historically solved vs unrelated errors
- Previous AGNT/OmniRoute experiment with AI Horde Combo DJMRN-Persian-L1 failed 400: AGNT submitted 104 tool definitions to an AI Horde model lacking function calling. This was a model/tool schema incompatibility, NOT today's 429. A successful fixed AGNT chat was NOT confirmed in that old record.
- A distinct Gemini routed 403/HTML problem for Gemma 26B WAS solved after PowerShell traced a missing effective proxy for the Gemini connection, while Windows had a working local proxy. A scoped connection proxy configured through /api/settings/proxy caused Gateway HTTP 200 READY in 2.95 sec. See CURRENT-STATUS section OMNIROUTE-GEMINI-403-HTML-PROXY-RECOVERY-20261027. Do not change proxy for today's 429 without new evidence.
- Gemma 31B intermittent 500 and today independent target health error are separate from 429. Prior errors do not imply the model was disabled or quota exhausted.

## Observed Resilience from 7 user screenshots
- Auto-disable banned accounts OFF; Model Lockout OFF; 500 not in listed model-lockout codes. API-key connection cooldown 3 sec; breaker degradation after 7 failures, open after 12, reset 30 sec. Wait for cooldown enabled 3 attempts. Combo wait enabled 5 attempts and 300-sec total budget; global provider cooldown OFF.
- Router request queue shown at 60 RPM does not prove upstream 30 RPM / 16k TPM Gemini guard. Actual Combo Retry/429 classification and AGNT sent tool list remain unverified.

## Next step in new conversation
1. Only inspect health without inference: GET localhost:3333/api/agents/health, localhost:3333/api/orchestrator/health, localhost:20128/v1/models; do not print API tokens.
2. Once 429 short window resets, make ONE low-token direct POST to localhost:20128/v1/chat/completions with saved model DJMRN-PM-Standard, stream false, max_tokens 70, no tools, and existing private Gateway API Key. Compare HTTP code, Retry-After, safe response. OmniRoute may internally make more than one upstream call.
3. AGNT docs confirm authenticated POST localhost:3333/api/orchestrator/chat with message, model and enabledTools=[] can test AGNT tool-free request; AGNT may require its own session JWT, which is NOT the OmniRoute Gateway Key. If authorization unavailable, use desktop UI and do not extract private sessions.
4. If direct Gateway 429, inspect OmniRoute calls/health, Google AI Studio quota, and actual rate limiting. If direct Gateway 200 but AGNT 429, compare AGNT tool/context payload, number of model calls and time window. Former 104-tool incident plus Gemma 16k TPM make long prompt a plausible hypothesis, NOT a confirmed cause.
5. Only after successful AGNT Persian chat, create PM-01 Persian project manager Persona with no broad tools; later add contract dispatch, specialists, modular long-term memory.

## Source references
- Current project status: https://github.com/mohammadrezanabizadeh41-png/DJMRN-Intelligent-Assistant/blob/main/07-operations-and-continuity/CURRENT-STATUS.md
- OmniRoute screenshot-verified UI and resilience: https://github.com/mohammadrezanabizadeh41-png/DJMRN-Intelligent-Assistant/blob/main/08-project-knowledge-base/tools/omniroute/WORKING-WITH-OMNIROUTE-v3.8.52-20261024.md
- Modular model/PM plan: https://github.com/mohammadrezanabizadeh41-png/DJMRN-Intelligent-Assistant/blob/main/03-architecture-and-tools/DJMRN-MODULAR-MEMORY-AND-PM-AGENT-ADOPTION-PLAN-20261027.md
- AGNT API: https://agnt.gg/docs/api/agents
- Google 429 rate documentation: https://ai.google.dev/gemini-api/docs/rate-limits
