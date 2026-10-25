# DJMRN — OmniRoute no-VPN Iran direct-access provider screen
**Reference date:** 2026-10-25; **scope:** public-source evaluation only; no user laptop or API credentials accessed; **status:** DEVICE_NETWORK_TEST_PENDING.

## User's newly binding constraint
User explicitly stated their Windows 11 laptop cannot currently use a VPN for this work, and asked **to test only providers not blocked in Iran**. Earlier "ignore Iran constraints" research instructions are overridden **for this concrete immediate operational onboarding**. Access proof requires a live minimal check from the user's actual unproxied Iranian network. Country-level reports cannot guarantee an ISP's path today. Differentiate browser console, authentication, API hostname, policy/region support, and real inference.

## Dated public evidence
1. Independent Iran-focused, reproducible research catalog [awesome-free-llm-apis-ir](https://github.com/alirezasafaei-dev/awesome-free-llm-apis-ir) and [direct-only listing](https://llm.persiantoolbox.ir/?access=direct) last named validations July/August 2026: **Direct connected** OVHcloud AI Endpoints, GitHub Models, Cloudflare Workers AI, SambaNova; **direct connection failed** Groq, OpenRouter in that catalog. These are dated observer-network observations, not proof on current user ISP. Groq console failed user browser, consistent but not full API finding.
2. **OVH official documentation** [Getting started](https://github.com/ovh/docs/blob/develop/pages/public_cloud/ai_machine_learning/endpoints_guide_01_getting_started/guide.en-ie.md) confirms Anonymous 2 requests/minute per IP/model and 429 on cap. Separate authenticated API keys require OVH Public Cloud project with payment method; **do not create that**. [OVH capabilities](https://github.com/ovh/docs/blob/develop/pages/public_cloud/ai_machine_learning/endpoints_guide_02_capabilities/guide.en-gb.md) same rate limits.
3. Independent [Iran provider record](https://llm.persiantoolbox.ir/providers/ovhcloud-ai-endpoints/) identifies `https://oai.endpoints.kepler.ai.cloud.ovh.net/v1`, anonym no-key no signup, direct successful July 24 2026. **One modern public third-party probe** (2026-10-19) lists anonymous access but also suggests shared anonymous throttling can make occasional 429: https://github.com/mvalentsev/awesome-free-ai-coding/blob/main/models/qwen3.8-27b.md .
4. OpenAI official supported-countries document says API unavailable in regions not listed, including Iran; do not confuse a gateway's network reachability with the end model's upstream region policy, and do not present foreign gateway or proxy as guaranteed authorization.

## New ranked operational route (zero cost, unproxied network)
**1. OVH anonymous trial is FIRST**: no key, account, card, payment or browser console, 2 RPM/model per vendor. Before custom provider setup, perform a cheap **read-only HTTP GET** from user's local PowerShell on the actual direct connection (VPN off):
```powershell
curl.exe -sS -o NUL -w 'HTTP %{http_code}\n' --connect-timeout 6 --max-time 12 'https://oai.endpoints.kepler.ai.cloud.ovh.net/v1/models'
```
Interpret `200` as HTTP API catalog reachable (but **not** inference verified); `401/403` as HTTP reached but auth/access gate; `429` as rate limit reached; `000` with curl DNS/TLS/timeout as no completed HTTP response. Mask any network identifiers in public logs. This GET is not inference/token usage and uses no credentials. It is a single conservative non-admin command, no security/VPN/firewall changes.
Then if direct-access PASS, test a single vendor-catalog-confirmed model with one synthetic tiny POST; then OpenAI-compatible Custom provider OmniRoute if UI allows truly no-auth provider creation. Distinguish OmniRoute's own client API key from external OVH anonymous upstream credentials. If built-in form requires upstream API key or price approval, stop and find a supported no-auth path; do not put user key upstream. 
**2. GitHub Models** and **3. Cloudflare Workers AI** as dated July 2026 Iran direct successes, but require account setup and issuance of scoped token. Cloudflare free quotas/eligibility must be revalidated for this account; do not take billing risk.
**4. SambaNova Free** as another dated Iran direct-success, registration may fail. Always check access on laptop before account creation.

## Status, not promises
No user network test actually run yet and **none of the above are guaranteed accessible today**; no Free provider attached. User prioritizes speed: no more chain of exploratory vendor suggestions that omit Iran connectivity. D-005 still OPEN, G3B/M1 CLOSED.
