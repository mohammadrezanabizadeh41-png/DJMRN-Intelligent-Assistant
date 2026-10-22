# DJMRN G3-B — opt-in synthetic runner built and tested off-device

**Date:** 2026-10-22 | **Status:** `SOURCE-READY / 27 ISOLATED MOCK-AND-HARNESS TESTS PASS / WINDOWS DEVICE NOT_RUN / G3 HOLD`.
**Authority:** private `mohammadrezanabizadeh41-png/DJMRN-Intelligent-Assistant`, `main`. This is an off-device test-development receipt, **not** permission to run on the user's laptop.

## Trusted starting point / permitted scope

- The user asked to continue after the coordinator explicitly proposed building a limited G3-B runner off-device. **No authorization for any new Windows device run was given.**
- Live Notion Operating Memory and Tool Governance fetched; GitHub `main@4e5c1e8afd4e22644e6407e058c54f1cf5346e83` checked. PROJECT-RULES, canonical CURRENT, the exact original `windows_reader.py`, `manifest.py`, `windows_guard.py`, G3 reader harness, G3B fault tests, and [previous G3B Windows plan](../protocols/G3B-WINDOWS-SYNTHETIC-NEGATIVE-PLAN-20261022.md) inspected. Microsoft official `CreateFileW` sharing rules and `CancelSynchronousIo` cancellation limitations reviewed.
- Reused current Python stdlib + original G3 fixture/enrollment/handle tracker, not a new provider, framework, agent, DB, service or installer.

## Newly committed exact source

| File | Git blob | Verification |
|---|---|---|
| [`g3b_synthetic_probe.py`](../../05-assistants-and-capabilities/src/m1_pilot/g3b_synthetic_probe.py) | `3dea7874048c4f03ee7709b7bb3204f75cf65015` | commit `0296f72c9ae150e690501ef03c06ec37ca0b3c78`; local source and commit-ref readback matched exactly, 12,495 bytes |
| [`tests/test_g3b_probe_offdevice.py`](../../05-assistants-and-capabilities/src/m1_pilot/tests/test_g3b_probe_offdevice.py) | `38306f65b4a1b98199eb7409058c200c6a9c4d88` | commit `941f471338cd05adefbbd47083610368844138c0`; local test and commit-ref readback matched exactly, 4,219 bytes |

Previous original source blobs confirmed in isolated test: reader `730f35208dd7f3f08cec3260b4fe7ef775d2faa2`, manifest `f505b0d3c65a8a421684e3055bc3be12ce19a9a7`, existing G3B fault test `9677d74aa557da55daf8d2b685ca54da267be573`.

## Actually executed / reproducible off-device evidence

- Host: assistant-owned Linux, Python **3.13.5**, no Windows or user machine access.
- Isolated staging: `/mnt/data/djmrn_g3b_exact_20261022` containing the exact canonical reader/manifest, original 12 fault-injection tests, plus the new runner and 15 runner checks; package marker only.
- Ran `python -m py_compile` on the new runner: **PASS**.
- Ran `PYTHONDONTWRITEBYTECODE=1 python -B -m unittest discover -s tests -p 'test_*.py' -v`: **27/27 PASS, 0 FAIL, 0 SKIP (0.009 s)**. The **12 original** cases call the exact canonical reader with a fake Win32 kernel; the **15 new** cases check plan-only default, non-Windows refusal, source-pin tamper denial, pre/during-read *test-only* delivery revoke, no-network Python audit decisions, two-file cleanup, symlink-safe cleanup and static source limits. No real Win32 API calls were performed.
- Invoked `python -B g3b_synthetic_probe.py` on Linux: returned `G3-B PLAN ONLY / DEVICE NOT RUN / GUARD CLOSED / NO USER APPROVAL ASSUMED`.
- Invoked `python -B g3b_synthetic_probe.py --run-synthetic` on Linux: deliberately returned `FAIL_HOLD/WINDOWS_ONLY` and exit code 2. This is an **expected refusal**, not failed Windows testing.

## Proposed later Windows behavior — UNTESTED

The new runner defaults to PLAN ONLY. Even with `--run-synthetic` it requires typing literal `RUN` locally, and refuses wrong source blobs or non-Windows. Its bounded code would create exactly two fictitious `.md` files in its own newly created NTFS temp folder, enroll identities from handles, read same-handle snapshots, attempt `os.replace(alpha, beta)` **only on these two fixtures while held**, check expected sharing/access-denied codes, exercise **test-only** pre-read and post-read delivery denial, verify the existing M1 guard is closed, account for intercepted Win32 handles, then remove only its owned fixtures without recursive deletion. No admin, Junction creation, installation or account/model/Jan use.

**What it CANNOT prove even after a future device run:**
- No real junction/reparse object is created; `G3B-02` explicitly `NOT_RUN`.
- A blocked single replacement attempt is **not** an adversarial concurrent rename race; `G3B-04` explicitly `NOT_RUN`.
- DeliveryFence is **test-local**, not an implemented production authorization/revocation system. `G3B-05` stays `PARTIAL`; after-return data handling and real user permission still require separate design.
- `CancelSynchronousIo` and physical I/O interruption are **not executed** (`G3B-06 NOT_RUN`).
- `sys.addaudithook` guards selected Python audit events, **not native/DLL network operations or an external egress monitor** (`G3B-08 PARTIAL`).
- Source pins cover the original G3 runner and three core files; **they do not independently attest to the new G3B executable or launcher itself**. Windows batch/runtime behavior is unverified. Tracked handles are not proof of OS-wide leak freedom.
- Stop and manually review on any unexpected rename success, source identity mismatch, failure, suspicious filesystem change or unsafe cleanup. Never elevate privileges, expand the fixture scope or auto-run another test.

**No production code modified:** `core/windows_reader.py`, `core/manifest.py`, `core/session.py`, `core/windows_guard.py`, CAP and Jan unchanged. `require_verified_read()` remains unconditionally fail-closed; D-005 OPEN.

## Next gate

Review these new source files for actual Windows-specific risks; fix only test-only code if justified. **Request a new explicit user approval** before any Windows G3-B execution, stating the only two synthetic file writes/replacement attempt and remaining NOT_RUN/PARTIAL cases. Until then: `G3-B DEVICE NOT_RUN; OVERALL PARTIAL_G3_HOLD`.
