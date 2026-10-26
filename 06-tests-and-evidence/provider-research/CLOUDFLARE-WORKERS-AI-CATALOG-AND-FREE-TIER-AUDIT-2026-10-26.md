# Cloudflare Workers AI catalog / free tier — 2026-10-26

## Scope and evidence
User created a separate Cloudflare account and opened AI → Workers AI and AI → Models. Screenshot shows **263 models** in unified catalog; this is NOT 263 free Workers AI models. Screenshots include Cloudflare-hosted and Third-party badges. Full authenticated catalog has **not yet been exported**, so no claim of exhaustive 263-row classification.

Official sources:
- Unified catalog: https://developers.cloudflare.com/ai/models/
- Workers AI catalog: https://developers.cloudflare.com/workers-ai/models/
- Pricing: https://developers.cloudflare.com/workers-ai/platform/pricing/
- Rate limits: https://developers.cloudflare.com/workers-ai/platform/limits/
- Model discovery API: https://developers.cloudflare.com/api/resources/ai/subresources/models/methods/list/
- Paid requirement announcement: https://developers.cloudflare.com/changelog/post/2026-07-28-models-require-workers-paid/

## Free policy (confirmed public docs)
- Workers Free: **10,000 Neurons/day** shared across eligible models; resets 00:00 UTC; no paid overage on Free, further usage fails.
- Some high-compute Workers AI models require Workers Paid or prepaid AI Gateway credits regardless of remaining daily Neurons.
- Paid-required explicit list in current pricing docs: `@cf/moonshotai/kimi-k2.6`, `@cf/moonshotai/kimi-k2.7-code`, `@cf/zai-org/glm-5.2`, `@cf/zai-org/glm-5.3`, `@cf/zai-org/glm-5.3-flash`, `@cf/deepseek-ai/deepseek-v4-flash-0731`, `@cf/deepseek-ai/deepseek-v4-pro-0813`.
- Official July changelog explicitly cites as still available on Free: `@cf/zai-org/glm-4.7-flash`, `@cf/google/gemma-4-26b-a4b-it`, `@cf/nvidia/nemotron-3-120b-a12b` (subject to model availability and current terms).
- Rate limits per task differ from daily Neurons; default text generation 300 RPM for non-paid-required models. Model-specific prices in official pricing table; do not assign one flat requests/day cap per model.

## Screenshot examples — provisional classification
- Cloudflare-hosted shown: `clairic`, `clef`, `clef-flash`, `clef-omni`, `apertus-v1.5-8b`, `eurollm-9b-it`, `phonellm-mini-alpha-2`, `deepseek-v4.1-flash-1017`. Cloudflare-hosted **does not guarantee** free eligibility; some paid-only.
- Third-party shown: `gpt-6-astra`, `gpt-6-sol`, `gpt-6-luna`, `gpt-6.1-sol`, `claude-opus-5.5`, `claude-sonnet-5.5`, `claude-haiku-5.5`, `gemini-4-argon`, `gemini-3.8-flash`, `grok-4.7`, `m3.1-flash`, `muse-spark-1.3`, `nano-banana-2.1`, `gpt-image-2.5-sunburst`, `gpt-image-2.5-flare`, `h3`, `h3-max`, `krea-3`, `flux-3-image-klein`, `fibo-edit-1.5`, `fibo-generate-1.5`, `remove-background`, `v-rmbg-3.0`, `ad-delayer`, `starlight-precise-2-6`, `starlight-fast-2`. These should NOT be marked free without separate billing confirmation.

## Exhaustive export plan (not yet executed)
1. Use authenticated `GET /accounts/{account_id}/ai/models/search` with `Workers AI Read` scoped token, paginate all pages, preserve raw JSON and retrieval date. Never store token.
2. Reconcile 263 unified-catalog rows with `@cf/` Workers AI catalog and pricing; preserve distinctions: free-confirmed, paid-required, third-party billed, unknown/unverified.
3. Extract each model's identifier, provider, task, hosting, capability, context, pricing units, neuron conversion, per-task RPM, terms, and evidence URL. Use `UNKNOWN` for missing values.
4. Compare account billing and usage dashboard and run tiny test calls only after explicit user approval; log responses and neuron deltas.
5. Do not infer that screenshot catalog count or rate-limit ceiling guarantees account access.

## Usage navigation issue
User screenshots of AI → Workers AI show onboarding cards and model links, **not a visible Usage widget**. Do not claim they missed it. Explore account-level Workers & Pages analytics, dashboard navigation, or direct Workers AI analytics link from official pricing docs. No measured account consumption yet.

## Governance
Free-first, no Workers Paid activation, no payment card, no paid Unified Billing or prepaid credit without user approval. No secret values in repo.
