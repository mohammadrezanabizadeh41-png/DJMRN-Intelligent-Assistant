# Task Register — canonical status of tasks, v0.1
**این فایل دفتر وظایف پروژه است؛ CURRENT-STATUS تنها خلاصهٔ وضعیت و نقطهٔ ادامه است.** هر task `TASK-####` مستقل از WQ/WA research ID است. شناسهٔ جدید بر اساس بیشینهٔ شناسهٔ ثبت‌شده و بازخوانی repo تخصیص می‌یابد؛ هیچ شماره‌ای حذف یا دوباره استفاده نشود.

| ID | کار | وضعیت | شواهد/پیش‌نیاز | بعدی |
|---|---|---|---|---|
| TASK-0001 | ساخت private GitHub repo | DONE USER / VERIFIED CONNECTOR | GitHub repository + main README fetched 2026-10-20 | نگهداری |
| TASK-0002 | ساخت ساختار و قوانین self-contained | DONE / VERIFIED 2026-10-20 | 45 blob files + 14 core file readbacks; bootstrap commit [6b9cee93](https://github.com/mohammadrezanabizadeh41-png/DJMRN-Intelligent-Assistant/commit/6b9cee93db61b515574834e627b41648aa908dbf) | نگهداری/اصلاح با ثبت شاهد |
| TASK-0003 | انتقال تاریخچهٔ دستگاه/نرم‌افزار/تست | HISTORICAL INVENTORY DOCUMENTED / GAPS TAGGED | 01 and 06, original Notion Journal | gap review only, no full D0 |
| TASK-0004 | تبادل T0001 برای Work در repo جدید | **DONE / VERIFIED 2026-10-20** | [response](../04-work-research-bridge/responses/T0001.md), [commit](https://github.com/mohammadrezanabizadeh41-png/DJMRN-Intelligent-Assistant/commit/d70a9a406a7057a7b40e11ad99e70d2574536e5c), blob `8094f76e732305fcc8d22a48639cb0e347325874` | No repeat; prepare bounded WQ0001 only when justified |
| TASK-0005 | تأیید نقشهٔ P0–P6 و use case نخست | PENDING USER REVIEW | ROADMAP, REQUIREMENTS | پرسش کاربردی و acceptance |
| TASK-0006 | پژوهش هدفمند مقایسهٔ معماری | NOT STARTED IN THIS REPO | TASK-0004 PASS; first real WQ0001 after task/scope confirmation | هدف و فیلتر پژوهش |
| TASK-0007 | انتخاب حداقل stack/تست | NOT AUTHORIZED | نتیجهٔ 0006، consent | NONE |
| TASK-0008 | توسعهٔ اولین قابلیت واقعی | NOT AUTHORIZED | تصویب P3، real I/O | NONE |
| TASK-0009 | ساخت دانشنامهٔ پروژه با INDEX/SRC/KB/protocol و موضوعات | DONE / VERIFIED GITHUB READBACK 2026-10-20 | [08-project-knowledge-base](../08-project-knowledge-base/README.md)، [initial commit afbe4f4](https://github.com/mohammadrezanabizadeh41-png/DJMRN-Intelligent-Assistant/commit/afbe4f48f8a3ee79177500b1db3bf24a3626994b)، main tree 64/64 blobs | نخستین پژوهش کاربر در TASK-0010 وارد شد؛ توسعهٔ پایگاه ادامه دارد |

| TASK-0010 | ورود پژوهش قبلی معماری و استخراج دانشی بدون انتخاب stack | **DONE / SOURCE & KB VERIFIED IN GITHUB 2026-10-20** | [SRC-0001](../08-project-knowledge-base/inbox/SRC-0001-djmrn-assistant-architecture-research-20261020.md), [INDEX KB-0001..0009](../08-project-knowledge-base/INDEX.md)؛ raw 607 lines / 41,901 bytes / SHA256 `1ce5db388e76f01d222753ac9cad09073be918a39c7c827947815869a664582f` / Git blob `6e1fcf18ce4cc86f4c52f70107e434d639b6d9da` **MATCHED** | بررسی منابع رسمی و gapها در زمان پژوهش؛ WQ0001 هنوز صادر نشده |

**در هر تغییر:** وضعیت، خطا، لینک output/commit، source/observed date، وابستگی، مالک، next action؛ sync CURRENT-STATUS. هیچ task صرفاً به خاطر ساخت فایل DONE اجرایی نمی‌شود.
