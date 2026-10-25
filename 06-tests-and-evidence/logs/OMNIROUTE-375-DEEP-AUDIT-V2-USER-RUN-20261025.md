# DJMRN — OmniRoute 375 provider / 817 HTTPS deep audit v2: actual user Windows results

**Date:** 2026-10-25 user-local. **Evidence:** exact verbatim console output pasted by the user in ChatGPT from Windows PowerShell (not independently executed on this computer by the assistant). **Scope:** installed OmniRoute v3.8.52 public catalog, direct Windows internet HTTP probes without configured proxy, no VPN reported by user. The script made only HTTPS GET requests, no paid API completions or user credentials.

## Source code and test data
Full v2 script and input files pinned at [commit `a4b3a9a6bf76bcaf9456ad4516c10ab7e394c323`](https://github.com/mohammadrezanabizadeh41-png/DJMRN-Intelligent-Assistant/tree/a4b3a9a6bf76bcaf9456ad4516c10ab7e394c323/06-tests-and-evidence/tools/omniroute-iran-direct-check/).
- [375 canonical providers](../tools/omniroute-iran-direct-check/OmniRoute_v3.8.52_375_providers.csv)
- [280 documented HTTPS inference endpoint addresses](../tools/omniroute-iran-direct-check/OmniRoute_v3.8.52_upstream_api_snapshot.csv)
- [54 supplementary discovery paths including UncloseAI and LLM7 dashboard](../tools/omniroute-iran-direct-check/OmniRoute_v3.8.52_api_discovery_additions.csv)

## Exact report copied by user
```text
DJMRN DEEP: 375 IDs; 280 real API mappings; 54 discovery URLs; 817 distinct HTTPS GETs.
Direct connection (proxy bypass), GET only, no secrets, no logins, no payments, no model inference.
PROGRESS 12/817 ... PROGRESS 817/817

DJMRN_DEEP_SCAN_DATE=2026-10-25
CATALOG_PROVIDERS=375; DOCUMENTED_API_ROUTES=280; EXTRA_TARGETS=54; UNIQUE_HTTPS=817
WEB_HTTP=341/363; API_HOST_HTTP=251/280; API_ROUTE_GET_HTTP=247/280
API_HOST_NO_HTTP=29; HTTP_403=177; HTTP_451=4
IMPORTANT_API_HTTP=chutes=403,cloudflare-ai=301,deepseek=401,deepseek-web=403,g4f-gemini=302,g4f-groq=302,g4f-pollinations=302,gemini=403,gemini-web=403,groq=200,huggingface=404,llm7=404,modelscope=200,openference-api=200,openrouter=403,pollinations=200,siliconflow=404,uncloseai=401,zai=301,zai-web=200
UNCLOSEAI_MODELS=401:HTTP_401_AUTH_REQUIRED; LLM7_DASHBOARD=200:HTTP_200_ONLY_NO_INFERENCE_PROOF
DATA_FOLDER=C:\Users\Mrn7206\Desktop\DJMRN-DEEP-375-20261025-042141
NEXT_SEND=02_ALL_375_PROVIDER_DECISIONS.csv + 01_ALL_ADDRESSES_AND_REASONS.csv (if full map and reasons needed)
```

**Artifacts physically reside ONLY on user's Windows device and have NOT been uploaded or retrieved here.** Do not pretend to know exact addresses/reasons per all 375 without those source CSVs. User says screenshots cannot be sent; CSV file attachments (or text export) should be requested instead. Avoid pasting secrets: scanner uses no auth and records no credentials, but results include all target URLs, server headers, redirect hosts, DNS results, and error strings.

## Correct interpretation
- All 817 *distinct URLs* probed, progress completed, strong coverage. `341/363` site rows produced *some HTTP status* (including 4xx); `251/280` API-host rows produced HTTP response, while 29 did not; `247/280` documented inference URL rows produced a response to **GET**, which often is not the endpoint's intended `POST`. The 177 403 results and four 451 results count **probe/address rows** (possibly repeated across providers); not distinct denied accounts or countries.
- **Never interpret 200 on host/root as successful inference, nor treat 404 on API root as server unreachable, nor assume 403 means Iran filtering.** Distinguish 401 auth, 403 policy/WAF/region/credential cause unknown, 405 method GET disallowed for POST route, 301/302 redirect, 451 explicit server legal restriction.
- **Groq API host 200** *but the earlier explicit public models path `https://api.groq.com/openai/v1/models` returned 403 on this user's prior curated GET*, and Groq Console was reported inaccessible. This is consistent: different URL paths, tests/time may differ. **Not usable/eligible verified.**
- **LLM7 host 404** *but user previously observed `https://api.llm7.io/v1/models` 200*; `https://dash.llm7.io/` now 200. Host/root 404 does NOT erase two stronger earlier observations; Free-plan access, account creation, permitted Iran use and actual inference still unverified. LLM7 remains first credible **account-requiring** experimental candidate among named results, if official Free quota and region policy confirm.
- **UncloseAI public `https://hermes.ai.unturf.com/v1/models` returned 401**, contrary to expected keyless public discovery, hence **No-auth availability on user's network NOT_VERIFIED** and cannot be placed first or called successful. It could be a changed server policy or request-source gate; no secrets or security bypass. Site docs at https://uncloseai.com/inference.html describe model discovery but the **live user result supersedes old documentation for this ISP/test time**.
- **OpenRouter API host 403** while earlier public model catalog `https://openrouter.ai/api/v1/models` 200: host GET 403 is not proof account API would fail. Official https://openrouter.ai/pricing currently documents Free 50/day, 25+ free models, $0 cost, no card; login and eligibility not tested. No paid auto routing or credits enabled.
- Cloudflare `301` indicates redirect, not model access; Hugging Face 404 root not provider rejection; `Jina 451` observed in prior scan points to server-side legal restriction on that route; do not recommend Jina as immediately usable.
- `modelscope 200`, `openference-api 200`, `pollinations 200` host GET only; their actual account/inference free and regional eligibility unknown. Pollinations public model catalogue 200 from prior scan cannot establish anonymous chat because vendor docs require tokens for most inference.

## Immediate roadmap based on observed, not speculative:
**Phase A (already done):** 375 catalog/817 URLs direct network sweep. **PASS for census only**.
**Phase B (next, NO network retest):** obtain exactly the generated `01_ALL_ADDRESSES_AND_REASONS.csv` and `02_ALL_375_PROVIDER_DECISIONS.csv` from Desktop (prefer file attachments; if impossible, offer one offline PowerShell filter to print all high-priority per-provider HTTP codes/real route and reasons). Analyze full per-provider URL-specific evidence, not the small `IMPORTANT_API_HTTP` abbreviated subset. Rank targets by actual access of _real_ API endpoint, public model/catalog, signup dashboard, then verified $0 and Iran account policy. Exclude only actual blockers and be explicit about unknowns.
**Phase C (conditional user-controlled):** connect one genuinely Free eligible account to local OmniRoute; test a tiny user-approved model call. Then collect more Free providers and configure routed quality tiers, shared quota and failover only in verified $0 allowlist.
- **NO new network probes suggested** until full CSV inspection. Device is Windows 11 desktop; no VPN required for current test. No settings, firewall, admin or billing changes.
- D-005 OPEN, G3B/M1 personal files guard CLOSED.
