# Groq — Organization Limits screenshot snapshot
Date captured: 2026-10-26
Evidence: Two user-provided screenshots of Groq Console → Organization → Limits, account scope Personal / Default Project.
**These are displayed rate limits, not observed successful model calls or guarantees of free pricing.**

The console says **No project limits set** and **Show Current Project Limits** is off; shown values are organization base limits. The page references Developer plan as offering higher limits; account billing plan is NOT verified by these screenshots.

## Chat Completions
| Exact displayed model ID | Requests/min (RPM) | Requests/day (RPD) | Tokens/min (TPM) | Tokens/day (TPD) |
|---|---:|---:|---:|---:|
| `allam-2-7b` | 30 | 7,000 | 6,000 | 500,000 |
| `meta-llama/llama-prompt-guard-2-22m` | 30 | 14,400 | 15,000 | 500,000 |
| `meta-llama/llama-prompt-guard-2-86m` | 30 | 14,400 | 15,000 | 500,000 |
| `openai/gpt-oss-120b` | 30 | 1,000 | 8,000 | 200,000 |
| `openai/gpt-oss-20b` | 30 | 1,000 | 8,000 | 200,000 |
| `openai/gpt-oss-safeguard-20b` | 3 | 1,000 | 2,000 | 200,000 |
| `qwen/qwen3.8-27b` | 30 | 1,000 | 8,000 | 200,000 |

## Speech to Text
| Exact displayed model ID | Requests/min | Requests/day | Audio seconds/hour | Audio seconds/day |
|---|---:|---:|---:|---:|
| `whisper-large-v3` | 20 | 2,000 | 7,200 | 28,800 |
| `whisper-large-v3-turbo` | 20 | 2,000 | 7,200 | 28,800 |

## Text to Speech
| Exact displayed model ID | Requests/min | Requests/day | Tokens/min | Tokens/day |
|---|---:|---:|---:|---:|
| `canopylabs/orpheus-arabic-saudi` | 10 | 100 | 1,200 | 3,600 |
| `canopylabs/orpheus-v1-english` | 10 | 100 | 1,200 | 3,600 |

## Notes for DJMRN
- Groq API key: user reports created and saved locally; never store actual secret in repository.
- No project-specific caps were set at time of screenshot; values above are **organization-level**. Quotas may be shared across requests/keys and subject to additional restrictions.
- Visible list comprises **7 chat, 2 speech-to-text, 2 text-to-speech = 11 model rows**.
- Model IDs are transcribed from screenshots. The unusual ID `qwen/qwen3.8-27b` is copied literally; do not silently normalize it. Verify live API model catalog before routing.
- User has not yet provided the Models list, billing page, or a test response; model availability, prices, free-plan status, context length, tool calling and reliability remain UNVERIFIED.
- Future: confirm plan is free, validate IDs with API, integrate into OmniRoute, test request, then choose per-task routing and failover based on evidence.
