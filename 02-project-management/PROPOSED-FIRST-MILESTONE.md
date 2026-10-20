# V0 — نخستین قابلیت پیشنهادی DJMRN (DRAFT, USER APPROVAL PENDING)

Date: 2026-10-20 | Sources: [WA0001](../04-work-research-bridge/responses/WA0001.md), [review](../04-work-research-bridge/reviews/WQ0001.md), [KB-0010](../08-project-knowledge-base/architecture/KB-0010-sequencing-thin-contract-first.md).

## Suggested deliverable
یک ابزار کم‌حجمِ **بدون Agent و LLM** که ۲–۳ فایل متنیِ محلی و غیرحساسِ تأییدشده را می‌خواند، اختلاف حروف فارسی و نیم‌فاصله را برای تطبیق جست‌وجو مدیریت می‌کند، فیلد یا عبارت درخواست‌شده را پیدا می‌کند و نتیجه را با **نام فایل و محل متن** گزارش می‌دهد. کاربرد مستقیمِ مقدماتی برای Research Curator / دانشنامه، نه ساخت یک پلتفرم کامل.

- **Input:** only user-approved synthetic or non-sensitive TXT/MD/CSV/JSON files (agree on exact subset before construction).
- **Read-only:** originals untouched; output/log separated from sources; no account, browsing, cloud, email, unattended processing or remote execution.
- **Lightweight conceptual contract:** `task_id`, `capability`, `input_ref`, `permission_scope`, `result_ref`, `status`, `receipt`, `error`; process ownership and cancellation if needed. No DB/queue/daemon/API gateway mandated yet.
- **Acceptance on paper:** given fixed Persian variants `ی/ي`, `ک/ك`, ZWNJ and digit forms, report correct exact file+line references and clearly indicate misses/errors; rerunning returns consistent output; all input bytes unchanged; no unapproved path accesses.
- **Stop & rollback:** if source altered, citation incorrect, path unsafe, memory causes foreground problems or required permission missing, stop and report; remove output and code if separately approved. No actual test has been run.

## Explicit decision gates
1. User accepts/changes proposed *sequence* for `D-009`.
2. User chooses the actual first capability/use case (this V0 vs another), fixture and pass criteria.
3. User explicitly authorizes code creation, local execution and any file access/download/install **separately**.
4. Choose the smallest adequate implementation approach on merits (ready Windows tools or a code language); installation history is not an architecture vote.

**Current state: proposal only, no software, build or test.** The later manager decision is triggered by measured concurrent-heavy-work RAM admission, model lease/unload, durable unattended recovery, safe process ownership or required cross-machine runtime.
