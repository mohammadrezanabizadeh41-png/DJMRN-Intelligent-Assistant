# INF-001 — Future Hybrid Inference Plane / Multi-Engine Model Lifecycle and Routing

**Project:** `mohammadrezanabizadeh41-png/DJMRN-Intelligent-Assistant` / `main`  
**Registered:** 2026-10-21  
**Status:** **FUTURE ARCHITECTURE RESEARCH REQUIREMENT / DEFERRED / NOT ADOPTED / NO INSTALL, MODEL OR ROUTER AUTHORIZED**.  
**Canonical raw user-supplied source:** [SRC-0010 — complete verbatim 1,915 lines](../08-project-knowledge-base/inbox/SRC-0010-hybrid-inference-plane-multi-engine-model-routing-future-20261021.md), original file `Pasted text (2).txt`, **54,678 bytes, SHA256 `7e504b00357d0444e20c2e0676d39832b46468c97101aa6df2e6e3744481c2e0`**, matching verified Git blob `7c4e1c7bba451ade5f11998cc11aef103da5771c`. Exact original includes preliminary outside citations, long research questions and a trailing copied-note fragment; none of its vendor claims is an adopted or independently device-tested fact.

**Tracking:** [TASK-0018 future inference research](../02-project-management/TASK-REGISTER.md). Existing [REQ-MPA-001 specialized assistants](../02-project-management/MULTI-PERSONA-SPECIALIST-ASSISTANTS-REQUIREMENT.md), [REQ-012 chat-first requirement](../02-project-management/CHAT-FIRST-ASSISTANT-INTERACTION-REQUIREMENT.md), [D-015 two-surface tool-core plan](DUAL-SURFACE-CHAT-TOOL-CORE-PROPOSAL-20261021.md), [existing candidate register](CANDIDATE-REGISTER.md), [hardware baseline](../01-system-inventory/hardware-baseline.md), [historical model inventory](../01-system-inventory/models-and-engines.md). This is **not** a new requirement to build a gateway before the local G1 tool-host inspection or chat-to-CAP-006 pilot.

## 1. User problem / essential separation

The user wants future DJMRN to switch between **deterministic tools, small local inference, eligible/free verified cloud APIs, specialist models, and remote GPU inference**, while avoiding simultaneous resident local models and unnecessary cost. A future assistant persona may maintain identity, permissions and skill regardless of which model/provider executes a given request.

Separate **ASSISTANT / MODEL WEIGHTS / INFERENCE ENGINE / PROVIDER / ROUTING POLICY / TOOL PERMISSION / DATA AUTHORITY**. `Many defined models` does not imply `many models resident in RAM`. A model-serving router, when actually needed, must be **replaceable**, observable, and never supersede project GitHub authority, Notion Applied/General catalog or any approved durable state.

**Research pattern only:** `User/chat request → trusted intent & policy → deterministic-capability-first → (only if needed) inference contract/model selection → local on-demand model OR legally eligible cloud OR future GPU server → source/receipt`.

Do **not** conflate inference switching with multi-agent coordination: [Ruflo research SRC-0009](../08-project-knowledge-base/inbox/SRC-0009-ruflo-multi-agent-orchestration-future-20261021.md) belongs to the related but separate orchestration/agent-harness category, enriched under [REQ-MPA-001](../02-project-management/MULTI-PERSONA-SPECIALIST-ASSISTANTS-REQUIREMENT.md).

## 2. Candidate roles (not a winner list)

| Role | User-supplied candidate leads | Preliminary placement / why research |
|---|---|---|
| Direct local inference | Ollama, llama.cpp/`llama-server`, LM Studio | Windows/CPU/Vega8 options; quantify actual memory, Persian quality and function calling against equivalent prompts and tool schemas, as distinct from a GUI host. |
| Native model lifecycle | Ollama `keep_alive`, LM Studio JIT/TTL/Auto-Evict, llama.cpp `--sleep-idle-seconds` | Prefer **already provided load/unload/idle** before adding a routing process; measure RAM **after unloading**, cold-start, idle, and recovery. |
| Lightweight external lifecycle proxy | `mostlygeek/llama-swap` | On-demand process/model switching across backends; additional moving part, compare only if native mechanism is insufficient. |
| Model/provider abstraction | LiteLLM SDK and direct per-provider calls | Compare a tiny direct client vs abstraction if two actual providers/inference backends are needed; distinguish API compatibility from semantic parity. |
| Full model/API gateway | LiteLLM Proxy/Gateway and alternatives | Extra database/security/budget/logging/reliability burden; **NOT required** for the first tool-call proof, possible later deployment. |
| Remote GPU inference | vLLM and SGLang | High-throughput, batching, prefix cache, multi-turn; user source considers them **remote/cloud-first candidates**, not default native Windows/Vega8 engines. |
| Distributed GPU orchestration | Ray Serve LLM | Multi-node/cloud cluster candidate only if real GPU serving and workload justify it, not a Windows laptop pilot. |

**Primary documentation spot-check 2026-10-21 (limited, not a full audit):**
- [LM Studio — Idle TTL and Auto-Evict](https://lmstudio.ai/docs/developer/core/ttl-and-auto-evict): documents JIT unload behavior; the default auto-evict applies to **JIT-loaded models**, not every manually loaded model. **Actual local RAM saving unmeasured**.
- [llama.cpp llama-server official documentation](https://github.com/ggml-org/llama.cpp/blob/master/tools/server/README.md): `--sleep-idle-seconds` can unload model/KV cache, default disabled. **Version, Windows/GPU behavior and RAM after sleep untested**.
- [llama-swap official GitHub repository](https://github.com/mostlygeek/llama-swap): on-demand model switching proxy; independently observed real unarchived MIT GitHub repo 2026-10-21. **Not installed or measured**.
- [Ruflo repository](https://github.com/ruvnet/ruflo): real unarchived MIT GitHub repo, separate **agent harness/orchestrator**, not an inference engine; marketed benchmark figures cannot establish DJMRN gains.

All other specifications/cost/performance/platform claims in SRC-0010 are **USER-REPORTED PRELIMINARY RESEARCH**, pending current official proof and real workload measurement. Never copy claimed speedups (including prefix-cache advantages), vendor self-reported costs, quotas, or suitability as independent facts.

## 3. Nonfunctional constraints / suitability tests when authorized

1. Hardware: Windows 11 Pro Lenovo Ryzen 5 3500U + Vega 8; **8 GiB physical, historically ~5.88 GiB OS-visible and ~2–3 GiB free**. The newest G1 device snapshot is **authorized but still pending user output**. Never infer that a server binary or model file fits from installer size.
2. **Single useful local model at a time** *as a conservative initial policy hypothesis*, not a maximum technical limit. Measure true RAM/commit/CPU/GPU, TTFT/throughput and context costs before allowing more parallelism. Distinguish weights on disk, loaded context and GPU preallocation.
3. **After-task RAM** matters as much as peak RAM: compare unload success, cooling period, lingering child processes, idle vs cold-start latency, shutdown, failure recovery and task correctness. Use existing native eviction before `llama-swap` or full gateway.
4. Provider/region/payment/Free-First: a free OSS router does **not** grant free inference. A cloud endpoint requires current actual legal region from user location/eligibility, sustainable free quota, account/card/overage, data retention/training/commercial privacy and explicit consent. `UNKNOWN → DENY ACTIVATION`. Do not route confidential data to remote provider by default.
5. Independent authority: model choice must not grant access to broader files/tools. `Tool permissions` remain outside model/controller. A model-agnostic API is not identical across chat, tool calls, structured output, multimodal, reasoning, cancellation or streaming; adapter must validate declared capabilities.
6. Cloud downtime or laptop powered off: no pretending local inference/document access is available. Fall back only along separately approved, legally accessible paths, or report `OFFLINE/BLOCKED`.
7. Zero-install candidate `existing direct model or deterministic tool` must be compared against local runner, simple rule router, lightweight SDK, `llama-swap`, full gateway and remote GPU serving on **one realistic use case**; more components is not automatically better.
8. No architecture authority transfer to LiteLLM/Ray/LLM proxy, no persistent service requirement or mandatory server stack. Keep model-router concept optional until real multiple-provider need emerges.

## 4. Future acceptance/research questions (NO EXECUTION NOW)

When priority and permission are separately granted, select representative safe workload fixtures (e.g. one actual authorised Persian CAP-006 search + a small grounded synthesis request) and compare:
- Does a **separate Inference Plane** add value over directly calling one existing host API?
- Which local engine already offers sufficient JIT/idle unload; does a small router save meaningful cost/RAM?
- Are two models/backends genuinely required? What is effective tool-call correctness in Persian at given context/quantization?
- After unload, is returned RAM actually observed? How much overhead does a proxy/router have, including itself, adapters and child processes?
- Under data redaction and approval, is lawful cloud fallback materially useful versus `BLOCKED`?
- Do future prefixes/shared persona contexts benefit from caching? Is high-throughput GPU serving present or merely speculative?
- Benchmark exact status: measured vs simulated vs published; record official versions and OpenAI-compatible semantic deviations.
- Pilot candidate **only with explicit future approval**: one existing local model + one authorized remote endpoint (if legitimately available) + simplest deterministic selector; or **no additional router** if one is sufficient. Test output integrity, latency, RAM before/during/after, egress, billing guarantees and fail closed.

## 5. Crosswalk and present-stage gate

- **REQ-MPA-001 / TASK-0014:** persona/team semantics (many assistants, few models, role-aware routing), enriched from Ruflo SRC-0009; does not decide inference backend.
- **REQ-OBS-001 / TASK-0013:** display future model processes, load/unload, routing cost/latency without becoming the model authority.
- **REQ-TDR-001 / TASK-0015:** future technology watch and independent discovery across backends, plan changes and legal/cost updates; not a running collector now.
- **REQ-012 / D-015 / TASK-0017:** the user-approved **dual chat surface + shared tool/permissions core**, G1 read-only device inspection authorized and **awaiting actual user output**; **no immediate inference router or cloud entitlement**.
- **INF-001 / TASK-0018:** future **optional inference-layer research**, **DEFERRED**, never used to hold up/expand G1, CAP-006 or current tool permission work. Revisit only after a real multi-backend need and user approval.

**Current status: SOURCE ORIGINAL VERIFIED; limited official spot-check of 3 mechanisms; implementation/performance/routing recommendation NOT VERIFIED; no system changes.**
