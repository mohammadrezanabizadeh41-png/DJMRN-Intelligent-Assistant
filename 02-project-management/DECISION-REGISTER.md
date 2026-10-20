# Decision Register — فقط تصمیم‌های واقعی، نه فرض برندگان
| ID | موضوع | وضعیت | دلیل/منبع | نتیجه |
|---|---|---|---|---|
| D-001 | **یک مخزن خصوصی برای کل پروژه و Work exchange داخلی** | USER-REQUESTED / ADOPTED DOC-STRUCTURE 2026-10-20 | گفتگو و ضرورت بازیابی کامل | GitHub repo canonical project artifacts؛ Applied Bridge مستقل |
| D-002 | **Greenfield, tech-neutral** | USER DIRECTIVE | نصب‌های قبلی الزام نیستند | بعد از نیاز، انتخاب مستقل tool/model/lang |
| D-003 | **Free-first, no overage unknown** | USER DIRECTIVE | سیاست DJMRN | provider فعال‌سازی بدون verify/approval ممنوع |
| D-004 | **P0–P6 replacing compulsory old A–G execution** | PROPOSED / USER REVIEW PENDING | 02/ROADMAP | هنوز تصویب نشده، A–G historical |
| D-005 | انتخاب language/runtime/database/agent host/inference engine | **NOT DECIDED** | نیاز به نیازمندی و مقایسهٔ معتبر | NONE |
| D-006 | اولین کاربرد عملی و اولویت resource-host | **NOT FINAL** | سناریوهای A/B/C نامزد | User review |
| D-007 | استفاده از Notion به‌عنوان source research بیرونی و GitHub برای تمام اسناد پروژه | USER DIRECTIVE | پایداری windows/Work | research catalogs not duplicated wholesale |
| D-008 | ایجاد دانشنامهٔ اختصاصی در همان مخزن پروژه، مستقل از raw Work correspondence | USER DIRECTIVE / DOCUMENTATION DECISION 2026-10-20 | نیاز به بازیابی پژوهش و استفادهٔ معماری/ساخت از نتایج | [08-project-knowledge-base](../08-project-knowledge-base/README.md) با source/raw→verified KB→decision/test و تفکیک پژوهش از اجرا؛ بدون انتخاب فناوری |

| D-009 | ترتیب شروع پیاده‌سازی: capability-first، قرارداد حداقلی منابع، manager-first یا ready-host-first | **WA0001 VERIFIED / COORDINATOR PROPOSAL: THIN CONTRACT + CAPABILITY FIRST / USER APPROVAL PENDING** | [WQ0001](../04-work-research-bridge/requests/WQ0001.md)، [KB-0001..0009](../08-project-knowledge-base/INDEX.md)، Applied v0.48، A0010–A0012 | [coordinator review](../04-work-research-bridge/reviews/WQ0001.md) accepted report partially; [V0 proposal](PROPOSED-FIRST-MILESTONE.md). After explicit user approval record ADOPTED or alternative; no implementation authorized |

| D-010 | Work پژوهشی باید **نام کامل مخزن مقصد** را برای جلوگیری از ثبت در مخزن مشابه بررسی کند | **USER DIRECTIVE / ADOPTED DOCUMENTATION POLICY 2026-10-20** | کاربر: جلوگیری از اختلاط `mohammadrezanabizadeh41-png/DJMRN-Intelligent-Assistant` و `mohammadrezanabizadeh41-png/DJMRN-Research-Bridge` | [Repository Lock](../04-work-research-bridge/REPOSITORY-LOCK.md): full_name/URL/branch و WQ/WA قبل از write، بعد commit/readback؛ failure = BLOCKED، بدون fallback |

**قالب تصمیم آینده:** problem → options (including simpler) → official evidence/versions → security/cost/region → test results → rejected alternatives → decision owner/date → approved/not approved → as-built evidence → reversibility → effects on Notion governance. تغییر consequential معماری را در Notion canonical cross-project هم ثبت/لینک کنید و در این register مرجع immutable داشته باشید.
