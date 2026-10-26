# Mistral Free Subscription and Organization Limits — screenshot snapshot

Date: 2026-10-26. Source: six user screenshots, Mistral Studio Admin → Subscription, Limits and document settings.

## Subscription screenshot
- Current Plan **Free**.
- Included monthly API/Studio allowance: **$10**, progress shown $0, resets in 6 days (monthly on first calendar day).
- Included monthly Vibe Code allowance: **$10**, progress shown $0, resets in 6 days; separate allowance, NOT pooled $20 API credits.
- API pay-as-you-go section shows **Enable** button and says free API tier can be used within limits even without PAYG enabled. Do not enable without user approval.
- Billing screenshot separately shows €0.00 purchased credits, no payment method and auto recharge disabled. Free included monthly allowance is distinct from purchased balance.

## Organization Limits: region Global, per-model
Visible figures below are **rate ceilings**, not free usage entitlement or guaranteed model availability. A dash means not specified, not unlimited.

| Model ID | Tokens/minute | Requests/second |
|---|---:|---:|
| `codestral-2508` | 625,000 | 2.08 |
| `codestral-embed` | 50,000 | 1.00 |
| `glm-5-2` | — | 1.00 |
| `labs-leanstral-1-5-1` | 5,000,000 | 0.63 |
| `ministral-14b-2512` | 937,500 | 0.50 |
| `ministral-3b-2512` | 1,300,000 | 12.50 |
| `ministral-8b-2512` | 625,000 | 3.13 |
| `mistral-embed-2312` | 20,000,000 | 1.00 |
| `mistral-large-2512` | 250,000 | 1.00 |
| `mistral-large-4` | 20,000 | 0.83 |
| `mistral-medium-latest` | 20,000 | 1.00 |
| `mistral-moderation-2603` | 50,000 | 1.67 |
| `mistral-small-2603` | 20,000 | 1.00 |
| `voxtral-mini-2602` | 50,000 | 1.00 |
| `voxtral-mini-transcribe-3` | 50,000 | 1.00 |
| `voxtral-mini-transcribe-realtime-2602` | 50,000 | 1.00 |
| `voxtral-mini-transcribe-realtime-3` | 50,000 | 1.00 |
| `voxtral-mini-tts-2603` | 50,000 | 1.00 |
| `voxtral-mini-tts-3-0` | 50,000 | 1.00 |
| `voxtral-small-2507` | 50,000 | 1.00 |
| `voxtral-small-transcribe-3` | 50,000 | 1.00 |
| `zai-glm-5-3` | 20,000 | 1.00 |
| `zai-glm-5-3-flash` | 6,666 | 1.00 |

## Additional observed limits
- Audio seconds per minute: **3,600**.
- Audio seconds per month: **—** (unspecified).
- Document OCR pages per minute: **625**.
- Documents maximum file size current effective limit: **100 MB**; UI slider up to **250 MB**, not changed.
- Disable file downloads toggle shown **off** (document downloads allowed).

## Pending
- Confirm what exact API endpoints/models are eligible for the included $10 monthly allowance, and whether any excluded service can bill separately.
- Confirm monthly quota usage and API availability via a zero-cost or allowance-contained test, no pay-as-you-go.
- Inspect remaining settings and privacy per user's request; no setting changes authorized.
- Map 23 visible model IDs to DJMRN role capabilities; validate model availability through authenticated model listing.
- Do not commit API secrets, account PII, or make payments.
