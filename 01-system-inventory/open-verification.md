# نواقص موجودی — نیازمند بررسی فقط در زمان لازم
ثبت حاضر **منبع کامل آنچه تاکنون می‌دانیم** است، نه ادعای داشتن فکت‌های مشاهده‌نشده:
- [ ] current Windows UBR/build، اگر dependency نسخه‌ای خاص مطرح شد.
- [ ] ظرفیت/تعداد پارتیشن/سلامت دیسک دقیق، فقط برای انتخاب نصب/فضا.
- [ ] current running processes، GPU/RAM/commit و file locations، فقط پیش از تست منتخب یا تغییر.
- [ ] نسخهٔ کنونی UI/CLI هر app، بعد از احتمال update/reinstall.
- [ ] نام/حجم/hash دقیق همهٔ GGUFها، فقط وقتی reuse/download/storage مطرح شد.
- [ ] عملیات واقعی network/provider در حساب کاربر یا legal access Iran؛ هیچ نتیجهٔ تاریخی ادعای مجوز آینده نیست.
- [ ] امن بودن sandbox/Tool permission هر Agent، مستقل از موفقیت text chat.

اگر نیازی به این موارد در تصمیم جاری نیست، **دوباره کل D0 را نخواهید**. خطا/ابهام را `UNKNOWN` بگذارید و در زمان مناسب حداقل تست read-only را با رضایت انجام دهید.

## 2026-10-21 G1 partially observed — remaining focused gaps
[User reported G1-R0001](../06-tests-and-evidence/logs/G1-R0001-20261021.md) verified Windows 11 Pro build 26300, OS visible 5.88GiB and available 1.73GiB in one timestamp-less snapshot; Jan Start entry present but two guessed exe paths absent. **Still UNKNOWN**: Jan shortcut target/exe version, whether its UI/tool approval/Shell settings are accessible or safe, genuine ChatGPT Desktop build and whether user's **Plus** ordinary conversation has an MCP servers option; Cherry install outside narrow paths. GPU and RAM installed hardware historical state not invalidated by mislabeled Win32_ComputerSystem `TotalPhysicalMemory` output. Avoid full D0 rerun or any model/Agent start just to resolve them.

## Jan G1 shortcut location found, version pending (2026-10-21)

Visual user screenshot confirms Start shortcut `Jan` → `%LOCALAPPDATA%\Programs\Jan\Jan-Desktop.exe`. Earlier `Jan.exe` probe used **wrong filename**. **Still to verify by read-only GUI:** whether the target `Jan-Desktop.exe` actually exists, its **Product/File version** from executable Properties → Details, and later existing Jan MCP/Shell/Allow All settings only when safely visible without starting model/Agent. ChatGPT Plus MCP feature remains unobserved. No path containing Windows account name stored. [G1-R0001](../06-tests-and-evidence/logs/G1-R0001-20261021.md).

## 2026-10-23 — Bifrost download/integrity and actual use gates
- [x] Win64 confirmed; Node.js v24.22.1 CLI confirmed by user.
- [x] Cached Bifrost `.exe-0` has MZ/PE/AMD64/PE32+ header **but is only 57,943 bytes vs 134,305,792 official advertised bytes**. **STOP rename-only ZIP**; not executable-ready.
- [ ] Get complete official native Windows/AMD64 Bifrost transport and verify file length plus publisher digest/signature when available.
- [ ] Confirm loopback `127.0.0.1:18080` health and admin authentication with NEW token (previous token exposed).
- [ ] Independently verify actual Groq Free account tier/no billable fallback and single model; then first real call.
- [ ] Jan-to-Bifrost actual Persian chat and Windows memory/CPU footprint; guard file access closed.
[Evidence](../06-tests-and-evidence/logs/WINDOWS-BIFROST-TRUNCATED-PE-20261023.md); [statistics](INSTALLATION-AND-DEPLOYMENT-STATISTICS-20261023.md).
