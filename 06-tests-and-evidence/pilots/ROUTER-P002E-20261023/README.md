# ROUTER-P002E: admitted request -> real pinned Bifrost -> fake HTTP providers

2026-10-23. **TEST EXPERIMENT** (not installed Windows middleware, not provider accounts). P2C was actual Bifrost with unmetered synthetic fallback; P2D was SQLite quota admitted with a mocked transport. P2E tests **both** with a private Docker network and pinned OSS Bifrost image, while keeping all model IDs and upstreams fake.

Design issue: if Bifrost makes multiple automatic upstream attempts invisibly, a pre-router that reserves only the first account cannot safely implement a strict zero-overage shared quota. For this P2E integration test, the pre-router explicitly does **not send** a Bifrost \`fallbacks\` array, uses each fake provider with \`max_retries: 0\` and one key, reserves once per outgoing HTTP attempt, classifies error, and atomically reserves a different vetted fake route before retry. Bifrost remains the **real OpenAI-compatible transport** for every attempt, but the P2E *pre-router*, not Bifrost, makes retry decisions. The native Bifrost fallback 429/503 was already demonstrated by P2C and remains separate proof. This tradeoff needs a further review before a product integration.

Safety: only \`djmrn-fake-a/b\` with model \`fixture-*\`; internal Docker bridge \`--internal\`, no host published ports, dummy token and ephemeral auth values, only public pinned OCI and vendor JSON assets, source-only admission, no real provider APIs, no secrets or Windows. The registered price/free/quota metadata is entirely **fictional** and does not establish entitlement to any cloud model.

Run: Python standard-library P2E 15 unit tests; then \`DJMRN_P2E_SYNTHETIC_INTEGRATION=yes\` adds the integration probe to the existing P2C CI runner. GitHub one-shot workflow triggers only when designated sentry file changes and matching commit message is used. Public standard \`ubuntu-latest\` uses GitHub's no-cost runner tier. No always-on service or schedule.

Gates: If the gateway or admission tests fail, do not silently promote; keep D-016 evaluation only, D-005 undecided, G3B/M1 closed. Real API / billing / account availability / Windows/localhost permissions still NOT APPROVED.
