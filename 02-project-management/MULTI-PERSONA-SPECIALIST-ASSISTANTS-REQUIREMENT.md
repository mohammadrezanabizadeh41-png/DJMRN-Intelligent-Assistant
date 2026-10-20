# REQ-MPA-001 — Many Logical Specialized Assistants / Personas on Shared DJMRN Infrastructure

**Status (2026-10-21): USER-REQUESTED FUTURE REQUIREMENT / DOCUMENTED & DEFERRED / RESEARCH PENDING / NOT IMPLEMENTED / NO ARCHITECTURE OR PROVIDER SELECTED**

**Canonical raw input:** [SRC-0004 — complete, unchanged user text (1,583 lines; 46,545 UTF-8 bytes)](../08-project-knowledge-base/inbox/SRC-0004-djmrn-multi-persona-logical-assistants-future-20261020.md). Original submitted filename: `Pasted text(20261020-205920).txt`; original SHA256 `0f3795a87a49ac6e0b4b9002e315ae4972fa0dbaf91caca4b2ba094e7061280f`; verified Git blob `f3536aa4a671f29ee0154f451d06889ad7e3a0ed`.

**Tracking:** [TASK-0014](TASK-REGISTER.md); aligned with [Project Charter](PROJECT-CHARTER.md), [ROADMAP](ROADMAP.md), [Project Rules](../PROJECT-RULES.md), and existing future [REQ-OBS-001 Live Observability Map](LIVE-OBSERVABILITY-MAP-REQUIREMENT.md).

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
