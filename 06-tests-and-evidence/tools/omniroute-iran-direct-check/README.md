# DJMRN — OmniRoute v3.8.52 Iran direct-access 375-provider census

**Created 2026-10-25**; source snapshot: official `release/v3.8.52`, [Provider Reference](https://github.com/cheaper-inference/OmniRoute/blob/release/v3.8.52/docs/reference/PROVIDER_REFERENCE.md), last generated 2026-10-18. User wants to check all **375** registered OmniRoute provider/integration IDs on **their own Iranian ISP without VPN**. User originally reported Groq console inaccessible, and direct `curl.exe` to OVHcloud `https://oai.endpoints.kepler.ai.cloud.ovh.net/v1/models` returned `curl: (35) Recv failure: Connection was reset` and `HTTP 000`; this is evidence only for that ISP/test time, not a blanket countrywide censorship conclusion.

## Canonical full catalog
[OmniRoute_v3.8.52_375_providers.csv](./OmniRoute_v3.8.52_375_providers.csv) was **actually parsed from 375 Markdown rows of the exact official version's `docs/reference/PROVIDER_REFERENCE.md`** and pinned into the project; GitHub commit `f76ce1a529b54f3fe0e3fec1e5156aaca84d8fea`. Counts: **9 No-auth + 27 OAuth + 37 Web Cookie + 252 API Key + 14 Local + 18 Search + 12 Audio + 2 Upstream Proxy + 3 Cloud Agent + 1 System = 375**. 363 official rows provide a website URL; 12 do not. The provider's website address is **NOT** its inference API hostname. Tags marking free are unverified discovery metadata, not an account-price guarantee.

## Ready-to-run Windows package
**Private ChatGPT Library archived binary:** `/DJMRN/OmniRoute/2026-10-25/DJMRN_OmniRoute_Iran_Direct_375_Provider_Tester_v1.zip` (id: `libfile_9169d51a56088191beee041098ac274e`), sha256 `a2970c5a8e5cda491bc313c8f1f67940a9393a3212863a0e29d8dfa151c867fa`; ZIP CRC checked. It is not committed to this public GitHub repository as binary. The same package was directly delivered to the user as a conversation file on 2026-10-25.

ZIP contains:
- `Test-DJMRN-OmniRoute-Providers.ps1` (Windows PowerShell 5.1 script)
- `RUN_DJMRN_PROVIDER_TEST.cmd` (double-click launcher; runs PowerShell with process-scoped `ExecutionPolicy Bypass`, not system policy)
- `OmniRoute_v3.8.52_375_providers.csv` (**offline** provider IDs + category + official website URL, **375 exact IDs and 363 source URLs**; for offline compression `ProviderName` field repeats the canonical ID; human-readable names and details remain available in the canonical full GitHub CSV above)
- `README_FA.md` (Persian instructions)

The script first loads the **bundled CSV offline**; it falls back to downloading the static **trusted project catalog CSV** from GitHub only when local CSV missing; it refuses to claim 375 coverage if row count differs. No code remotely downloaded/executed. Every source provider gets at least one **output result row**, including `NO_HTTPS_TARGET_IN_SOURCE` and `LOCAL_OR_INTERNAL_SKIP`. It sends **GET** requests with `HttpCompletionOption.ResponseHeadersRead` (does not consume bodies), no tokens, no login, no `POST`, no model inference, no billing, no software installs, no privilege escalation, no Windows network/firewall/registry changes. `HttpClientHandler.UseProxy = false` bypasses explicit system proxy configuration for direct-ISP probe, without changing user network settings.

- Default async batches of **16**, timeout **9 seconds** per request; deduplicates identical URLs; tests provider's **HTTPS website origin** only for domains from the official reference; excludes local/internal providers by default. Does **not** attempt unsafe reverse-engineered web/cookie/OAuth endpoints.
- Separately curates **51 public API URL candidates** (OpenAI, Anthropic, Gemini, Groq, OVH, Cloudflare, NVIDIA, Cerebras, Together, Fireworks, DeepSeek, etc.) and performs read-only GET to their public API endpoint or root, **not a billable inference request**. Some URLs may have changed; they are candidates, not guaranteed official current defaults.
- If a website returns 200, 301, 401, 403, 404, 429, 451, etc., it is evidence of HTTP response only. **401/403 do not prove a provider is usable**, and website success does not prove its API works. Error taxonomy distinguishes DNS, TLS, reset/closed, timeout, HTTP restriction and untestable entries. Geo/legal 451 indicates explicit restriction, other failures alone do not prove censorship.
- All outputs written to a new dated folder on user's desktop: `DJMRN_ALL_375_provider_test_results.csv`, `DJMRN_ALL_375_provider_test_results.json`, `DJMRN_API_HTTP_RESPONDED.csv`, `READ_ME_RESULTS.txt`, full offline source catalog. No keys or private IP/device IDs in published project doc. **No actual user network test has been run with this script yet.**

## Next step and interpretations
1. User downloads archived ZIP, extracts it, double-clicks `RUN_DJMRN_PROVIDER_TEST.cmd`; if Windows warns, user reviews script and decides whether to execute; no admin required.
2. Collect CSV result from user and filter `API_CANDIDATE` rows with an HTTP response first, then `WEBSITE` success that may warrant provider API discovery. Never call results `Iran unblocked` without proving the actual API and account eligibility.
3. For 2–5 best candidates, verify **real free $0 without payment card**, terms for Iranian residents, a separate *authorized* public API endpoint, model ID and one small inference call only with user permission. Then add usable route(s) to the already installed Desktop OmniRoute; prohibit charged fallback.
4. Preserve exact false positives (website open/API blocked), provider throttling and read-only network evidence. Do not revive Groq/OVH without a changed ISP/path.

**State:** TOOL_DELIVERED, DEVICE_RUN_PENDING, CONNECTED_FREE_PROVIDER_NONE_VERIFIED, cost controls remain explicit, D-005 OPEN; G3B/M1 file guard CLOSED.

## Direct manual copy/paste alternative — no ZIP or double-click needed (2026-10-25)
When user wants to manually paste a PowerShell command and return its answer as plain chat text, use the project-maintained [Test-DJMRN-375-Manual.ps1](./Test-DJMRN-375-Manual.ps1) together with this [pinned 375-record catalog](./OmniRoute_v3.8.52_375_providers.csv). Fetch these two **static reviewed files** into `$env:TEMP\DJMRN-375` via `Invoke-WebRequest`, then run `powershell.exe -NoProfile -ExecutionPolicy Bypass -File ...` to change execution policy for just the subprocess (no permanent machine changes). This does not use `Invoke-Expression`, `irm | iex`, administrator rights or system/registry edits.

The script checks each of 375 catalog IDs for a usable HTTPS site origin, marks unknown/local missing entries separately, and performs 51 separately curated public API probes, with batched .NET HttpClient GET requests and `UseProxy=false`. It saves complete CSV on Desktop and **prints four text-only lines** with `API_HTTP_RESPONDED=` and `API_NO_HTTP=` to paste into chat. This is *network reachability only* (not proof of model inference, free account, service eligibility, or absence of ISP filtering). If `raw.githubusercontent.com` itself is inaccessible from the user ISP, use the earlier offline ZIP fallback instead of inventing a partial catalog.

Direct-copy bootstrap for Windows PowerShell 5.1 (all 4 lines are part of the command):
```powershell
$dir = Join-Path $env:TEMP 'DJMRN-375'; New-Item -ItemType Directory -Force -Path $dir | Out-Null
$root = 'https://raw.githubusercontent.com/mohammadrezanabizadeh41-png/DJMRN-Intelligent-Assistant/main/06-tests-and-evidence/tools/omniroute-iran-direct-check'
Invoke-WebRequest "$root/Test-DJMRN-375-Manual.ps1" -UseBasicParsing -OutFile "$dir/Test-DJMRN-375-Manual.ps1"
Invoke-WebRequest "$root/OmniRoute_v3.8.52_375_providers.csv" -UseBasicParsing -OutFile "$dir/OmniRoute_v3.8.52_375_providers.csv"
powershell.exe -NoProfile -ExecutionPolicy Bypass -File "$dir/Test-DJMRN-375-Manual.ps1"
```
