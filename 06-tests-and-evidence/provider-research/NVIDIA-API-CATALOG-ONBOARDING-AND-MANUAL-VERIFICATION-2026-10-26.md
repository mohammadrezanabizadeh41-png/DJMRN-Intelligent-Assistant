# NVIDIA API Catalog — DJMRN onboarding / verification dossier
**Date:** 2026-10-26  
**Provider queue order:** #6, after Google Gemini, GroqCloud, OpenRouter, Mistral AI and Cloudflare Workers AI.  
**Overall status:** `ACCOUNT_CREATED / DEVELOPER_PROGRAM_WELCOME_RECEIVED / CLOUD_ACCOUNT_CREATED / PHONE_VERIFICATION_BLOCKED / SUPPORT_REQUEST_SENT / API_KEY_NOT_CREATED / API_NOT_TESTED / OMNIROUTE_NOT_CONNECTED`  
**Classification:** USER-OBSERVED + GMAIL-SENT-VERIFIED + OFFICIAL-DOCS; account-specific quotas, billing and model access remain **UNKNOWN / UNVERIFIED**.  
**Scope:** User expressly requested a dedicated NVIDIA record alongside the existing provider-research dossiers. Never publish credentials, phone numbers, personal email, OTPs, or account identifiers.

## 1. Why this provider is in the queue
- NVIDIA API Catalog / build.nvidia.com is the sixth candidate in the project's existing [free-cloud provider queue](DJMRN-FREE-CLOUD-API-KEY-QUEUE-2026-10-26.md).
- Goal: evaluate the genuinely free NVIDIA-hosted NIM inference endpoints for development/prototyping, then (only if the account is eligible and an API call works) consider a private key and later a free-only OmniRoute integration.
- NVIDIA's official NIM FAQ and Run NIM Anywhere docs say NVIDIA Developer Program members have free access to hosted NIM API endpoints **for prototyping/development/research**; production use is a different licensing/entitlement question. Do **not** interpret free prototyping as an unrestricted ongoing commercial/production API.
- Actual account-specific models, credits, RPM/TPM, total API allowance, expiration/reset, billing/overage behavior, regional eligibility and commercial-use permission are **NOT YET VERIFIED**.

## 2. Chronological user onboarding evidence — 2026-10-26
1. Opened NVIDIA API Catalog: https://build.nvidia.com/explore/discover and proceeded with account/Developer Program registration.
2. The user displayed the final registration screen with optional **Recommendation Settings** and developer-news subscription preferences and a **Submit** action. The assistant recommended disabling optional personalization/news. **Whether those options were actually disabled is unverified.**
3. The user displayed **Create an NVIDIA Cloud Account → Provide a Cloud Account Name**. Suggested project identifier: `djmrn-omniroute` (fallback suggestion: `djmrn-ai-cloud`). **The name actually entered was NOT confirmed; do not state that either name was created.**
4. The connected mailbox received NVIDIA's **“Welcome to NVIDIA Cloud Account!”** and **“Welcome to the NVIDIA Developer Program”** messages on 2026-10-26. This establishes cloud-account and Developer Program welcome, but **NOT** phone verification or hosted model/API entitlement. Evidence: authenticated Gmail search in this ChatGPT session; no private mailbox content/links/IDs/verification codes copied into this public GitHub repository.
5. The user reported that NVIDIA required **telephone verification** to continue. They could not complete that step. **No successful phone verification** has been reported. Whether a particular country's number is supported was **NOT verified**.
6. **No NVIDIA API Key was created or supplied**, no model/API request was run, and NVIDIA was not added to OmniRoute. Account and Cloud Account creation must **not** be conflated with API availability.
7. The user explicitly requested that support be contacted for **manual account verification based on the registered email**, without discussing nationality or residence.

## 3. Verified support request
- **To:** `help@build.nvidia.com`
- **Subject:** `Request for Manual NVIDIA Account Verification and API Access`
- **Sent:** 2026-10-26 12:53:06 (timestamp returned by Gmail; offset not specified in connector response)
- **Evidence:** Authenticated Gmail `read_email` on the outgoing message returned label `SENT`, exact destination, subject and content. This proves Gmail accepted the sent action; **not** delivery to a human, ticket creation, manual verification or a support response.
- **Sanitized request summary:** The account holder created an NVIDIA and NVIDIA Cloud Account; the automated verification step could not be completed; support was asked to review the account manually by its registered email or advise an alternative email-based verification method. The actual outgoing message contained the registered email address, but it is **intentionally omitted from this public GitHub record**.
- **User-requested framing:** No nationality or residence details were included. No fabricated circumstances were stated.
- NVIDIA Developer Forum staff direct account-verification issues to the same support address. This is a support request, not a guaranteed manual-approval method.
- **Support response:** `PENDING / NOT VERIFIED`; **case/ticket number:** `UNKNOWN`. Do not invent a response, date, or follow-up.

## 4. Precise current gates
| Gate | Current status | Evidence / qualification |
| --- | --- | --- |
| NVIDIA identity account | CREATED, per user flow | Welcome correspondence; exact dashboard status not separately audited |
| NVIDIA Developer Program | WELCOME RECEIVED | Gmail welcome, **not** API entitlement |
| NVIDIA Cloud Account | CREATED, welcome received | Exact Cloud Account Name/ID private or unverified |
| Phone/SMS verification | BLOCKED / NOT COMPLETED | User's live registration experience |
| Alternative/manual verification | REQUEST SENT, PENDING | Gmail SENT verification 2026-10-26 |
| NVIDIA API Key | NOT CREATED / NOT AVAILABLE | No confirmed Generate API Key success |
| Current free account quota, credits and rate limits | UNKNOWN | Must inspect authorized NVIDIA account dashboard after verification |
| Payment method, paid status and overage guard | UNKNOWN / NOT AUDITED | No known payment action during this flow; **do not claim no card on file** |
| NVIDIA model catalogue and exact model IDs | RESEARCH PENDING | Catalogue display is not free/usable proof |
| Real API response | NOT TESTED | No key and no authenticated inference |
| OmniRoute 3.8.52 NVIDIA connection | NOT CONNECTED | User chose to finish provider account/key collection first |
| Production/commercial eligibility | NOT APPROVED / RESEARCH PENDING | Free developer access is for prototyping; production differs |

## 5. Next actions (not executed; manual stage gates)
1. Wait for a reply to the already sent email from NVIDIA support; if it arrives, assess exact verification instructions, scope, terms and any request for sensitive information. **Do not auto-send a follow-up or activate paid features.**
2. If support provides a legitimate verification path, the user can complete it and confirm access to **Generate API Key**. If not, maintain `PHONE_VERIFICATION_BLOCKED / PARKED` and proceed with the existing queue, #7 **Cohere**, without repeated signup attempts.
3. Once account verification succeeds, separately review: current plan; whether any card/payment method/paid trial is requested; exact zero-cost entitlement, quota units and limits; per-model catalogue access; rate limits; expiration/reset; acceptable development/prototyping use; contractual and regional eligibility. `UNKNOWN` means no assumed safe access/activation.
4. Only after the user agrees and free-only terms are verified, generate a dedicated private key (e.g., name `DJMRN-OmniRoute`, if the platform supports key names). Store the secret **privately**, never in GitHub, chat, logs or screenshot. Record only key creation status.
5. Later, run one low-volume, non-sensitive NVIDIA API inference request and capture sanitized model ID, HTTP status, error/usage and evidence. Successful account/signup **does not** imply a working API call.
6. Only after the user's overall provider-onboarding phase is complete, consider free-only NVIDIA→OmniRoute setup, test routing/fallback safely, then classify model capability and costs. No present router modifications.
7. Keep NVIDIA as **PENDING SUPPORT**, not **REJECTED** or **API CONNECTED**. Avoid assuming any alternative NVIDIA models available through other vendors inherit NVIDIA's free tier.

## 6. Official references checked on 2026-10-26
- NVIDIA Developer API Catalog: https://build.nvidia.com/explore/discover
- NVIDIA NIM FAQ: https://docs.api.nvidia.com/nim/docs/product
- NVIDIA API Catalog Quickstart: https://docs.api.nvidia.com/nim/re/docs/api-quickstart
- NVIDIA Run NIM Anywhere / prototype versus production terms: https://docs.api.nvidia.com/nim/docs/run-anywhere
- NVIDIA Developer Forum verification support instruction (staff, 2026-10-08): https://forums.developer.nvidia.com/t/manual-phone-verification-request-for-nvidia-build-api/385379/2
- Project provider queue: [DJMRN Free Cloud API Key Queue](DJMRN-FREE-CLOUD-API-KEY-QUEUE-2026-10-26.md)

**Provenance boundary:** User-provided page text and decisions; authenticated Gmail confirmation of account welcome and sent support message; vendor documentation. No automated login, phone attempt, NVIDIA API call, billing activation, key capture or OmniRoute edit was performed in preparing this dossier.
