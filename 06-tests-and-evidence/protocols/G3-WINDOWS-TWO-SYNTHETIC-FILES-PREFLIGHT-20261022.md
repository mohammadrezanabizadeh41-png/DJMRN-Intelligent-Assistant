# DJMRN G3 — Windows 11 two-synthetic-file preflight | PROPOSAL / NOT RUN

**Date:** 2026-10-22
**Authority:** project source GitHub; consult live Notion governance before actual execution.
**Baseline:** `main@9eb0cb2621440503b62ca15b6547ed8cf86ac10e`, [G2A source receipt](../logs/G2A-WINDOWS-HANDLE-READER-SOURCE-20261022.md).
**Scope:** source/documentation review ONLY. This document is NOT consent to run a command on the user's PC, not a security approval, not deployment, and not permission to wire the assistant/Jan. `require_verified_read()` remains unconditionally fail-closed.

## Findings from current source/test inspection (evidence, not Windows runtime proof)

1. `core/windows_reader.py` uses `CreateFileW` with `OPEN_EXISTING`, `FILE_FLAG_OPEN_REPARSE_POINT`, retained parent handles, `GetFileInformationByHandle`, `GetVolumeInformationByHandleW`, `GetFinalPathNameByHandleW`, and `ReadFile` on the SAME target handle, then identity/size/mtime/SHA rechecks. Declared Win32 functions and general approach are broadly consistent with canonical Microsoft API documentation. **Actual ctypes calling conventions, root-directory path output, NTFS behavior and cleanup under failures have not been Windows-tested.**
2. `tests/test_windows_reader.py::test_actual_win32_junction_and_race` is decorated with `skipUnless(win32)` BUT **also invokes unconditional `self.skipTest(...)`**. Thus simply running existing tests on Windows will NOT perform G3; it will SKIP this case.
3. Source reader has **no cancellation token/abort hook**, no independently verified cancellation cleanup, no trusted Windows enrollment of two real fixture file identities, and no instrumented real handle-leak check. These are necessary additions to the G3 harness or must be separately labeled NOT TESTED.
4. Existing `Manifest` permits 1–2 approved IDs and `read_manifest_snapshots_source_only` rejects a third/unlisted ID before file open, but `Manifest` is **not OS consent**, and `SearchSession` still does not call the reader. This is intentional.
5. Path/root/ancestor, alias and DOS-device spellings, symlink/junction, hardlink and rename/replacement races need real negative cases; passing current pure-logic mocks cannot prove them.
6. Microsoft documents Win32 API semantics, not this custom module's safety. In particular, `GetFinalPathNameByHandleW` returns a normalized `\\?\` DOS path by default; root path normalization must be observed on Windows. `CreateFileW` share modes have interaction with other open handles, so fail-closed access-denied is possible and should not be bypassed. `CancelSynchronousIo` does not guarantee immediate cancellation; the test must record cooperative state and cleanup.

## Minimum G3 isolated test plan — later explicit device approval

**Fixture boundary:** create exactly TWO small fake UTF-8 Markdown files under a temporary, newly created, user-controlled local NTFS directory (not OneDrive/cloud, not the project source tree). No real documents, accounts, third file, admin privileges, model, Jan, browser, Internet, installation, paid services or registry/system configuration changes. The fake contents must be distinctive and deterministic. Verify file system type, root and parent behavior, real volume serial/file index and hashes using local Win32 handle-based enrollment before the read. Never derive approved identity from model text.

**Cases and pass criteria:**

| Case | Action | Expected |
|---|---|---|
| G3-00 | Confirm precise repo file blob SHAs and Windows/Python environment | Match pinned sources, supported Windows + local NTFS, otherwise STOP |
| G3-01 | Enroll then read only fake A and B via same handles | Both bytes/IDs/lengths/SHA match, max 1 MiB each |
| G3-02 | Request nonexistent third ID, duplicate ID, or more than two IDs | BLOCKED before any third-path attempt |
| G3-03 | Modify one fixture after enrollment; wrong SHA/size/identity | BLOCKED, no accepted snapshot |
| G3-04 | Try a synthetic renamed/replaced file or reparse/junction alias under the isolated fixture area | BLOCKED (or explicit SKIP if unable to construct safely); never use real user paths |
| G3-05 | Test early revoke/cancel and cancellation during read with a dedicated cancellable design | BLOCKED promptly, no stale snapshot; **NOT RUN/UNIMPLEMENTED until a tested cancellation route exists** |
| G3-06 | Instrument `CloseHandle` and compare handle counts across repeated success/failure paths | All acquired handles closed, no sustained leak or unbounded memory |
| G3-07 | Re-run existing M1 negative guard/dispatcher tests | Still always `FILE_BOUNDARY_UNPROVEN`, even if direct prototype works |
| G3-08 | Ensure no outbound network or personal file paths touched; clean only created fixtures | Evidence captures permitted paths, return codes, errors, cancellation, cleanup |

**Stop conditions:** unexpected file access; directory/volume mismatch; missing Win32 API; uncaught exception; handle leak; hash/identity mismatch not blocked; unexpected guard success; any ambiguous outcome. On STOP, do not auto-retry with an alternate reader, CAP pathname search, elevated privileges or a cloud fallback.

## Engineering order (smallest adequate)

1. Review Win32 signatures/error checks and root/final-path behavior, ensure defensive cleanup; add narrowly scoped synthetic-only Windows test runner and trusted fixture-enrollment helper. Do **not** modify `SearchSession`, `windows_guard.py`, CAP original `search(root,...)`, Jan or the model.
2. Design a clear cooperative cancellation point and its deterministic unit test before claiming G3 cancellation; do not use forced termination of user processes as a substitute.
3. Only after the user explicitly authorizes local G3, provide a one-action user-run launch path and exact command/output checklist. The assistant has no direct Windows device execution access in this session.
4. Record Windows environment, exact executed files/blob SHAs, all cases PASS/FAIL/SKIP, handle resource evidence and zero external effects in a new dated `06-tests-and-evidence/logs/` report. Independently review; leave G3 `PARTIAL/HOLD` if any mandatory case is skipped. Only then consider a separate permissioned integration design/approval.

**G3 preflight outcome:** `REVIEW COMPLETE / G3 EXECUTION NOT RUN / NO-GO FOR CLAIMING FULL G3 WITH CURRENT TESTS / GUARD HOLD`.

## Primary references

- [Microsoft CreateFileW](https://learn.microsoft.com/en-us/windows/win32/api/fileapi/nf-fileapi-createfilew)
- [Microsoft GetFileInformationByHandle](https://learn.microsoft.com/en-us/windows/win32/api/fileapi/nf-fileapi-getfileinformationbyhandle)
- [Microsoft GetFinalPathNameByHandleW](https://learn.microsoft.com/en-us/windows/win32/api/fileapi/nf-fileapi-getfinalpathnamebyhandlew)
- [Microsoft GetVolumeInformationByHandleW](https://learn.microsoft.com/en-us/windows/win32/api/fileapi/nf-fileapi-getvolumeinformationbyhandlew)
- [Microsoft ReadFile](https://learn.microsoft.com/en-us/windows/win32/api/fileapi/nf-fileapi-readfile)
- [Microsoft Canceling Pending I/O Operations](https://learn.microsoft.com/en-us/windows/win32/fileio/canceling-pending-i-o-operations)
