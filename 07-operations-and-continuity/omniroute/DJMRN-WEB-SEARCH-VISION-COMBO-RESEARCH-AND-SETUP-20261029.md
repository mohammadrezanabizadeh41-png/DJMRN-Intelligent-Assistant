# DJMRN Web Search / Visual Website Analysis — OmniRoute Combo Research and Setup
Date: 2026-10-29
Status: RESEARCHED_AND_PROPOSED — NOT YET CREATED IN USER'S OMNIROUTE
Source: user-confirmed six-model inventory; 2026-10-27 local Gateway receipts; Google official model descriptions/pricing retrieved 2026-10-29.

## User's intended workflow
Maintain existing `DJMRN-PM-Standard` Combo and create a separate model family for browser-based website search and opportunity extraction. Reuse the same already-connected Gemini account/models: **do not move/delete the six models from existing PM Combo**, do not register new API keys, do not install local model weights. Browser automation (Ui.Vision/Chrome/DOM extraction) fetches pages; LLM analyzes extracted text or screenshots. A model connected to OmniRoute does NOT by itself control the browser or browse websites.

## Evidence and candidate comparison
| Model route | User-observed OmniRoute smoke evidence | Official capability and proposed role | Web-vision admission |
|---|---|---|---|
| `gemini/gemini-3.6-flash` | text 200 / 3.07s; inline JPEG 200 / 9.35s | stronger complex page interpretation, structured extraction and agent loops; multimodal Gemini 3 | ADMIT as provisional first route |
| `gemini/gemini-3.5-flash-lite` | text 200 / 1.11s; inline JPEG 200 / 6.41s | high-volume routine screening, text+image extraction | ADMIT as second route |
| `gemini/gemini-3.1-flash-lite` | text 200 / 11.95s; inline JPEG 200 / 8.38s | lightweight backup for simple extraction | ADMIT as third route |
| `gemini/gemma-4-26b-a4b-it` | text and inline JPEG PASS per established sequential receipts | fast MoE Gemma with visual UI/ocr support; candidate fallback | ADMIT as fourth route |
| `gemini/gemma-4-31b-it` | gateway text 200 / 35.93s; image 200 / 7.53s | stronger Gemma 4 complex image/document reasoning, but slow text observed | ADMIT as fifth route |
| `gemini/gemini-3-flash-preview` | text 200 / 2.11s ONLY; IMAGE_ATTACHED=False | official Google model supports image, function calling, structured outputs, search grounding | HOLD OUT of vision Combo until one limited screenshot/inline JPEG gateway test passes; retain in PM-Standard |

This is a reasoned **provisional order**, not a benchmark: CAT/OTHER photo recognition does not establish website-screen reading/coordinate accuracy. An actual sample of a job-listing screenshot, mixed languages, field extraction, error recovery and latency comparison is required for selecting the primary model.

## Proposed dedicated Combo in OmniRoute
- **Name:** `DJMRN-Web-Vision`
- **Description:** `Visual website and freelance listing analysis for DJMRN Opportunity Hunter. Chrome/Ui.Vision provides DOM text and screenshots; models extract structured fields and interpret complex page layouts. Use existing Gemini routes; no autonomous browsing or paid Search grounding assumed.`
- **Source UI path:** `OmniProxy -> Combos -> Create Combo` (documented in screenshot-derived menu inventory).
- **Strategy:** `PRIORITY` if supported, **not** parallel/chaos; order 3.6 Flash, 3.5 Flash-Lite, 3.1 Flash-Lite, Gemma 4 26B A4B, Gemma 4 31B.
- **Account:** user-existing `DJMRN-OmniRoute-Gemini` when selecting each step; no secrets needed in notes.
- **Status:** DO NOT MARK CREATED until new UI screenshot or direct combo metadata confirms creation. DO NOT MARK GATEWAY-VERIFIED until a bounded real request via the Combo returns correct structured extraction.
- **Security:** Do not send passwords, private personal data, authenticated page secrets, or sensitive tokens in screenshots or LLM requests; redact when needed.
- **Fallback/compatibility:** Verify Combo handles `image_url` payload and that failover retains image content. Treat provider-level Gemini shared account quotas as a common failure domain: five steps are NOT five separate provider quotas. Allow no speculative automatic switch into paid model tier.
- **Model sixth:** `gemini/gemini-3-flash-preview` has official image support but only local text smoke evidence; add to this Combo later only on an actual user-supplied image test PASS.
- **Do not include:** deferred `gemini/gemini-3.8-flash` (known instability), embedding models, TTS, Robotics, or Google 2.5 Flash models restricted for new project.

## Important distinction — Web Search vs Vision
- A text or image LLM is **not a search engine**. Browser/Ui.Vision/DOM or an authorized search API must retrieve the website content first; Gemini processes text/screenshots and emits structured data.
- Google official model docs list Google Search grounding, URL context, and function calling for several Gemini models; **this does not establish that OmniRoute's OpenAI-compatible Chat Completions route exposes those tools**, nor that the user's free API account has access.
- As of 2026-10-29 Google's official pricing tables list Google Search grounding as **not available in Free Tier** for the selected Gemini Standard routes (may be testable in AI Studio); avoid designing the free automation around paid Google Search grounding or inferring that a '5000 free' monthly paid-tier allowance applies to the user's free tier.
- Site-specific browser automation must be separately permission-reviewed; use DOM-first extraction and screenshot Vision only when necessary.

## Suggested acceptance test after UI Combo creation
1. Confirm exact member IDs, order, account and Priority in the OmniRoute UI; do not modify `DJMRN-PM-Standard`.
2. One request to the new Combo at `POST http://127.0.0.1:20128/v1/chat/completions` using a sanitized static screenshot (e.g. mocked job listing) and prompt for JSON `{title, budget, deadline, language, site, missing_fields}` with explicit `null` for unknowns.
3. Validate returned fields against screenshot/DOM, capture latency, output shape, exact model used, HTTP status, billing/quota usage, error class, and whether non-ASCII text is preserved.
4. Test forced fallback only if needed, safely and with budget/quotas guarded; do not assume multiple models on one provider protect against provider outage.
5. Log a separate screenshot/test receipt to GitHub; no API keys or private job-page data.

## Official sources (read 2026-10-29)
- https://ai.google.dev/gemini-api/docs/models/gemini-3.6-flash
- https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash-lite
- https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite
- https://ai.google.dev/gemini-api/docs/models/gemini-3-flash-preview
- https://ai.google.dev/gemma/docs/core/model_card_4
- https://ai.google.dev/gemini-api/docs/pricing
- https://ai.google.dev/gemini-api/docs/tools
- Prior user execution receipts: `06-tests-and-evidence/logs/GEMINI-3.6-FLASH-GATEWAY-VERIFIED-20261027.md`, `GEMINI-3.5-FLASH-LITE-GATEWAY-VERIFIED-20261027.md`, `GEMINI-3.1-FLASH-LITE-GATEWAY-VERIFIED-20261027.md`, `GEMMA4-31B-GATEWAY-VERIFIED-20261027.md`, `GEMINI-3-FLASH-PREVIEW-TEXT-PASS-20261027.md`.
- Current two-Combo screenshot receipt: `07-operations-and-continuity/omniroute/DJMRN-OMNIROUTE-TWO-COMBOS-UI-CONFIRMED-20261029.md`.

No live inference, OmniRoute group creation or model setting change was performed in this documentation-only research step.
