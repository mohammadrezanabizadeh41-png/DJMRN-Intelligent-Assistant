# DJMRN G3-B Windows negative test — narrow proposed gate (NOT approved to run)

**Created:** 2026-10-22 | **State:** `PROPOSAL / SOURCE-ONLY / NO WINDOWS TEST APPROVAL`.
**Baseline:** [G3 user-Windows partial result](../logs/G3-USER-WINDOWS-SYNTHETIC-RESULT-20261022.md), [G3-B exact original source 12/12 mock test](../logs/G3B-EXACT-SOURCE-MOCK-RETEST-20261022.md).
**Scope:** evaluate missed security cases before any M1/Jan tool integration. This proposal itself is NOT executable consent and does not remove `core/windows_guard.py` HOLD.

## Use existing components and avoid extra infrastructure

- Reuse current Python stdlib Win32 `ctypes`, existing `G3` two-fake-document constraint, `core/windows_reader.py` and `tests/test_g3b_win32_faults.py`.
- Keep `SearchSession`, `windows_guard`, CAP and Jan unchanged. No new package, installer, admin elevation, persistent daemon, cloud provider, model, personal directory scan or third document. Test code must default to **plan-only** and require opt-in at execution.
- Keep fixtures in one unique local NTFS non-cloud directory with exactly two test Markdown files. Cleanup only created artifacts, no broad recursive delete. Store sanitized case outcomes, avoid user paths/SIDs/serials.

## Acceptance matrix — do not conflate separately scoped tests

| ID | Check | Required evidence / stop rule |
|---|---|---|
| G3B-00 | Git hash of exact runner/reader/manifest and approved isolated directory | Mismatch => STOP before file creation |
| G3B-01 | Existing authorized A/B same-handle positive control | Correct bytes/hash/identity; parent and file handles closed |
| G3B-02 | Synthetic parent reparse/junction + leaf link cases (where safely possible without elevation) | Rejected before reading target bytes; if Windows privileges prevent setup, record NOT_RUN / HOLD, do not request admin |
| G3B-03 | Rename/replacement attempt while exact parent/leaf handles remain held, using bounded separate test worker on only the fixture directory | Expected denial or verified identity-safe read; capture explicit Win32 errors without pretending a blocked rename proves every race |
| G3B-04 | Injected change between pre-/post-read metadata | Hash/identity mismatch DENIED; no output delivered |
| G3B-05 | Cooperative cancel/revoke prior to read + after read but before result release | Prevent result release; cancellation state and final user permission checked by caller at delivery boundary; currently **not implemented in production** |
| G3B-06 | OS synchronous I/O interruption only if independently justified | `CancelSynchronousIo` can request cancellation, not guarantee it; no forced process/thread termination; mark DEFERRED unless a safe bounded purpose is demonstrated |
| G3B-07 | Handle accounting on success, error and cancellation | All tracked opens balanced by closes; report bounded process handle delta separately if measured (not OS-wide leak proof) |
| G3B-08 | Network egress | No network code and independent process-level monitoring if actually available; otherwise PARTIAL, not PASS |
| G3B-09 | Guard/dispatcher remains fail-closed | Existing `FILE_BOUNDARY_UNPROVEN` unchanged; no Jan/model account traffic |

**Security stop conditions:** any nonfixture path touched, privilege escalation prompt, path or source hash mismatch, unexpected successful reparse read, unhandled exception, persistent handle leak, leaked snapshot after revocation, attempted network transfer or ambiguous source identity. Do not retry with path-based CAP search, disabled Windows security, elevated privileges, a bigger file scope, or a cloud API.

## Specific conclusions grounded in current official Microsoft Win32 documentation

- `CreateFileW` with `FILE_FLAG_OPEN_REPARSE_POINT` changes behavior for a reparse point at the object opened; preserve checks of ancestors and final paths. `FILE_SHARE_READ` omits `FILE_SHARE_DELETE` and may block rename/delete attempts, but successful bounded tests do not prove protection against all races/filesystem drivers. Reference: [Microsoft CreateFileW](https://learn.microsoft.com/en-us/windows/win32/api/fileapi/nf-fileapi-createfilew).
- `GetFinalPathNameByHandleW` returns a handle-based path view with OS normalization semantics; it is a check, not the sole security oracle. Reference: [Microsoft API](https://learn.microsoft.com/en-us/windows/win32/api/fileapi/nf-fileapi-getfinalpathnamebyhandlew).
- `CancelSynchronousIo` is an *attempt* and may target the wrong operation if thread lifecycle/synchronization is not controlled. Separate: (A) **application-level no-release-after-revoke** from (B) **physical I/O cancellation**, then test both or defer B. Reference: [Microsoft I/O cancellation](https://learn.microsoft.com/en-us/windows/win32/fileio/canceling-pending-i-o-operations).

## Staging/approval order

1. Design or implement the minimum synthetic-only test code; test it off-device with negative/fault injection; no production guard edits.
2. Review permissions, source blobs, test-only filesystem behavior, cancellation boundaries and observed vs unobserved egress.
3. **Request explicit new user permission** for only the G3-B fixture run on Windows 11 after showing its exact launcher/effects. The earlier G3 approval does not automatically extend to new junction/rename or cancellation tests.
4. User returns sanitized case report; log PASS/FAIL/NOT_RUN and resource/cleanup outcomes in GitHub. Never label security `DONE` if a required case remains NOT_RUN/PARTIAL.

**Go/No-go now:** `SOURCE MOCKS 12/12 PASS; WINDOWS G3-B NOT_RUN; USER DEVICE APPROVAL PENDING; FILE GUARD HOLD`.
