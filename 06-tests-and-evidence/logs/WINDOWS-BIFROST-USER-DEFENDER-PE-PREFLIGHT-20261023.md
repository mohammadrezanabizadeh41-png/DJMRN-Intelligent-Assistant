# Bifrost Windows 2.3.2 — User local pre-execution PowerShell and Defender receipt

**2026-10-23 — USER-REPORTED DEVICE RESULT / PRELAUNCH ONLY / NO USER GATEWAY EXECUTION YET.**

## Exact minimal, sanitized user command output
| Check | User output | Correct scope |
|---|---|---|
| SHA256 and exact 134305792-byte selection | `FILE_SIZE_SHA256: PASS` | Compared to user's previous locally computed SHA256 `430D365584D6F47CC8167AC65A747163AB6FB1ECCF666978F37B263E63C377B2` and previously reported official HTTP HEAD length, not an independently verified publisher hash |
| Windows PE executable structural check | `PE64_FORMAT: PASS` | PE signature, AMD64 machine and PE32+ magic only, not cryptographic code authenticity |
| Windows Defender `Start-MpScan -ScanType CustomScan -ScanPath <file>` | `DEFENDER_SCAN: COMPLETED_WITHOUT_COMMAND_ERROR` | PowerShell command completed without throwing. **Does not independently establish Defender detection history or guarantee malware-free bytes.** |
| User Bifrost launch | `BIFROST_EXECUTION: NOT_ATTEMPTED` | **Not run, no native process/UI/HTTP health proof** |

**Preceding device evidence:** direct download of 134305792 bytes from `https://downloads.getmaxim.ai/bifrost/v2.3.2/windows/amd64/bifrost-http.exe`; local SHA-256 as above, Windows Authenticode `NotSigned`. [Download evidence](WINDOWS-BIFROST-FULL-SIZE-DOWNLOAD-20261023.md). Exact version vendor documentation confirms named CLI parameters (`-host`, `-port`, `-app-dir`). Official SHA256 for this exact binary was not independently verified. Unsigned status remains, and user should give deliberate consent before running a local unsigned executable even if Defender scan did not error.

**Safety/design boundary of next step:** only the unique user-private file matching exact SHA256/size; bound on `127.0.0.1:18080`, using existing `%LOCALAPPDATA%\DJMRN\Bifrost` data directory and no overwrite of config. No backend cloud credentials or payment. Generate NEW first-admin setup token privately and NEVER send it to ChatGPT/GitHub. If Windows security issues an alert, do not override it; stop and report sanitized nonsecret diagnostic. Original NPX-cached 57943-byte `bifrost-http.exe-0` and rename-only repair ZIP remain **DO_NOT_EXECUTE**. Remote actual provider and Jan chat **NOT_RUN**, D-005 OPEN, file-access G3B/M1 CLOSED.

**Inventory change:** `01-system-inventory/installation-events.csv` adds one user-run prelaunch security check; software installed state unchanged `DOWNLOADED_FULL_SIZE_NOT_EXECUTED`. All paths sanitized; no token, account name or raw user-specific filesystem path stored.
