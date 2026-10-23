# P2F — Synthetic-only admission boundary and restart ledger recovery

2026-10-23; scope: **fake models/providers and authenticated transport through real pinned Bifrost OCI**, never production API, account, Windows, payment or user documents.

## Purpose
P2C proved Bifrost native failover on mock providers; P2D proved source-level SQLite atomic quota guards; P2E passed individual metered requests to genuine Bifrost. P2F tests the missing *network boundary*: an untrusted caller on a **separate Docker --internal frontend bridge** must reach only a small quota-admitting adapter. The Bifrost gateway and fake A/B HTTP providers sit on a **different Docker --internal backend bridge**. Adapter is dual-homed and uses P2D ledger on runner-private ephemeral bind storage; no host port published.

Input is only a synthetic request_id + scenario; caller cannot select model/provider/tier/quota/fallback. Adapter authenticates an ephemeral synthetic client token, uses server-assigned trusted-only metadata, reserves P2D quota before each outbound HTTP request to Bifrost, and never forwards client credentials to Bifrost. All actual upstream credentials are ephemeral Bifrost test passwords and dummy provider tokens. Front probe independently tries to contact Bifrost and mock A/B directly and **must fail to resolve/reach them**, not merely get 401.

Test verifies paid/unknown price denial, unauthorized/malicious field rejection, A 429 -> B, A 503 -> B, partial stream stop, request IDs and full quota exhaustion. It removes and recreates the adapter container with **the same SQLite ledger mount but bootstrap disabled**, proving completed reservations do not reset. Corrupt/missing DB or marker => fail-closed at startup. 16 additional Python standard-library offline tests target safety and restart behavior.

Important: The test's "free" metadata, quota and reset day are entirely **fictional**. It tests completed-request container replacement, not a real Windows power outage or process death mid-SQLite commit. Docker network separation prevents unauthorized *front-only clients* reaching backend; it does NOT constrain a host admin, Docker daemon owner or a compromised dual-homed adapter. A single test token is NOT real authentication/identity management; the proxy is not a secure customer-facing product.

No real provider API, account credentials, payment, model quality/routing benchmarks, local Windows resource measurement or OS file access. Bifrost's **native fallback remains disabled in the metered P2E/P2F path**, because it could otherwise be invisible to P2D reservations; P2C proved native fallback separately. D-016 evaluation, D-005 broader host decision OPEN, G3B/M1 file guard CLOSED.

Run once via synthetic-only public standard Ubuntu GitHub Actions; verify exact run/job log before advancing. Never promote P2F pass into real API/billing/production proof.
