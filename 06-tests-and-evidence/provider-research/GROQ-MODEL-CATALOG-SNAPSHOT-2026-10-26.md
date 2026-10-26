# GroqCloud Model Catalog — screenshot evidence
Captured 2026-10-26 from four user screenshots of Groq Supported Models documentation. **Documentation catalog, not account-specific availability or Free pricing.** Separate actual organization Free limits: `GROQ-ORGANIZATION-LIMITS-SNAPSHOT-2026-10-26.md`. Billing Free plan: `GROQ-BILLING-FREE-PLAN-SNAPSHOT-2026-10-26.md`.

## Production models (visible)
| Model ID (verbatim) | Speed tok/s | Developer price | Developer limit | Context | Max completion | Max file | Access note |
|---|---:|---|---|---:|---:|---|---|
| `llama-3.1-8b-instant` | 560 | Contact Sales | Contact Sales | 131,072 | 131,072 | — | Enterprise label |
| `llama-3.3-70b-versatile` | 280 | Contact Sales | Contact Sales | 131,072 | 32,768 | — | Enterprise label |
| `openai/gpt-oss-120b` | 500 | $0.15/M input; $0.60/M output | 250K TPM, 1K RPM | 131,072 | 65,536 | — | In account Limits screenshot |
| `openai/gpt-oss-20b` | 1000 | $0.075/M input; $0.30/M output | 250K TPM, 1K RPM | 131,072 | 65,536 | — | In account Limits screenshot |
| `whisper-large-v3` | — | $0.111 per hour | 200K ASH, 300 RPM | — | — | 100 MB | Speech to text |
| `whisper-large-v3-turbo` | — | $0.04 per hour | 400K ASH, 400 RPM | — | — | 100 MB | Speech to text |

## Additional supported models visible
| Model ID (verbatim) | Speed tok/s | Developer price | Developer limit | Context | Max completion | Max file | Note |
|---|---:|---|---|---:|---:|---|---|
| `canopylabs/orpheus-arabic-saudi` | — | $40 per 1M characters | 50K TPM, 250 RPM | 4,000 | 50,000 | — | TTS |
| `canopylabs/orpheus-v1-english` | — | $22 per 1M characters | 50K TPM, 250 RPM | 4,000 | 50,000 | — | TTS |
| `meta-llama/llama-prompt-guard-2-22m` | — | $0.03/M input; $0.03/M output | 30K TPM, 100 RPM | 512 | 512 | — | Prompt guard |
| `meta-llama/llama-prompt-guard-2-86m` | — | $0.04/M input; $0.04/M output | 30K TPM, 100 RPM | 512 | 512 | — | Prompt guard |
| `meta-models/muse-spark-open` | 350 | Contact Sales | Contact Sales | 131,072 | 131,072 | — | Enterprise label |
| `minimaxai/minimax-m2.7` | 260 | Contact Sales | Contact Sales | 196,608 | 131,072 | — | Enterprise label |
| `openai/gpt-oss-safeguard-20b` | 1000 | $0.075/M input; $0.30/M output | 150K TPM, 1K RPM | 131,072 | 65,536 | — | Safety |
| `qwen/qwen3.8-27b` | 450 | $0.80/M input; $4.00/M output | 250K TPM, 1K RPM | 131,072 | 16,384 | 20 MB | ID copied literally; verify live API |

## Featured model detail
- GPT-OSS 120B featured as an open-weight 120B model; documentation describes built-in browser search, code execution and reasoning capabilities; text-in/text-out and ~500 tps. These claims are documentation-level and do **not** establish that hosted Groq endpoint exposes browser/code tools for this account. Verify via API.

## Live catalog endpoint shown in screenshot
- Groq docs describe GET `https://api.groq.com/openai/v1/models` with bearer token in `Authorization`, yielding active model IDs. The secret must remain local; do not put it in GitHub/chat. Actual API call not performed here.

## Critical distinctions
- The **Developer plan** price and limits in docs are not the user's **Free plan** quota. Never use 1K RPM or 250K TPM as free-tier quota. Refer to the account-specific Limits snapshot (e.g., GPT-OSS 120B 30 RPM, 1K RPD, 8K TPM, 200K TPD).
- Enterprise/contact-sales models are **not confirmed accessible** to the Free account.
- Published catalog may include models not in the user's organization limits. Account access and model IDs require authenticated live catalog/test.
- Documentation has a 'Deprecated Models' section but screenshot does not show its model entries.
- No payment or upgrade approved.

## Proposed task routing (hypotheses, not benchmark results)
- Fast lightweight chat: GPT-OSS 20B candidate; benchmark before promotion.
- Complex reasoning/coding: GPT-OSS 120B candidate; Qwen 27B candidate; benchmark Persian, coding, structured tool use.
- Speech recognition: Whisper V3/Turbo.
- TTS: Orpheus English/Arabic; Persian not confirmed.
- Prompt safety: Prompt Guard 22M/86M, Safeguard 20B, separate from primary general assistants.

## Next steps
1. Optional local authenticated GET /models to establish live access; no key disclosure.
2. Test models via OmniRoute and log statuses, latency, errors, capability results.
3. Complete other providers' onboarding; then build shared pool, routing/failover and cost/usage policy.
