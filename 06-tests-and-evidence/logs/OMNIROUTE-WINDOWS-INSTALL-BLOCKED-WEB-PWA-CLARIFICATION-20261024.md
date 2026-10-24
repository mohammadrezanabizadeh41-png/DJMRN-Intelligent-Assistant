# OmniRoute Windows installation blocked; web/PWA and hosted alternative clarification
Date: 2026-10-24. Category: user-reported attempt + independent vendor public documentation research. **No local diagnostic/installer log; no actual program execution observed.**

## Device evidence
- User reports downloading `OmniRoute.Setup.3.8.52.exe` (Windows installer for OmniRoute v3.8.52, from previously validated project GitHub Releases), but could not get Windows to install/allow the application to run after multiple attempts. The exact error dialog/event log/download SHA or Windows Security classification was **NOT supplied**. State is `BLOCKED_INSTALL_UNDIAGNOSED`, not `PRODUCT_FAIL` and not `INSTALLED`.
- Assistant previously suggested disabling Windows Security features; future assistants must **not** claim this is required, nor advise bypassing a malware detection. User does not want repeated PowerShell troubleshooting.

## Re-check web facts (public docs, no login)
- Open-source OmniRoute offers web UI and PWA as a **client of the running OmniRoute server**, usually `http://localhost:20128/dashboard`. No verified hosted full-feature OmniRoute user dashboard is available directly from product marketing site alone; references: https://github.com/cheaper-inference/OmniRoute , https://github.com/diegosouzapw/OmniRoute/blob/release/v3.8.51/docs/guides/PWA_GUIDE.md , https://omniroute.cheaperinference.com/deploy/.
- Publisher-related `https://cheaperinference.com/` offers a **different managed inference wallet-based service** with top-up from $5 and per-token billing, not the same self-hosted BYOK free-quota gateway and not compatible with free-only hard-zero assumption; terms: https://cheaperinference.com/ and https://www.cheaperinference.com/docs .
- Following D-017 and user web-only preference, Cloudflare AI Gateway is next: https://dash.cloudflare.com/ ; https://developers.cloudflare.com/ai-gateway/reference/pricing/ ; https://developers.cloudflare.com/ai-gateway/features/dynamic-routing/ . Hosted core API gateway may be free but account-specific Dynamic Routes Beta and upstream provider costs/quotas remain unknown until user checks.

## Decision boundary
Next: **Cloudflare AI Gateway website access/discovery only**; NOT signed in yet, no paid plan, no provider keys, no external model requests, no domain/webhook created by assistant, no credential capture. Preserve OmniRoute download/data for later diagnostics on explicit request. Never mark all 27 alternatives rejected; only rank 1 suspended for an undiagnosed installer blocker.
