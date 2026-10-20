# HANDOFF — شروع در گفتگوی تازه یا برای دستیار دیگری

## متن کوتاه قابل ارسال در گفتگو
«پروژهٔ DJMRN Intelligent Assistant System را از مخزن خصوصی `mohammadrezanabizadeh41-png/DJMRN-Intelligent-Assistant` ادامه بده. ابتدا README.md، PROJECT-RULES.md، 07-operations-and-continuity/CURRENT-STATUS.md، 02-project-management/TASK-REGISTER.md، 01-system-inventory/، 08-project-knowledge-base/INDEX.md و پروتکل 04-work-research-bridge/README.md را واقعاً از GitHub بخوان. همهٔ وضعیت‌ها را بر اساس ثبت زنده و شواهد بخوان؛ هیچ معماری/نصب/اجرای Work را فرض نکن. قبل از تصمیم نیازمحور کتابخانهٔ Applied در Notion و منابع رسمی تازه را بررسی کن. آخرین وضعیت/شناسهٔ research ledger را بخوان و از اقدام ناتمام ادامه بده.»

## دستورالعمل برای خود دستیار
1. Read **real GitHub** (not a cached chat snippet); verify repository visibility, main HEAD and this file. If inaccessible → BLOCKED and ask for access/link, no guessing.
2. Read PROJECT-RULES / CURRENT / TASK-REGISTER / DECISION-REGISTER / relevant subject docs. Reconcile last commit SHA, historical vs current, provenance. This repo should be self-contained for project objectives, current progress and procedures.
3. Research needed? First read **08-project-knowledge-base/INDEX.md, SOURCE-REGISTER.md and relevant KB entries** to reuse project-specific knowledge; then exact Applied Library / General as source catalogs if relevant; only if a gap remains use project Work protocol/LEDGER; compare current official sources, do not blindly ask Work broad repetitions; allocate next ID only after checking actual files.
4. Distinguish `USER-REPORTED TEST PASS` from source-tested tool behavior and real deployment. Software installed historically has no ranking bonus.
5. Each finished substantive action: create actual artifact/commit, fetch readback, log evidence, update task register and CURRENT with next step. If important architecture decision approved, link/update global Notion rationale as required by governance.
6. On errors, report path/step/source exactly, do not issue fictitious commit/SHA or mark unverified DONE.
7. Sensitive secrets and private customer data never go into GitHub, even if private. Work is research-only until user expressly authorizes other effects.

## How to brief Work
«مخزن `mohammadrezanabizadeh41-png/DJMRN-Intelligent-Assistant`، `04-work-research-bridge/README.md` و درخواست `04-work-research-bridge/requests/[EXACT-ID].md` را از GitHub بخوان، فقط پاسخ متناظر را در `responses/` ثبت و بازخوانی کن.» بدون فایل درخواست واقعی هرگز ID حدسی نسازید.

## پروندهٔ اصلی برای مخاطب انسانی
[README](https://github.com/mohammadrezanabizadeh41-png/DJMRN-Intelligent-Assistant/blob/main/README.md) → [CURRENT](https://github.com/mohammadrezanabizadeh41-png/DJMRN-Intelligent-Assistant/blob/main/07-operations-and-continuity/CURRENT-STATUS.md) → [Work bridge](https://github.com/mohammadrezanabizadeh41-png/DJMRN-Intelligent-Assistant/blob/main/04-work-research-bridge/README.md).

## Guard against confusing Work GitHub repositories — D-010
در همهٔ پیام‌های Work از **نام کامل** `mohammadrezanabizadeh41-png/DJMRN-Intelligent-Assistant` و URL `https://github.com/mohammadrezanabizadeh41-png/DJMRN-Intelligent-Assistant` با branch `main` و exact paths استفاده کنید؛ نه عبارت کوتاه «مخزن DJMRN». Work اول [REPOSITORY-LOCK](../04-work-research-bridge/REPOSITORY-LOCK.md) را بخواند، live repo `full_name` را بسنجد و فقط در `responses/WA####.md` در **همان** repo Commit و readback کند. `mohammadrezanabizadeh41-png/DJMRN-Research-Bridge` فقط input read-only است. اگر اشتباه/ابهام = BLOCKED، بدون نوشتن در مخزن دیگر.

### نمونهٔ دستور آماده (شناسه‌ها فقط بعد از ثبت WQ واقعی جایگزین شوند)
«تنها مخزن مقصد برای این کار **`mohammadrezanabizadeh41-png/DJMRN-Intelligent-Assistant`** به آدرس **https://github.com/mohammadrezanabizadeh41-png/DJMRN-Intelligent-Assistant** و شاخهٔ **`main`** است. ابتدا هویت مخزن `full_name` را از GitHub بررسی کن؛ سپس `04-work-research-bridge/REPOSITORY-LOCK.md` و `README.md` همان بخش و درخواست **`requests/WQ####.md`** را بخوان. فقط پاسخ **`responses/WA####.md`** را در **همین repo** ثبت کن، Commit بزن، از همین repo بازخوانی کن و **repository_full_name، commit، blob و نتیجهٔ readback** را اعلام کن. مخزن `mohammadrezanabizadeh41-png/DJMRN-Research-Bridge` مقصد نیست؛ اگر هویت مخزن/دسترسی تأیید نشد، توقف و BLOCKED. هیچ تغییر دیگری مجاز نیست.»

## Newest V0 step — user-approved but not Windows-tested (2026-10-20)
- [D-009/D-011/D-012](../02-project-management/V0-BUILD-DECISION.md): sequence adopted: thin task contract → small no-Agent capability; resource controller only on observed triggers. Python stdlib is **scoped to CAP-006**.
- [CAP-006 source/usage](../05-assistants-and-capabilities/src/document_search_v0/README.md) and [16-test synthetic receipt](../06-tests-and-evidence/logs/NEW-V0001-20261020.md). Checked code/fixture SHA identity; no Windows local smoke, no private source use. Do not ask user to rebuild from scratch or rerun all system inventories.
- Ask for separate explicit authorization before any on-device code execution or installation; if approved, start only with bundled synthetic fixtures. Preserve [Work Repository Lock](../04-work-research-bridge/REPOSITORY-LOCK.md) for future Work tasks.
