# KB-0005 — حافظه و دادهٔ ماندگار مستقل از مدل
- **Tags:** `database-first`, `markdown`, `JSONL`, `SQLite`, `FTS5`, `DuckDB`, `PostgreSQL`, `vector search`, `source of truth`, `durable state`.
- **Status:** CURATED-UNVERIFIED (2026-10-20)
**پایهٔ این مدخل:** [SRC-0001 — متن کامل پژوهش ارسالی کاربر](../inbox/SRC-0001-djmrn-assistant-architecture-research-20261020.md)، ۲۰ اکتبر ۲۰۲۶، ۶۰۷ خط. برچسب: `USER-SUPPLIED / CURATED-UNVERIFIED`؛ ادعاها و لینک‌های داخل منبع هنوز مستقلاً با مراجع اصلی/بنچمارک بررسی نشده‌اند. هیچ معماری، زبان یا فناوری بر اساس این مدخل انتخاب نشده است.

## مفهوم پیشنهادی (§6)
ذخیره/جست‌وجوی داده با فرآیند عادی نرم‌افزار و **خارج از حافظهٔ مکالمهٔ LLM** ممکن است. چهار چیز را یکی نگیرید:
- canonical source (مثلاً Notion پژوهش عمومی و Github کد/وضعیت همین پروژه)
- local reproducible knowledge projection / cache
- operational task state & idempotency ledger
- model analysis/chat memory.

## گزینه‌های منبع
Markdown/JSON/JSONL برای حجم کم؛ SQLite برای transactional local data و FTS؛ DuckDB برای تحلیل ستونی؛ PostgreSQL برای نیاز چندکاربره/بزرگ‌تر؛ Vector DB زمانی که retrieval معنایی ارزش واقعی دارد. **همه نامزدند و ترتیب اجباری نصب نیستند**.

## وضعیت شواهد/محدودیت‌ها
در منبع، FTS5 و توان SQLite مطرح‌اند؛ test تاریخی Python+SQLite synthetic در [دفتر آزمون پروژه](../../06-tests-and-evidence/TEST-REGISTER.md) وجود دارد ولی DB عملیاتی پروژهٔ جدید انتخاب نشده. WAL یک نویسندهٔ همزمان دارد؛ patch/version/concurrency/recovery را در زمان تصمیم مستقل بررسی کنید.
**Related:** [KB-0004](KB-0004-non-llm-nlp-persian.md)، [KB-0003](../workflow-agents-and-control/KB-0003-architecture-families.md).
**پیگیری:** پس از بازخوانی `Applied Capability Index` در Notion و جست‌وجوی رسمیِ روز، موارد نیازمند تأیید را مشخص کنید؛ آزمون واقعی صرفاً با مجوز جداگانه. ثبت اطلاعات دانشنامه‌ای مجوز نصب/تغییر سیستم نیست.
