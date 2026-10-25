# DJMRN — User Windows direct API/model-list scan: 314 URLs, 375 OmniRoute providers (2026-10-25)

**Evidence class:** USER-PASTED CONSOLE RESULT / OBSERVED ON USER WINDOWS / NOT INDEPENDENTLY RERUN. **State:** NETWORK GET SCAN COMPLETE; PROVIDER FREE/REGION/INFERENCE/OMNIROUTE CONNECTION NOT VERIFIED.

**Purpose:** Persist a directly machine-readable (line-delimited, stable `ProviderID | endpoint-kind:HTTP,... | optional first-five-model-IDs`) transcription of the user's actual completed run, so the DJMRN project assistant can continue selection WITHOUT more unguided scanning.

## Provenance and method

- Captured directly from the user's pasted full PowerShell console in this DJMRN conversation on **2026-10-25**. Progress reported `Checked 12/314` through `Checked 314/314`; final marker `DJMRN_OMNIROUTE_DIRECT_TEST=COMPLETE`.
- User ran **one inline PowerShell command in memory**, not a downloaded script, that used `System.Net.Http.HttpClient` with `UseProxy=false`, `UseCookies=false`, `AllowAutoRedirect=false`, 10-second timeout, GET only, up to 12 asynchronous requests per batch. No API keys, POSTs, generation, accounts, charging, installation, security changes or permanent output files by that command.
- Exact source lists loaded at Git commit `a4b3a9a6bf76bcaf9456ad4516c10ab7e394c323` from `06-tests-and-evidence/tools/omniroute-iran-direct-check/`: `OmniRoute_v3.8.52_375_providers.csv` (375 IDs), `OmniRoute_v3.8.52_upstream_api_snapshot.csv` (at least 280 mapped inference endpoints), `OmniRoute_v3.8.52_api_discovery_additions.csv` (at least 54 curated paths).
- De-duplicated 314 **HTTPS API/discovery URLs** (no provider website origin scan). 375 are **catalog IDs** including OAuth/web/local/other; do not equate them with 375 usable LLM APIs. The raw output prints row-level HTTP codes but **does not preserve exact error classes, response bodies, raw model list, DNS/TLS causes, timings, or complete model IDs**. Only first 5 discovered model IDs per provider are displayed; free hints blank across all rows.
- Provider group classification order in the user-executed script: any successfully parsed public `/models` response → A; otherwise any 401/405 → B_AUTH; otherwise any 200/400/404/429 → B_RESPONDED; otherwise 403/451 → C_ACCESS; other HTTP → C_OTHER; otherwise 0 → D; absent fixed public URL → E. **Group B classification is not proof of actual model reachability or working authentication. Group A is not an inference PASS.**
- User supplied final output explicitly reads `NO_KEYS=YES; NO_POST=YES; NO_BILLING=YES` and `FREE_AND_INFERENCE_NOT_YET_VERIFIED`.

## Verified console totals

```text
DJMRN_OMNIROUTE_DIRECT_TEST=COMPLETE
PROVIDERS=375; TESTED_URLS=314
NO_KEYS=YES; NO_POST=YES; NO_BILLING=YES
FREE_AND_INFERENCE_NOT_YET_VERIFIED
GROUP=A_PUBLIC_MODEL_LIST; COUNT=10
GROUP=B_AUTH_OR_METHOD_PENDING; COUNT=101
GROUP=B_API_RESPONDED_REVIEW; COUNT=72
GROUP=C_ACCESS_DENIED_REVIEW; COUNT=54
GROUP=C_OTHER_HTTP_REVIEW; COUNT=12
GROUP=D_NO_HTTP; COUNT=37
GROUP=E_NO_PUBLIC_API; COUNT=89
```

## Entire user-visible provider classification (transcribed without added provider rows)

**Format:** `ProviderID | kinds:HTTP | first-five public model IDs (A group only)`. The user's output reported `FREE_HINTS=` empty for **all** A–D rows; that empty finding is retained here by this declaration, not interpreted as paid or free.

### A_PUBLIC_MODEL_LIST (10)

```text
aimlapi | API_ROUTE:404,CURATED_PUBLIC_DISCOVERY:200 | moonshot/kimi-k3-1-pro,moonshot/kimi-k3-1-pro-highspeed,minimax/minimax-m3.1-flash,elorian/glimpse,inception/mercury-3
deepinfra | API_ROUTE:405,CURATED_PUBLIC_DISCOVERY:200 | meta-llama/Llama-Guard-4-12B,inclusionAI/Ling-3.0-flash-VL,anthropic/claude-opus-4-7,openai/whisper-large-v3,Qwen/Qwen3-Coder-480B-A35B-Instruct-Turbo
huggingface | API_ROUTE:401,CURATED_PUBLIC_DISCOVERY:200 | deepseek-ai/DeepSeek-V4.1-Flash-1017,Qwen/Qwen3.8-27B,meta-models/Muse-Spark-Open-816B-A42B,reflection/Beam-1.0-501B-A23B,deepseek-ai/DeepSeek-V4.1-Flash
llm7 | API_ROUTE:405,CURATED_PUBLIC_DISCOVERY:200 | DeepSeek-V4.1-Flash,Inkling-Small,L3-8B-Lunaris-v1-Turbo,Voxtral-Mini-3B-2507,Voxtral-Small-24B-2507
modelscope | API_ROUTE:404,CURATED_PUBLIC_DISCOVERY:200 | deepseek-ai/DeepSeek-V4-Flash-0731,deepseek-ai/DeepSeek-V4-Pro,deepseek-ai/DeepSeek-V4-Pro-0813,deepseek-ai/DeepSeek-V4.1-Flash,deepseek-ai/DeepSeek-V4.1-Flash-1017
novita | API_ROUTE:404,CURATED_PUBLIC_DISCOVERY:200 | deepseek/deepseek-v4.1-flash-1017,moonshotai/kimi-k3.1-pro-highspeed,moonshotai/kimi-k3.1-pro,minimax/minimax-m3.1-flash,zai-org/glm-5.3-flash
openference-api | API_ROUTE:401,CURATED_PUBLIC_DISCOVERY:200 | GLM-5.2,GLM-5.3,GLM-5.3-Flash,DeepSeek-V4-Flash-0731,MiniMax M3
requesty | API_ROUTE:404,CURATED_PUBLIC_DISCOVERY:200 | moonshot/kimi-k3.1-pro,moonshot/kimi-k3.1-pro-highspeed,melious/clef,melious/clef-flash,minimaxi/minimax-m3.1-flash
sambanova | API_ROUTE:405,CURATED_PUBLIC_DISCOVERY:200 | DeepSeek-V3.1,DeepSeek-V3.2,Meta-Llama-3.3-70B-Instruct,MiniMax-M3.1-Flash,gemma-4-31B-it
venice | API_ROUTE:404,CURATED_PUBLIC_DISCOVERY:200 | gemini-4-argon,gemini-3-6-flash,gemini-3-7-flash,gemini-3-8-flash,gemini-3-5-flash-lite
```

### B_AUTH_OR_METHOD_PENDING (101)

```text
aihorde | API_ROUTE:405
uncloseai | API_ROUTE:401,SOURCE_REGISTRY_MODELS:401
claude | API_ROUTE:405
codebuddy-cn | API_ROUTE:401
codex | API_ROUTE:405
ghe-copilot | API_ROUTE:405
github | API_ROUTE:405
grok-cli | API_ROUTE:405
muse-code | API_ROUTE:401
openference | API_ROUTE:401
qoder | API_ROUTE:401
xai-oauth | API_ROUTE:405
adapta-web | API_ROUTE:401
chatplayground | API_ROUTE:401
grok-web | API_ROUTE:401
inner-ai | API_ROUTE:405
notrack-web | API_ROUTE:405
perplexity-web | API_ROUTE:405
alibaba | API_ROUTE:400,CURATED_PUBLIC_DISCOVERY:401
anthropic | API_ROUTE:405,CURATED_PUBLIC_DISCOVERY:401
api-airforce | API_ROUTE:405
arcee-ai | API_ROUTE:405
auriko | API_ROUTE:405
bai | API_ROUTE:405
baichuan | API_ROUTE:401
baidu | API_ROUTE:401
bailian-coding-plan | API_ROUTE:401
bazaarlink | API_ROUTE:405
bigmodel | API_ROUTE:401,CURATED_PUBLIC_DISCOVERY:401
byteplus | API_ROUTE:401
cerebras | API_ROUTE:401,CURATED_PUBLIC_DISCOVERY:403
cheaperinference | API_ROUTE:405
cloudcode-one | API_ROUTE:405
clova-studio | API_ROUTE:401,CURATED_PUBLIC_DISCOVERY:401
codestral | API_ROUTE:401
deepai | API_ROUTE:401
deepseek | API_ROUTE:401,CURATED_PUBLIC_DISCOVERY:401
dgrid | API_ROUTE:401
digitalocean | API_ROUTE:405
dit | API_ROUTE:401
free-ai | API_ROUTE:405
freeaiapikey | API_ROUTE:405
glm | API_ROUTE:401,CURATED_PUBLIC_DISCOVERY:401
glm-cn | API_ROUTE:401
glmt | API_ROUTE:401
greenpt | API_ROUTE:401
helyxai | API_ROUTE:401
hyperbolic | API_ROUTE:405,CURATED_PUBLIC_DISCOVERY:401
iflytek | API_ROUTE:401
internlm | API_ROUTE:405
kenari | API_ROUTE:405
leonardo | API_ROUTE:401
liquid | API_ROUTE:405,CURATED_PUBLIC_DISCOVERY:403
literouter | API_ROUTE:401
llm-kiwi | API_ROUTE:405
logfare | API_ROUTE:405
longcat | API_ROUTE:405
meganova-ai | API_ROUTE:405
meta-llama | API_ROUTE:405
minimax | API_ROUTE:404,CURATED_PUBLIC_DISCOVERY:401
minimax-cn | API_ROUTE:404,CURATED_PUBLIC_DISCOVERY:401
mistral | API_ROUTE:401,CURATED_PUBLIC_DISCOVERY:401
mnn-ai | API_ROUTE:405
morph | API_ROUTE:401
naga-ac | API_ROUTE:405
naga-ai | API_ROUTE:405
nan | API_ROUTE:405
nara | API_ROUTE:401
nebius | API_ROUTE:405,CURATED_PUBLIC_DISCOVERY:401
nube | API_ROUTE:405
ofoxai | API_ROUTE:401
openai | API_ROUTE:401,CURATED_PUBLIC_DISCOVERY:401
openvecta | API_ROUTE:401
poe | API_ROUTE:405
qianfan | API_ROUTE:401
qwen-cloud | API_ROUTE:400,CURATED_PUBLIC_DISCOVERY:401
qwen-cloud-token-plan | API_ROUTE:401
regolo | API_ROUTE:405
sarvam | API_ROUTE:405
scaleway | API_ROUTE:401
sealion | API_ROUTE:405
siliconflow | API_ROUTE:404,CURATED_PUBLIC_DISCOVERY:401
sparkdesk | API_ROUTE:401
speka | API_ROUTE:405
stepfun | API_ROUTE:401
sumopod | API_ROUTE:405
synthetic | API_ROUTE:405
together | API_ROUTE:405,CURATED_PUBLIC_DISCOVERY:401
tokenmarket | API_ROUTE:401
typhoon | API_ROUTE:405
udio | API_ROUTE:405
unorouter | API_ROUTE:401
upstage | API_ROUTE:405
vercel-ai-gateway | API_ROUTE:405
volcengine-agent-plan | API_ROUTE:401
volcengine-coding-plan | API_ROUTE:401
wafer | API_ROUTE:401
xai | API_ROUTE:405,CURATED_PUBLIC_DISCOVERY:401
yi | API_ROUTE:405
zai | API_ROUTE:401,CURATED_PUBLIC_DISCOVERY:401
zerolimitai | API_ROUTE:405
```

### B_API_RESPONDED_REVIEW (72)

```text
cloudflare-playground | API_ROUTE:200
duckduckgo-web | API_ROUTE:400
veoaifree-web | API_ROUTE:400
kiro | API_ROUTE:404
zed-hosted | API_ROUTE:404
deepseek-web | API_ROUTE:200
maxai | API_ROUTE:200
promptql | API_ROUTE:200
syntx | API_ROUTE:404
t3-web | API_ROUTE:429
tinycms-web | API_ROUTE:404
yuanbao-web | API_ROUTE:404
zai-web | API_ROUTE:200
zenmux-free | API_ROUTE:404
agentrouter | API_ROUTE:404
agnes | API_ROUTE:404
agnes-cn | API_ROUTE:404
alibaba-cn | API_ROUTE:400
ant-ling | API_ROUTE:404
apmix | API_ROUTE:404
beatapi | API_ROUTE:404
bluesminds | API_ROUTE:404
charm-hyper | API_ROUTE:404
chenzk | API_ROUTE:404
cloudflare-ai | API_ROUTE:403,CURATED_PUBLIC_DISCOVERY:400
command-code | API_ROUTE:200
dahl | API_ROUTE:200
daoxe | API_ROUTE:404
demonroute | API_ROUTE:404
dify | API_ROUTE:404
dxnt | API_ROUTE:404
featherless-ai | API_ROUTE:404
freebuff | API_ROUTE:404
freetheai | API_ROUTE:404
friendliai | API_ROUTE:400
g4f-groq | API_ROUTE:429
g4f-nvidia | API_ROUTE:404
gitlawb | API_ROUTE:404
gitlawb-gmi | API_ROUTE:404
hcnsec | API_ROUTE:404
helixmind | API_ROUTE:404
heroku | API_ROUTE:404
ideogram | API_ROUTE:404
inference-net | API_ROUTE:400
kie | API_ROUTE:200
navy | API_ROUTE:404
nlpcloud | API_ROUTE:404
oneminai | API_ROUTE:404
onomeo | API_ROUTE:404
openadapter | API_ROUTE:404
opencode-go | API_ROUTE:404
opencode-zen | API_ROUTE:404
opper | API_ROUTE:404
poixe-ai | API_ROUTE:404
pollinations | API_ROUTE:404,CURATED_PUBLIC_DISCOVERY:200
publicai | API_ROUTE:404
seekai | API_ROUTE:404
sensenova | API_ROUTE:404
stability-ai | CURATED_PUBLIC_DISCOVERY:404
token-kiosk | API_ROUTE:404
tokenreply | API_ROUTE:404
tokenrouter | API_ROUTE:404
unifically | API_ROUTE:404
v0-vercel | API_ROUTE:404
xiaomi-mimo | API_ROUTE:404
xiaomi-mimo-token-plan | API_ROUTE:404
xkiro | API_ROUTE:404
y-api | API_ROUTE:404
yolo-auto | API_ROUTE:404
zenmux | API_ROUTE:404
zylo-api | API_ROUTE:404
assemblyai | CURATED_PUBLIC_DISCOVERY:404
```

### C_ACCESS_DENIED_REVIEW (54)

```text
cline | API_ROUTE:403
clinepass | API_ROUTE:403
cursor | API_ROUTE:403
kilocode | API_ROUTE:403
kimi-coding | API_ROUTE:403
blackbox-web | API_ROUTE:403
chatgpt-web | API_ROUTE:403
chatgpt-web-codex | API_ROUTE:403
claude-web | API_ROUTE:403
conol-web | API_ROUTE:451
gemini-web | API_ROUTE:403
hyperagent | API_ROUTE:403
kimi-web | API_ROUTE:403
lmarena | API_ROUTE:403
twinmind | API_ROUTE:403
uc | API_ROUTE:403
ai21 | API_ROUTE:403
baseten | API_ROUTE:403,CURATED_PUBLIC_DISCOVERY:403
blackbox | API_ROUTE:403
bytez | API_ROUTE:403
chutes | API_ROUTE:403,CURATED_PUBLIC_DISCOVERY:403
cohere | API_ROUTE:403,CURATED_PUBLIC_DISCOVERY:403
cursor-api | API_ROUTE:403
electronhub | API_ROUTE:403
factory | API_ROUTE:403
fastrouter | API_ROUTE:403
fireworks | API_ROUTE:403,CURATED_PUBLIC_DISCOVERY:403
gemini | API_ROUTE:403,CURATED_PUBLIC_DISCOVERY:403
groq | API_ROUTE:403,CURATED_PUBLIC_DISCOVERY:403
inception | API_ROUTE:403
jina-ai | CURATED_PUBLIC_DISCOVERY:451
jina-reader | CURATED_PUBLIC_DISCOVERY:451
kilo-gateway | API_ROUTE:403
kimi | API_ROUTE:403,CURATED_PUBLIC_DISCOVERY:403
kimi-coding-apikey | API_ROUTE:403
llmgateway | API_ROUTE:403
moonshot | API_ROUTE:403,CURATED_PUBLIC_DISCOVERY:403
nanogpt | API_ROUTE:403
nous-research | API_ROUTE:403
nvidia | API_ROUTE:403,CURATED_PUBLIC_DISCOVERY:403
ollama-cloud | API_ROUTE:403,CURATED_PUBLIC_DISCOVERY:403
openrouter | API_ROUTE:403,CURATED_PUBLIC_DISCOVERY:403
perplexity | API_ROUTE:403,CURATED_PUBLIC_DISCOVERY:403
perplexity-agent | API_ROUTE:403
plamo | API_ROUTE:403
poolside | API_ROUTE:403
reka | API_ROUTE:403,CURATED_PUBLIC_DISCOVERY:403
routeway | API_ROUTE:403
uc-direct | API_ROUTE:403
vertex | API_ROUTE:403
void-ai | API_ROUTE:403
wandb | API_ROUTE:403
writer | API_ROUTE:403
elevenlabs | CURATED_PUBLIC_DISCOVERY:403
```

### C_OTHER_HTTP_REVIEW (12)

```text
trae | API_ROUTE:503
doubao-web | API_ROUTE:503
huggingchat | API_ROUTE:302
chat-oripe | API_ROUTE:530
chatanywhere | API_ROUTE:302
coze | API_ROUTE:503
crof | API_ROUTE:302
freeinference | API_ROUTE:502
orcarouter | API_ROUTE:301
pioneer | API_ROUTE:410
tabitoken | API_ROUTE:500
x5lab | API_ROUTE:530
```

### D_NO_HTTP (37)

```text
agy | API_ROUTE:0
antigravity | API_ROUTE:0
codebuddy-intl | API_ROUTE:0
devin-desktop | API_ROUTE:0
gitlab-duo | API_ROUTE:0
workbuddy | API_ROUTE:0
muse-spark-web | API_ROUTE:0
notion-web | API_ROUTE:0
tencent-aistudio-web | API_ROUTE:0
ainative | API_ROUTE:0
aion | API_ROUTE:0
anyapi | API_ROUTE:0
databricks | API_ROUTE:0
doubao | API_ROUTE:0
eurouter | API_ROUTE:0
fal-ai | CURATED_PUBLIC_DISCOVERY:0
freemodel-dev | API_ROUTE:0
g4f-gemini | API_ROUTE:0
g4f-ollama | API_ROUTE:0
g4f-pollinations | API_ROUTE:0
galadriel | API_ROUTE:0
gigachat | API_ROUTE:0
haiper | API_ROUTE:0
lambda-ai | API_ROUTE:0
llamagate | API_ROUTE:0
lyceum | API_ROUTE:0
maritalk | API_ROUTE:0
mixlayer | API_ROUTE:0
modal | API_ROUTE:0
monsterapi | API_ROUTE:0
nscale | API_ROUTE:0
ovhcloud | API_ROUTE:0,CURATED_PUBLIC_DISCOVERY:0
predibase | API_ROUTE:0
qiniu | API_ROUTE:0
tencent | API_ROUTE:0
vertex-partner | API_ROUTE:0
volcengine | API_ROUTE:0
```

### E_NO_PUBLIC_API (89)

The PowerShell report explicitly printed `GROUP=E_NO_PUBLIC_API; COUNT=89` and `No fixed public API in catalog; not a censorship result.` **It did not print individual names** for those 89. Recover their IDs only by set-difference against the pinned 375-provider CSV, not invention. These entries may be local, account/session-dependent, or without a documented fixed external URL.

## Analysis guardrails and handoff for project assistant

1. **Ten valid public model-catalog parses (A)**: `aimlapi`, `deepinfra`, `huggingface`, `llm7`, `modelscope`, `novita`, `openference-api`, `requesty`, `sambanova`, `venice`. Each provided first five ID strings shown above (50 strings total, **not** evidence of all or free models). For actual chat, auth/billing/region/allowed-model metadata must be independently checked.
2. **101 auth/method and 72 route-response records** include 401/405/404; 405 is expected for GET to a POST-only inference route; 404 may be wrong method/path or unavailable endpoint; 401 is auth required. None is a final network-censorship diagnosis. **54 denial-like, 12 other HTTP, 37 no HTTP**, and 89 undocumented fixed API entries remain distinct buckets.
3. Contradiction/temporal movement is a useful finding, not data corruption: `sambanova` was TIMEOUT in an earlier limited scan but this run has models HTTP 200 + inference-path GET 405; `openrouter` was models HTTP 200 in an earlier limited scan but this run shows HTTP 403 on both checked paths. `uncloseai` still returns 401 on anonymous models discovery. Preserve timestamps, paths, and methods; avoid blanket statements `works in Iran` or `blocked in Iran`.
4. Free-tier status **UNKNOWN** for every model in this run. The `FREE_HINTS=` field is blank for every printed row; no `:free` or zero-price API-model metadata was captured. Do not translate model names into free entitlements. Cost UNKNOWN → no activation/inference.
5. **No new mass GET scan required by this evidence.** Compare with earlier [v2 user deep audit](https://github.com/mohammadrezanabizadeh41-png/DJMRN-Intelligent-Assistant/blob/main/06-tests-and-evidence/logs/OMNIROUTE-375-DEEP-AUDIT-V2-USER-RUN-20261025.md) and [v3 offline AnalyzeExisting result](https://github.com/mohammadrezanabizadeh41-png/DJMRN-Intelligent-Assistant/blob/main/06-tests-and-evidence/logs/OMNIROUTE-PROVIDER-GATE-V3-USER-ANALYZE-20261025.md); each tests different scope, preserves separate provenance and may show time/path differences.
6. Next useful output is a **single actionable connection shortlist** built from these row results, real vendor policy/eligible Free $0/no card and model ID confirmation (with source links), plus explicit status columns `NETWORK_CATALOG_PASS`, `AUTH_PENDING`, `INFERENCE_NOT_TESTED`, `FREE_NOT_VERIFIED`, `REGION_NOT_VERIFIED`. To confirm one service actually works with OmniRoute, a separate minimal approved non-billable inference/model integration is necessary.
7. Do NOT silently mutate the existing provider source lists or prior reports; this is an additional observation only. No operational architecture decision, Notion current authority change, rollout or activated Provider is authorized by this evidence.

**Retention:** raw user-pasted text is the evidence authority for this observation; this GitHub report is a structured transcription with exactly 286 printed ID rows + 89 unlisted IDs (375 total). Prefix `DJMRN_OMNIROUTE_DIRECT_TEST=COMPLETE` is not equivalent to `PROVIDER_OPERATIONAL=PASS`.
