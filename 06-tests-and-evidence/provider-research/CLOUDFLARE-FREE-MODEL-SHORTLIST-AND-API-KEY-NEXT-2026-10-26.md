# Cloudflare Workers AI: verified free shortlist and token setup (2026-10-26)

**Status:** PUBLIC DOCUMENTATION VERIFIED; account-specific API access UNTESTED; API TOKEN NOT YET CREATED. The user's authenticated catalog showed 263 models; public https://developers.cloudflare.com/ai/models/ currently shows 262. These are not all free.

## Verified free-plan examples
Cloudflare official 2026-07-28 changelog https://developers.cloudflare.com/changelog/post/2026-07-28-models-require-workers-paid/ explicitly identifies:
- `@cf/zai-org/glm-4.7-flash` — candidate reasoning/coding/general
- `@cf/google/gemma-4-26b-a4b-it` — candidate general/multilingual
- `@cf/nvidia/nemotron-3-120b-a12b` — candidate advanced reasoning
These are publicly documented Free-compatible examples, **not** evidence of successful account-specific calls.

## Paid-required exclusions (official pricing updated 2026-10-20)
https://developers.cloudflare.com/workers-ai/platform/pricing/
- `@cf/moonshotai/kimi-k2.6`
- `@cf/moonshotai/kimi-k2.7-code`
- `@cf/zai-org/glm-5.2`
- `@cf/zai-org/glm-5.3`
- `@cf/zai-org/glm-5.3-flash`
- `@cf/deepseek-ai/deepseek-v4-flash-0731`
- `@cf/deepseek-ai/deepseek-v4.1-flash-1017`
- `@cf/deepseek-ai/deepseek-v4-pro-0813`
Require Workers Paid or prepaid AI Gateway credits; never silently route these under free-only policy.

## Budget
Workers Free: 10,000 Neurons/day shared, resets 00:00 UTC. Different models consume Neurons at different rates. Public pricing includes per-model input/output neuron conversion, and the Free plan has no paid overage. Never equate model catalog visibility with free eligibility.

## Remaining research
- Obtain the full public model list with fields (model ID, provider, hosted/third-party, task, capabilities) and reconcile against Workers AI model catalog/pricing.
- Full 262/263-row verified per-model classification **NOT YET COMPLETE**; no claim otherwise.
- Third-party models are not assumed to consume the Workers AI Free allocation. Separate third-party billing status UNKNOWN until verified.
- Account usage and access remain UNVERIFIED.

## Next user action — create token
On Cloudflare dashboard → AI → Workers AI → top right `REST API` → `Create a Workers AI API Token` → review permissions → `Create API Token`; securely save token privately, NEVER send to chat or commit. Copy Account ID separately. Official instructions: https://developers.cloudflare.com/workers-ai/get-started/rest-api/ . After key creation, verify API with a tiny request to one Free-compatible model and inspect response/status; no paid plan activation.

## Governance
No billing activation, no paid credits, no secret storage in GitHub, and no unapproved deployment. Free-first routing.
