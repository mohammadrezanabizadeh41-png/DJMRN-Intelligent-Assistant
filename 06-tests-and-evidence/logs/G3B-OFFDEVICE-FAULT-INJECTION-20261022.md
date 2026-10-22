# DJMRN G3-B — off-device fault-injection source checks and proposed Windows gates

**Date:** 2026-10-22 | **Status:** `TEST SOURCE COMMITTED; 12/12 IN ISOLATED SHIM; REAL REPO EXECUTION NOT_RUN; WINDOWS G3-B NOT_RUN / GUARD HOLD`.
**Scope authorized by user:** prepare the next G3-B source-only tests outside the laptop, following the previous real Windows G3 result of 9 PASS/2 NOT_RUN/1 PARTIAL. No new laptop run, installation, Jan/model activation, account or filesystem permission.

## Canonical source preflight and changed files

- Pre-work live Notion Operating Memory and Tool Governance fetched; exact private GitHub repo `mohammadrezanabizadeh41-png/DJMRN-Intelligent-Assistant`, `main@79cdfa34f37fe65611c9e1cb8d0e3029503a48a6` read. `PROJECT-RULES.md`, leading CURRENT, G2A Win32 reader, manifest, session, guard, G3 runner and user-Windows evidence inspected.
- Added **one test-only file**: [`tests/test_g3b_win32_faults.py`](../../05-assistants-and-capabilities/src/m1_pilot/tests/test_g3b_win32_faults.py), commit [`201486314230cd7d4e06b8a75cb7c9a95929dd9c`](https://github.com/mohammadrezanabizadeh41-png/DJMRN-Intelligent-Assistant/commit/201486314230cd7d4e06b8a75cb7c9a95929dd9c), Git blob `9677d74aa557da55daf8d2b685ca54da267be573` verified against the local staged test file and readback, 8,153 UTF-8 bytes.
- Existing `core/windows_reader.py` blob `730f35208dd7f3f08cec3260b4fe7ef775d2faa2`, `core/windows_guard.py` blob `2ad992932489b1f12417c9e5e5eb4a1d2c40d12a` and `core/session.py` blob `2f04a2c5b7ab650211d85577c56faebfb87c0707` **unchanged**. No production code, CI workflow, external service or Windows setup altered.

## Exact test execution and evidence limits

- Assistant-owned Linux Python **3.13.5**, isolated `/mnt/data/djmrn_g3b`, no network and no user machine operations. `python -m py_compile tests/test_g3b_win32_faults.py` PASS.
- Command: `python -B -m unittest discover -s tests -p 'test_g3b_win32_faults.py' -v`; result **Ran 12 tests in 0.003s, OK**.
- **Critical test validity boundary:** The staging directory contained a minimal **stand-in** `core.windows_reader` + `core.manifest` implementing the relevant G2A contract, not the exact original 10,896-character GitHub reader nor the full original repository checkout. The **test source** was identical to committed GitHub blob. Consequently 12/12 PASS confirms the test cases, fake-kernel harness and a representative contract only; it **does not count as tests run against the actual canonical reader**, nor does it validate ctypes/Win32 behavior.
- Test fake kernel intercepts handles and metadata inside memory. No real junction, ACL, NTFS, race threads, cancellation API or OS egress monitoring was exercised. Tests 09–11 model a *post-read delivery gate*, not interruption of a blocked `ReadFile`.

## 12 deterministic cases and what they establish within the shim

| Test | Simulated result | Claim limit |
|---|---|---|
| 01 | Approved snapshot, same simulated handle, all acquired handles closed | No actual kernel32 handles |
| 02 | Parent directory reparse flag rejected pre-read | No actual Windows junction |
| 03 | Parent final path redirected and rejected | No concurrent rename |
| 04 | Leaf reparse flag rejected pre-read | No OS symlink |
| 05 | Leaf final path redirected and rejected | No in-flight race |
| 06 | File ID modified between read and post-read metadata rejected | Deterministic injected state, not concurrent adversary |
| 07 | Wrong bytes fail SHA check | Simulated content |
| 08 | Read failure closes all tracked handles | Only fake handle accounting |
| 09 | Revocation before read blocks model delivery | Pure test gate, NOT reader feature |
| 10 | Revocation during fake read blocks model delivery after read returns | Cannot cancel blocked Win32 call |
| 11 | No revocation allows simulated bytes | Not permission enforcement |
| 12 | AST of staged reader has no listed network-library imports | Static import absence only; not real process/network egress audit |

## Official API boundary and next steps

- [Microsoft CreateFileW](https://learn.microsoft.com/en-us/windows/win32/api/fileapi/nf-fileapi-createfilew): opening with `FILE_SHARE_READ` without `FILE_SHARE_DELETE` limits rename/delete access on compatible open handles; do not generalize to full ancestor/driver/race-proof semantics.
- [Microsoft Canceling Pending I/O](https://learn.microsoft.com/en-us/windows/win32/fileio/canceling-pending-i-o-operations): `CancelSynchronousIo` is an attempt, not an assured immediate cancellation; new reads and callback/order races must be handled explicitly.
- **Next source-review gate, before any Windows G3-B run:** execute these 12 tests in an isolated **exact full canonical repo checkout**, verify Git blobs, inspect any differences from the stand-in, repair tests only where evidence warrants; extend carefully to bounded synthetic junction and concurrent rename cases with privilege-free test setup, or mark unsupported environment `NOT_RUN`. Separate revocation state and final-release fence from OS-level interrupt. For egress, use an independently verified plan; AST alone is not enough.
- **User approval boundary:** no new on-laptop G3-B execution, user documents, Jan adapter, removal of guard, OS/network setting, installation, privileged junction creation or security decision authorized by this source-only work. When the exact-repo tests pass, propose a minimal Windows test packet for new user approval.

**Verdict:** `G3-B TEST SOURCES READY; 12 SHIM PASSES; EXACT-REPO AND WIN32 VALIDATION PENDING; G3 OVERALL PARTIAL_G3_HOLD`.
