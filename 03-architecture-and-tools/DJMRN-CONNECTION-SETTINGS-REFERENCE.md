# DJMRN — مرجع واحد تنظیمات اتصال سرویس‌ها و دستیارها
**Date:** 2026-10-26 · **Branch:** main · **Scope:** technical configuration inventory, not a progress log. **Created on the user's explicit request to preserve settings for future chat windows.**

## قواعد ثبت
- تنظیم‌های زیر برچسب **VERIFIED**, **OBSERVED**, **PLANNED**, یا **TEST-PENDING** دارند. فقط با شواهد واقعی Windows وضعیت را تغییر بده.
- **هیچ API key، رمز، token، cookie، ایمیل شخصی یا فایل خصوصی در GitHub (public) نگهداری نشود.** فقط نام فیلد و محل ورود خصوصی ثبت شود. برای دستیار بعدی لازم نیست کلیدها را از کاربر بخواهد؛ هنگام انجام آزمایش، کاربر مقدار موجود را مستقیماً داخل برنامه وارد می‌کند.
- روتر مرکزی فعلی OmniRoute مستقل از محیط AGNT است. برای اتصال جدید **تنظیمات فعال OmniRoute را تغییر نده**؛ فقط client/AGNT را روی endpoint فعلی تنظیم کن.
- این فایل محل مرجع **تنظیمات فنی و کانکشن‌های برنامه‌ها** است؛ برای ثبت وضعیت روزمره همچنان از `07-operations-and-continuity/CURRENT-STATUS.md` با درخواست صریح کاربر استفاده کن. به‌روزرسانی این مرجع فقط به درخواست کاربر یا اجازهٔ مشخص مجدد انجام می‌شود.

## 1. OmniRoute — Central local model gateway
| Key | Value | Confidence |
|---|---|---|
| Software | OmniRoute desktop, reported v3.8.52 | OBSERVED in earlier Windows work |
| OpenAI-compatible API base | `http://127.0.0.1:20128/v1` | VERIFIED by previous direct PowerShell pilot |
| Local management UI (documented path) | `http://127.0.0.1:20128/dashboard` | DOCS / availability to recheck |
| DJMRN custom combo/model ID | `DJMRN-Persian-L1` | VERIFIED by earlier direct HTTP 200 completion |
| Upstream on earlier successful pilot | `aihorde/koboldcpp/gemma-4-E4B-it` | Historical observation, do **not** assume always routed there |
| Auth method | Bearer API key required in earlier direct pilot | OBSERVED; **SECRET NOT STORED** |
| Local network scope | Loopback only, `127.0.0.1` on user's own Windows PC | PLANNED integration assumption; do not expose externally |
| Agent-tool calling, workflows, failover, performance | Not proven by text-only completion | TEST-PENDING |

API key handling: user previously used PowerShell `Read-Host -AsSecureString` and passed `Authorization: Bearer <key>` only inside private user device session. Do not store actual key in code/repo or claim it is remembered. No substitution with OpenRouter: **OpenRouter and OmniRoute are different products**.

## 2. AGNT Desktop — GUI agent host
| Key | Value | Confidence |
|---|---|---|
| Product/release | AGNT desktop Windows `0.6.7`, `agnt-gg/agnt` | OBSERVED installed and opened by user |
| Installation download | `https://github.com/agnt-gg/agnt/releases/download/v0.6.7/AGNT-0.6.7-win-x64.exe` | Official release |
| GUI status | Initial email/Google sign-in blocker eventually overcome; actual main desktop UI appeared | VERIFIED from user screenshots |
| Profile shown in main UI | `InnovativeAmethystFly` | OBSERVED; user was advised to rename to DJMRN but screenshot still showed old name |
| Current selected AI model in UI | `ChatGPT / gpt-6.1-sol` | OBSERVED, NOT OmniRoute |
| Local backend (product documentation) | `http://127.0.0.1:3333` (port 3333) | DOCUMENTED, not locally port-checked on user's machine |
| Model picker | Ask anything → current model pill → `Specific` → `+ Add Custom` | VERIFIED user followed via screenshots |
| Open dialog | `Add Custom Provider`, shows Start from template / Provider Name / Base URL / API Key / Models / Test Connection / Save | VERIFIED screenshot 2026-10-26 |
| License/cost | Avoid upgrade, optional paid services, external execution until separately approved | USER CONSTRAINT |

### AGNT → OmniRoute: exact proposed input (NOT YET SAVED OR TESTED)
| Field | User should enter |
|---|---|
| Start from template | `Custom (blank)` |
| Provider Name | `DJMRN OmniRoute` |
| Base URL | `http://127.0.0.1:20128/v1` |
| API Key (Optional by UI) | **Enter existing OmniRoute API key privately in AGNT UI only; actual value MUST NOT be recorded** |
| Models (Optional by UI) | `DJMRN-Persian-L1` (one ID per line) |
| First action after filling fields | `Test Connection` and inspect exact result **before** `Save` |
| Post-test action | Save only if test succeeds or after diagnosing a model-catalog-only problem; then choose this provider/model explicitly |
| Next independent smoke | One harmless Persian-only prompt, with no file/MCP/tool permissions; record status only from actual user result |

**Current state:** dialog was open but BLANK in the last screenshot; user has not yet provided Test Connection success, Save result, AGNT → OmniRoute chat completion, model calls with tools, memory, or agent delegation. Do not report any as PASS.

The custom provider form's Models field says *Leave blank to detect automatically*; explicitly adding Combo ID avoids dependence on `/v1/models` listing when the gateway or model catalog does not expose it. A passing *Test Connection* may mean provider discoverability but not successful inference; run a separate harmless completion after configuration.

## 3. Other installed / contemplated components (connection inventory, not acceptance)
- **Agno** package `agno==3.1.10`, isolated Python 3.12.15 venv at `%LOCALAPPDATA%\DJMRN\agent-foundation\.venv`; **import checks PASS**, in-process chat pilot blocked by Windows PowerShell-to-Python quoting before API request. Do not re-install or treat as model failure. See CURRENT-STATUS.
- **Jan, LM Studio, Ollama, other local apps:** prior installation/model tests exist, but **do not assume currently running** or capable of hosting central cloud model. No need to configure these to connect AGNT to OmniRoute.
- **AionUi**: user could not download Windows 2.2.2 installer (WinGet `0x80072ee2` timeout despite HEAD 200 to static host); NOT INSTALLED in current attempt. Its GUI suitability not user-tested.
- **Orkas**: `https://orkas.ai/views/login/login.html` reported `HTTP=200` by curl, but page **did not open in user's Chrome**. Packaged installer requires vendor account. Not installed/accepted.
- **OpenWork**: official Win-x64 desktop installer link identified for v0.18.62 but user returned to working AGNT; **no OpenWork install evidence**.
- Future AionUi/Orkas/OpenWork/AnythingLLM/Cherry/Eigent research is a candidate list only. Do not repeat full discovery until needed.

## 4. Generic entry format for future integrations
For every new external or local provider use the same schema:
`Product; App version; OS; local process/port; management URL; API base; API compatibility; exact model IDs; auth TYPE (never secret VALUE); service hostnames if any; VPN/direct-Iran connectivity result; status VERIFIED/PLANNED/FAILED; test date/evidence; permissions scope; cost/free tier; RAM footprint if measured; fallback/dependency notes.`

### Evidence boundary / next action
Current user image shows AGNT **Add Custom Provider** form ready. User should enter the five values above, run **Test Connection**, and paste only the **status/error text**, redacting secrets if shown. Only then mark the test outcome. The current document records configuration instructions; it does not claim AGNT and OmniRoute are already integrated.
