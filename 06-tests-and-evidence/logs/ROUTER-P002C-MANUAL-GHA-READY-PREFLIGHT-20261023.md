# ROUTER-P002C — exact-source preflight successful, manual GitHub Actions integration NOT RUN
**Date:** 2026-10-23 | **Evidence:** isolated assistant Linux local `unittest`, code static audit, one synthetic localhost HTTP request. **7/7 PASS; real Bifrost NOT_RUN; GitHub Actions NOT_RUN (zero runs observed); real providers NOT_RUN; Windows NOT_RUN.**
**Original user instruction:** "ادامه بده" after P2B failed because vendor download/Docker unavailable and new OCI-pinned route was documented. Following project's D-003 no-unknown-overage rule, coordinator did NOT start a GitHub-hosted runner because private repo remaining minutes and zero-overage policy could not be independently checked.

## Source and reproducible evidence
Canonical `mohammadrezanabizadeh41-png/DJMRN-Intelligent-Assistant` repo ID 1427268660, branch `main`; starting HEAD before this turn `6eb0da0b23bd0252b142970d8d405d3482446c37`. User rules/current, TASK-0027, prior P2B 8/8 fixture, pinned OCI evidence and official GitHub release read first.

Local test executed on isolated assistant Linux (not user Windows), Python **3.13.5**, no `pip`, no cloud model API, no OCI image, no Docker/Podman, no tokens or customer files. Test command in a staging directory mirroring exact GitHub `.github/workflows` and `06-tests-and-evidence/pilots` paths:
`python -W error::ResourceWarning -m unittest -v test_p2c_preflight.py`.
**Terminal:** `Ran 7 tests in 0.516s\n\nOK`, no errors/skips/warnings. `bash -n run_ci.sh` and `python -m py_compile mock_provider.py probe_gateway.py` plus JSON syntax validation passed. These are **source/static/synthetic localhost** results, not Docker/Bifrost startup. All six committed file Git blobs were independently re-fetched from canonical `main` and matched Git blobs calculated from the *exact tested local bytes*:

| File | Exact Git blob, locally git-hash-object verified | Evidence scope |
|---|---|---|
| `.github/workflows/djmrn-p2c-manual.yml` | `b33b677f16b6a792a3ab902c91a20aef97b4b6bc` | only workflow_dispatch; approval gate; 8min job; checkout pinned |
| `config.json` | `4bd68b6f1798cb7dea63f0d0bf5d143fe79e3bf1` | fake providers only; auth config and restricted model IDs |
| `mock_provider.py` | `d082766c3b9fc06ea5367a30960d2f2553effe89` | localhost scripted fake 429 and JSON/SSE; container-private behavior not run |
| `probe_gateway.py` | `886c458b405ca6f93ad8072add494bb23b63653e` | test source speaks to gateway localhost; actual gateway not run |
| `run_ci.sh` | `8ec53a9f247aa54d66b230acfa7007b344f1a59e` | refused missing free-minute flag in isolated shell; rest only source |
| `test_p2c_preflight.py` | `44a7076cdceb065eac6de45056014d97d2dc8d94` | 7 unit methods actually executed with identical bytes |

## Explicit 7-case receipt
| ID | What was actually tested | Result |
|---|---|---|
| C01 | `config.json` has only two synthetic custom providers; no real API URL or model | PASS |
| C02 | source configuration demands inference VK + admin auth, explicit finite model allowlist, env-ref secrets | PASS (configuration source, not enforced Bifrost runtime) |
| C03 | real workflow file has ONLY workflow_dispatch, no push/schedule, max 8-minute job and human billing acknowledgment field | PASS (YAML textual preflight, not full GitHub workflow parse/CI) |
| C04 | Bash contains internal Docker network, digest pin, host-loopback publish and cap-drop | PASS static only |
| C05 | Running Bash with no `DJMRN_APPROVED_FREE_ACTIONS_MINUTES` returns exit **90** before attempting Docker | PASS |
| C06 | One actual **loopback HTTP socket** sent to standalone fake mock provider A receives scripted **429**; /health returns 200 | PASS; NOT Bifrost |
| C07 | Gateway probe source points to Bifrost localhost endpoint, contains explicit missing-auth and automatic-fallback probes; does not call mock A/B directly | PASS static only |

## Network / artifact retest
- Checked assistant execution container: Linux x86_64, Go/Node/Python present, **no Docker or Podman**; DNS `downloads.getmaxim.ai` remains unresolved with curl 6. Vendor binary via sanctioned download failed its verified-page gate. No bytes downloaded or runtime executed here.
- Independent official Docker Hub manifest metadata used for pinned OCI `maximhq/bifrost@sha256:d53775fd4b1d444c350443d2487ceb8aa8c0bab722cd5dc7b0001a7fa88ecd7f`, https://hub.docker.com/r/maximhq/bifrost/tags, official source release https://github.com/maximhq/bifrost/releases/tag/transports%2Fv2.3.2 . **OCI digest identity externally documented, not pulled**.
- Discovered an opt-in **GitHub Actions** testing runner option. Official GitHub docs specify **private repo hosted Actions can incur billed usage beyond included minutes**: https://docs.github.com/en/billing/concepts/product-billing/github-actions . Cannot know account-specific remaining free minutes or budget; **no automatic trigger, no running workflow**. GitHub `actions/runs` endpoint actually checked after workflow registration and returned `total_count:0`.
- Workflow file is registered in repo but dormant. Note a human-set boolean is **not** an external budget enforcement guarantee: verify actual billing limit and stop-usage before dispatching. No user/remote-system execution authorized merely by source registration.

## Status and follow-up
**P2A:** Python policy mock 16/16 PASS only. **P2B:** two fake HTTP servers 8/8 PASS only, actual Bifrost BLOCKED. **P2C:** new self-contained manual-only true Bifrost CI package, preflight **7/7 PASS**, **actual CI NOT_RUN**, **actual Bifrost NOT_RUN**. No promotion to production/Windows. NEXT after verifying GitHub private Actions remaining free minutes and $0-overage stop policy: manually dispatch one short action, then inspect live logs for Bifrost auth/fallback/stream outcomes; if overage cannot be categorically blocked, do not dispatch, use verified unbilled isolated runner/binary path. **D-016 evaluation only, D-005 OPEN, G3B/CAP-006 CLOSED.**
