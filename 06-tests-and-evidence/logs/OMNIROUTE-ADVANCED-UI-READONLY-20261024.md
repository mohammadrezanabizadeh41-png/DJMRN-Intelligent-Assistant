# DJMRN — OmniRoute v3.8.52 Advanced UI screenshot audit (read-only)
**Date:** 2026-10-24. **Status:** USER_SCREENSHOT_OBSERVED / NO_CONFIG_CHANGE / NO_PROVIDER / NO_API_REQUEST. **Authority:** evidence for ongoing OmniRoute working guide, not a new CURRENT.

## Originals retained and verified
The user submitted 4 screenshots of Configuration → Advanced. Original PNG bytes were verified **4/4 exact matches** against a ZIP SHA256 manifest. Originals are stored in private ChatGPT Library, **not in public GitHub**, at:
`/DJMRN/OmniRoute/2026-10-24/DJMRN_OmniRoute_Advanced_Screenshots_20261024.zip` (Library ID `libfile_d76258f5f930819189e6fc7eb07e461a`). ZIP SHA-256: `044befcf6ffd6f02833f0ec2f3f48257ac9ed2ac5c130c3c959336b23ac403fb`.

| Archived original | SHA256 |
|---|---|
| `screenshots/01-advanced-debug-and-rules.png` | `a54568fce368fecad7f6e86413597564c854bf2b5bb90222c03e9fe5a3b93077` |
| `screenshots/02-advanced-payload-editor.png` | `6568c80e566b3aafd5382d4c1b2b12866f77ea20c9043e66bf3d19fb8be94adb` |
| `screenshots/03-advanced-limits-cliproxy.png` | `56d7bf3601a3b9cbe0add8eb0ae790c98bc5d0660c93aa54d70b3c2210ba2349` |
| `screenshots/04-advanced-headroom.png` | `7adade0f92d802a871869b50a3d83210c000d5a3e45d495c011b3d2693da0944` |

## Exact UI observations
1. **Enable Debug Mode = OFF**; **Log Tool Sources = OFF**. Do not enable diagnostic capture without reviewing sensitivity and logging implications.
2. **Payload Rules** contains methods `default`, `override`, `filter`, `defaultRaw` and four counters each **0**; editor currently displays empty arrays for all four. Do not click `Save Payload Rules`, `Reset` or make unsolicited edits.
3. **Request Body Limit = 10 MB**, before parsing. Screenshot states dedicated upload routes retain built-in at least 100MB behavior. Keep at default for now.
4. **CLIProxyAPI Fallback = OFF**; **CLIProxyAPI Status: Not detected**. Import accounts from CLIProxyAPI button visible, noting re-use of existing OAuth accounts under `~/.cli-proxy-api/` for Gemini, Codex, Claude, Antigravity, Qwen, Kimi. This is a **sensitive account migration**, not a free-provider discovery test; no importing or starting CLIProxyAPI is authorized.
5. **Headroom proxy** optional URL textbox has placeholder `http://localhost:8787`; Start/Stop disabled-looking in captured view; this is **not evidence** that Headroom is running. No activation or usage planned.
6. **Not visible anywhere in four captured Advanced screenshots:** `REQUIRE_API_KEY`, `OMNIROUTE_SERVER_HOST`, bind host, LAN allowlist, or endpoint authentication toggle. This is **absence from shown UI**, not proof those controls are absent from all versions / lower pages / configuration files.

## Security inference and vendor canonical docs
- [Maintainer response discussing local-first 0.0.0.0 without key default](https://github.com/cheaper-inference/OmniRoute/discussions/11645). It documents `REQUIRE_API_KEY=true` or `OMNIROUTE_SERVER_HOST=127.0.0.1` as possible environment configuration — **does not establish actual effective Desktop settings**.
- [User Guide environment variable table](https://github.com/cheaper-inference/OmniRoute/wiki/de%E2%80%90User-Guide) documents `REQUIRE_API_KEY` separately from dashboard sign-in; docs are not independently tested on current Windows desktop.
- Screenshot evidence from Endpoints includes advertised `http://localhost:20128/v1`, green Running, and one private LAN address, and shows **0 chat/media models**. The LAN address is purposely omitted from GitHub public evidence. LAN exposure and unauthenticated calls still UNKNOWN.

## Strict smallest next safe test
While Desktop v3.8.52 is open, read local listening address with one **non-admin, no-write** Windows PowerShell query:
```powershell
Get-NetTCPConnection -State Listen -LocalPort 20128 | Select-Object LocalAddress,LocalPort,OwningProcess
```
Interpret `127.0.0.1` and `::1` as loopback-only; `0.0.0.0` or `::` indicates all-interfaces TCP bind, **not itself proof reachable past firewall**. Querying listener does not issue a model request, reveal secrets, install packages, alter network/firewall, or enable paid use.
- If all-interfaces: **STOP any provider connections** and propose reversible least-scope local-only binding/API-auth configuration for user approval (no unverified edits to secrets file or manual Windows firewall disabling).
- If loopback only: still check **API-key enforcement** before attaching paid or free provider credentials; dashboard login success does not prove inference endpoint authorization.
- If blank/error: debug listener state without guessing or changing platform security.

**Project status:** OmniRoute Desktop/UI RUNNING, core model catalog 0, real inference NOT_RUN, local listener scope UNKNOWN, API-key requirement UNKNOWN, free-only account eligibility UNKNOWN. No permissions or credentials were handled. G3B/M1 CLOSED; D-005 OPEN.
