# DJMRN — OmniRoute Windows sign-in UI visible (user screenshot, 2026-10-24)

**Evidence classification:** USER_SUPPLIED_SCREENSHOT + USER_STATEMENT. **Scope:** observed UI only; do **not** equate to authenticated dashboard, healthy inference API, or successful provider connection.

## Observation
- User supplied a screenshot showing an ordinary Windows window titled **OmniRoute — AI Gateway for Multi-Provider LLMs**. The local app renders a login page, heading **Sign in**, password form, **Continue** button, and caption `Default password: CHANGEME (unless INITIAL_PASSWORD was set)`.
- User explicitly wrote in Persian "این نصب شد" ("This installed"). This **supersedes the earlier I018 install/launch-blocked snapshot for present status**. The earlier failure was a historical attempt, not to be deleted or rewritten.
- UI **launched**. Exact running EXE file path, package hash, installed version, install mode, start-menu entry, Windows shortcut, backend HTTP health, local port binding, database migration, credentials, provider account and model usage **NOT VERIFIED**. The v3.8.52 version is merely the *prior target download*, not identified in the new screenshot.
- User asked for the official website/sign-up and desktop shortcut. Explain that the screenshot is the **local management password** and ordinarily does NOT require a separate OmniRoute website registration. Official project: https://github.com/cheaper-inference/OmniRoute ; product overview: https://omniroute.cheaperinference.com/
- Vendor auth reference: https://github.com/cheaper-inference/OmniRoute/wiki/Management-Auth ; UI screenshot itself shows the default string; security docs: https://github.com/cheaper-inference/OmniRoute/blob/release/v3.8.51/.env.example . Default `CHANGEME` is insecure: only enter it locally if user has not configured `INITIAL_PASSWORD`, then **immediately change to a unique password in Settings → Security**. Never send the password, key or token to the assistant or public repo.
- For shortcut: use Windows Run `shell:AppsFolder` → OmniRoute → Create shortcut → Desktop. Alternative Start menu search OmniRoute → Open file location → right-click app shortcut → Show more options → Send to → Desktop (create shortcut).
- Do not ask user to disable security tools. Prior Windows Security changes, if any, should be restored.

## Follow-up gates (NOT YET PASSED)
1. **AUTHENTICATED_DASHBOARD:** evidence user was able to sign in and changed insecure default, with any screenshots redacted for accounts and secrets.
2. **LOCAL_GATEWAY_HEALTH:** local HTTP endpoint alive on loopback, safe auth enabled, no system-wide proxy, MITM or imported root cert, no unapproved startup/background access.
3. **FREE_ONLY_PROVIDER:** verify one or more genuine permitted Free provider entitlements, billing-disabled and hard free-only provider/model allowlist, then separately approved single live call.
4. **QUOTA/ROUTING:** high/medium/low per-assistant limits, exhaustion/switch, fail-closed on unknown paid routes, rollback and backup; not yet run.

**Architectural state:** OmniRoute goes from INSTALL_BLOCKED to USER_REPORTED_INSTALLED_SIGNIN_UI_VISIBLE; conditional evaluation resumed. D-005 host/router final selection still OPEN. Bifrost and Cloudflare remain fallback candidates; no new paid service/account, API connection or inference performed by this research note. G3B/M1 personal-file guard CLOSED.
