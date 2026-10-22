# DJMRN G3 — synthetic Win32 harness source package (OFF-DEVICE ONLY)

**Date:** 2026-10-22 | **Evidence class:** `TESTED-SYNTHETIC / SOURCE-ONLY` | **Windows G3:** `NOT_RUN / HOLD` | **Authority:** GitHub `mohammadrezanabizadeh41-png/DJMRN-Intelligent-Assistant`, `main`.

## What was actually created

- [g3_synthetic_probe.py](../../05-assistants-and-capabilities/src/m1_pilot/g3_synthetic_probe.py), Git blob `1988282914635940e485dc246a0b6ff0fc87db6b`; original source commit [4e53e61](https://github.com/mohammadrezanabizadeh41-png/DJMRN-Intelligent-Assistant/commit/4e53e6197b10dbb58b7721b48b5a030357395fd5), revised source commit [c217b9a](https://github.com/mohammadrezanabizadeh41-png/DJMRN-Intelligent-Assistant/commit/c217b9a4665229956b1fe8ffdb82911781bfb3bc). Exact local Git-object SHA agreed with independent GitHub commit-ref fetch; a transient `main` content fetch returned old content immediately after commit, therefore the pinned commit ref was used for accurate readback.
- [tests/test_g3_offdevice_source.py](../../05-assistants-and-capabilities/src/m1_pilot/tests/test_g3_offdevice_source.py), Git blob `f079cb3961112e1977f26fa285dbab0f4005e8e7`, commit [1f65bdf](https://github.com/mohammadrezanabizadeh41-png/DJMRN-Intelligent-Assistant/commit/1f65bdfeeef517b23fcb1f3a4dfa5a67fdbd2890).
- [G3-REVIEW-AND-RUN.cmd](../../05-assistants-and-capabilities/src/m1_pilot/G3-REVIEW-AND-RUN.cmd), Git blob `9dc47a7a68557cf7000232845adcfceb55b31c81`, commit [5f6040b](https://github.com/mohammadrezanabizadeh41-png/DJMRN-Intelligent-Assistant/commit/5f6040b486dd75501ea2e7227c794b7919d37a9). The launcher previews and requires user to type `RUN` before Windows execution. This launcher's Windows batch behavior is NOT tested in this environment.

## Actual off-device checks

- **Environment:** assistant-owned isolated Linux Python 3.13.5 container, `/mnt/data/djmrn_g3/`; no user's Windows process, no Windows syscall, no private user document, no model/Jan/network/installation.
- **Source parse:** `python -m py_compile g3_synthetic_probe.py` → success.
- **Command:** `python -m unittest discover -s tests -v -p 'test_g3_offdevice_source.py'` → **Ran 7 tests in 0.001s; OK (7 PASS)**.
- **Exactly what those seven cases prove:** Python source AST parsed; source encoding roundtrip; correct Git-blob computation; mocked handle open/close accounting detects an unclosed handle; denial function rejects fail-open; Linux refuses synthetic Windows fixture creation; basic no-network/no-recursive-delete static checks. **No real Win32 handle, NTFS volume, concurrency, actual cancellation, deployment, package extraction or Windows launcher was exercised.**
- **Raw local source fingerprints:** runner SHA256 `6ee039fa89aa6a5be5da7c43fdd61f076aa3e69c8e07fa88d879976affb87f64`; test SHA256 `f3fb3abaca32ea34e42019c0ff50858cf6aab3c2644023fe75306c3e82badf1c`. Local and GitHub Git blob IDs matched. These are artifact integrity checks, NOT evidence of behavioral safety.

## Limited intended Windows procedure (future, separate consent)

The Python runner checks pinned Git blobs BEFORE importing repository core modules, defaults to plan/no-run, refuses Linux, uses only Python stdlib and two fake .md files inside a uniquely created local `%LOCALAPPDATA%\Temp\DJMRN_G3_SYNTHETIC_*` directory. It enrolls file serial/index/size from Win32 handle metadata (test SID is a sentinel, NOT user authorization), asks the existing source-only reader to return two same-handle snapshots, rejects a third/duplicate ID before file open, tests same-size mutation and replacement, compares acquired/released handles and checks the still-closed M1 guard. On completion it attempts non-recursive deletion of only its own created fake files and folder. The user can see a sanitized JSON report on screen.

**Known gaps must remain visible:** cancellation path G3-05 `NOT_RUN`; junction/reparse and concurrent rename race G3-04B `NOT_RUN`; actual network monitoring G3-08 `PARTIAL`; real operator SID/consent not bound to device manifest; Windows NTFS system behavior and actual `CloseHandle` lifecycle `NOT_RUN`; no Jan/model/assistant tool integration. An off-device PASS or even a successful narrow device probe does NOT automatically approve G3-complete, code safety, production deployment or removal of `WindowsGuardHold`.

**State:** `HARNESS READY FOR USER REVIEW / G3 DEVICE NOT_RUN / FAIL-CLOSED`. Keep original `core/windows_reader.py`, `core/manifest.py`, `core/windows_guard.py`, `core/session.py`, CAP, Jan and accounts unchanged. Compare future exact checkout blobs with PINNED_BLOBS; abort on mismatch rather than silently substituting code.

**Sources:** [G3 preflight plan](../protocols/G3-WINDOWS-TWO-SYNTHETIC-FILES-PREFLIGHT-20261022.md); [Microsoft directory handles](https://learn.microsoft.com/en-us/windows/win32/fileio/obtaining-a-handle-to-a-directory); [Microsoft CreateFileW](https://learn.microsoft.com/en-us/windows/win32/api/fileapi/nf-fileapi-createfilew); [Microsoft final path](https://learn.microsoft.com/en-us/windows/win32/api/fileapi/nf-fileapi-getfinalpathnamebyhandlew); [Microsoft handle identity](https://learn.microsoft.com/en-us/windows/win32/api/fileapi/nf-fileapi-getfileinformationbyhandle); [Microsoft volume info](https://learn.microsoft.com/en-us/windows/win32/api/fileapi/nf-fileapi-getvolumeinformationbyhandlew).
