# KB-0010 — ترتیب شروع: قرارداد نازک، قابلیت مستقل، سپس مدیر منابع مشروط

**Status:** SOURCE CURATED / INDEPENDENT OFFICIAL SPOT-CHECK LIMITED / D-009 NOT ADOPTED  
**Captured/reviewed:** 2026-10-20  
**Sources:** [WA0001](../../04-work-research-bridge/responses/WA0001.md), [WQ0001](../../04-work-research-bridge/requests/WQ0001.md), [coordinator review](../../04-work-research-bridge/reviews/WQ0001.md), [SRC-0002](../SOURCE-REGISTER.md); [Work commit](https://github.com/mohammadrezanabizadeh41-png/DJMRN-Intelligent-Assistant/commit/6b29c81f4e90d45207e56a3e39eba66e3213d143), WA blob `907cdb29dfec0393aa31c75e1e9bdcf78f64ce81`.  
**Tags / aliases:** `sequencing`, `thin contract`, `capability first`, `deterministic`, `no agent`, `RAM admission`, `resource management`, `model on demand`, `ترتیب ساخت`, `قرارداد سبک`.

## Key finding derived from WA0001
A manually started, low-risk, read-only deterministic task does not require Agent, model engine, durable queue, DB or central resource manager. Favor a small conceptual task contract first: id/capability, approved input ref, owner/access scope, result/status/error/receipt, cancellation/deadline. **Contract definition is not a requirement to build infrastructure.** Build smallest useful capability with source receipts. Only then add persistence if necessary, model inference if task demands it, and resource controller *before* automated concurrent heavy processes/unattended failure recovery when that need is demonstrated.

**Candidate V0 for approval:** source-citing local text/document search and Persian normalization/extraction using explicitly approved non-sensitive documents. Script/GUI/language remain undecided; working software cannot be claimed.

## Counterfactuals and limits
For automatic multiple worker launches, model lease sharing, pressure-sensitive admission, process orphan prevention, or uncertain external effects, resource/permission controls must be considered **before activating** those workloads, not after an incident. For the initial manual read-only case, avoid unsupported claims of reduced RAM or a faster development time on this laptop.
Official docs [Task Scheduler](https://learn.microsoft.com/en-us/windows/win32/taskschd/task-triggers), [Job Objects](https://learn.microsoft.com/en-us/windows/win32/procthread/job-objects), [Dagu](https://docs.dagu.sh/writing-workflows/dag-run-resource-limits), [Ollama](https://github.com/ollama/ollama/blob/main/docs/faq.mdx) were *spot-checked*, not benchmarked. Work WQ/bridge source SHA mismatches are recorded in review; product-specific numbers/licenses remain uncertain.

Related: [KB-0001](KB-0001-capability-first-hybrid.md), [KB-0008](KB-0008-three-build-bundles.md), [KB-0006](../hardware-and-performance/KB-0006-local-memory-budget.md), [KB-0004](../knowledge-search-and-memory/KB-0004-non-llm-nlp-persian.md). `D-009` **awaits user approval**; no installation or code authorization.
