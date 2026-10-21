# models-engines-and-hosts — دانش کاربردی پروژه
**دامنه:** تمایز مدل‌های زبانی، فایل weights، engine inference، host/UI، Agent/CLI، Windows compatibility، Persian quality و lifecycle بارگذاری.

**وضعیت:** هنوز هیچ KB تحلیلی به این شاخه تخصیص داده نشده است. پس از دریافت/اعتبارسنجی پژوهش، مقالهٔ `KB-####-[slug].md` با یک canonical location اینجا ثبت می‌شود؛ اگر چندموضوعی بود سایر READMEها فقط لینک می‌دهند.

به [فهرست دانشنامه](../INDEX.md)، [قواعد ورود و اعتبار](../INTAKE-PROTOCOL.md) و [ثبت منابع](../SOURCE-REGISTER.md) مراجعه کنید. هیچ ابزار/راهکار صرفاً به دلیل نام‌برده‌شدن در متنی که بعداً وارد می‌شود **SELECTED** نیست.

## 2026-10-21 future research inputs (source-only)
- [SRC-0010](../inbox/SRC-0010-hybrid-inference-plane-multi-engine-model-routing-future-20261021.md) full 1,915-line user-supplied proposal, [INF-001](../../03-architecture-and-tools/FUTURE-INFERENCE-PLANE-RESEARCH-REQUIREMENT.md): `local inference engine` vs `model weights` vs `model router` vs `inference gateway` vs `cloud GPU serving` vs `assistant/agent orchestrator`. LM Studio JIT/TTL/Auto-Evict, llama.cpp sleep, Ollama keep_alive, optional llama-swap, optional LiteLLM SDK vs Gateway, future vLLM/SGLang/Ray. **Research candidates only; not installed by intake nor user-benchmarked now**.
- [SRC-0009](../inbox/SRC-0009-ruflo-multi-agent-orchestration-future-20261021.md) is a separate `agent/orchestration harness` family, linked to [REQ-MPA-001](../../02-project-management/MULTI-PERSONA-SPECIALIST-ASSISTANTS-REQUIREMENT.md). Shared logical agents may use one on-demand model, but framework claims are not measurements.
- Original text files preserved exactly in the GitHub SOURCE-REGISTER; inferences, release/cost/region changes and current hardware fit require new official verification and separate permission before pilot.
