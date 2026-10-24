# DJMRN OmniRoute v3.8.52 — unauthenticated fake-model inference probe: HTTP 400

**Date:** 2026-10-24; **classification:** USER_EXECUTED_LOCAL_WINDOWS_POWERSHELL / OBSERVED_HTTP_STATUS_ONLY; **scope:** strict synthetic invalid model on user's localhost, not live inference.

## Exact evidence
User executed from Windows PowerShell:
```powershell
$body = '{"model":"__djmrn_auth_probe_nonexistent__","messages":[{"role":"user","content":"ping"}]}'
try {
  $r = Invoke-WebRequest -Uri 'http://127.0.0.1:20128/v1/chat/completions' -Method POST -ContentType 'application/json' -Body $body -TimeoutSec 8 -UseBasicParsing
  "HTTP $([int]$r.StatusCode)"
} catch {
  if ($_.Exception.Response) {
    "HTTP $([int]$_.Exception.Response.StatusCode)"
  } else {
    "ERROR: $($_.Exception.GetType().Name)"
  }
}
```
**Actual returned text:** `HTTP 400`. No API key / Authorization header, no configured real model ID, no user provider credentials. The command emitted **only the numeric HTTP status** and discarded the JSON/error response body.

## Interpretation
- **The local HTTP route responded.** `400` may represent validation, a blocked input/guardrail, a nonexistent model, or routing error. Because response body wasn't captured, neither specific reason nor whether the request reached model resolution can be proven.
- **No `401` returned** on this attempt, so expected **require-key enforcement is NOT VERIFIED**, with a plausible risk it is currently disabled (the documented `REQUIRE_API_KEY` default is `false`). This does **not** prove credential bypass and should never be labeled AUTH_PASS or AUTH_FAIL without stronger evidence.
- This **does not prove** a provider call, token use, free entitlement, spend, security exposure from another machine, or completion. Earlier Endpoints UI showed zero chat/media models, but present provider state was not rechecked.
- Previous real Windows TCP check showed `127.0.0.1:20128` listener only (PID transient) at observation; port exposure and API-key enforcement are **two independent gates**.

## Newly verified official canonical vendor sources
- [Inference Auth Posture](https://omniroute.hagicode.com/en-US/security/inference-auth-posture/): `POST /v1/chat/completions` and other client inference routes use `REQUIRE_API_KEY`, whereas `GET /v1/models` follows dashboard auth; a 401 on models is not sufficient to prove inference auth.
- [Authorization Guide](https://omniroute.hagicode.com/en-US/architecture/authz-guide/): CLIENT_API auth uses `isRequireApiKeyEnabled()`; without that effective flag anonymous request may pass to downstream routing.
- [Feature Flags](https://omniroute.hagicode.com/en-US/reference/feature-flags/): the exact security toggle `REQUIRE_API_KEY` exists under Dashboard → Settings → Feature Flags; documented default `false`; precedence DB override > env > default; no restart needed for this particular flag. User's **current effective value NOT YET SEEN**.
- [Environment Variables](https://omniroute.hagicode.com/en-US/reference/environment/): documents default `REQUIRE_API_KEY=false`, separate from management-login settings.

## Decision and immediate next minimum step (GUI-first, read-only)
1. With existing working OmniRoute Desktop **Configuration → Feature Flags**, use built-in search for `REQUIRE_API_KEY`. Observe card effective value, source `DB` / `ENV` / `DEF`, restart requirement and any warning; only show screenshot with tokens/account details masked.
2. **Do not toggle blindly** or create a key/provider: confirm current state then propose explicitly bounded reversible security enablement if OFF. Activating require-key can affect existing unauthenticated IDE integrations; currently none proved configured.
3. After separately approved enablement, rerun the *same* fake-model, no-auth POST to verify `HTTP 401`; do not use `GET /v1/models` as a substitute.
4. Verify individual virtual API keys, per-assistant request caps and no-billable-provider allowlist before adding any actual free account or real model.

**State:** `HTTP_400_CONFIRMED`, `REQUIRE_API_KEY_NOT_VERIFIED`, `MODEL_VALIDATION_NOT_PROVEN`, `LOCAL_LOOPBACK_OBSERVED_PREVIOUSLY`, `REAL_PROVIDER_NOT_CONNECTED_AS_EVIDENCE`, `FREE_ONLY_COST_NOT_TESTED`. D-005 architecture OPEN, G3B/M1 personal-file guard CLOSED. No settings, security, files, secrets or provider accounts changed by this evidence record.
