# نقشهٔ راه بازتعریف‌شده — Proposed P0–P6 | 2026-10-20
**وضعیت: PROPOSAL برای ترتیب اجرا؛ نه انتخاب معماری/stack.** نقشهٔ قدیمی A–G در [Notion original](https://app.notion.com/p/3fcc8c684690813a82b3d0ce909534e3) حفظ شده و تاریخچهٔ عملی آن حذف نمی‌شود.

## ترجمهٔ نقشهٔ قدیمی A–G
- A: فهرست دستگاه و نصب‌ها؛ بخش بزرگی از hardware/RAM/system و چند CLI **قبلاً مستند**؛ inventory live و کل تکمیل مدل‌ها **ناقص**.
- B: جست‌وجو، مقایسهٔ محصولات و معماری‌ها؛ **بسیاری از گزارش‌های کتابخانه/Work وجود دارند ولی هیچ winner پروژهٔ جدید تصویب نشده**.
- C: engine/model validation؛ **basic API/inference و چند خطای تاریخی واقعی** ثبت؛ benchmark منصفانهٔ full-stack انجام‌نشده.
- D: نخستین assistant؛ Jan محدود file read مشاهده شده و P1-A synthetic deterministic PASS کاربر گزارش داده؛ **دستیار عملی یکپارچه کامل نشده**.
- E: memory/search/Notion integration؛ **پیشنهاد و پژوهش، نه یک ماژول عملی پذیرفته‌شده**.
- F: specialist collaboration؛ **هنوز هیچ همکاری Agent عملی اثبات نشده**.
- G: stable daily service؛ **انجام‌نشده**.

## مسیر پیشنهادی جدید — deliverable-based
| Phase | خروجی واقعی | گیت خروج |
|---|---|---|
| **P0 — PROJECT FOUNDATION** | مخزن خصوصی با full rules, device history, model/tool inventory, source links, CURRENT, task index, Work exchange protocol | GitHub file/commit readback PASS؛ gaps برچسب دارند |
| **P1 — USE CASE & ACCEPTANCE** | تعریف یک کار کوچک واقعی با ورودی/خروجی، consent و خروجی قابل سنجش | کاربر اولویت/حدود را تأیید کند |
| **P2 — OPTIONS RESEARCH** | بر اساس Applied/General + official live + Work گزارش رقابتی same-role options و failure modes | source, license, free/cost/region/security, alternative quality مشخص |
| **P3 — IMPLEMENTATION DECISION** | حداقل stack قابل تست؛ deterministic baseline و ready product/agent/hybrid comparison؛ rollback/BOM | تصویب محدودهٔ نصب/تست، نه پذیرش کور معماری |
| **P4 — SMALLEST WORKING VERTICAL** | real I/O, correct state, bounded permissions, failure recovery, performance observation، log/metrics | آزمون واقعی روی workload مجاز، not only synthetic |
| **P5 — INCREMENTAL EXPANSION** | فقط نیازهای ثابت‌شده: knowledge, source citations, tool interfaces, specialist capabilities | هر capability جداگانه acceptance دارد |
| **P6 — DAILY OPERATION** | resource-aware lifecycle, resume/recovery, backups, maintenance and observed costs | usable/durable support + simple rollback |

Cross-cutting: امنیت، observability، cost gates و tests از P0/P1 مطرح می‌شوند؛ P6 به معنی تعویق امنیت نیست. کار پژوهش Work بخشی از P2 و حتی P4 در صورت نیاز است، نه یک پروژهٔ research بی‌پایان.

**پیشرفت واقعی 2026-10-20:** نخستین قابلیت کوچک CAP-006 (جست‌وجوی خطیِ فقط‌خواندنی با منبع) با تأیید کاربر انتخاب و کد آن ثبت شد؛ 16 آزمون ساختگیِ خارج از دستگاه موفق‌اند. طبق D-009 قرارداد سبک پیش از ساخت مدیر مرکزی انتخاب شد. **اجرای smoke ساختگی روی Windows اکنون توسط کاربر مجاز است اما هنوز نتیجه ندارد.** نقشهٔ گستردهٔ P0–P6 همچنان پیشنهاد کلی است، نه الزام stack یا وعدهٔ اجرای همهٔ مراحل. برای ادامه [Snapshot](../07-operations-and-continuity/PROJECT-STATE-HANDOFF-20261020.md).


## Future cross-cutting capability — Live Observability Map
نیاز کاربر برای یک **نقشهٔ زندهٔ کم‌مصرف** از اجزا و ارتباطات سیستم ثبت شد: [REQ-OBS-001](LIVE-OBSERVABILITY-MAP-REQUIREMENT.md). این capability باید از P4 به بعد همراه با real I/O تکامل یابد، ولی provider/stack آن هنوز انتخاب نشده است. اولویت فعلی cloud-first/direct-OTLP برای کمینه‌کردن RAM محلی است؛ local all-in-one فقط پس از benchmark. این requirement مسیر فعلی CAP-006 را متوقف یا جابه‌جا نمی‌کند.

## Future requirement — Logical Specialized Assistants / Persona Profiles (REQ-MPA-001)
- [REQ-MPA-001](MULTI-PERSONA-SPECIALIST-ASSISTANTS-REQUIREMENT.md), original [SRC-0004](../08-project-knowledge-base/inbox/SRC-0004-djmrn-multi-persona-logical-assistants-future-20261020.md) and future `TASK-0014` preserve the user's full concept. This **does not change the approved first vertical or P0–P6 proposed sequence**.
- Keep future contracts extensible for identity/role, explicitly scoped knowledge/skills/tools, permissions, output validation, model-agnostic profile execution, independent durable state and traces. Reuse one shared/on-demand engine if suitable; no mandatory resident Agent/process per persona.
- **Trigger:** after user requests prioritization or a real use case justifies it. Future research must compare ready-made cloud/local workflow+persona platforms with light custom alternatives, official Free-First/cost/region/security and Windows RAM tests; only then propose a minimal pilot with consent. No choice, signup, install, model download or implementation now.

## Deferred future product requirement — Technology Discovery Radar / Innovation Intelligence (REQ-TDR-001)
- [REQ-TDR-001](TECHNOLOGY-DISCOVERY-RADAR-REQUIREMENT.md) / [full original SRC-0005](../08-project-knowledge-base/inbox/SRC-0005-djmrn-technology-discovery-innovation-radar-future-20261020.md) / `TASK-0015` preserve the user's 65-section requirement; this is **not a change of current approved milestones or a provider/architecture decision**.
- Distinguish broad discovery and watchlist from verified Research Curator/CAP-004; reuse Applied/General evidence library and taxonomy, no parallel research authority. Desired path: authorized source APIs/RSS → deterministic normalized/dedup → independent official verification → relevant shortlisting → optional AI ideation/opportunity review → low-noise digest/watchlist → curated existing knowledge store.
- Local Python/Task Scheduler, cloud serverless, scheduled GitHub Actions, ready-made workflow platforms and hybrid are **future comparative families**, not adopted. Laptop is 8GiB RAM and not always-on; free/card/overage/region/privacy gates before any future cloud use.
- Future incremental MVP hypothesis: 2–3 trusted feeds such as GitHub, Hugging Face and Hacker News, no Agent/vector DB, bounded daily digest; **pilot not authorized now**. No live monitor, automation, scheduled work, software installation or Windows/cloud action initiated.

## CORE USER CLARIFICATION — Chat-first assistant integration rather than end-user PowerShell (2026-10-21)
- [REQ-012](CHAT-FIRST-ASSISTANT-INTERACTION-REQUIREMENT.md) / [D-014](DECISION-REGISTER.md): **daily product UX = user sends a message and collaborates with assistants/authorized Agents**. Local PowerShell is an **internal tool or a test harness only**, not a satisfactory normal control interface. B (data/CSV) and C (source research) remain planned **complementary capability classes** to A (documents), and may be invoked together in one conversational workflow; they are not forced sequential test choices or CLI apps the user must run.
- This makes the next practical gate **P4 real end-to-end conversational vertical**, not another raw lookup test: message → scoped intent → permission check → actual CAP-006 tool invocation on authorized file(s) → source-backed Persian explanation with honest limitations, all initiated **without user issuing shell commands each time**. Keep technical evidence [NEW-V0004](../06-tests-and-evidence/logs/NEW-V0004-20261021.md) (two-file PASS); it establishes just the underlying deterministic tool, not the assistant interface.
- [TASK-0017](TASK-REGISTER.md): technology-neutral comparison of local chat interface/ready assistant host/hybrid ChatGPT-connected tool bridge and safe execution permissions; determine exact missing bridge, model/agent necessity, RAM/privacy/region/cost, then request user approval for minimal reversible implementation. Planning for future automation, job management and specialist Agents should preserve extensibility, **but does not mean building them all up-front**.
- After conversational A works, add B and C under same interface when a use case warrants and user authorizes. Later pursue durable/scheduled resource management and specialist/Agent coordination based on evidence. **No runtime/vendor/GUI/cloud connection selected or installed by this clarification.**
