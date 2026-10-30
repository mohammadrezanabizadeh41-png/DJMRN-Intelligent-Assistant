# DJMRN — 9-stage free API availability research queue (252 OmniRoute providers)

**Reference date:** 2026-10-30  |  **Status:** Stages 1–4 PUBLIC RESEARCH COMPLETE, remaining stages 5–9 pending. The roster and membership are immutable. See the separate S01 findings and cumulative positive register.
**Frozen source:** [OmniRoute v3.8.52 complete 252 API-key provider catalog](OMNIROUTE-252-APIKEY-PROVIDER-CATALOG-V3852-20261030.md). Stage IDs and memberships remain immutable until the user explicitly asks for a new partition.

## Exactly one research question

> Does this provider offer a genuinely free, ongoing/renewable API usage allowance, or only a one-time trial/promo credit? If neither, is the API paid-only? Verify with **current official sources** whenever available.

**Scope:** API access—not free website chat, free open-source model weights, free SDKs, self-hosting, paid subscriptions, marketing "free" labels without recurring allowances, or models on unrelated hosts. A startup credit that expires does NOT qualify as a renewable free tier. A recurring small monthly credit can qualify as `RECURRING_FREE_CREDIT` only with verified applicability and recurrence; record it separately from zero-priced per-model requests. Provider may offer a mix of recurring free models and trial credit: classify `MIXED` with evidence.

## Run rules (for when the user asks for a stage)

1. The phrase **«مرحله N»**, **«سرچ مرحله N»**, or **`DJMRN-FREE-API-SCAN-SNN`** unambiguously selects exactly that numbered stage's provider rows below. Research ALL assigned rows using fresh public official pricing/free-tier/API policy, Terms or FAQ sources where possible; confirm information publication/update dates and don't silently rely on the 2026-10-30 OmniRoute catalog as proof of free offerings. When sites are blocked or uncertain, mark `UNVERIFIED` and cite the limitation rather than fabricate.
2. Investigate **ONLY the single free-API question** per provider. Do not perform model quality tests, register accounts, use users' credentials, enable billing, send paid calls, or divert into broader model comparison.
3. For each assigned row capture: row #, provider name and provider ID, classification, brief free/API evidence (e.g. recurring cap and unit if published), one-time credit if any, official pricing/policy URL(s), as-of research date, confidence (`OFFICIAL_VERIFIED`, `SECONDARY_ONLY`, or `UNVERIFIED`). Unknown shared-account quota or requirements should remain unknown.
4. Mutually understandable final classification values: `RECURRING_FREE_API` (verified renewable request/token/free model allowance), `RECURRING_FREE_CREDIT` (verified renewed monthly/other credit for API), `TRIAL_ONLY` (one-time/temporary), `PAID_ONLY` (explicit current official billing, no documented free API), `MIXED` (both renewable free and trial/paid options), `NO_PUBLIC_API` (verified no publicly offered API), `UNVERIFIED` (insufficient/contradictory sources). Do not assume free web chat = free API.
5. After stage execution, prepare a separate **stage findings** file under `06-tests-and-evidence/provider-research/` (suggested `DJMRN-FREE-API-SCAN-SNN-RESULTS-YYYYMMDD.md`) only if the user has asked to save it or the ongoing workflow explicitly directs archiving; cite links per row. Track completed/remaining stages and preserve audit trail without retroactively altering frozen roster.
6. At the end of each stage report how many were found recurring free, one-time trial, paid only, mixed, and unverified. Prioritize unresolved official corroboration as follow-up, never claim the whole 252 done from a partial batch.

### CONDITIONAL-FREE-API-INCLUSION-POLICY-20261030 — policy for stages S04–S09

Record **real renewable free API** as **POSITIVE even if conditional** on GitHub signup/history, noncommercial/research use, manual approvals, daily Check-in, region, identity, privacy terms, or other requirements. Keep it in the same cumulative positive master. Write the condition and a `POSITIVE_CONDITIONAL` secondary status, and expressly distinguish **free API existence** from **commercial-use approval** and **DJMRN account eligibility**.

Only mandatory up-front paid balance/deposit or paid subscription (without another genuine zero-payment API route), non-replenished trial credit, and time-limited free promotions are excluded from the strict zero-payment recurring list. Ordinary quota limits are documented, not disqualifiers. For otherwise positive entries not thoroughly assessed for eligibility conditions, use `CONDITIONS_NOT_YET_AUDITED`, **never assume unconditional**.

## 9 locked stages

| Stage trigger | Source rows | Entries | Initial status |
|---|---:|---:|---|
| `DJMRN-FREE-API-SCAN-S01` / «مرحله 1» | 1–30 | 30 | COMPLETED PUBLIC RESEARCH 2026-10-30 · [S01 findings](DJMRN-FREE-API-SCAN-S01-RESULTS-20261030.md) · [positive master](DJMRN-FREE-API-POSITIVE-MASTER-252-20261030.md) |
| `DJMRN-FREE-API-SCAN-S02` / «مرحله 2» | 31–60 | 30 | COMPLETED PUBLIC RESEARCH 2026-10-30 · [S02 findings](DJMRN-FREE-API-SCAN-S02-RESULTS-20261030.md) · [34-positive master](DJMRN-FREE-API-POSITIVE-MASTER-252-20261030.md) |
| `DJMRN-FREE-API-SCAN-S03` / «مرحله 3» | 61–90 | 30 | COMPLETED PUBLIC RESEARCH 2026-10-30 · [S03 findings](DJMRN-FREE-API-SCAN-S03-RESULTS-20261030.md) · [39-positive master](DJMRN-FREE-API-POSITIVE-MASTER-252-20261030.md) |
| `DJMRN-FREE-API-SCAN-S04` / «مرحله 4» | 91–120 | 30 | COMPLETED PUBLIC RESEARCH 2026-10-30 · [S04 findings](DJMRN-FREE-API-SCAN-S04-RESULTS-20261030.md) · [52-positive-ID master](DJMRN-FREE-API-POSITIVE-MASTER-252-20261030.md) |
| `DJMRN-FREE-API-SCAN-S05` / «مرحله 5» | 121–150 | 30 | READY / NOT RESEARCHED |
| `DJMRN-FREE-API-SCAN-S06` / «مرحله 6» | 151–180 | 30 | READY / NOT RESEARCHED |
| `DJMRN-FREE-API-SCAN-S07` / «مرحله 7» | 181–210 | 30 | READY / NOT RESEARCHED |
| `DJMRN-FREE-API-SCAN-S08` / «مرحله 8» | 211–240 | 30 | READY / NOT RESEARCHED |
| `DJMRN-FREE-API-SCAN-S09` / «مرحله 9» | 241–252 | 12 | READY / NOT RESEARCHED |

---

## Stage 1 — DJMRN-FREE-API-SCAN-S01 (source rows 1–30)

**Trigger:** «مرحله 1» · **Entries:** 30 · **Status:** PUBLIC RESEARCH COMPLETED 2026-10-30; [full 30-provider result](DJMRN-FREE-API-SCAN-S01-RESULTS-20261030.md); [master 20 positives](DJMRN-FREE-API-POSITIVE-MASTER-252-20261030.md).

| Source row | Provider ID (exact) | Catalog name | UI status |
|---:|---|---|---|
| 1 | `onomeo` | onomeo | VISIBLE |
| 2 | `unifically` | Unifically | VISIBLE |
| 3 | `oneminai` | 1min.AI | VISIBLE |
| 4 | `cheaperinference` | Cheaper Inference | VISIBLE |
| 5 | `freebuff` | Freebuff | VISIBLE |
| 6 | `charm-hyper` | Charm Hyper | VISIBLE |
| 7 | `agentrouter` | AgentRouter | VISIBLE |
| 8 | `unorouter` | UnoRouter | VISIBLE |
| 9 | `command-code` | Command Code | VISIBLE |
| 10 | `openrouter` | OpenRouter | VISIBLE |
| 11 | `opper` | Opper | VISIBLE |
| 12 | `requesty` | Requesty | VISIBLE |
| 13 | `zylo-api` | Zylo API | VISIBLE |
| 14 | `fastrouter` | FastRouter | VISIBLE |
| 15 | `anyapi` | AnyAPI AI | VISIBLE |
| 16 | `electronhub` | Electron Hub | VISIBLE |
| 17 | `llmgateway` | LLM Gateway | VISIBLE |
| 18 | `lyceum` | Lyceum | VISIBLE |
| 19 | `llm-kiwi` | LLM.Kiwi | VISIBLE |
| 20 | `literouter` | LiteRouter | VISIBLE |
| 21 | `greenpt` | GreenPT | VISIBLE |
| 22 | `eurouter` | EURouter | VISIBLE |
| 23 | `y-api` | Y-API | VISIBLE |
| 24 | `mnn-ai` | MNN AI | VISIBLE |
| 25 | `meganova-ai` | MegaNova AI | VISIBLE |
| 26 | `mixlayer` | Mixlayer | VISIBLE |
| 27 | `speka` | Speka AI | VISIBLE |
| 28 | `tokenreply` | TokenReply | VISIBLE |
| 29 | `yolo-auto` | Yolo-Auto | VISIBLE |
| 30 | `dxnt` | DXNT / DX Token | VISIBLE |


## Stage 2 — DJMRN-FREE-API-SCAN-S02 (source rows 31–60)

**Trigger:** «مرحله 2» · **Entries:** 30 · **Status:** PUBLIC RESEARCH COMPLETED 2026-10-30 · [S02 30-provider report](DJMRN-FREE-API-SCAN-S02-RESULTS-20261030.md) · [cumulative 34 positives](DJMRN-FREE-API-POSITIVE-MASTER-252-20261030.md).

| Source row | Provider ID (exact) | Catalog name | UI status |
|---:|---|---|---|
| 31 | `cloudcode-one` | CloudCode.ONE | VISIBLE |
| 32 | `ofoxai` | OfoxAI | VISIBLE |
| 33 | `zerolimitai` | ZeroLimitAI | VISIBLE |
| 34 | `chatanywhere` | ChatAnywhere | VISIBLE |
| 35 | `helyxai` | Helyx AI | VISIBLE |
| 36 | `auriko` | Auriko | VISIBLE |
| 37 | `poixe-ai` | Poixe AI | VISIBLE |
| 38 | `naga-ai` | Naga AI | VISIBLE |
| 39 | `chat-oripe` | Chat Oripe | VISIBLE |
| 40 | `freeinference` | FreeInference | VISIBLE |
| 41 | `free-ai` | Free.ai | VISIBLE |
| 42 | `dgrid` | DGrid | VISIBLE |
| 43 | `qiniu` | Qiniu | VISIBLE |
| 44 | `orcarouter` | OrcaRouter | VISIBLE |
| 45 | `api-airforce` | Api.airforce | VISIBLE |
| 46 | `crof` | CrofAI | VISIBLE |
| 47 | `bazaarlink` | BazaarLink | VISIBLE |
| 48 | `synthetic` | Synthetic | VISIBLE |
| 49 | `kilo-gateway` | Kilo Gateway | VISIBLE |
| 50 | `wafer` | Wafer AI | VISIBLE |
| 51 | `opencode-zen` | OpenCode Zen | VISIBLE |
| 52 | `opencode-go` | OpenCode Go | VISIBLE |
| 53 | `dahl` | Dahl | VISIBLE |
| 54 | `freetheai` | FreeTheAi | VISIBLE |
| 55 | `g4f-groq` | g4f.space — Groq | VISIBLE |
| 56 | `g4f-gemini` | g4f.space — Gemini | VISIBLE |
| 57 | `g4f-pollinations` | g4f.space — Pollinations | VISIBLE |
| 58 | `g4f-ollama` | g4f.space — Ollama | VISIBLE |
| 59 | `g4f-nvidia` | g4f.space — NVIDIA | VISIBLE |
| 60 | `vercel-ai-gateway` | Vercel AI Gateway | VISIBLE |


## Stage 3 — DJMRN-FREE-API-SCAN-S03 (source rows 61–90)

**Trigger:** «مرحله 3» · **Entries:** 30 · **Status:** PUBLIC RESEARCH COMPLETED 2026-10-30 · [S03 30-provider report](DJMRN-FREE-API-SCAN-S03-RESULTS-20261030.md) · [cumulative 39 positives](DJMRN-FREE-API-POSITIVE-MASTER-252-20261030.md).

| Source row | Provider ID (exact) | Catalog name | UI status |
|---:|---|---|---|
| 61 | `llm7` | LLM7.io | VISIBLE |
| 62 | `llamagate` | LlamaGate | VISIBLE |
| 63 | `gitlawb` | Gitlawb Opengateway (MiMo) | VISIBLE |
| 64 | `gitlawb-gmi` | Gitlawb Opengateway (GMI Cloud) | VISIBLE |
| 65 | `nanogpt` | NanoGPT | VISIBLE |
| 66 | `nan` | NaN.Builders | VISIBLE |
| 67 | `aimlapi` | AI/ML API | VISIBLE |
| 68 | `novita` | Novita AI | VISIBLE |
| 69 | `piapi` | PiAPI | VISIBLE |
| 70 | `getgoapi` | GoAPI | VISIBLE |
| 71 | `laozhang` | LaoZhang AI | VISIBLE |
| 72 | `thebai` | TheB.AI | VISIBLE |
| 73 | `bai` | b.ai | VISIBLE |
| 74 | `fenayai` | FenayAI | VISIBLE |
| 75 | `empower` | Empower | VISIBLE |
| 76 | `poe` | Poe | VISIBLE |
| 77 | `chutes` | Chutes.ai | VISIBLE |
| 78 | `factory` | Factory | VISIBLE |
| 79 | `bluesminds` | BluesMinds | VISIBLE |
| 80 | `freemodel-dev` | FreeModel.dev | VISIBLE |
| 81 | `freeaiapikey` | FreeAIAPIKey | VISIBLE |
| 82 | `zenmux` | ZenMux | VISIBLE |
| 83 | `openadapter` | OpenAdapter | VISIBLE |
| 84 | `dit` | DIT.ai | VISIBLE |
| 85 | `tokenrouter` | TokenRouter | VISIBLE |
| 86 | `token-kiosk` | Token Kiosk | VISIBLE |
| 87 | `sumopod` | SumoPod | VISIBLE |
| 88 | `x5lab` | X5Lab | VISIBLE |
| 89 | `chenzk` | Chenzk API | VISIBLE |
| 90 | `kenari` | Kenari | VISIBLE |


## Stage 4 — DJMRN-FREE-API-SCAN-S04 (source rows 91–120)

**Trigger:** «مرحله 4» · **Entries:** 30 · **Status:** PUBLIC RESEARCH COMPLETED 2026-10-30 · [S04 30-provider findings](DJMRN-FREE-API-SCAN-S04-RESULTS-20261030.md) · [cumulative 52 positive provider IDs](DJMRN-FREE-API-POSITIVE-MASTER-252-20261030.md).

| Source row | Provider ID (exact) | Catalog name | UI status |
|---:|---|---|---|
| 91 | `tokenmarket` | Token Market | VISIBLE |
| 92 | `navy` | NavyAI | VISIBLE |
| 93 | `ainative` | AINative Studio | VISIBLE |
| 94 | `aion` | Aion Labs | VISIBLE |
| 95 | `routeway` | Routeway | VISIBLE |
| 96 | `nara` | NaraRouter | VISIBLE |
| 97 | `xkiro` | xKiro | VISIBLE |
| 98 | `regolo` | Regolo AI | VISIBLE |
| 99 | `naga-ac` | Naga.ac | VISIBLE |
| 100 | `void-ai` | Void AI | VISIBLE |
| 101 | `helixmind` | HelixMind | VISIBLE |
| 102 | `logfare` | Logfare | VISIBLE |
| 103 | `tabitoken` | TabiToken | VISIBLE |
| 104 | `seekai` | SeekAi | VISIBLE |
| 105 | `demonroute` | Demon Route | VISIBLE |
| 106 | `daoxe` | DaoXE | VISIBLE |
| 107 | `beatapi` | BeatAPI | VISIBLE |
| 108 | `openai` | OpenAI | VISIBLE |
| 109 | `reka` | Reka | VISIBLE |
| 110 | `pioneer` | Pioneer AI | VISIBLE |
| 111 | `uc-direct` | UC Direct (uncensored.com) | VISIBLE |
| 112 | `anthropic` | Anthropic | VISIBLE |
| 113 | `gemini` | Gemini (Google AI Studio) | VISIBLE |
| 114 | `groq` | Groq | VISIBLE |
| 115 | `blackbox` | Blackbox AI | VISIBLE |
| 116 | `xai` | xAI (Grok) | VISIBLE |
| 117 | `mistral` | Mistral | VISIBLE |
| 118 | `perplexity` | Perplexity | VISIBLE |
| 119 | `perplexity-agent` | Perplexity Agent | VISIBLE |
| 120 | `cohere` | Cohere | VISIBLE |


## Stage 5 — DJMRN-FREE-API-SCAN-S05 (source rows 121–150)

**Trigger:** «مرحله 5» · **Entries:** 30 · **Status:** READY / NOT RESEARCHED

| Source row | Provider ID (exact) | Catalog name | UI status |
|---:|---|---|---|
| 121 | `meta-llama` | Meta Llama API | VISIBLE |
| 122 | `morph` | Morph | VISIBLE |
| 123 | `galadriel` | Galadriel | VISIBLE |
| 124 | `ai21` | AI21 Labs | VISIBLE |
| 125 | `venice` | Venice.ai | VISIBLE |
| 126 | `codestral` | Codestral | VISIBLE |
| 127 | `upstage` | Upstage | VISIBLE |
| 128 | `maritalk` | Maritalk | VISIBLE |
| 129 | `nous-research` | Nous Research | VISIBLE |
| 130 | `arcee-ai` | Arcee AI | VISIBLE |
| 131 | `liquid` | Liquid AI | VISIBLE |
| 132 | `inception` | Inception | VISIBLE |
| 133 | `writer` | Writer | VISIBLE |
| 134 | `together` | Together AI | VISIBLE |
| 135 | `openvecta` | OpenVecta | VISIBLE |
| 136 | `openference-api` | Openference API | VISIBLE |
| 137 | `poolside` | Poolside | VISIBLE |
| 138 | `fireworks` | Fireworks AI | VISIBLE |
| 139 | `cerebras` | Cerebras | VISIBLE |
| 140 | `nvidia` | NVIDIA NIM | VISIBLE |
| 141 | `nebius` | Nebius AI | VISIBLE |
| 142 | `nube` | Nube.sh | VISIBLE |
| 143 | `siliconflow` | SiliconFlow | VISIBLE |
| 144 | `hyperbolic` | Hyperbolic | VISIBLE |
| 145 | `ollama-cloud` | Ollama Cloud | VISIBLE |
| 146 | `huggingface` | HuggingFace | VISIBLE |
| 147 | `deepinfra` | DeepInfra | VISIBLE |
| 148 | `lambda-ai` | Lambda AI | VISIBLE |
| 149 | `sambanova` | SambaNova | VISIBLE |
| 150 | `nscale` | nScale | VISIBLE |


## Stage 6 — DJMRN-FREE-API-SCAN-S06 (source rows 151–180)

**Trigger:** «مرحله 6» · **Entries:** 30 · **Status:** READY / NOT RESEARCHED

| Source row | Provider ID (exact) | Catalog name | UI status |
|---:|---|---|---|
| 151 | `baseten` | Baseten | VISIBLE |
| 152 | `publicai` | PublicAI | VISIBLE |
| 153 | `featherless-ai` | Featherless AI | VISIBLE |
| 154 | `friendliai` | FriendliAI | VISIBLE |
| 155 | `wandb` | Weights & Biases Inference | VISIBLE |
| 156 | `inference-net` | Inference.net | VISIBLE |
| 157 | `predibase` | Predibase | VISIBLE |
| 158 | `bytez` | Bytez | VISIBLE |
| 159 | `monsterapi` | MonsterAPI | VISIBLE |
| 160 | `modelscope` | ModelScope | VISIBLE |
| 161 | `byteplus` | BytePlus ModelArk | VISIBLE |
| 162 | `digitalocean` | DigitalOcean | VISIBLE |
| 163 | `azure-openai` | Azure OpenAI | VISIBLE |
| 164 | `azure-ai` | Azure AI Foundry | VISIBLE |
| 165 | `bedrock` | Amazon Bedrock | VISIBLE |
| 166 | `watsonx` | IBM watsonx.ai Gateway | VISIBLE |
| 167 | `oci` | OCI Generative AI | VISIBLE |
| 168 | `sap` | SAP Generative AI Hub | VISIBLE |
| 169 | `modal` | Modal | VISIBLE |
| 170 | `vertex` | Vertex AI | VISIBLE |
| 171 | `vertex-partner` | Vertex AI Partners | VISIBLE |
| 172 | `cloudflare-ai` | Cloudflare Workers AI | VISIBLE |
| 173 | `scaleway` | Scaleway AI | VISIBLE |
| 174 | `ovhcloud` | OVHcloud AI | VISIBLE |
| 175 | `heroku` | Heroku AI | VISIBLE |
| 176 | `databricks` | Databricks | VISIBLE |
| 177 | `datarobot` | DataRobot | VISIBLE |
| 178 | `clarifai` | Clarifai | VISIBLE |
| 179 | `snowflake` | Snowflake Cortex | VISIBLE |
| 180 | `qianfan` | Baidu Qianfan | VISIBLE |


## Stage 7 — DJMRN-FREE-API-SCAN-S07 (source rows 181–210)

**Trigger:** «مرحله 7» · **Entries:** 30 · **Status:** READY / NOT RESEARCHED

| Source row | Provider ID (exact) | Catalog name | UI status |
|---:|---|---|---|
| 181 | `glm` | GLM Coding | VISIBLE |
| 182 | `glm-cn` | GLM Coding (China) | VISIBLE |
| 183 | `bigmodel` | BigModel.cn (Zhipu) | VISIBLE |
| 184 | `glmt` | GLM Thinking | VISIBLE |
| 185 | `bailian-coding-plan` | Alibaba Token Plan | VISIBLE |
| 186 | `qwen-cloud` | Qwen Cloud | VISIBLE |
| 187 | `qwen-cloud-token-plan` | Qwen Cloud Token Plan | VISIBLE |
| 188 | `kimi` | Kimi (Legacy Moonshot API) | HIDDEN |
| 189 | `kimi-coding-apikey` | Kimi Code API Key | HIDDEN |
| 190 | `minimax` | Minimax Coding | VISIBLE |
| 191 | `minimax-cn` | Minimax (China) | VISIBLE |
| 192 | `deepseek` | DeepSeek | VISIBLE |
| 193 | `zai` | Z.AI | VISIBLE |
| 194 | `alibaba` | Alibaba Cloud Model Studio | VISIBLE |
| 195 | `alibaba-cn` | Alibaba (China) | HIDDEN |
| 196 | `longcat` | LongCat AI | VISIBLE |
| 197 | `moonshot` | Kimi | VISIBLE |
| 198 | `volcengine` | Volcengine | VISIBLE |
| 199 | `volcengine-agent-plan` | Volcengine Ark Agent Plan | VISIBLE |
| 200 | `volcengine-coding-plan` | Volcengine Ark Coding Plan | VISIBLE |
| 201 | `gigachat` | GigaChat (Sber) | VISIBLE |
| 202 | `xiaomi-mimo` | Xiaomi MiMo | VISIBLE |
| 203 | `xiaomi-mimo-token-plan` | Xiaomi MiMo Token Plan | VISIBLE |
| 204 | `baidu` | Baidu (ERNIE) | VISIBLE |
| 205 | `tencent` | Tencent Hunyuan | VISIBLE |
| 206 | `iflytek` | iFlytek Spark | VISIBLE |
| 207 | `baichuan` | Baichuan | VISIBLE |
| 208 | `yi` | Yi (01.AI) | VISIBLE |
| 209 | `stepfun` | StepFun | VISIBLE |
| 210 | `coze` | Coze | VISIBLE |


## Stage 8 — DJMRN-FREE-API-SCAN-S08 (source rows 211–240)

**Trigger:** «مرحله 8» · **Entries:** 30 · **Status:** READY / NOT RESEARCHED

| Source row | Provider ID (exact) | Catalog name | UI status |
|---:|---|---|---|
| 211 | `360ai` | 360 AI | VISIBLE |
| 212 | `doubao` | Doubao | VISIBLE |
| 213 | `sensenova` | SenseNova | VISIBLE |
| 214 | `sparkdesk` | SparkDesk | VISIBLE |
| 215 | `hcnsec` | Huancheng Public API | VISIBLE |
| 216 | `agnes` | Agnes AI | VISIBLE |
| 217 | `agnes-cn` | Agnes AI (China) | VISIBLE |
| 218 | `sealion` | SEA-LION | VISIBLE |
| 219 | `clova-studio` | Naver CLOVA Studio | VISIBLE |
| 220 | `internlm` | InternLM (Intern-S1) | VISIBLE |
| 221 | `ant-ling` | Ant Ling / Ring (inclusionAI) | VISIBLE |
| 222 | `sarvam` | Sarvam AI | VISIBLE |
| 223 | `plamo` | PLaMo | VISIBLE |
| 224 | `typhoon` | Typhoon | VISIBLE |
| 225 | `apmix` | Apmix | VISIBLE |
| 226 | `nlpcloud` | NLP Cloud | VISIBLE |
| 227 | `runwayml` | Runway | VISIBLE |
| 228 | `kie` | KIE.AI | VISIBLE |
| 229 | `pollinations` | Pollinations AI | VISIBLE |
| 230 | `haiper` | Haiper | VISIBLE |
| 231 | `leonardo` | Leonardo AI | VISIBLE |
| 232 | `ideogram` | Ideogram | VISIBLE |
| 233 | `magnific` | Magnific | VISIBLE |
| 234 | `udio` | Udio | VISIBLE |
| 235 | `v0-vercel` | v0 (Vercel) | VISIBLE |
| 236 | `gitlab` | GitLab Duo PAT | VISIBLE |
| 237 | `voyage-ai` | Voyage AI | VISIBLE |
| 238 | `jina-ai` | Jina AI (Foundation API) | VISIBLE |
| 239 | `typesafe` | TypeSafe AI | VISIBLE |
| 240 | `fal-ai` | Fal.ai | VISIBLE |


## Stage 9 — DJMRN-FREE-API-SCAN-S09 (source rows 241–252)

**Trigger:** «مرحله 9» · **Entries:** 12 · **Status:** READY / NOT RESEARCHED

| Source row | Provider ID (exact) | Catalog name | UI status |
|---:|---|---|---|
| 241 | `stability-ai` | Stability AI | VISIBLE |
| 242 | `black-forest-labs` | Black Forest Labs | VISIBLE |
| 243 | `recraft` | Recraft | VISIBLE |
| 244 | `topaz` | Topaz | VISIBLE |
| 245 | `segmind` | Segmind | VISIBLE |
| 246 | `dify` | Dify | VISIBLE |
| 247 | `nomic` | Nomic | VISIBLE |
| 248 | `mixedbread` | Mixedbread AI | VISIBLE |
| 249 | `jina-reader` | Jina Reader (r.jina.ai) | VISIBLE |
| 250 | `tinyfish` | TinyFish Fetch | VISIBLE |
| 251 | `deepai` | DeepAI | VISIBLE |
| 252 | `cursor-api` | Cursor API | VISIBLE |


## Integrity and future maintenance

- Source contains **252 unique ID rows**, with **249 visible and 3 hidden**; hidden ids are still research subjects and appear in Stage 7.
- Frozen stage mapping is 8 × 30 entries + 1 × 12 entries = **252**. No duplicates or missing IDs; master file created from actual tagged provider IDs, not manually retyped labels.
- An earlier 152-card user screenshot archive is a partial UI view and not a separate research stage.
- Preserve no-spend / free-first DJMRN policy and keep historical unrelated 375-provider deep audit separate.
