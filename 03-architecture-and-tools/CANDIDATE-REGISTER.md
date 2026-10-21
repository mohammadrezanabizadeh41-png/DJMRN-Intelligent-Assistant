# نامزدهای فناوری — INITIAL NO WINNER
این جدول **نامزد نقش** است؛ هیچ عنصر به عنوان محصول منتخب/اجراشده علامت نخورده است.

| نقش | دستهٔ گزینه‌های تحقیق (غیرانحصاری) | state |
|---|---|---|
| Desktop / agent host | Jan Agent, goose, AnythingLLM, QwenPaw, PicoClaw, AionUi, ready Windows alternatives | RESEARCH CANDIDATES |
| Inference engine | llama.cpp/Jan backend, Ollama, LM Studio, Lemonade, other CPU/Vega8 backends | RESEARCH CANDIDATES |
| Agent orchestration harness | **Ruflo** (`ruvnet/ruflo`, formerly Claude Flow), AutoGen, CrewAI, lean coordinator; distinct role from chat UI, model engine and tool permissions | **FUTURE/DEFERRED RESEARCH LEADS; not selected** — [SRC-0009](../08-project-knowledge-base/inbox/SRC-0009-ruflo-multi-agent-orchestration-future-20261021.md), [REQ-MPA-001](../02-project-management/MULTI-PERSONA-SPECIALIST-ASSISTANTS-REQUIREMENT.md); full swarm vs lite and RAM/security unknown |
| Agent SDK / workflow alternatives | OpenAI Agents SDK, Microsoft Agent Framework, Google ADK, LangGraph, minimal one-agent/no-agent, n8n/Activepieces/Dify/Flowise | **COMPARE BY ROLE, NOT REPLACEABLE AS A SINGLE CLASS** — future only; actual status/releases/current maintenance to verify |
| Inference lifecycle / router | Native Ollama keep_alive, LM Studio JIT/TTL/Auto-Evict, llama.cpp sleep-idle; optional `llama-swap`, direct provider calls, LiteLLM SDK vs Proxy | **FUTURE INF-001 RESEARCH / NOT IMPLEMENTED** — [SRC-0010](../08-project-knowledge-base/inbox/SRC-0010-hybrid-inference-plane-multi-engine-model-routing-future-20261021.md) / [requirement](FUTURE-INFERENCE-PLANE-RESEARCH-REQUIREMENT.md); compare no router/native lifecycle first |
| Remote GPU model serving (future) | vLLM, SGLang (KV-cache/multi-turn), Ray Serve LLM (distributed serving) | **REMOTE/HYBRID FUTURE CANDIDATES**; device Vega 8 suitability, Windows native support, region/free/egress/cost require separate official/benchmark checks; no cloud GPU approved |
| Model weights | Jan-v3.5, Gemma variants, Qwen families, Granite/Phi/small Farsi/multilingual models | RESEARCH CANDIDATES |
| Deterministic tooling | Windows-native PowerShell/Task Scheduler, Python stdlib, .NET, Go, Rust etc. | RESEARCH CANDIDATES |
| Durable workflows | one-shot ledger, native scheduling, LangGraph, DBOS, Dagu, alternatives | RESEARCH CANDIDATES |
| Extraction/knowledge | plain files + FTS, SQLite/FTS5, DuckDB, parsers, RAG/vector only if needed | RESEARCH CANDIDATES |
| Remote services | free websites, models/search APIs, regionally available services/cloud | CURRENT COST/REGION UNKNOWN UNTIL SOURCE CHECK |

**ثبت هر گزینه:** `CAND-ID | role | official URL | version/verified date | use case | license | platform | published spec | measured result? | real-free quota/card/overage | Iran eligibility | permissions/data | alternatives | verdict | evidence | reviewer`.
Consult [Applied library](https://app.notion.com/p/3fdc8c684690817a9b5acef3c108253f); dedupe aliases, differentiate official fact from claim/test. رتبهٔ فنی پیش از محاسبهٔ زمان نصب; installed does not score.
