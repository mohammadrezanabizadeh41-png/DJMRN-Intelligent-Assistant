# برنامه‌ها و محیط توسعه — سابقهٔ واقعی، نه stack انتخاب‌شده
**Observed 2026-10-17 تا 2026-10-19 از [Windows Journal](https://app.notion.com/p/3fbc8c6846908184b4bbe32c586686e3).** نسخهٔ امروز ممکن است تغییر کرده باشد. هر سطر = product/observed version/evidence/status/known issue/selection؛ user-installed ≠ benchmark winner.

| مورد | آخرین نسخه/وضعیت مستند | محدودیت |
|---|---|---|
| Python | **3.14.7**؛ `py` و interpreter در user Windows آزمایش شده | `python` PATH در بعضی sessionها موقت بوده؛ wheel/SDK compatibility را مستقل بررسی کنید |
| pip | **26.2.1**، CLI TESTED | جزء Python، نه محصول جدا |
| venv / ensurepip | INSTALLED/TESTED | یکی از پروژه‌های تاریخی .venv واقعی دارد |
| SQLite Python module | **3.50.4**؛ DB/FTS5 synthetic smoke PASS | **نسخهٔ تاریخی**؛ نگرانی WAL-reset: قبل از WAL/concurrency نیاز به ارزیابی وصله/version |
| WinGet | **1.11.510**, TESTED | unrelated to architecture winner |
| Git for Windows | **2.55.0.windows.5**, CLI TESTED | GitHub App connection مستقل از local Git auth است |
| VS Code | INSTALLED **by user report**, version/CLI not verified | الزام پلتفرم نیست |
| Windows Task Scheduler | سرویس Running/Automatic در snapshot P0 | recovery workflow کامل هنوز انتخاب نشده |
| Research Architect v0 | پروژهٔ local historical؛ CLI init/inspect/index/search/packet و SQLite basic POC آزموده | مربوط به تجربهٔ قبلی؛ baseline اجباری برای پروژهٔ greenfield نیست |
| Node.js | **v24.22.1** — current user `node --version` 2026-10-23 | CLI works, exact installer transaction not captured |
| npm/npx | npx invoked in Bifrost launcher; individual version UNKNOWN | Bundled with Node; do not count as second independent installation |
| Bifrost native v2.3.2 | **BLOCKED:** cached 57,943-byte `.exe-0` vs official 134,305,792 bytes | PE64 signature alone not integrity; no local gateway health; earlier rename-only ZIP DO NOT RUN |
| Docker, WSL distro, PowerShell7, .NET, FFmpeg, uv, build tools | **NOT VERIFIED CURRENT** | Historic WSL feature ≠ distribution; GitHub Docker ≠ laptop Docker |

وضعیت خودکار: `DOWNLOADED_ONLY` با `INSTALLED` و `LAUNCHED` با `FUNCTION_TESTED` و `OPERATIONAL` متفاوت است. برای هر نصب جدید، source/vendor/version/license/download/install logs, security, rollback, RAM/CPU footprint, test outcome و user approval را در 05 و 06 و این فایل ثبت کنید. هیچ نصب تازه‌ای با ایجاد این پرونده انجام نشده است.

## G1 real read-only Windows app metadata — 2026-10-21
[User-run G1-R0001](../06-tests-and-evidence/logs/G1-R0001-20261021.md) returned `START_MENU_APP: Jan`, while `Jan.exe` was NOT found at just the two scripted common paths; Jan may be installed elsewhere or the shortcut may be stale. **CURRENT JAN VERSION/PATH/MCP/APPROVAL = UNKNOWN**, no app was started. Cherry Studio file missing at just two common paths, actual install unknown. `CHATGPT_STORE_PACKAGE: NOT FOUND` under the restricted Get-AppxPackage name query, and no ChatGPT exact-filter Start menu/process evidence; **DOES NOT rule out Win32/portable ChatGPT Desktop or determine Plus MCP entitlement**. No `Jan`, `ChatGPT`, `CherryStudio`, `Codex` exact process match at snapshot; not a global process survey. No app installed/updated by this read-only script. G1 GUI inspection still pending.

## G1 Jan shortcut target evidence — Jan-Desktop.exe (2026-10-21)

User screenshot of **Jan shortcut Properties** reports **target `%LOCALAPPDATA%\Programs\Jan\Jan-Desktop.exe`** (redacted relative path, no username). This **explains** earlier G1 probe failures: script incorrectly tested `Jan.exe` at guessed directories rather than the observed executable basename `Jan-Desktop.exe`. The registered Start menu item is now supported by screenshot target evidence; **current exe existence and file/product version still UNKNOWN**, because a shortcut alone can point to a missing executable. Previous historical Jan Desktop installation/launch still historical, not current runtime test. Shell/MCP/Allow All, actual ChatGPT Desktop Plus setting and current model status unobserved. [G1-R0001 addendum](../06-tests-and-evidence/logs/G1-R0001-20261021.md). No new install/config/run or permanent file path stored.

## 2026-10-23 — latest current CLI and statistics correction
Windows x64 True, Node.js v24.22.1 currently user-verifiable from PowerShell. Native Bifrost incomplete and not usable: [read-only evidence](../06-tests-and-evidence/logs/WINDOWS-BIFROST-TRUNCATED-PE-20261023.md). Do NOT execute prior rename-only repair package. [Statistics by 21 component states](INSTALLATION-AND-DEPLOYMENT-STATISTICS-20261023.md), [CSV snapshot](installed-software-snapshot-20261023.csv), [14 chronologically sourced events](installation-events.csv). Goose Desktop was later **launched and generated Persian text** in 2026-10-22 (see GOOSE-G3/G4); any old Goose not-installed note is superseded, but response quality failed. Historical Jan/Ollama/LM Studio/KYNXA etc app states remain historical, not newly reverified by current PowerShell.
