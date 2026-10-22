# DJMRN Cloud-First P0 — Request, Model Tier, Eligibility, Quota and Failover Contract (v0.1)
**Date:** 2026-10-23 | **Status: DOCUMENTED SPECIFICATION; NOT AN IMPLEMENTED API OR USER-APPROVED RUNTIME** | **Scope:** one common cloud inference service for independent Persian chat/coding/research clients using the selected gated-evaluation `maximhq/bifrost` gateway (D-016).
**Sources:** [project Cloud-First roadmap](CLOUD-FIRST-MINIMUM-VIABLE-PATH-20261023.md), [KB-0020](../08-project-knowledge-base/models-engines-and-hosts/KB-0020-capability-tiered-model-routing-and-free-quota-preservation.md), [KB-0021](../08-project-knowledge-base/tools-and-integrations/KB-0021-ai-coding-clients-free-hosted-models-vs-reusable-apis-20261023.md), [Bifrost P1 independent preflight](BIFROST-OSS-WINDOWS-P1-SOURCE-PREFLIGHT-20261023.md). Source-verified official Bifrost CEL routing rules, virtual keys and request fallbacks are documented at the bottom. **None of the invented DJMRN fields below are claimed native Bifrost API properties.**

## 1 — Minimal deployment roles / boundary
CLIENT (Jan candidate, Persian chat, VS Code coding client only when separately authorized) -> **DJMRN task-admission policy** (conceptual thin deterministic preprocessor, may collapse into native Bifrost CEL if tests permit) -> authenticated, loopback **Maxim Bifrost gateway** -> specifically approved free API provider/model. **Independent** local CAP-006/file executor receives only explicitly authorized tool actions under existing guard; cloud model text/replies can NEVER change Windows privilege scope.

For a simple client: one OpenAI-compatible `/v1/chat/completions` URL, with an **explicit preapproved logical model alias mapped/pinned on the DJMRN side**, not a promise arbitrary proposed aliases work in a vanilla unconfigured Bifrost build. Enforce deny by default for providers, credentials, models and tool actions.

## 2 — Canonical policy/envelope fields (DJMRN internal **PROPOSAL**, NOT READY-MADE Bifrost REST)
Policy metadata MUST be trusted from the DJMRN caller identity or explicit human preferences, not accepted blindly from LLM-generated text, arbitrary untrusted HTTP headers or user-supplied pasted text:
```json
{
  "contract_version": "0.1-draft",
  "request_id": "synthetic-uuid",
  "client_id": "approved-persian-chat",
  "task_class": "standard",
  "task_source": "client-explicit",
  "min_capabilities": ["persian", "chat"],
  "context_tokens_estimate": 512,
  "needs_tools": false,
  "needs_vision": false,
  "privacy_class": "normal",
  "free_only": true,
  "allow_paid_fallback": false,
  "allow_tier_downgrade": false,
  "max_upstream_attempts": 2,
  "streaming": false,
  "tool_execution_approval": "none"
}
```
The specimen is **not a functional request to Bifrost or a credential**. The thin policy component maps accepted fields to official Bifrost-supported model/provider/routing rule/virtual key mechanisms only *after exact-version tests*. Unknown `contract_version/client_id/task_class/capabilities/price/provider` => **reject**, do not route. Unknown complexity => explicitly select safer adequate tier or ask user; never assume `lite` grants capabilities. Do not transmit private local document contents outside without discrete approval and disclosure.

### Task tiers vs capability filters
| DJMRN lane | Minimum work class | Candidate capability gates | Reserve/fallback rule |
|---|---|---|---|
| `lite` | classify/transform one brief text, simple Persian chat | language/task benchmark pass, context adequate, optional JSON | choose measured free quick route; no automatic consumption of protected reasoning reserve |
| `standard` | summaries, translation, routine code and document reasoning | full context, adequate coding/Persian quality, required JSON/tool schema | fallback to equal or better tested capability without protected high-tier reserve leakage |
| `reasoning` | multi-file code, hard debugging, synthesis and multi-step architecture | empirically stronger reasoning/coding, context and tooling | protected scarce daily allowance; when exhausted, equal-tier fallback or `FREE_POOL_EXHAUSTED`; **never silently downgrade** |
| `specialist` | vision, audio, embeddings, structured tool plans | exact modality/API, tool schema support and privacy fit | independent capability pools; label is ORTHOGONAL to reasoning tier, not a fifth intelligence rank |

Model B-parameter count or marketing name is **not** sufficient quality evidence. Store task-specific benchmark and tested API behavior, `observed_at`, `evidence_url` and recheck expiry.

## 3 — Provider/model registry requirements
Provider credential *account* and model identifiers are separate objects. Each approved route carries: `provider_id`, `model_id`, `api_endpoint`, adapter/status, supported methods, `context_limit`, `tools_supported`, `json_supported`, `modalities`, measured Persian/coding tier, shared account/quota group, official recurring-free eligibility and provider terms, price and overage flags, RPM/RPD/token limits when known, window/reset timezone and `Retry-After`, confidence/source + check date, credential reference (**never actual API secret in GitHub**), privacy class, usage observations and hold/circuit state. Billing/price **UNKNOWN -> DENY**. `trial` and `$0 subscription UI model` != renewable free third-party API.

**No approved active providers as of creation.** Kilo AI Gateway `kilo-auto/free` and OpenCode Zen free HTTP are *candidate discoveries*, not tested/connected. An Antigravity account's in-product free Claude quota must NOT be transplanted to this API (terms).

## 4 — Admission, shared quota and reserve semantics
1. Authenticate caller + map to a permitted policy/virtual key; owner of permissions remains local DJMRN. Rate budgets attach to **upstream provider/account quota group across ALL client apps**, not one free counter per VS Code and Jan (would double-spend).
2. Filter: `enabled && vetted_free_API && price==0 && not_paid_fallback && health` AND required capabilities/context/privacy AND suitable tier. Exclude held/retry-after models until justified recheck. Do not use wildcard `allowed_models:["*"]` for production free-only.
3. Protect high-tier reserve: for a *measurable* true quota `Q`, policy-protected `R` is configurable, initially a **future policy parameter, not a chosen percentage**. Noncritical requests may use at most `Q-R`; reasoning requests may use all permitted remaining. If `Q` or usage is unknown, **do not claim available protected reserve**.
4. Use an **atomic shared reservation / settle / release** or equivalent provider-enforced capacity evidence to prevent simultaneous requests double-spending the last free calls. Native Bifrost dollar budgets/rate limits have been source-documented but **provider daily allowance accounting and reserve semantics have NOT been proven**. If no native solution satisfies this, evaluate the smallest *pre-router admission ledger* or **replace** Bifrost (not add a second gateway by habit), after scoped comparison/approval.
5. Retry/fallback: route to FIRST compatible free, allowed, same-tier route; bounded request-wide attempts/time. `429` may mean RPM/TPM/RPD: parse only supported returned policy headers; do not infer daily reset merely from generic 429. `401/403` may be authorization, not a temporary quota. `402` signals stop/billing, no paid fallback and no workaround key farms. `5xx/network` retry bounded; `400/422` schema incompatible => do not blindly replay.
6. Tool outputs, streaming partials and authenticated action side effects must be idempotency-aware. **Never replay a Windows/financial/email side effect due to model fallback**. Streaming failure after first output can only terminate cleanly; no guaranteed seamless cross-model continuation.
7. No capable/eligible provider => machine-readable `FREE_POOL_EXHAUSTED` / `NO_COMPATIBLE_FREE_MODEL` plus Persian user-facing explanation, NOT a chargeable route or unbounded queue.

## 5 — Native vs DJMRN extensions
- **Source-verified Bifrost Dev documentation:** `/v1/chat/completions`; virtual keys, provider/model allowlists and rate limits; weighted routing; explicit `fallbacks` request array; CEL routing rules with `headers`, `model`, `budget_used`, `complexity_tier`; `extra_fields.routing_info` indicates fallback serving route. These require correct scoped identity, safe headers and testing on pinned exact OSS binary.
- **IMPORTANT DISCOVERY:** Bifrost **already has a Beta Complexity Router**, not previously assumed in the project. It emits only `SIMPLE/MEDIUM/COMPLEX` via `complexity_tier`; its decision classifier does an **additional model call** or semantic mode does an **embedding call**. Defaults use Typesafe Jev, NOT presumed free. `specialist` is **DJMRN capability filter**, not native `complexity_tier`; if classifier times out no tier is emitted and CEL routing normal path continues (needs strict default deny). No free-cost or Persian benchmark established. Prefer deterministic trusted task class and Bifrost native CEL; use beta complexity router only if approved/baseline quality/cost gates pass.
- **DJMRN-only requirements not yet demonstrated by Bifrost:** auto-truthful dynamic per-account free grants and reset, atomic reservation across simultaneous apps, high-tier reserve, zero-overage provider guarantee, task quality threshold, authorized local file/tool bridge, secure Persian interface, honest error contract. **Do not equate** server-side `budget_used` with remaining provider free-API request count.

## 6 — P2 MOCK acceptance suite (design only, no test results)
| ID | Fixture/action | PASS observation |
|---|---|---|
| R-01 | lite requested; healthy lite+reserved advanced | answer lite; protected advanced unchanged |
| R-02 | standard 429 minute window, compatible free standard B healthy | B selected within bounded calls; A held only for justified time |
| R-03 | reasoning A daily budget exhausted, B equally qualified | B serves; **no downgrade to lite** |
| R-04 | reasoning tier all free routes exhausted | `FREE_POOL_EXHAUSTED`, no paid/trial route attempted |
| R-05 | provider 401, 403, 402, expired free promotion | no credential abuse/paid route, explicit classified error |
| R-06 | lite requests from two apps simultaneously with only one shared slot | at most one admitted; stable account counter after restart |
| R-07 | tool-call needed but models text-only | `NO_COMPATIBLE_FREE_MODEL`; no tool authorization upgrade |
| R-08 | stream emits partial token then 503 | controlled stream error, no unmarked successful completion |
| R-09 | untrusted client header claims `reasoning` or changes `client_id` | identity policy enforced; cannot bypass reserve or paid deny |
| R-10 | classifier unavailable/timeout | deterministic fallback only if vetted, else fail closed |
| R-11 | gateway restarts / fake quota window reset | persistent reservations not lost; no fabricated provider reset |
| R-12 | different models both share one upstream free account | total shared usage never exceeds account allowance |
| R-13 | actual serving provider/model differs from primary after fallback | log reason/route metadata only, no prompt/secret logging |
| R-14 | cloud unavailable, local CAP-006 protected | no unauthorized local file read or power action; human approval still required |

**Definition of DONE P0:** this document includes the request policy, aliases, denied states, feature/permission separation and 14 acceptance cases. Implementation/version-specific fields and invariants remain to be proven at P2. No executable code/client/provider test.

## Sources explicitly inspected 2026-10-23
- https://github.com/maximhq/bifrost/blob/dev/docs/providers/routing-rules.mdx
- https://github.com/maximhq/bifrost/blob/dev/docs/features/complexity-router.mdx
- https://github.com/maximhq/bifrost/blob/dev/docs/features/governance/routing.mdx
- https://github.com/maximhq/bifrost/blob/dev/docs/features/governance/virtual-keys.mdx
- https://github.com/maximhq/bifrost/blob/dev/docs/features/retries-and-fallbacks.mdx
**Version caveat:** these sources are dev docs at pinned snapshot `24f6c3eadb99573684edb298196dff3be03b3077`; not automatically evidence all features ship in earlier chosen binary.
