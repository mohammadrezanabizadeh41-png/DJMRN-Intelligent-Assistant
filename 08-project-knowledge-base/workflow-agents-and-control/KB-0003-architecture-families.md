# KB-0003 — هفت خانوادهٔ معماری از Rule-Based تا Agent Worker
- **Tags:** `rule-based`, `data-centric`, `modular monolith`, `event-driven`, `classical ML`, `LLM-on-demand`, `agent worker`, `workflow`.
- **Status:** CURATED-UNVERIFIED (2026-10-20)
**پایهٔ این مدخل:** [SRC-0001 — متن کامل پژوهش ارسالی کاربر](../inbox/SRC-0001-djmrn-assistant-architecture-research-20261020.md)، ۲۰ اکتبر ۲۰۲۶، ۶۰۷ خط. برچسب: `USER-SUPPLIED / CURATED-UNVERIFIED`؛ ادعاها و لینک‌های داخل منبع هنوز مستقلاً با مراجع اصلی/بنچمارک بررسی نشده‌اند. هیچ معماری، زبان یا فناوری بر اساس این مدخل انتخاب نشده است.

## طبقه‌بندی دقیق منبع (§4)
- **A — Rule-Based Automation:** رویداد → شرط ثابت → عمل ثابت؛ بدون نیاز ذاتی LLM.
- **B — Data-Centric/Database-First:** داده/سوابق مرکزی، مدل فقط ابزار تحلیل اختیاری.
- **C — Modular Monolith/Capability-Based:** قابلیت‌های جدا و قراردادهای روشن در یک برنامه؛ سرویس مستقل فقط در صورت اثبات نیاز.
- **D — Event-Driven/Workflow:** رویداد آغازگر؛ state/retry/recovery باید مستقل طراحی/از محصول آماده تأمین شود.
- **E — Classical ML + Deterministic:** مدل طبقه‌بندی کوچک و controller عادی بدون chatbot.
- **F — Hybrid AI/LLM-on-Demand:** مسیر عادی deterministic؛ در ابهام از local/remote LLM درخواست؛ structured output validate.
- **G — Agent as Supervisor/Worker:** نقش محدود Agent؛ policy/approval خارج از prompt.

**مهم:** این A–G **طبقه‌بندی معماری داخل منبع** است و با **A–G تاریخی نقشه راه ویندوز پروژه** یکسان نیست؛ شناسهٔ آن‌ها را اشتباه نگیرید.

## فرضیهٔ ترکیبی
B + C + D + F در متن یک ترکیب ممکن معرفی شده، نه برنده. حتی B+C+D+F می‌تواند برای نخستین نیاز over-engineering باشد. باید حداقل معماری هم‌سطح نیاز را با ready products مقایسه کرد.

## مسیر اعتبارسنجی
برای یک event یکسان: شروع/توقف، ذخیره state، duplicate/retry, approval boundary، cold-start RAM، نتیجهٔ واقعی. Work لازم نیست همه گزینه‌ها را «منتخب» بنامد.
**Related:** [KB-0001](../architecture/KB-0001-capability-first-hybrid.md)، [KB-0008](../architecture/KB-0008-three-build-bundles.md)، [KB-0006](../hardware-and-performance/KB-0006-local-memory-budget.md).
**پیگیری:** پس از بازخوانی `Applied Capability Index` در Notion و جست‌وجوی رسمیِ روز، موارد نیازمند تأیید را مشخص کنید؛ آزمون واقعی صرفاً با مجوز جداگانه. ثبت اطلاعات دانشنامه‌ای مجوز نصب/تغییر سیستم نیست.

## 2026-10-21 User future research supplements — NOT KB claims
- [SRC-0009](../inbox/SRC-0009-ruflo-multi-agent-orchestration-future-20261021.md): Ruflo/swarm/coordinator, OpenAI Agents SDK, Microsoft Agent Framework, Google ADK, AutoGen, CrewAI, LangGraph and ready visual workflow suites are **different product families**. This is **RAW USER RESEARCH** extending [REQ-MPA-001](../../02-project-management/MULTI-PERSONA-SPECIALIST-ASSISTANTS-REQUIREMENT.md), not new verified KB claims, required runtime or mandate to implement multi-agent now. Prefer lean coordinator + fixed tools and add autonomous agents only if factual usefulness follows a bounded test.
- [SRC-0010](../inbox/SRC-0010-hybrid-inference-plane-multi-engine-model-routing-future-20261021.md) adds a **distinct inference router/model lifecycle** category to research, linked to [INF-001](../../03-architecture-and-tools/FUTURE-INFERENCE-PLANE-RESEARCH-REQUIREMENT.md), not an eighth existing architecture family or selected gateway. Local first-on-demand, remote with legal/free/privacy gates, no RAM assertions without test.
- Original KB-0003 status **CURATED-UNVERIFIED** and its A–G family classification remain intact.
