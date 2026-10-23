# ROUTER-P002D — Free-Only Shared-Quota Admission, SYNTHETIC VERIFIED (2026-10-23)
**Status: TESTED-SYNTHETIC Python admission control, NOT integrated with Bifrost, NOT real-provider/free-quota validation, NOT installed on user's Windows.**
Repository `mohammadrezanabizadeh41-png/DJMRN-Intelligent-Assistant` branch `main`. User explicitly asked to continue after P2C, with real-account/provider action guarded separately.

## Evidence timeline, original failures preserved
- P2C independently achieved **real pinned Bifrost with two fake HTTP upstreams**: [GitHub run 39955366862](https://github.com/mohammadrezanabizadeh41-png/DJMRN-Intelligent-Assistant/actions/runs/39955366862) PASS. P2D is a different conceptual *pre-router* admission and does not inherit operational approval.
- Exact testable Python 3 standard-library source [admission.py](../pilots/ROUTER-P002D-20261023/admission.py) and [test_admission.py](../pilots/ROUTER-P002D-20261023/test_admission.py) committed under `06-tests-and-evidence/pilots/ROUTER-P002D-20261023/` in [commit 89fd01c](https://github.com/mohammadrezanabizadeh41-png/DJMRN-Intelligent-Assistant/commit/89fd01c711fce6a9598b3efccf0da96fdf4f4338). Off-device Linux/Python standard-library 25/25 PASS, later [GitHub Actions run 39958750766](https://github.com/mohammadrezanabizadeh41-png/DJMRN-Intelligent-Assistant/actions/runs/39958750766) SUCCESS with 25/25 PASS.
- Security enhancement [commit 72b553b](https://github.com/mohammadrezanabizadeh41-png/DJMRN-Intelligent-Assistant/commit/72b553b849ee676a1b258b000188fe9d1bc13340) changed `Request.trusted` default to `False`, test request explicitly marked trusted, added default-untrusted denial case. **GitHub Actions [run 39958980545](https://github.com/mohammadrezanabizadeh41-png/DJMRN-Intelligent-Assistant/actions/runs/39958980545) COMPLETED SUCCESS**, job `120431861081`, independently read job log: **26 tests, OK (0.117 seconds)**, ResourceWarning strict. Workflow is path-filtered, standard public `ubuntu-latest`, pinned checkout action SHA, 5min cap, contents:read. No external model/API calls, installed dependencies, API keys or secrets. No paid cloud inference.
- Per-request user-provided fields/UTC day and `confirmed_free_api` metadata are **synthetic attestations only**. Real implementation must derive identity, source of price/cost/entitlement and date from trusted provider/account and policy logic; defaults alone do not establish upstream free-only safety.

## Coverage (verified code/unit tests)
- Rejects unknown/positive price, unknown daily limit, unverified free provider, enabled billing, untrusted/sensitive requests, paid fallback, unsupported capability, too-small context, quality downgrade.
- `lite / standard / reasoning` tier admission and protected reasoning slots; strict provider/account group quotas with SQLite `BEGIN IMMEDIATE`; 24 concurrent synthetic requests with only three slots resulted in 3 admitted, remaining denied.
- Conflict checks for account-group daily limit and reserves, duplicate request ID/attempted history, max two attempts, explicit UTC day; conservative reservations are consumed on errors.
- 429/503 (and bounded transient 5xx) marked eligible to test another **permitted free** route; 401/402/403 stop; partial SSE stop rather than replay. **No actual Bifrost integration in P2D**.

## Fresh official provider candidates, RESEARCH ONLY, no credentials or eligibility verified
| Candidate | Public documented free program | Gate / unknown |
|---|---|---|
| Groq | [Model-specific free plan limits](https://console.groq.com/docs/rate-limits), `openai/gpt-oss-120b` among documented models | Exact account RPM/RPD/TPM unknown; Free vs Developer billing separate |
| Gemini API | [Free tier](https://ai.google.dev/gemini-api/docs/pricing) and [per-project/model limits](https://ai.google.dev/gemini-api/docs/rate-limits) | Model eligibility, real account limits, project billing status and privacy unknown |
| OpenRouter | [Free 50 RPD, 20 RPM](https://openrouter.ai/pricing) and free-model catalog | Some models free, not all; data/use/model whitelist require actual checking; no paid fallback |
| Cloudflare Workers AI | [Free 10,000 daily Neurons](https://developers.cloudflare.com/workers-ai/platform/pricing/) with Free cap; specific paid-only models | Per-model neuron conversion/adapter and account status unknown |
| Cerebras | [Free API tier](https://inference-docs.cerebras.ai/support/pricing) | Fresh user account/model-specific limit not yet established |
| Hugging Face Providers | [Free monthly $0.10 credit](https://huggingface.co/docs/inference-providers/pricing) subject to change | Credit allowance, not generally free forever per-model; pay-as-you-go path must remain disabled |

**Iran geography excluded from TECHNICAL RANKING per user's prior directive; real account's use rights and provider legal terms still must be obeyed and must be verified separately.**

## NOT PROVEN and next gates
No real account, key, monetary hard-zero guarantee, current live quota inspection, auto-reset headers, minute/token counters, model capability benchmark, async/adversarial SQLite interprocess stress, Bifrost-side admission integration, backpressure/load, crash durability contract, per-account disabled billing enforcement or user Windows installation. **D-016 remains technical evaluation, D-005 undecided, G3B/M1 access guard closed.**
Next proposed: independently validate an existing provider's account-level genuine free quota and disabled paid/overage, get explicit separate authorization for a **single minimal real request**, then route via pinned Bifrost only after a short side-by-side safety gate. No API actions auto authorized.
