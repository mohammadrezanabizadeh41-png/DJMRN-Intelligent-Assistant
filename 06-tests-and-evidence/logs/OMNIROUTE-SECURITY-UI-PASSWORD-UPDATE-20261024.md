# OmniRoute v3.8.52 — Security UI and password update banner (2026-10-24)

**Evidence:** User screenshot from Windows Desktop OmniRoute → Configuration → Security. This document is a sanitized description only; original screenshot remains a conversation attachment, not uploaded to public GitHub. Observed outcomes are UI assertions, not independently executed account/backend probes.

## Directly visible
- Application version: **v3.8.52** and title **Security — Authentication, authorization, and access control settings**.
- **Require login** switch visually **ON** (red switch with knob at right). UI text indicates dashboard requires password when on.
- Password form Current Password / New Password / Confirm New Password blank in screenshot; green status text **“Password updated successfully”**. We can conclude **UI_REPORTED_PASSWORD_CHANGE_SUCCESS**, but persistence after restart, effectiveness of a distinct strong password and rejection of the original `CHANGEME` are **not independently verified**. Do not request passwords or their contents.
- **IP Access Control** section has four modes: Disabled, Blacklist, Whitelist, WL Priority. **Disabled** is selected. This does **not establish remote exposure or vulnerability on its own**: must verify actual server bind, firewall, management and `/v1/*` API authentication without exposing a port.
- Earlier screenshot shows first-run auto-generated secrets persisted to `%APPDATA%\omniroute\server.env`; never read or upload actual secrets to public repo.

## Official security context
- Vendor security policy https://github.com/cheaper-inference/OmniRoute/security documents dashboard JWT cookie, API key auth, IP allow/block lists and authz tiers; server network exposure and API-key requirement are distinct from dashboard `Require login`.
- Vendor docs https://github.com/cheaper-inference/OmniRoute/wiki/de%E2%80%90User-Guide document `REQUIRE_API_KEY` default `false` for some deployment modes. **Not evidence that this Desktop installation uses the same value**. Strict API key authentication must be verified before any real provider connection.
- Whitelist/IP deny changes made prematurely can lock user out, so **leave current IP control untouched** pending actual listen/bind review and a reversible plan. Do not disable Microsoft Defender/firewall or add Windows port forwarding.

## Next steps and acceptance
1. Prefer to log out and test login with the user's private new password in their local GUI once convenient; never send credentials in chat. Only then mark persistence `USER_RELOGIN_CONFIRMED`.
2. Navigate **OmniProxy → Endpoints** and inspect local base URL, protection and bind exposure. For screenshots, mask API keys, one-time tokens, personal identifiers and tokenized URLs; do not copy secrets to GitHub.
3. Before calling any real model/provider: verify non-public loopback access, `/v1` API auth, no paid fallback, account-level free eligibility, quota/overage controls and explicit user authorization for connecting a service.
4. **No claims of** running models, paid/free API entitlements, quotas, security certification, or production readiness at this stage.

**Project state:** `SECURITY_REQUIRE_LOGIN_ON`; `UI_PASSWORD_UPDATE_SUCCESS`; `IP_ACL_DISABLED`; `NETWORK_BIND_UNKNOWN`; `API_KEY_ENFORCEMENT_UNKNOWN`; `MODEL_CONNECTION_NOT_RUN`. No credentials or new permissions supplied in screenshot. D-005 OPEN, G3B/M1 personal-file guard CLOSED.
