# DJMRN — OmniRoute v3.8.52 authenticated Windows Home screen observed

**Evidence:** User-supplied screenshot shown in current conversation on 2026-10-24. Status: `USER_SCREENSHOT_DASHBOARD_HOME_VISIBLE` (newer than I019 sign-in screen and I018 installation blocker). **Do not store original screenshot in public GitHub.**

## What is directly visible
- Native Windows window title `OmniRoute — AI Gateway for Multi-Provider LLMs`; left sidebar version **v3.8.52**.
- **Home — Welcome to OmniRoute** authenticated dashboard UI visible (login screen no longer showing). Left sidebar: Home, **OmniProxy** (collapsed), Analytics, Costs, Monitoring, Dev Tools, Agentic Features, Other Features, Restart, Shutdown. This is **GUI sign-in success**, not API-health or model inference success.
- Yellow banner: **Running in zero-config mode** — application claims it generated initial cryptographic keys on first launch, persisting them under `%APPDATA%\omniroute\server.env`. The banner suggests custom `JWT_SECRET` and `STORAGE_ENCRYPTION_KEY`; **do not publish or request contents of this file**. Treat presence and quality of keys as unverified beyond UI vendor message.
- Three promotion banners (Kimi API / Cheaper Inference provider API / OmniCopilot extension). None prove provider accounts, free tier, credits, or an attached API key. User should not activate any paid provider or partner top-up in this step.
- **Not yet evidenced:** whether the default admin password was changed; startup mode, loopback-only bind, management/API authentication, actual backend health, model/provider configuration, free remaining quotas, costs, persistent data backup, CPU/RAM, assistant endpoints, failover, or any live cloud call.

## Next smallest safe GUI steps
1. Open OmniProxy section to inspect navigation only and return a **sanitized screenshot of visible submenus**; do not add provider, OAuth, keys, card, or route.
2. If admin password is still `CHANGEME`, change it to a unique password **Dashboard → Settings → Security** before any external provider or network exposure. Do not enter credentials in chat; no secret disclosure in public GitHub. Source: https://github.com/diegosouzapw/OmniRoute/blob/release/v3.8.52/.env.example
3. Later, confirm local-only exposure and per-assistant API auth, and validate one actual eligible free provider with explicit approval, before any inference. **No production adoption** based on this screenshot.

**Project decision status:** `OMNIROUTE_WINDOWS_UI_AUTHENTICATED` limited to GUI. Prior I018 failure and I019 sign-in retained historically. This is not evidence that required routing/free-only quotas/429 failover work. D-005 OPEN; G3B/M1 private-file guard CLOSED; 27 alternative router candidates unchanged.
