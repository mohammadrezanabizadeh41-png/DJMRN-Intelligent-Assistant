# DJMRN — OmniRoute Setup, Provider Onboarding & Agent Integration Log
Date opened: 2026-10-26
Status: IN PROGRESS — user-directed operational record, not confirmation of working agent integration.
Repository: mohammadrezanabizadeh41-png/DJMRN-Intelligent-Assistant (main)

## Scope and evidence rules
Track OmniRoute Windows install, login, configuration, provider registration, model catalogs, routing, quota/failover, and Agno/AGNT end-to-end tests. Distinguish observed screenshots/PowerShell outputs from assumptions and untested plans. Do not put passwords, API keys, access tokens or sensitive account details in GitHub. Do not modify canonical CURRENT-STATUS.md without explicit separate instruction.

## Current verified progress
- Windows 11 OmniRoute Setup 3.8.52 graphical installer obtained and eventually installed after a first stalled attempt.
- Initial installer stalled ~70%; process was responsive, consumed CPU; install directory existed with 18,116 files (~1299.4 MB), OmniRoute.exe 246,407,168 bytes.
- User-approved cleanup removed `%LOCALAPPDATA%\Programs\OmniRoute`; `%APPDATA%\OmniRoute` and `%LOCALAPPDATA%\OmniRoute` absent. Downloaded `%USERPROFILE%\Downloads\OmniRoute.Setup.3.8.52.exe` preserved. Restart and reinstall followed.
- Latest screenshot (2026-10-26): OmniRoute desktop window opens at **Sign in** screen. UI shows **Invalid password** after attempted entry; default password hint: `CHANGEME` unless `INITIAL_PASSWORD` was set. Successful login NOT YET VERIFIED.
- Earlier OmniRoute test before reinstall reportedly returned HTTP 200 at local gateway port 20128; **not evidence current reinstall works**.
- Gemini provider account: user has existing API key(s), not stored here; detailed free-tier screenshot snapshot stored separately. Actual connection to current OmniRoute NOT YET TESTED.
- No other provider keys confirmed created in this onboarding sequence. No Agno→OmniRoute→provider end-to-end confirmed.

## Next execution checklist (update only on observed results)
1. [ ] Login using default `CHANGEME` if applicable; if rejected, inspect app's supported password reset/recovery without deleting data.
2. [ ] Confirm dashboard and current local API endpoint/port, provider list, version.
3. [ ] Add existing Gemini key locally, map exact model IDs from live API; verify free-tier eligibility and zero-cost settings.
4. [ ] Test simple request and log result/model/HTTP status (no secret values).
5. [ ] Register additional free API providers one by one; record actual keys-created and connected status separately.
6. [ ] Configure shared model pool, capability tiers, load balancing, quota and 429 failover; do not hard-cap individual agents.
7. [ ] Verify Agno / AGNT client integration and end-to-end agent test.
8. [ ] Record operational findings, limitations, model-provider mapping, rollback steps and exact test evidence.

## Provider onboarding queue
| Provider | Key status | OmniRoute status | Notes |
|---|---|---|---|
| Google Gemini API | Existing per user | Pending | Free-tier snapshot saved; verify exact model IDs |
| GroqCloud | Not yet confirmed | Pending | Next key registration candidate |
| OpenRouter | Not yet confirmed | Pending | Filter free models, verify shared account quota |
| Mistral AI | Not yet confirmed | Pending | Verify free-mode limits |
| Cloudflare Workers AI | Not yet confirmed | Pending | Free daily neurons and supported integration |
| NVIDIA API Catalog | Not yet confirmed | Pending | Verify trial/commercial terms |
| Cohere | Not yet confirmed | Pending | Verify trial restrictions |
| Hugging Face | Not yet confirmed | Pending | Optional; verify inference credit |
| DeepSeek and other hosts | Research candidate | Pending | Official DeepSeek API not assumed free; investigate third-party free hosting |

## Linked evidence and research
- Gemini screenshot-based model and quota snapshot: `06-tests-and-evidence/provider-research/GEMINI-FREE-TIER-RATE-LIMIT-SNAPSHOT-2026-10-26.md`
- Provider research and onboarding queue: `06-tests-and-evidence/provider-research/DJMRN-FREE-CLOUD-API-KEY-QUEUE-2026-10-26.md`

## Governance
Free-first. Never enable billing/paid features or store secrets in repository. Do not treat a listed model or visible quota as a successful API connection. Account/project/model rate limits may overlap. Avoid repeated non-idempotent agent tool execution during automatic retries.
