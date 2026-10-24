# DJMRN — OmniRoute npm+local web dashboard vs Cloudflare hosted AI Gateway

**Date:** 2026-10-24. **Status:** EVIDENCE-BASED RECOMMENDATION / NO ARCHITECTURE ADOPTION / USER REVIEW PENDING.
**Authority:** Project GitHub is code/implementation authority; Notion Operating Memory and Tool Governance are cross-project rules. This report extends the 2026-10-24 router handoff, not a competing CURRENT record.

## User's specific choice
Should DJMRN give OmniRoute *one bounded native Node/npm engine + local web dashboard pilot*, bypassing previously blocked 620 MB Electron Windows installer, or move directly to hosted Cloudflare AI Gateway (the second candidate)?

## Proven DJMRN baseline
- Windows 11 Pro AMD64, AMD Ryzen 5 3500U, 8 GB installed RAM; verified historical Node.js **v24.22.1** on the user's Windows (not reconfirmed now).
- OmniRoute Desktop Setup **v3.8.52** user-downloaded, could not install/launch; **NO exact event or error log**, product not disproven. Installed desktop vs npm backend are separate deployment paths.
- Bifrost Windows native v2.3.2 booted and SQLite migrated but exited due to mandatory pricing catalog timeout; synthetic-only GitHub tests unrelated to actual free provider limits.
- No live central router to real free provider verified. Provider-specific rate, quota, costs, billing protections unverified; D-005 OPEN, file guard G3B/M1 CLOSED. Existing 27-candidate queue unchanged.

## Independently checked canonical public facts
### OmniRoute (npm, native Node)
- GitHub release **v3.8.52** (Oct 19, 2026) and npm registry package **`omniroute@3.8.52`** are published. Vendor supports `npm install -g omniroute` + `omniroute`, with **same local process serving web dashboard http://localhost:20128 and OpenAI-compatible /v1 endpoint**. Official Node range `>=22.22.2 <23 || >=24.0.0 <27`, hence historical 24.22.1 in range. No Electron installer required. **This npm route has not been executed on the user's laptop**.
- The 3.8.52 package has many dependencies and vendor-reported npm 11 postinstall script allowlist (`omniroute,keytar,onnxruntime-node,@parcel/watcher,@swc/core,protobufjs,esbuild`); package postinstall executes code, so source provenance, least privilege, antivirus and rollback are material. Keep pin, no latest auto-update.
- Vendor documents ~1.62B *estimated monthly aggregate across distinct externally obtained free accounts*, NOT a user quota or model credits from OmniRoute. Per-account qualifications, resets, ToS, region/account restrictions, and model availability vary. Free-tier summary, quota-weighted/Headroom/reset strategies, per-API-key budget, `auto/coding` and `auto/*` routes are documented; still need functional tests.
- Optional *Radar* live overlay with supporter entitlements exists; its exact cost and eligibility were **not verified** and must NOT be enabled for free-only assumptions. Built-in community catalog is free but not proof of real-time autonomous discovery of every new free service, or exact remaining quotas.
- CRITICAL: `auto/thrifty` explicitly can advance to cheap **paid** targets; unrestricted `auto` and stale provider prices do **not** establish a hard free-only guard. Permit only explicit free-verified providers/models, disable paid routes/credits, include 429/5xx fail-closed negative tests and per-key allowance. Enable required management secrets, encryption key, API auth, dashboard password before any third-party connection; bind loopback only, do not enable MITM/root certificates/system proxy/browser-cookie re-use.
- RAM/CPU on the user's machine, secured first boot and rollback of npm installation NOT TESTED; 8GB class requires direct Task Manager observation. Dashboard is browser UI only while local engine runs; remote assistant clients would need separately approved secure access/hosting.
Canonical vendor: https://github.com/cheaper-inference/OmniRoute/releases/tag/v3.8.52 ; https://www.npmjs.com/package/omniroute ; https://github.com/cheaper-inference/OmniRoute ; https://github.com/cheaper-inference/OmniRoute/security ; https://github.com/diegosouzapw/OmniRoute/blob/release/v3.8.52/docs/reference/FREE_TIERS.md

### Cloudflare AI Gateway (hosted)
- No local install, hosted uptime, official core Gateway analytics/rate limiting/caching offered free on plans (upstream inference not included). Dynamic Routing Beta supports condition, per-key rate/budget limits, model fallback and version rollback.
- **Newly identified official Auto Router (2026-10-02):** `cloudflare/auto` does task difficulty classification, model quality/cost ranking, availability fallback and optional allowlisted providers/models (`cf-aig-allowed-models`). This corrects any inference that Cloudflare has *no* task-aware routing. **Default selected model pool names include paid commercial models**; unrestricted Auto Router is NOT free-only, and allowed-model support does not verify any specific account's zero-cost free access. No proven live cross-provider free quota catalog, renewal/rate-limits known for each BYOK account.
- Auto-created `default` gateway may use Workers AI **Standard billing** with no rate limit; manual creation also defaults Standard Workers AI billing. BYOK-only prevents Unified Billing fallback for providers but does NOT by itself prove Workers AI zero spend. User/account permission, Dynamic Route entitlement, hard-zero safeguards, privacy and cross-provider free-model selection NOT VERIFIED.
- Official docs: https://developers.cloudflare.com/ai-gateway/features/auto-router/ ; https://developers.cloudflare.com/ai-gateway/features/dynamic-routing/ ; https://developers.cloudflare.com/ai-gateway/reference/pricing/ ; https://developers.cloudflare.com/ai-gateway/configuration/manage-gateway/

## Comparison for actual DJMRN goals
| Gate | OmniRoute npm engine / web UI | Cloudflare hosted |
|---|---|---|
| Windows installer dependency | Bypassed; Node/npm still required | None |
| Time to first account/GUI access | Potentially short if npm startup works; security bootstrap/Node script risk | Short if account already eligible; unknown account entitlements |
| Free-tier discovery / provider modeling | Better domain fit (free catalog, pools, quota scheduling); claims NOT live-user verified | No comparable complete free-tier catalog verified |
| Task-aware model choice | auto/coding and custom combos documented | Auto Router **exists**; default selection has paid-model hazard |
| Per-assistant controls | Per-key access and budgets claimed; needs hard 0-overage test | Routes, rate/budget limits; auth/metadata configuration |
| Provider exhaustion 429/5xx | First-class combo fallback; prove no paid fallback | Dynamic flows, Auto Router fallback; prove no paid fallback |
| Cost-hard-zero | NOT PROVEN; catalog estimates and some strategies include paid | NOT PROVEN; billing defaults need explicit safeguards |
| Offline / uptime | User's Windows must be on; local-only scope | Hosted, always available (account/network dependence) |
| Security / secrets | Local account keys; npm postinstall, auth, encryption, local exposure | Cloud-stored credentials, request routing/logging/data egress |
| Machine footprint | 8GB CPU/RAM start still unmeasured | No local gateway CPU |
| Tool churn | One bounded npm route before moving on | No local installation |
| Reversibility | Stop process, uninstall pinned global package; preserve/back up state | Disable/delete deployed route/gateway per authorized plan |

## Recommendation — CONDITIONAL, NOT A FINAL ADOPTION
Because **finding/manage existing free providers and quotas** is the primary DJMRN differentiator, OmniRoute via **pinned native npm backend + local web dashboard** deserves ONE bounded attempt before abandoning it. It uses historically installed Node, bypasses the Electron installer problem and more closely matches the free-pool management need. This is **not** proof of security or functioning.

**Smallest adequate acceptance sequence (no custom launcher, no Docker):**
- P0 NO-WRITE verification on user Windows via regular unelevated PowerShell: `node -v`, `npm -v`, `npm view omniroute@3.8.52 version engines --json`; optionally run Task Manager baseline; no download, installation or secrets yet.
- P1 only on explicit user go-ahead: install **pinned 3.8.52** from official npm with source and script-risk review, never disable Windows security; secure private local `127.0.0.1` process and local generated admin/JWT/API/encryption keys, not user-posted secrets. No key/provider/cloud calls. Stop if npm scripts, bind/auth or malware warning unclear.
- P2 confirm local dashboard, auth, zero paid connections, model visibility, memory/cpu; backup local state; STOP after startup failure rather than building bespoke launcher.
- P3 separately approved *two real legitimate Free accounts with verified overage-off*, hard allowlists High/Medium/Low and per-assistant key caps, test free-exhaustion/429+503 and fail-closed, without hidden paid fallback. No automatic new provider-account signup.
- P4 add periodic free-tier/catalog discovery from official approved providers **only if necessary**; reported new entry = REVIEW, not auto-connected billing.
- If P0/P1 fails or complexity exceeds small pilot, **switch directly to Cloudflare read-only account/plan check**, then New API from existing queue. Bifrost stays on HOLD.

**Decision state:** `PROPOSAL_ONE_BOUNDED_OMNIROUTE_NPM_PILOT` pending user's explicit preference/permission for local npm install. Cloudflare is not rejected; D-017 queue remains intact until approval. No actual device, account, billing, schema, inference or deployed configuration has been changed by this research.
