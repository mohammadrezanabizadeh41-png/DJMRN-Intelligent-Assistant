# G2A-WINHANDLE-001 — isolated Win32 same-handle reader prototype, off-device tests, deployment HOLD

**Date:** 2026-10-22 | **Scope:** narrow user-authorized G2A source development, not Windows G3.  
**Status:** `SOURCE COMMITTED / ISOLATED NON-WINDOWS TESTS 6 PASS + 1 SKIP / NO REAL WIN32 TEST / M1 GUARD STILL FAIL-CLOSED`.  
**Canonical project:** `mohammadrezanabizadeh41-png/DJMRN-Intelligent-Assistant`, `main`.  
**Implementation commit:** [47dcd3d07b908985a5eae5b85bbf497658477dc8](https://github.com/mohammadrezanabizadeh41-png/DJMRN-Intelligent-Assistant/commit/47dcd3d07b908985a5eae5b85bbf497658477dc8), single parent `dab6a609522ed32345b764dec2ed5872e388da60`. GitHub independently compared: **one commit**, **exactly three ADDED files**, no other modifications:
- [core/windows_reader.py](../../05-assistants-and-capabilities/src/m1_pilot/core/windows_reader.py): Git blob **`730f35208dd7f3f08cec3260b4fe7ef775d2faa2`** (10,896 characters; Git blob matches independently tested local source exactly).
- [tests/test_windows_reader.py](../../05-assistants-and-capabilities/src/m1_pilot/tests/test_windows_reader.py): Git blob **`385bb5265660d8f440da4577f33536f23744e58d`** (3,355 characters; Git blob matches independently tested local test source exactly).
- [WINDOWS-READER-DESIGN.md](../../05-assistants-and-capabilities/src/m1_pilot/WINDOWS-READER-DESIGN.md): source design and limitations.

## 1. Narrow source mechanics (prototype, NOT verified safe Windows runtime)

- Reject malformed/non-drive-absolute/UNC/device/ADS/extended/special DOS names; paths restricted to one local `.md` file on an NTFS drive with conservative unambiguous spelling.
- Win32 `CreateFileW`: parent directories opened with `FILE_FLAG_BACKUP_SEMANTICS | FILE_FLAG_OPEN_REPARSE_POINT`; individual handles retained through `ExitStack` with read-only sharing. Target file opened by `CreateFileW` with `FILE_READ_DATA | FILE_READ_ATTRIBUTES`, `FILE_SHARE_READ`, `OPEN_EXISTING` and `FILE_FLAG_OPEN_REPARSE_POINT`.
- Via **handle-based** `GetFileInformationByHandle`, `GetFileType`, `GetVolumeInformationByHandleW`, `GetFinalPathNameByHandleW`: reject reparse/offline, non-file, hardlink count!=1, wrong NTFS volume serial/file index, size mismatch/oversize, final path changes. Read raw bytes with `ReadFile` on **same handle**, bound <=1MiB; recheck handle metadata and compare raw SHA256 with manifest before returning a `VerifiedSnapshot`.
- **No caller consent proof inside this component.** `read_manifest_snapshots_source_only` takes a trusted operator-side manifest and selected IDs but does not grant authorization or trust user-supplied manifests. The component is intentionally **NOT IMPORTED/CALLED** from [core/session.py](../../05-assistants-and-capabilities/src/m1_pilot/core/session.py). [core/windows_guard.py](../../05-assistants-and-capabilities/src/m1_pilot/core/windows_guard.py) **still ALWAYS RAISES `WindowsGuardHold`**, including after mocked approval. CAP-006 existing `search_preloaded_bytes` can consume verified bytes *later* only after explicit control-plane wiring and Windows tests, **not now**.
- User's Windows 11 machine, filesystem settings, Jan version, model and path/hardlink/symlink/junction handling have not been observed in this turn. Source does **not** establish an OS sandbox against same-user malicious code or guarantee all filesystem driver corner cases.

## 2. Actual isolated test receipt and limits

**Environment:** assistant-owned Linux Python interpreter, in ephemeral `/mnt/data/djmrn_g2_win` source staging. In that temporary test directory, `core/manifest.py` was a **minimal structural dataclass stub**, not the full canonical GitHub manifest implementation; verified reader/test exact bytes match GitHub blob after creation. **No user private files, real Windows calls, downloads, installer, network APIs or inference involved.**

Actual command: `PYTHONPATH=. python -m unittest discover -s tests -p 'test_reader.py' -v`  
**Result:** `Ran 7 tests in 0.002s; OK (skipped=1)` = **6 PASS + 1 SKIP**. Scope: local Windows spelling rejection, mocked handle metadata comparison, hardlink/reparse/directory rejection, off-Windows denial, third-ID rejection. The skipped test is actual Windows junction/rename/race; SKIP is NOT a PASS. Both Python files passed off-device `py_compile` syntax check. **Not** a G3 device test, WinAPI runtime proof, a full M1 regression suite or a full original repo checkout.

## 3. Independent GitHub readback

Compared `dab6a609...` to `47dcd3d...`: 1 commit, only 3 new paths under `05-assistants-and-capabilities/src/m1_pilot/`, zero changed pre-existing CAP, tests, dispatch, code configuration, runtime model or accounts. Git blob of Windows reader `730f352...` and test source `385bb52...` equal the actual off-device test files' Git object hashes. Existing [core/session.py](../../05-assistants-and-capabilities/src/m1_pilot/core/session.py) blob `2f04a2c5b7ab650211d85577c56faebfb87c0707` unchanged; existing guard unconditional denial confirmed.

## 4. Source citations and hard next gate

Official Microsoft primary documents checked for source design: [CreateFileW](https://learn.microsoft.com/en-us/windows/win32/api/fileapi/nf-fileapi-createfilew), [ReadFile](https://learn.microsoft.com/en-us/windows/win32/api/fileapi/nf-fileapi-readfile), [BY_HANDLE_FILE_INFORMATION](https://learn.microsoft.com/en-us/windows/desktop/api/fileapi/ns-fileapi-by_handle_file_information), [GetVolumeInformationByHandleW](https://learn.microsoft.com/en-us/windows/win32/api/fileapi/nf-fileapi-getvolumeinformationbyhandlew), [GetFinalPathNameByHandleW](https://learn.microsoft.com/en-us/windows/win32/api/fileapi/nf-fileapi-getfinalpathnamebyhandlew). Documentation proves API semantics, **not this module's end-to-end OS safety**.

**HOLD:** before connecting it to session/model, complete a deliberate WinAPI code review (including root vs child handle semantics and alias/parent race), real Windows synthetic-only T05/T06/T08/T09/T10 negative tests with **separate user G3 approval**, and verify exact local file IDs+real SHA through trusted operator enrollment; error/no read/no external effects must fail closed. If any violation, report BLOCKED and revise source; never fall back to `search(root,...)` or silently enable Jan/LLM. No G2B-A Jan adapter or B UI is authorized by this receipt.
