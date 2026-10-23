# Windows Bifrost 2.3.2 — confirmed truncated executable despite valid PE header
**2026-10-23 — direct user-executed PowerShell evidence; sanitized for public repo.**
**Immediate disposition: BLOCKED. Do NOT run or rename the 57,943-byte cached file, and do NOT use previously issued EFTYPE rename/copy ZIP on this cache.**

## Exact sanitized user-observed outputs
| Check | Actual output | Source |
|---|---|---|
| Windows architecture | `[Environment]::Is64BitOperatingSystem = True` | User PowerShell |
| Node.js CLI | `node --version = v24.22.1` | User PowerShell |
| Cached transport file | `%LOCALAPPDATA%\bifrost\v2.3.2\bin\bifrost-http.exe-0` FOUND | User PowerShell (username normalized) |
| Exact cached byte size | **57,943 bytes** | User `Get-Item.Length` |
| DOS/MZ signature | `True` | User read-only BinaryReader |
| PE signature | `PE_SIGNATURE_VALID: True` | User read-only BinaryReader |
| Windows x64 CPU machine | `AMD64_MACHINE: True` | User read-only BinaryReader |
| PE32+ optional-header magic | `PE32_PLUS: True` | User read-only BinaryReader |
| Official vendor URL | `https://downloads.getmaxim.ai/bifrost/v2.3.2/windows/amd64/bifrost-http.exe` | Explicit vendor launcher URL, queried by user's PowerShell HEAD |
| Official HTTP HEAD | `OFFICIAL_HTTP_STATUS: 200` | User Invoke-WebRequest -Method Head |
| Vendor advertised Content-Length | **134,305,792 bytes** | User HTTP HEAD response |
| Prior NPX launch | `spawnSync ...\bifrost-http.exe-0 EFTYPE`, system `-4028`, gateway exit 1 | Prior user console output |
| Actual gateway status | **NOT_OPERATIONAL / NO_HEALTH_PASS** | No user successful start yet |

**Byte difference:** 134,247,849 bytes. Locally cached file is only **0.0431%** of the advertised official binary size. A correct DOS/PE header validates only the *beginning* of a file, **not completeness, vendor origin, publisher signature or safety**. The old view that simply removing suffix `.exe-0` would suffice is **SUPERSEDED** by direct file size evidence; NPX odd filename may still be a separate launcher bug.

## Required next safe operation (not yet executed)
1. Retain old file as failure evidence. No arbitrary deletion, Defender exclusions, unsigned installer overrides or bypassing SmartScreen.
2. Redownload the full Bifrost `v2.3.2/windows/amd64` official executable into a **new private local download destination**. Verify HTTP success, exact expected size, MZ/PE x64 format, matching cryptographic checksum if the vendor publishes one and Authenticode signature if present. No claim that HTTPS and length alone prove authentic bytes.
3. Start correctly named `bifrost-http.exe` with `-host 127.0.0.1 -port 18080`, existing `%LOCALAPPDATA%\DJMRN\Bifrost` data; do not overwrite configuration. Generate a **NEW** first-admin setup token (old one was inadvertently disclosed and is not copied to the repo). Apply dashboard authentication and keep inference denied by default until single Groq Free account and explicit no-billing/no-overage settings verified.
4. Ask user for **only sanitized** HTTP/health or error status. No secret, raw username, config key, unmasked screenshot or private prompts in public repo.
5. If transport file fails after a clean verified download, investigate Windows trust/antivirus/runtime logs separately, without asserting file name alone is root cause.

**Distinctions:** No user-machine Bifrost service installed/started successfully; test-only P2C–P2F Bifrost successes ran **on GitHub Linux**, not on this laptop. Node CLI was actually verified on user's laptop. Jan/Goose/KYNXA etc already inventoried with historical statuses, not newly installed by this command. Installer operation receipt and statistics are linked from [inventory](../../01-system-inventory/INSTALLATION-AND-DEPLOYMENT-STATISTICS-20261023.md).
