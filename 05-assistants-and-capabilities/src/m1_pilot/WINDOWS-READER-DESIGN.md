# DJMRN G2A Windows verified-handle reader — SOURCE ONLY / G3 HOLD

**Implementation status:** a native Windows `ctypes` reader exists as a **prototype** in [core/windows_reader.py](core/windows_reader.py), with [source-level negative unit tests](tests/test_windows_reader.py). It is NOT imported or called by `core/session.py`, whose `require_verified_read` call remains fail-closed unconditionally. `search_preloaded_bytes` remains a separate pure byte matcher; no real local files were opened for this development iteration.

## Documented Win32 mechanics (source design, not a tested guarantee)
- [CreateFileW](https://learn.microsoft.com/en-us/windows/win32/api/fileapi/nf-fileapi-createfilew): open exact path with `OPEN_EXISTING`, `FILE_FLAG_OPEN_REPARSE_POINT`, `FILE_SHARE_READ`; directory handles additionally need `FILE_FLAG_BACKUP_SEMANTICS`. Keep all parent handles open through the read; reject reparse/offline flags, directory misidentification, unsupported path forms, device/UNC/ADS and not-NTFS volumes.
- [GetFileInformationByHandle](https://learn.microsoft.com/en-us/windows/win32/api/fileapi/ns-fileapi-by_handle_file_information): compare volume serial, 64-bit NTFS file index, byte count and hardlink count **before reading bytes**, and verify again afterward.
- [GetVolumeInformationByHandleW](https://learn.microsoft.com/en-us/windows/win32/api/fileapi/nf-fileapi-getvolumeinformationbyhandlew) and [GetFinalPathNameByHandleW](https://learn.microsoft.com/en-us/windows/win32/api/fileapi/nf-fileapi-getfinalpathnamebyhandlew): reject non-NTFS or noncanonical final paths (source code only; Windows behavior NOT RUN).
- [ReadFile](https://learn.microsoft.com/en-us/windows/win32/api/fileapi/nf-fileapi-readfile): read from the SAME approved open handle, no path reopen; bound <=1MiB, reread handle metadata and compute SHA256 before producing a snapshot. No speculative path-based read, no fallback to legacy CAP-006 `search(root,...)`.
- Parent-directory replacement/reparse/hardlink scenarios need separately approved, real Win32 negative tests. Handle identity+SHA protects *which bytes can be returned*, not malicious same-user process attacks, and opening paths may itself trigger OS/filesystem effects. This is NOT an OS sandbox.

## Evidence and test limits
- Isolated off-device test of the same proposed pure validation logic/source reader: **7 test cases executed, 6 PASS and 1 SKIPPED** (Windows-only). Performed in a Linux Python container with a minimal structural `ApprovedFile`/`Manifest` stub matching the required fields, **not** the user's Windows or a full original repository checkout. Metadata mocks are not Windows OS evidence.
- Code was syntax-compiled in that container; runtime Windows `ctypes` function signatures and actual kernel behavior have NOT been checked on Windows.
- Real Jan, MCP adapters, actual user-approved local manifest creation, owner SID control, native consent GUI, human approval binding, cancellation/EOF/process lifecycle, model weight/engine, RAM, Persian caret, source card and network egress ALL remain untested or unimplemented.
- **Guard remains HOLD**: `core/windows_guard.py:require_verified_read` always raises `WindowsGuardHold` and `core/session.py` still cannot read any file.

## Next gate
Prior to any G3, review WinAPI signatures, root/parent handle behavior, reparse/junction/rename/hardlink/ADS and concrete Windows errors; create an explicit synthetic-only plan for Windows. The user must authorize running any Windows probe on their device separately. If unsafe, fix source without widening tools or removing the HOLD. Do not wire reader to tool dispatcher, CAP or Jan merely because this code has been committed.
