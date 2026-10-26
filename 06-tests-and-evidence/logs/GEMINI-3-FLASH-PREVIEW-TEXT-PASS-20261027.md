# Gemini 3 Flash Preview: successful text smoke test

Date: 2026-10-27
Provider route: gemini/gemini-3-flash-preview
Gateway: http://127.0.0.1:20128/v1/chat/completions

Actual user-run Windows PowerShell result:

- IMAGE_ATTACHED=False
- HTTP_STATUS=200
- SECONDS=2.11
- RESPONSE=READY.
- TEXT_TEST=PASS
- max_tokens=128; stream=false.

Conclusion: This model completed one text request successfully through OmniRoute. Image was not tested. No settings or model registry changes in this test. Free-only billing, stability, Combo and Agno eligibility still require separate verification.

Across eight reviewed models: five prior text-plus-image smoke passes; model six Gemini 3.8 Flash has one older text pass but later timeouts, so deferred for instability; model seven Gemini 2.5 Flash-Lite received 404 restricted-to-existing-users; model eight Gemini 3 Flash Preview now has text-only PASS.

Next possible historical coverage: Gemini 2.5 Flash, which Google documents as restricted for new users/projects. Test one short text request only if continuing; no image test and no automatic retry. Specialist models need their relevant non-chat endpoints.
