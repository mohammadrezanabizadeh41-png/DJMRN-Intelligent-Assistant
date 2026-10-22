# DJMRN G3-B — exact canonical source mock re-test | 12/12 PASS | Win32 NOT_RUN

**Date:** 2026-10-22. **Evidence status:** `VERIFIED EXACT-GIT-BLOBS + TESTED-SYNTHETIC ON ORIGINAL SOURCE / REAL WINDOWS NOT_RUN`.
**Authority:** `mohammadrezanabizadeh41-png/DJMRN-Intelligent-Assistant`, `main`.
**Scope:** user's approved continuation of off-device testing, no device execution or security guard changes.

## Source verification before execution

Live Notion Operating Memory + Tool Governance fetched; actual private GitHub main HEAD `62366aea090034b0cfd78de6614f598f99151b2a` read; PROJECT-RULES and leading canonical CURRENT reviewed. Retrieved the **complete original source files via authenticated GitHub access** and placed exact copies in isolated assistant-owned `/mnt/data/djmrn_g3b` (previous stand-in files were replaced). Independently computed native Git blob IDs and matched them to GitHub:

| File | Bytes | Git blob SHA-1 (MATCH) | Local SHA-256 |
|---|---:|---|---|
| `core/windows_reader.py` | 10,896 | `730f35208dd7f3f08cec3260b4fe7ef775d2faa2` | `b23c263454d10e6466b49371616d7cefcd4feb5f9330f54e777d4188d22b0f1a` |
| `core/manifest.py` | 3,399 | `f505b0d3c65a8a421684e3055bc3be12ce19a9a7` | `cd6b01cabce5f5d3005f7e7106344e6035151029cbe09d6fe96eb6bb6fa143fa` |
| `tests/test_g3b_win32_faults.py` | 8,153 | `9677d74aa557da55daf8d2b685ca54da267be573` | `df970512400631e54d75156440d8fb89f028170a216f4532857d746dfef4dd69` |

This corrects the prior [G3B isolated shim report](G3B-OFFDEVICE-FAULT-INJECTION-20261022.md): **the source under test is now the exact original GitHub reader/manifest**, not a representative stand-in. Only these exact files and a zero-byte local `core/__init__.py` package marker plus generated noncanonical prior test cache were present in the isolated staging. This is the exact three-file target for G3B; NOT a complete GitHub repository checkout or full project regression suite.

## Actual command and outcome

- Host: assistant-owned **Linux Python 3.13.5**, no Windows access, no calls to `kernel32`, no external network or account. All OS API functions in the reader intercepted by `unittest.mock.patch.multiple` and in-memory `FakeKernel`.
- Executed in isolated staging: `PYTHONDONTWRITEBYTECODE=1 python -B -m unittest discover -s tests -p 'test_g3b_win32_faults.py' -v`.
- **Result: Ran 12 tests in 0.004s — OK (12 PASS, 0 FAIL, 0 SKIP).**
- Cases 01–08 execute the **actual GitHub reader function** `read_approved_file_source_only()` with fake Win32 handle, metadata, path and byte operations; cover same-handle path, parent/leaf reparse, redirected final path, postread file index mismatch, digest mismatch and read-exception handle cleanup. Cases 09–11 exercise only the **test-local** `simulate_release_after_read()` helper; **not** an actual cancellation/revoke method in the source reader or dispatcher. Case 12 parses the actual reader source imports to exclude selected network libraries; it **does not prove no network egress**.

## Acceptance and hard limitations

**Passed:** integrity matching GitHub sources and 12 isolated off-device deterministic tests against the original core.
**Not run / not established:** genuine NTFS reparse/junction and concurrent rename, cancellation or `CancelSynchronousIo` correctness, production revoke/consent binding, actual OS handle leak/driver behavior, process-level egress/network monitoring, on-laptop G3-B, Jan or model tool integration, complete repo-wide regressions.
**Source code changes:** NONE. Existing `core/windows_reader.py`, `core/manifest.py`, `core/windows_guard.py`, `core/session.py` and CAP remain exactly as before. Guard `require_verified_read` still always BLOCKS.
**Current safety status:** G3 overall `PARTIAL_G3_HOLD`. Evidence does not authorize G3-B device execution, a production file permission grant or Jan connection.

## Next proposed narrow gate (user approval required before any new device execution)

1. Prepare a **separate** G3-B Windows fixture plan for only TWO synthetic files. Include a fail-closed junction/rename negative check without admin elevation (if unable to construct safely: SKIP/HOLD, no privilege escalation) and a cooperative cancellation/revocation *delivery* fence with deterministic tests; distinguish this from OS I/O interruption.
2. Define an independent, low-dependency egress observation mechanism and owner/consent binding test before claiming the network or operator security boundary.
3. Review the test-only packet and request explicit new user permission for **any** additional Windows laptop test. Do not change Windows settings, expose real documents or release `windows_guard` as part of G3-B.

**Conclusion:** `EXACT-CANONICAL-READER/MANIFEST FAULT-INJECTION 12/12 PASS / OFF-DEVICE ONLY / WIN32 G3-B NOT_RUN / GUARD HOLD`.
