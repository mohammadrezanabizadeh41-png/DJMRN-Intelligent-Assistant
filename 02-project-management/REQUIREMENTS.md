# نیازهای پروژه / معیار قبول — اولیه، قابل اصلاح
| ID | خواسته | معیار اثبات و Status |
|---|---|---|
| REQ-001 | کار فارسی و برنامهٔ مناسب Windows 11، Ryzen3500U، 8GB RAM | ورودی فارسی به خروجی مستند با real I/O، اندازه‌گیری منابع / PROPOSED |
| REQ-002 | گزینه‌های remote رایگان و local/hybrid | بررسی رسمی quota/card/region/overage/legal/privacy و fallback / PROPOSED |
| REQ-003 | منبع پروژه قابل بازیابی مستقل از چت | README→CURRENT→inventory→source/tests/work logs با GitHub live readback / IN PROGRESS |
| REQ-004 | سؤال/پاسخ پژوهشی کامل Work در همین repo | T0001 PASS و WA0001/Review VERIFIED (ACCEPTED-PARTIAL due to internal SHA mismatch)؛ پژوهش ترتیب شروع انجام شده |
| REQ-005 | منابع دانش و سرچ هدفمند | Applied + General + official fresh search + independent Work و source citations / PROPOSED |
| REQ-006 | مدیریت مصرف/فرایند و قابلیت توقف | manager-native vs minimal-controller comparison + bounded test / RESEARCH |
| REQ-007 | مجوز حساس انسانی | قبل از email/site post, file edit, delete, payment, account change / POLICY |
| REQ-008 | پیگیری دقیق what done/failed/next | ID, artifact, evidence, reviewer, stop reason, recovery / IN PROGRESS |
| REQ-009 | توسعهٔ ماژولار و قابل تعویض، بدون stack bias | نقش engine/model/host/worker/state جدا و با معیار مشترک مقایسه / PROPOSED |
| REQ-010 | حذف دوباره‌کاری در diagnostics/research | خواندن شواهد پیشین و ثبت gap واقعی، سپس فقط آزمون ضروری / POLICY |

| REQ-011 | CAP-006 V0 جست‌وجوی فارسی فقط‌خواندنی و منشأدار | 16 synthetic tests in isolated assistant container PASS؛ Windows/real workload NOT TESTED؛ [scope](V0-BUILD-DECISION.md) |

| REQ-012 | **Chat-first / Message-driven assistants**: کاربر فقط با پیام، نظارت و همکاری با دستیار/Agent تعامل می‌کند؛ نه استفادهٔ دوره‌ای از PowerShell و CLI؛ دستیار باید A (اسناد)، B (داده)، C (پژوهش) را پشت صحنه با ابزارهای دارای مجوز و شواهد اجرا/ترکیب کند | **CORE USER DIRECTIVE / REQUIREMENT CONFIRMED, INTEGRATION UNBUILT**؛ [spec](CHAT-FIRST-ASSISTANT-INTERACTION-REQUIREMENT.md)، [D-014](DECISION-REGISTER.md)، [task](TASK-REGISTER.md). معیار گیت: یک پیام فارسی → فراخوانی واقعی محدود CAP-006 بدون دستور دستی هر بار → پاسخ منبع‌دار و رفتار permission/FAIL درست؛ انتخاب runtime/رابط و approval ساخت جدا. چند Agent دائمی الزام نیست |

هر نیاز جدید فقط با use case مشخص، معیار قبول و اولویت وارد شود. Unknown ≠ Failed؛ reported PASS ≠ independently verified production.
