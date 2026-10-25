# گزارش آزمون نهایی — 2026-10-25

فایل اجرایی: `Test-DJMRN-OmniRoute-Provider-Gate-v3.ps1`

SHA256: `415033d5e9148f867f08f5d7c72eb79c3e4ff6b04d9cdc868e5fa5f868854fa8`

نتیجه: PASS در محیط Linux / PowerShell 7.4.6، .NET 8.

- آزمون داخلی: 52 assertion، همگی PASS.
- بررسی یکپارچه: 42 مورد، همگی PASS؛ شامل اجرای کامل transport مصنوعی، ۳۷۵ شناسه، ۱۲ خروجی، عدم افشای sentinel، توقف/ادامه، checkpoint backup، ورودی خراب و Export از v2/v3.
- Parser PowerShell 7: PASS؛ C# با language version 5: PASS.
- تعداد درخواست واقعی شبکه از اسکریپت و harness در آزمون‌ها: صفر.
- Windows PowerShell 5.1 Parser/runtime و .NET Framework واقعی: NOT_RUN.
- اجرای معمولی بدون Administrator روی Windows: NOT_RUN؛ کد دسترسی elevated درخواست نمی‌کند.
- DNS/TCP/TLS/reset/قطع اینترنت واقعی، trust store Windows، IPv6 و اینترنت کاربر: NOT_RUN.
- injection خطای .NET و transport ساختگی، شاهد اختلال واقعی شبکه نیستند.
- Ctrl+C/قطع برق واقعی: NOT_RUN؛ interruption مصنوعی و بازیابی storage آزموده شده است.

نتایج تک‌به‌تک در VALIDATION-RESULTS.json است. نمونه‌های پوشه SYNTHETIC-SAMPLE-OUTPUT کاملاً ساختگی‌اند؛ از آن‌ها هیچ نتیجه‌ای دربارهٔ اینترنت ایران، Providerهای قابل استفاده یا تعداد صف واقعی کاربر استخراج نکنید.
