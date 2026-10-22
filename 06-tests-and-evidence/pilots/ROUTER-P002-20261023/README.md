# DJMRN P2 — OFF-DEVICE SIMULATED ROUTER POLICY (NOT BIFROST)
This local Python-only test prototype demonstrates free-only tier routing, shared quotas, cooldown and failover *in an explicitly fake backend*. It uses neither the Bifrost binary nor any HTTP requests, provider keys, private files, Windows APIs, or agent tools. It is not intended for deployment or as a security authorization system.

**Run synthetic-only:** `python -m unittest -v test_p2.py`

The tests implement the fourteen R-01..R-14 contract examples plus two extra edge cases. SQLite quota ledger uses `BEGIN IMMEDIATE` before reserve/settle, but the prototype is not an audited production-grade accounting system. Fixed error response strings and mock timestamps demonstrate policies, not provider behavior. No authenticated Bifrost headers or real streaming are exercised.

**Next:** integration test against pinned genuine OSS Bifrost `transports/v2.3.2` and two synthetic HTTP upstreams, with preconfigured localhost auth; future Windows tests require separate approval. This standalone mock must not be reported as successful Bifrost integration or Windows deployment.
