# KB-0007 — پیش از ساخت اختصاصی، ابزارهای آمادهٔ Workflow را بررسی کن
- **Tags:** `Task Scheduler`, `Power Automate Desktop`, `n8n`, `Activepieces`, `Playwright`, `ONNX Runtime`, `ready-made`, `workflow`.
- **Status:** CURATED-UNVERIFIED (2026-10-20)
**پایهٔ این مدخل:** [SRC-0001 — متن کامل پژوهش ارسالی کاربر](../inbox/SRC-0001-djmrn-assistant-architecture-research-20261020.md)، ۲۰ اکتبر ۲۰۲۶، ۶۰۷ خط. برچسب: `USER-SUPPLIED / CURATED-UNVERIFIED`؛ ادعاها و لینک‌های داخل منبع هنوز مستقلاً با مراجع اصلی/بنچمارک بررسی نشده‌اند. هیچ معماری، زبان یا فناوری بر اساس این مدخل انتخاب نشده است.

## نامزدها و نقش ادعاشده (§9)
- Windows Task Scheduler: شروع کار با زمان/event؛ state business چندمرحله‌ای مستقل.
- Power Automate Desktop: RPA محلی با حضور کاربر؛ **unattended licensing and resource requirements** در متن ادعا شده و برای تصمیم باید مستند رسمی نسخهٔ روز بررسی شود.
- n8n: workflow integrations؛ خودمیزبان Community و محدودیت Sustainable Use License طبق متن؛ **free ≠ open-source unrestricted**.
- Activepieces: self-host low-code؛ متن از MIT برای core و تفکیک enterprise/cloud یاد می‌کند؛ release/license/feature امروز نیازمند تأیید.
- Playwright: browser automation در سناریوی مجاز؛ browser RAM footprint مستقل.
- ONNX Runtime: مدل ML بدون Agent؛ وزن مدل و task quality جداگانه.

## معیار اصلی پژوهش
در برابر minimal script + Task Scheduler، هزینهٔ نصب/idle RAM/ports/background services, account permissions, recovery state, retry/idempotency, license/commercial terms, free quota/card/overage/Iran/legal و نگهداری هر محصول را در همان کاربرد واقعی بسنجید.

**هیچ‌کدام از سرویس‌ها روی laptop جدید نصب/فعال نشده‌اند و هیچ قیمت/قانونی از این منبع به‌عنوان وضعیت کنونی تأیید نشده است.**
**Related:** [KB-0008](../architecture/KB-0008-three-build-bundles.md)، [KB-0002](../build-and-implementation/KB-0002-language-runtime-role-matrix.md).
**پیگیری:** پس از بازخوانی `Applied Capability Index` در Notion و جست‌وجوی رسمیِ روز، موارد نیازمند تأیید را مشخص کنید؛ آزمون واقعی صرفاً با مجوز جداگانه. ثبت اطلاعات دانشنامه‌ای مجوز نصب/تغییر سیستم نیست.

## 2026-10-21 — Reuse-before-build **SOURCE** distinct from product/runtime choice
- [SRC-0011: complete user 885-line source](../inbox/SRC-0011-n8n-workflows-template-library-reuse-discovery-20261021.md) introduces **workflow template reuse patterns**, not a recommendation to install n8n; [independently reviewed dossier](SRC-0011-WORKFLOW-LIBRARY-EVALUATION-20261021.md) and [REQ-WFR-001](../../02-project-management/WORKFLOW-PATTERN-DISCOVERY-REUSE-REQUIREMENT.md) / TASK-0019 own the future task→template search and safe adaptation. This extends KB-0007 and does **not** create duplicate KB article or replace its historical CURATED-UNVERIFIED vendor content.
- Current upstream [Zie619/n8n-workflows](https://github.com/Zie619/n8n-workflows) main `94007c1445d9258a7da116646b79473e7c7c3282`: real public, unarchived **MIT collection repository**, Git-tree **2,061 tracked workflow JSONs**; README **claims 4,343** workflows, 365 integrations, 29,445 nodes, `100% Import` and `<50MB` (NOT verified as same corpus/current laptop benchmark). Three actual JSON examples included Code+GitHub/HTTP, RSS+Gmail/Jira, and `ExecuteCommand`+Webhook+Mailgun; imports/code/external APIs must remain separately reviewed and unapproved. Repo MIT ≠ n8n fair-code engine or paid service rights.
- **Current verdict:** source as **DISCOVERY/REFERENCE/INSPIRATION CANDIDATE = YES, conditionally**; **RUNTIME/WORKFLOW/Security authority = NO**. The safe initial approach when user needs an automation is **online/GitHub read-only selective retrieval of up to three candidates**, no local clone or n8n server on RAM-constrained Windows. Compare official [n8n templates](https://n8n.io/workflows/), [Activepieces Template Library](https://www.activepieces.com/docs/flows/template-library), [Node-RED Flow Library](https://flows.nodered.org/). Actual need/time savings remain unproven, to be checked later.
- [REQ-TDR-001](../../02-project-management/TECHNOLOGY-DISCOVERY-RADAR-REQUIREMENT.md) owns future **new source/change signal** monitoring; [REQ-WFR-001](../../02-project-management/WORKFLOW-PATTERN-DISCOVERY-REUSE-REQUIREMENT.md) owns **user-need→reviewed reuse recommendation**. No new monitoring/runtime installed, Task-0017 G1 unchanged.
