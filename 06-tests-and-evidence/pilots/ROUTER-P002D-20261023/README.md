# ROUTER-P002D — Shared Free-Only Admission / Synthetic Quota Ledger

2026-10-23. **EVALUATION ONLY, TESTED-SYNTHETIC**, NOT a Bifrost plugin/production admission service, no provider account, network, key, billing or Windows access. Source matches an independent Linux standard-library Python 3.13.5 synthetic test (25/25 initial; live GitHub 26/26 after fail-closed hardening).

Design source: [DJMRN P0 policy contract](../../../03-architecture-and-tools/DJMRN-CLOUD-ROUTER-P0-REQUEST-POLICY-CONTRACT-20261023.md). Bifrost real gateway with fake providers already passed [P2C](../../logs/ROUTER-P002C-REAL-BIFROST-SYNTHETIC-GATEWAY-PASS-20261023.md); **P2D is a separate pre-router policy proof and has not been connected to Bifrost**.

- All accounts/models in tests are **fictional**. No external paid or free-provider API calls.
- Admission requires attested free API, zero unit price, billing disabled, exact capability/context/tier, known positive daily limit; otherwise deny. These are **self-declared synthetic fields**, not proof of a real provider free entitlement.
- SQLite uses shared account quota grouping and `BEGIN IMMEDIATE` for atomic reservations. Any attempted request conservatively consumes a slot, including 429/5xx. Two-attempt hard bound and identical request-id history guard. A protected reasoning reserve cannot be consumed by low-tier requests.
- The `utc_day` and request trust flag are **test inputs**. In deployment, an authenticated request gateway must derive trusted identity, time and provider spend/quota data; untrusted input must not set these values.
- Partial streaming never falls back silently, 401/402/403 stop; 429/5xx permit **only a subsequent eligible free route**. No promise of auto recovery or free quotas on external services.
- No real enforcement of minute/token quotas, retention/pruning of the SQLite ledger, restart integration, external rate-limit headers, proof of price, capacity benchmark or long-term reliability. The test's 24 threads prove only one SQLite process/thread scenario, not multi-machine distributed coordination.
- No model ranking performance empirical benchmark yet. Model tiers are synthetic classification values, NOT real provider model ratings.
- Run: `python3 -W error::ResourceWarning -m unittest -v test_admission.py`. Python standard library only.
- Native P2C Bifrost gateway and this conceptual pre-router have not been integrated; D-016 evaluation preference and D-005 undecided remain unchanged.

**Latest live GitHub Actions verification:** [run 39958980545](https://github.com/mohammadrezanabizadeh41-png/DJMRN-Intelligent-Assistant/actions/runs/39958980545) completed SUCCESS, 26/26 tests including default `trusted=False`; original [25/25 run](https://github.com/mohammadrezanabizadeh41-png/DJMRN-Intelligent-Assistant/actions/runs/39958750766) also SUCCESS. Full evidence: [P2D source/test receipt](../../logs/ROUTER-P002D-FREE-QUOTA-ADMISSION-TESTED-SYNTHETIC-20261023.md).

## Current public API candidates (RESEARCH ONLY; not approved/activated)
- [Groq rate limits](https://console.groq.com/docs/rate-limits): organizational/account model-specific quotas; actual limits must be read from the account.
- [Gemini pricing](https://ai.google.dev/gemini-api/docs/pricing), [rate limits](https://ai.google.dev/gemini-api/docs/rate-limits): free models vary by model/project, data-use privacy considerations; no paid tier.
- [OpenRouter free plan](https://openrouter.ai/pricing): 50 requests/day, 20/min default free tier; avoid selecting non-free model or any auto-topup path.
- [Cloudflare Workers AI](https://developers.cloudflare.com/workers-ai/platform/pricing/): daily neurons on Free and hard failure at Free limit; model-dependent units and paid-only models.
- [Cerebras pricing](https://inference-docs.cerebras.ai/support/pricing): free tier, model-dependent rate limits; current exact account quota unknown.
- [Hugging Face Inference Providers](https://huggingface.co/docs/inference-providers/pricing): monthly free-credit *allowance*, not necessarily evergreen free inference; requires credit/billing guard.

No account on any of these has been examined or connected. **Country is not a technical ranking filter**, but permission under provider terms/account eligibility must be confirmed before a real call.
