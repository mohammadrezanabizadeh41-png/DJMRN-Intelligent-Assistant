# ROUTER-P002C — Manual-only CI package for genuine Bifrost synthetic upstream experiment
**Created 2026-10-23; TYPE:** version-pinned future test harness; **STATUS:** `7/7 SOURCE/PREFLIGHT PASS` in isolated Linux/Python; **GITHUB ACTIONS NOT_RUN**, **MAXIM BIFROST NOT_RUN**, **WINDOWS NOT_RUN**, **REAL CLOUD PROVIDERS NOT_USED**. No paid provider, accounts, secret, local files, or CAP-006 tool access.

## Goal and identity
Try the *real* OSS Maxim Bifrost HTTP gateway selected conditionally under D-016 with two controlled, purely fake OpenAI-shaped upstreams, rather than confuse a Python policy mock or a direct fake-upstream request with true gateway Failover. This is the blocked P2B remediation, now named P2C manual CI gate.

- Pinned official `linux/amd64` manifest: `maximhq/bifrost@sha256:d53775fd4b1d444c350443d2487ceb8aa8c0bab722cd5dc7b0001a7fa88ecd7f` (official [Docker Hub v2.3.2-amd64](https://hub.docker.com/layers/maximhq/bifrost/v2.3.2-amd64/images/sha256-d53775fd4b1d444c350443d2487ceb8aa8c0bab722cd5dc7b0001a7fa88ecd7f); OCI manifest/source association is a metadata claim, not a runtime/signed binary attestation).
- Official source transport tag `transports/v2.3.2`, source commit `a05ea20e68bf116a35e9f05b1a3d749624b3935e`.
- Workflow [`.github/workflows/djmrn-p2c-manual.yml`](../../../.github/workflows/djmrn-p2c-manual.yml): **`workflow_dispatch` ONLY**, no push/PR/schedule, no trigger on creating the file. Official checkout action pinned Git SHA; GitHub token `contents: read` only; standard `ubuntu-latest`; **8-minute job timeout, no artifacts**. Source test does not consume Actions minutes until manually dispatched; GitHub billing remains separate from shell gating.

## Why NOT auto-run yet: user-owned financial permission
This is a **private** repository. GitHub-hosted Actions minutes are included only to plan quota; usage after quota can be billed to repository owner. Coordinator has **NOT** verified the account's remaining included minutes, billing setup, or zero-overage budget. The workflow is intentionally dormant. A boolean `billing_guard_confirmed` input is a human acknowledgment, **not** a technical guarantee the account actually has a $0 maximum. Verify free minutes AND enabled stop-spend policy via GitHub Billing/Budgets first; if not clearly guaranteed, **DO NOT RUN**. Do not turn on larger runners.

## What a future manually confirmed run does
1. Checkout only this private repo, run standard-library **preflight** tests and hard-stop if missing `DJMRN_APPROVED_FREE_ACTIONS_MINUTES=yes` or wrong platform.
2. Pull digest-pinned Bifrost and public Python 3.13 slim only in ephemeral standard GitHub runner. Verify Bifrost image OS/arch. Only image download stage has internet; **later synthetic containers run on a distinct `--internal` Docker bridge with no external egress**.
3. Start `djmrn-mock-a` and `djmrn-mock-b` on private network with **no host port publication**; Bifrost on same internal bridge; only its port published to **host 127.0.0.1:18080**, never public `0.0.0.0` host.
4. Pass fresh random **ephemeral** setup-token, admin password and Bifrost virtual key via process env; only `env.*` references appear in checked-in config. `config_store` and `logs_store` disabled; provider API key = fixed dummy text; provider endpoints = mock-a/mock-b only. Enable OSS inference VK auth, restrict exact fake model IDs, no wildcard model allowlist and no LLM/API provider secrets.
5. Require Bifrost readiness and negative auth/model probes **before** success tests. Actual client->Bifrost->upstream probes test normal synthetic 200, Bifrost-initiated 429 and 503 fallback to mock B and completed SSE. Partial stream is **diagnostic-only**: no claim of failover guarantee after output begins. Failed expectation exits nonzero. Cleanup containers/internal network even on error.
6. Output intentionally excludes prompts, passwords, provider key values, customer content or memory statistics. No API keys for external models. Integration verification requires inspecting the GitHub Actions run receipt afterward.

## Files and local preflight (DONE, distinct from gateway)
- `config.json` — OSS candidate fake provider config/virtual-key allowlist/auth. **Schema/runtime compatibility still needs actual Bifrost verification**.
- `mock_provider.py` — two fake networked services with 200, 429, 503, fake OpenAI JSON/SSE incl broken stream.
- `probe_gateway.py` — must talk ONLY to Bifrost localhost port; explicit `fallbacks` in request, not a test-client retry.
- `run_ci.sh` — binary digest, internal Docker network, ephemeral auth, 8-minute outer job guard and cleanup.
- `test_p2c_preflight.py` — **7 tests actually executed**, including source fields, manual-only workflow, deny-without-budget-flag (exit code 90), and live loopback fake A 429. **No Docker/Bifrost invoked in these tests**.
- [GitHub manual workflow](../../../.github/workflows/djmrn-p2c-manual.yml).

Isolated exact-source reproduction (Linux Python 3.13.5, no Docker needed):
```bash
cd 06-tests-and-evidence/pilots/ROUTER-P002C-20261023
python3 -W error::ResourceWarning -m unittest -v test_p2c_preflight.py
```
Observed: **7 tests, OK (0.516s)** with no warnings. **Every one of the six committed source blobs including workflow exactly matched the preflighted local files**; Git blobs and hashes in [test receipt](../../logs/ROUTER-P002C-MANUAL-GHA-READY-PREFLIGHT-20261023.md).

## Remaining gates and limits
- No account usage data => **manual dispatch MUST remain off**; shell-enforced env flag alone is NOT zero-billing proof.
- The real `maximhq/bifrost` OSS binary, config parsing, startup auth, routing, model alias, VK headers, streaming normalization, OCI pull and Docker internal host port behavior are still **NOT RUN** and can fail; a workflow failure is evidence, not license to bypass checks.
- CI Python base image is version-line pinned `python:3.13-slim`, **not immutable digest**, and actions `ubuntu-latest` can evolve. High-assurance CI later can pin all components.
- Docker internal bridge limits container outbound routes; no proof of perfect anti-egress in a compromised host. No claim of bill-free hosting, upstream free quota/resets, quality tier classification or Windows RAM.
- No GitHub Actions workflow logs/artifacts consumed or inspected; **actual run status NOT_RUN** as of 2026-10-23.
- When a run occurs, coordinator must read its run/job step logs, classify **actual Bifrost PASS/FAIL/BLOCKED** and separately register evidence. Do not upgrade D-016 to deployed until route and cost safety prove. **D-005 OPEN; G3B CLOSED**.
