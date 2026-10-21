# REQ-MPA-001 — Many Logical Specialized Assistants / Personas on Shared DJMRN Infrastructure

**Status (2026-10-21): USER-REQUESTED FUTURE REQUIREMENT / DOCUMENTED & DEFERRED / RESEARCH PENDING / NOT IMPLEMENTED / NO ARCHITECTURE OR PROVIDER SELECTED**

**Canonical raw input:** [SRC-0004 — complete, unchanged user text (1,583 lines; 46,545 UTF-8 bytes)](../08-project-knowledge-base/inbox/SRC-0004-djmrn-multi-persona-logical-assistants-future-20261020.md). Original submitted filename: `Pasted text(20261020-205920).txt`; original SHA256 `0f3795a87a49ac6e0b4b9002e315ae4972fa0dbaf91caca4b2ba094e7061280f`; verified Git blob `f3536aa4a671f29ee0154f451d06889ad7e3a0ed`.

**Tracking:** [TASK-0014](TASK-REGISTER.md); aligned with [Project Charter](PROJECT-CHARTER.md), [ROADMAP](ROADMAP.md), [Project Rules](../PROJECT-RULES.md), and existing future [REQ-OBS-001 Live Observability Map](LIVE-OBSERVABILITY-MAP-REQUIREMENT.md).

## 2026-10-21 ADDENDUM — Ruflo / Claude Flow research lead, SAME existing REQ-MPA-001

**User's new complete original:** [SRC-0009 — Ruflo and competing multi-agent frameworks, 2,119 verbatim lines](../08-project-knowledge-base/inbox/SRC-0009-ruflo-multi-agent-orchestration-future-20261021.md), original uploaded `Pasted text(20261021-000658).txt`, **50,192 bytes**, SHA256 `5f724204deb15e375abbe94e8129ac5f63f0ebdd38877d3ab978e8777a176660`, Git blob `06101bdc123caa4b13549b2005365b113c760797`; original CRLF and all lines preserved and verified. **This supplements old SRC-0004, not a replacement, second MPA requirement or new currently active task.** [Existing TASK-0014](TASK-REGISTER.md) remains FUTURE/DEFERRED; [model-plane separate SRC-0010](../08-project-knowledge-base/inbox/SRC-0010-hybrid-inference-plane-multi-engine-model-routing-future-20261021.md) is tracked separately as future INF-001/TASK-0018.

### Distinct incremental user research needs
- **Candidate:** [Ruflo (`ruvnet/ruflo`), formerly Claude Flow](https://github.com/ruvnet/ruflo), described by the author as an **agent meta-harness / coordination, workflow, memory, routing, MCP server and swarm/orchestration layer**, **not itself an LLM, inference engine or DJMRN authority**. Direct GitHub API read 2026-10-21 independently verified a **real, unarchived, MIT repository**, not broad functionality, self-learning claims, tests or Windows low-RAM suitability. Multiple project versions, permissions, release maturity and exact feature implementation need future independent official/code audit.
- Candidate research categories must not be collapsed into one "Agent Framework" ranking: **agent harness/swarm** (Ruflo, AutoGen, CrewAI), **agent SDK** (OpenAI Agents SDK, Microsoft Agent Framework, Google ADK), **graph/durable workflow** (LangGraph), **ready/visual app** (Dify, Flowise, Langflow, Open WebUI, AnythingLLM), **automation** (Activepieces, n8n, Node-RED), and **minimal script/one-agent/no-agent**. Investigate lifecycle/cost/permissions across equivalent WORKLOADS, not names or social-media marketing.
- Many logical personas/agents, shared skills/tools/memory and **one or few on-demand models**, rather than one resident model/process per role. Distinguish `AgentState`, registered identity and subscription from model inference call, worker OS process, background loop or remote job.
- Candidate coordination patterns: `one coordinator + two specialists` first, before distributed mesh/hive/consensus/federation; explain when hierarchies, weighted review, handoff, retries and meaningful consensus beat ordinary coordinator + human approval. `Queen/Hive Mind` is terminology, not independently proven capability.
- **Routing ladder:** deterministic tool → direct small model → stronger lawful cloud model → optional scoped Agent; `MoE routing` of role/capability is not necessarily MoE within neural weights. Keep model routing distinct from **tool authorization**, which cannot be delegated to arbitrary model prompts.
- Treat `352x`, `75% cost reduction`, `100+ agents`, `<10ms security`, `12 workers`, `8 experts`, "self-learning" or "sandbox" as **vendor/creator claims unless separately measured/specified for the exact component/workload**; 12 named background workers do not imply 12 resident independent models. Distinguish pattern/routing/trajectory selection from actual model fine-tuning; never accept project security speed claims as certification.
- Ruflo MCP server could be an *optional future orchestrator behind* the shared ChatGPT/local-chat Tool Core, but **MCP integration alone doesn't make ChatGPT Plus custom MCP available or reach a powered-off laptop**; the current [G0 dual-surface direction](../03-architecture-and-tools/DUAL-SURFACE-CHAT-TOOL-CORE-PROPOSAL-20261021.md) continues, and the already authorized one-off G1 inspection is still waiting on the user's results. **Do not install/initialize Ruflo to perform G1**.
- Reuse [REQ-OBS-001](LIVE-OBSERVABILITY-MAP-REQUIREMENT.md) for possible Ruflo Console coverage; `Ruflo Console` observes its own ecosystem by default, **not DJMRN's full local/cloud map** without separate instrumentation. Durable state and canonical GitHub/Notion authority remain outside any framework memory, RuVector, learned routing or agent traces.
- For **future user-approved disposable, read-only pilot**, compare `no new framework/one tool` against Ruflo minimal MCP/harness and one or two smaller candidate frameworks, using **one coordinator + two specialist profiles + one shared model + one existing deterministic tool**, with no permanent daemon, no main-repo initialization and no unnecessary local inference. Measure startup/idle/load/after-stop RAM, worker/process count, security/permission behavior, failure/recovery, latency, tool correctness, repeatability, provider/privacy/Free-First. Only after passing could expanded framework components be separately approved.

### Non-approval & state boundary
**Ruflo = WATCH / FUTURE DEEP RESEARCH CANDIDATE / NOT SELECTED RUNTIME**. No `npx ruflo`, package installation, agent spawn, workers, MCP start, cloud model, API key, security plugin, checkout/init in DJMRN repo, experiment, extra RAM test or fee now. The user currently prioritizes **G1 one-off read-only device/Jan/ChatGPT readiness**. Historical Applied/General library entries are evidence and candidates, not a winner; active repo results and further official release/security/compatibility research determine future decisions.

## 1. Need and boundaries

The user wants the future DJMRN environment to allow a potentially large number of **independently defined logical specialist assistants** with stable identity, distinct mission, reasoning approach, permitted knowledge, shared/specialist skills, tools, model policy, permissions and output contract; assistants can collaborate within explicit workflows and may be upgraded to actual autonomous Agents only when the task warrants it.

**Fundamental distinction: Many Logical Assistants ≠ Many Resident Models/Agents.** A persona/profile is not automatically a separate process or separately loaded inference model. Multiple profiles can reuse one on-demand model engine (local or remotely hosted), while tool/data collection is deterministic where possible.

Examples in the submitted text: `Idea Scout`, `Finance Thinker`, `Research Analyst`, `Critic/Reviewer`, `Opportunity Analyst`, `Technical Architect`, `Creative Assistant`; names and counts are **examples, not a requirement to instantiate all today**.

This is a future feature already broadly consistent with the existing mission for specialist capabilities and technology-neutral, small-first architecture. **User intent is to preserve the entire idea and make it researchable later**, without displacing bounded CAP-006 work or declaring any implementation choice today.

## 2. Proposed logical profile fields — research candidate, not a finalized schema

- Stable ID, name, version, role/purpose, mission, personality/behavior style, reasoning guidance and explicit prompt/instructions.
- Specific and shared Knowledge Sources, retrieval scope and memory namespace. Shared project/state authority stays outside prompt/chat memory.
- Reusable Skill references and versions, allowed/forbidden tools, capability permissions, security/approval/escalation rules and input/output contracts.
- Preferred models, model routing policy, privacy/residency/cost constraints, explicit resource budget, status and provenance.

**Personality ≠ prompt only.** Prompt + Skills + authorized Knowledge + Tool/Permission boundary + outputs + optional Memory + Model Policy may define meaningful stable persona behavior. Enforcement must reside in real tool/runtime boundary; natural-language instructions alone are not security boundaries. Git-backed versioning is a candidate, not a prescribed runtime.

## 3. Processing boundaries and collaboration — options to test later

`Sources (web/API/RSS/files/GitHub/Notion/etc.) → authorized deterministic collect/normalize/filter/dedup/provenance → shared/specialist retrieval → profile-guided reasoning or tools → structured results/review`.

Differentiate clearly:
- **Persona:** identity/profile and task-specific constraints; not necessarily an Agent.
- **Direct model call:** prompt+profile+retrieved context, often adequate for ideation, finance review or criticism.
- **Deterministic workflow:** fixed ordered/parallel stages, reviews or handoffs, possibly calling one shared model multiple times under different profiles.
- **Agent with tools:** conditional tool choice, retries and adaptive information gathering that a fixed workflow cannot economically handle.
- **Multi-agent:** autonomous specialist delegation/handoffs only after measured incremental value.

Potential collaborations: sequential, parallel, supervisor, reviewer/debate and handoff. Example: authorized inputs → deterministic preparation → Idea Scout → Finance Thinker → Research Analyst → Critic → deterministic ranking → final synthesis; no assumption that each stage needs a distinct model or Agent daemon.

## 4. Resource / hosting requirements and assumptions

- Hardware baseline (historical): Windows 11 Pro, Ryzen 5 3500U/Vega 8, 8 GB physical RAM; OS-accessible / free RAM constrained. Re-measure only when a concrete pilot needs it. **Profile count is not model/process count**; high RAM arises from resident model weights, KV cache, engine/UI/backend, parallel context/workers and data services.
- Local/shared model and engine, cloud model, hybrid/offline fallback, on-demand load/unload and lightweight rule-based model routing are **architectural alternatives**, not selected defaults. Local model weight size alone does not establish actual Windows memory footprint; test engine/context/cache/overhead.
- Local RAM does not itself disqualify cloud-hosted inference/workflows, but Free-First, geography/eligibility (including Iran), quota renewal, card, overage, privacy/data handling and account authorization are mandatory gates.
- No separate database, vector store, long-running worker, runtime or resource manager per profile without need and evidence.

## 5. Source examples and future research landscape — all UNVERIFIED candidates

Products mentioned **for future comparison**, not approved:
- Interfaces/ready-made personal AI workspaces: Open WebUI, AnythingLLM and independently discovered alternatives.
- Cloud workflows/agents: Activepieces Cloud, Dify and others.
- Agent/workflow frameworks: LangGraph, PydanticAI, Google ADK, Semantic Kernel, AutoGen, CrewAI, n8n AI, Flowise, Langflow, Node-RED and others.
- Further named alternatives: QwenPaw/PicoClaw/AionUi/goose (availability, names, version, capability and platform fit to be verified independently).
- Local inference: llama.cpp family, LM Studio, Ollama, Jan, Foundry Local and new Windows-native options. **Do not treat historical installs as positive ranking factors.**
- Cloud model APIs named as investigation leads: Cloudflare Workers AI, GroqCloud, Gemini Developer API and any better current competitor; no entitlement, lawful access, free tier or acceptable privacy is assumed.
- Lightweight custom runtime and declarative `assistant_profiles` plus simple workflow runner is a **comparison candidate**, not a selected Python architecture or authorization to build.

Required architecture families for future comparison: many personas/one cloud model; many personas/one local shared model; workflow plus persona steps; one Agent+tools; supervisor/workers; cloud agent platform; local host; minimal custom core (Python **and** credible alternatives where appropriate); deterministic local data plus cloud inference; small local fallback plus remote inference.

A catalog review should identify what is truly ready-made vs needs building, shared-engine ability, RAM/CPU, Windows compatibility, API/Skills/knowledge separation, enforceable permissions, cost/region/quotas, modularity and replacement/migration risk. **No broad research/tool install is commissioned by this archival step.**

## 6. Security, permissions, state and observability

- Default-deny tool access beyond explicit per-profile role; no implied access to filesystem, email, websites/browser account, bank/payment, publish/delete, production database or user data.
- Human approval required for consequential financial, send, publish, delete, security, account and production actions, independent of persona content.
- Shared canonical project/business state is outside persona memory; namespaces/index filters preferred for data isolation if sufficient, avoiding duplicate authorities or extra databases.
- Future [REQ-OBS-001](LIVE-OBSERVABILITY-MAP-REQUIREMENT.md) should be able to trace profile/workflow/model/tool usage and local/cloud ownership as observer only, without copying sensitive payloads and without making runtime depend on dashboard health.

## 7. Future acceptance gates — user-sourced requirements, to refine

1. Independently define and version multiple personas with stable identity, mission and observable behavior.
2. Provide separate and reusable/shared skills, explicit scoped knowledge and permissions.
3. Reuse a single local or remote model across several profiles; swap model without redefining persona.
4. Offer appropriate local/cloud routing/fallback within security, cost and RAM limits; avoid mandatory resident process per persona.
5. Combine deterministic processing and AI outputs in specified sequential/parallel/review workflows.
6. Keep persona separate from autonomous Agent; use Agent only when justified.
7. Validate outputs, cite provenance, keep durable state separate from context/memory.
8. Enforce authorization and human approvals in code/platform, not merely system prompts.
9. Measure idle/active RAM, latency, throughput, unload and crash isolation on permitted workloads.
10. Keep each role/engine/provider replaceable; observability can trace task boundaries without owning control.
11. Meet Free-First, privacy, jurisdiction and eligibility gates before any cloud account/API activation.
12. Demonstrate real user value before promoting status to `OPERATIONAL`.

Original 18 numbered acceptance items and full 40-part rationale are preserved **verbatim** in [SRC-0004](../08-project-knowledge-base/inbox/SRC-0004-djmrn-multi-persona-logical-assistants-future-20261020.md); the above is a working index, not a replacement.

## 8. Integration decision and follow-up (NO new architecture adoption)

- **Requirement registered, implementation deferred.** Keep existing practical CAP-006 milestone as current priority; resume/reprioritize only by user instruction. Profile schema, backend, model, router, Agent framework, memory store and host remain undecided.
- When user requests this work later: first inspect current project/Notion Applied+General research; independently discover current competing products and official documentation; perform cost/free/regional/privacy/security verification; distinguish facts/inferences/proposals; compare alternatives, choose smallest bounded prototype and seek explicit approval for installations, cloud, telemetry, tests and new work.
- Do **not** register a new D-architecture decision, a chosen vendor, deployed capability, new runtime, financial action or test pass based only on this statement.
- Open questions: one or more shared models vs sequential re-use, declarative profile standard, runtime permission enforcement, tool scopes, semantic and deterministic output validation, durable receipts, cost/region gates, Windows RAM, retrieval isolation, safe workflow vs Agent escalation, measurement design.

**Documentation only; no install, account connection, new model, external search/report, Windows action, telemetry or external send was performed for this future idea.**
