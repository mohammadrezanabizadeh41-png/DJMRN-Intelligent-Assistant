# DJMRN — COMPLETE single-run v3.8.52 provider + API reachability deep audit v2

**Created:** 2026-10-25. **Status:** Fully authored, pinned, data coverage validated and scripts read back; **USER_DEVICE_EXECUTION NOT RUN YET**. The user explicitly demanded **one full PowerShell operation**, not serial 2-at-a-time suggestions.

## Data provenance and exhaustive accounting
Pinned branch `release/v3.8.52` of official [OmniRoute provider reference](https://github.com/cheaper-inference/OmniRoute/blob/release/v3.8.52/docs/reference/PROVIDER_REFERENCE.md) contains **375** provider/integration IDs and official UI/website metadata. Our [complete CSV](./OmniRoute_v3.8.52_375_providers.csv) exactly 375 records, GitHub mirror. Sources that add actual inference routes:
- Official [OmniRoute v3.8.52 route test snapshot](https://github.com/cheaper-inference/OmniRoute/blob/release/v3.8.52/tests/snapshots/provider/translate-path.json), parsed **280 validated public HTTPS real inference URLs**, with host origins, provider IDs and protocol format, not guessed from websites: [upstream registry CSV](./OmniRoute_v3.8.52_upstream_api_snapshot.csv).
- **54 additional GET-only probes**: the 51 prior curated public API catalog/root URLs, plus documented `https://hermes.ai.unturf.com/v1/models` for **UncloseAI** from canonical upstream v3.8.52 registry, LLM7 Free dashboard `https://dash.llm7.io/`, OpenRouter signup `https://openrouter.ai/`: [discovery targets CSV](./OmniRoute_v3.8.52_api_discovery_additions.csv).
- The remaining 95 catalog IDs have **no fixed HTTPS inference URL in this specific snapshot**, and are **explicitly flagged**, not lost: includes local, OAuth, web-cookie, account-dependent and special/internally managed providers. This is full 375-provider accounting but **NOT a claim that every possible externally configurable API in the world has a static testable address**. Each of 375 gets an individual report row, even if no direct public API exists. Local servers are not interpreted as censored overseas hosts.

## PowerShell script
[Deep Audit v2](./Test-DJMRN-Provider-Deep-Audit-v2.ps1) is pinned to actual content at commit `54cae2be7102da8e300498f46ccf320bb5e2491b`; verified readback. Windows PowerShell **5.1**, GET / response-headers only, asynchronous 12-way batches, 8-second per-request timeout, HTTPS, **UseProxy=false**, no API tokens, no registration, no inference POST/usage, no firewall/hosts/registry/OS writes, no elevated privileges. It makes one network probe per distinct URL, even if shared by multiple providers, and maps result back onto all relevant provider rows. For HTTP failures, tries bounded DNS (3.5 seconds) and direct public-IP TCP443 (2.5 seconds), segregating DNS vs socket vs TLS vs timeout/reset. It does not attempt TCP to RFC1918 resolved-only addresses. The code does not automatically follow redirects and logs only the redirect host, not query strings/tokens. It records status codes and safe headers; it does not capture body or login tokens. `403` never attributed to government filtering unless explicit corroboration; `451` records legal restriction; `405` on a POST-only inference URL should be taken as expected GET disallowed, **not** a provider dead. A `200` on API host/website and `401` are never equated to working model inference or free account.

### Recommended 4-line manual PowerShell command
Paste directly into normal PowerShell (Internet direct, no VPN; **no ZIP, CMD, or admin**):
```powershell
$dir=Join-Path $env:TEMP 'DJMRN-FULL-AUDIT-v2'; New-Item -ItemType Directory -Force -Path $dir | Out-Null
$root='https://raw.githubusercontent.com/mohammadrezanabizadeh41-png/DJMRN-Intelligent-Assistant/54cae2be7102da8e300498f46ccf320bb5e2491b/06-tests-and-evidence/tools/omniroute-iran-direct-check'
@('OmniRoute_v3.8.52_375_providers.csv','OmniRoute_v3.8.52_upstream_api_snapshot.csv','OmniRoute_v3.8.52_api_discovery_additions.csv','Test-DJMRN-Provider-Deep-Audit-v2.ps1') | ForEach-Object { Invoke-WebRequest -Uri "$root/$_" -UseBasicParsing -TimeoutSec 30 -OutFile (Join-Path $dir $_) }
powershell.exe -NoProfile -ExecutionPolicy Bypass -File (Join-Path $dir 'Test-DJMRN-Provider-Deep-Audit-v2.ps1')
```
If any download fails, re-run **only after resolving it**; the script itself validates all input files and counts and refuses partial execution, avoiding false coverage. Temporary-process ExecutionPolicy Bypass applies only to that launched PowerShell process (not a Windows policy/registry change); user can inspect GitHub code before running.

### Desktop outputs
- `00_COPY_SUMMARY_TO_CHAT.txt` — compact results printout, user's immediate response to assistant
- `01_ALL_ADDRESSES_AND_REASONS.csv` and `.json` — complete endpoint tests: provider, kind, true URLs, HTTP status/reason, error text, DNS result, TCP443, content type, server header, redirect host, authorization scheme, latency, source
- `02_ALL_375_PROVIDER_DECISIONS.csv` — **exactly 375 providers**, website vs API host vs real API-route GET vs catalog reachability and all still unverified gates
- `03_REASON_COUNTS.csv` — reason-code and request-kind distribution
- `04_API_HTTP_RESPONDED_NOT_YET_USABLE.csv` — API HTTP response shortlist (NOT working model/free account)
- `05_FAILURE_OR_RESTRICTION_DETAILS.csv` — failures, 403/451, DNS/TCP diagnostics
- `06_REGISTRATION_DASHBOARDS.csv` — tested signup UIs 
- `07_NEXT_CONNECTION_ROADMAP.md` — ranked safe-next-action decision logic, still requiring real Free + Iran eligibility verification

Only **remote HTTP accessibility** can be inferred. Not proof of Iran regulatory authorization, successful local OmniRoute routing, per-account free tier, key issuance, or completion. `no API in snapshot` is a legitimate finding, not automatic block.

### Status / request to user
Ask the user to paste the **seven summary lines** displayed between `COPY THESE LINES TO CHAT` and `END`, and if they can attach a file send `02_ALL_375_PROVIDER_DECISIONS.csv` with `01_ALL_ADDRESSES_AND_REASONS.csv` for full address-by-address diagnosis. If file upload unavailable, use PowerShell `Get-Content -LiteralPath ... -Raw` and paste in batches; avoid pasting hundreds of lines without need. After real output, update this README + GitHub evidence and Notion continuity, then choose one verified Free provider and connect installed Desktop; no more 2-at-a-time speculative tests.

**Governance:** No credential collection, subscriptions, payment methods, blind provider activation, paid fallback, registry/config writes, source trust elevation or personal filesystem access. G3B/M1 CLOSED.
