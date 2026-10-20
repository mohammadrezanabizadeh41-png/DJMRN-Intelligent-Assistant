# REQ-012 — Chat-first assistant control and autonomous-capability integration (USER CLARIFICATION)

**Source:** Explicit user instruction after the user-run CAP-006 Option A test `NEW-V0004`, 2026-10-21.  
**Type:** **CORE PRODUCT REQUIREMENT / USER-DIRECTED CORRECTION**, not a purely deferred optional observability feature.  
**Status:** REQUIREMENT CONFIRMED BY USER / ARCHITECTURE & IMPLEMENTATION NOT SELECTED OR APPROVED; next scoped design pending.  
**Decision:** [D-014](DECISION-REGISTER.md); continuation tasks [TASK-0016 and TASK-0017](TASK-REGISTER.md).  
**Related facts:** [NEW-V0004](../06-tests-and-evidence/logs/NEW-V0004-20261021.md) **technical two-file CLI success only**, [WA0002](../04-work-research-bridge/responses/WA0002.md), existing [Project Charter](PROJECT-CHARTER.md).

## 1. Corrected user intent — product value ≠ manual proof-of-component

The user's exact clarification in context:
> «روش فعلی PowerShell برای استفادهٔ مرتب من راحت نیست من فقط برای امتحانی که کردی این کار را کردم ... من نمی خئام دستی کاری رو انجام بدم و باید در اینده اتومات بشه و توسط دستیاران و حتی در مراحل بالاتر مدیریتی توسط ایحنتها مدیریت بشه ... کار من در نهایت با پیام و کنترل و همکار با دستیاران و ایجنها خواهد بود که اینها رو مدیریت و کنترل کنند.»

**Interpretation:** The user's primary experience is **conversational, message-driven collaboration with assistants/authorized Agents**; manual commands are acceptable only as *bounded installation/debug/test steps*, not as a routine user workflow. The assistant should accept goals and permitted source references, choose the appropriate capability (A document lookup, B structured data, C evidence/research, etc.), execute it within explicit capability/permission boundaries and return a helpful, source-backed Persian answer, while transparently requesting approval for sensitive actions. In later phases specialized assistants and, where needed, manager Agents may coordinate tasks in a durable, resource-aware fashion.

**The earlier assistant wrongly treated the choice A as a terminal UX choice** and offered a "short PowerShell command" versus GUI. That proposed UX choice is **WITHDRAWN as a product-target decision**. It is not necessary to ask whether the user wants routine CLI: user has already answered **NO**.

**What remains valid:** User chose A as the *first verified underlying capability to connect* and separately approved a very narrow test. `NEW-V0004` really passed for a two-file literal query with source/line/SHA. Do **not** retrospectively mark test failed or operational. `D-013` selection of a starting capability is retained; its UX interpretation is corrected and clarified by `D-014`.

## 2. Desired interaction and separate roles

Example user request in natural Persian:
> «در اسناد پروژه بررسی کن وضعیت مدیریت منابع چیست، تصمیم‌ها و شاهد مربوط را بده، و اگر منبعی قدیمی است روشن بگو.»

Future intended path, **conceptual not current implementation**:

`User message → Conversational interface → Intent/goal interpretation → Authorized capability selection & scoped inputs → Deterministic tools/workflow (CAP-006, later B/C) → Source/evidence & errors → Assistant explanation/next suggestions → User approval for consequential action → Controlled execution if approved → Receipt/state`.

Role distinctions:
- **Conversation/experience layer:** natural-language messages and clarification, not asking user for raw CLI switches, JSON hashes, or paths on every request.
- **Assistant reasoning/intent layer:** decide if lookup suffices or further research/structured transform needed; generate human-readable answers; no independent claim that a lexical search "understands" or that it examined unavailable sources.
- **Capability/tool layer:** narrowly authorized deterministic helpers (today CAP-006, future B validated CSV/data and C official-source evidence), with replaceable adapters; scripts can remain internal implementation tools invisible to user.
- **Execution/orchestration layer:** start with an explicit simple request→result tool call; add durable jobs, retries, checkpoints, queues, scheduling or delegated specialist Agents **only when the real workflow requires it**. User requiring eventual automation is a requirement to plan for, **not authorization to install a multi-Agent runtime now**.
- **Policy/approval boundary:** enforce in code or platform outside untrusted assistant prompts; no implicit write/send/read-all/Internet/account permissions; human approval for impactful external actions.
- **State and evidence:** real task references and receipts; the GitHub project remains authoritative for project artifacts, Notion Applied/General for their research domains. Conversation memory is not a replacement for explicit project state. Future persona [REQ-MPA-001](MULTI-PERSONA-SPECIALIST-ASSISTANTS-REQUIREMENT.md), observer [REQ-OBS-001](LIVE-OBSERVABILITY-MAP-REQUIREMENT.md) and Radar [REQ-TDR-001](TECHNOLOGY-DISCOVERY-RADAR-REQUIREMENT.md) are extensibility considerations, not immediate prerequisites.

## 3. A, B and C are additive capabilities, not mutually exclusive final product paths

In [WA0002](../04-work-research-bridge/responses/WA0002.md), A=usable cited document lookup, B=validated CSV/data extraction with user-defined rules, C=evidence/claim comparison from official permitted sources. That ranking was for deciding the **next narrow test**, not a demand that the user choose exactly one permanent service or personally operate the software.

**Architecture intent:** build a shared, modular capability system in which the assistant can invoke A, then optionally B or C within the same goal when each has been properly implemented and authorized. A-only initial end-to-end conversational demonstration is a possible next milestone, followed by B/C integration based on actual priority and resources; **not** mandatory A→B→C release order, not permission to build all immediately, not a commitment to a specific stack.

Illustrative future workflow:
- Message: `بر اساس این چند سند بررسی کن چه ابزارهایی قبلاً ارزیابی شده‌اند، شرایط رایگان را جدا کن و نتیجهٔ مستند بده.`
- Assistant searches authorized project docs via A, fetches/compares authorized up-to-date official evidence via C when research is required, optionally structures/validates rows via B, and replies with source links, uncertainty and status. Complex cross-capability planning or unattended work may later need specialist Agents/manager, not necessarily multiple concurrently loaded AI models.

## 4. Non-negotiable usability and acceptance gates

1. The user can **start from a message**, not PowerShell or selecting Python file manually. Normal successful use of A **requires no manual PowerShell**. The user's computer may need a one-off authorized setup, but that is not the everyday control surface.
2. For an initial chat→A vertical: one **user-authorized small fixed document allowlist**; typed natural-language request; appropriate literal-keyword selection/disambiguation; CAP-006 call (directly or via an authorized local/cloud bridge); grounded understandable response containing document/line and original quote or citation. If semantic intent exceeds literal coverage, ask/disclose, **not hallucinate answer**.
3. Demonstrate **actual authorized tool invocation + receipt**, not simulate by having a model describe a search it never ran. Exact direct execution environment, permission scope, host, portability, model/api cost, privacy and Windows RAM must be independently determined.
4. If an external conversation interface **cannot directly access the local Windows filesystem**, the missing trusted local bridge/host must be explicitly designed, evaluated, deployed and permissioned with user approval. Do not imply ChatGPT in its present session already runs `docsearch_v0.py` on the user's Windows laptop.
5. Prefer existing safe software/OS/native integration and current models/resources if fit; compare alternative chat surfaces, local interface, a lightweight tool adapter, connected assistant and hybrid deployment on equal evidence. Installation history is not a merit score; no stack, Agent framework, token, scheduler or provider yet selected.
6. Minimum future demonstration: user sends one real scoped Persian request; a permitted tool runs without manual per-request terminal commands; user gets a useful grounded result or an honest `blocked/need approval/not supported`; logs/permissions allow audit. No accidental read/write/send of private files/accounts or paid/cloud activation.
7. Error handling and optional human approval/stop must work **from the same conversational context**; unknown access/cost/region blocked; UI remains usable when a tool is offline. The user is a **supervisor/collaborator**, not a person manually coordinating CLI programs.
8. Structured output contracts and capability boundaries permit later local/remote model routing, data extraction, research workflows, specialist personas, durable resource admission and monitoring **without rebuilding each underlying capability**.

## 5. Narrowest credible next project milestone — RESEARCH/DESIGN ONLY pending approval

**Proposed M1: "User message → one scoped CAP-006 search tool call → Persian grounded reply".**

Before building it:
- Inspect existing project runtime/Notion architecture and what actual chat interface/host bridge is accessible and lawful; verify local vs remote execution, approved-data transport, authorization on Windows, free recurring service limits and resource overhead using current official documentation where necessary.
- Compare a few real **same-role implementation options**: (a) a lightweight local chat/control program that spawns the permitted tool on demand, (b) an existing ready-made assistant/workflow host that supports a permissioned local tool/capability, (c) a hybrid/connected chat UI with a truly authenticated Windows tool bridge; don't use an Agent just for label.
- Define exact message, allowed files, invocation contract, tool response, answer template/evidence and failed/denied path; agree whether a model or deterministic intent parser is necessary. A chat response can be AI generated, while the search itself stays deterministic.
- Select the smallest reversible option and request **separate explicit user authorization** for code edits, new local app/interface, bridge/network, installing software, hosted account, paid tokens or Windows execution. Document observed performance rather than invent numbers.

**Current state:** The user has **corrected and clarified the end-state requirement**. The new chat→tool implementation is **not yet built or approved**. We should stop repeating manual CLI demos as if they were product milestones; their engineering evidence is already captured in NEW-V0004.

## 2026-10-21 ADDENDUM — User explicitly chose both conversational surfaces

After reading the fully verified Work [WA0003](../04-work-research-bridge/responses/WA0003.md) and [coordinator review](../04-work-research-bridge/reviews/WQ0003.md), the user explicitly requested **BOTH**: future DJMRN control from ChatGPT and from a separately hosted Windows/private chat interface. This closes the earlier unresolved *which conversational surface?* question; it **does not** grant access to local files from this chat, choose a technical host/model or approve installation/runtime changes.

The only **PROPOSED** solution for user sign-off is a **portable shared DJMRN tool and policy core** with host-specific adapters (possibly distinct stdio child processes, not a compulsory always-running shared service). Initial PRIMARY local-chat pilot may try **Jan Desktop v0.8.7** only with Shell OFF, other broad tools OFF, autoapprove OFF, actual permission checks, measured RAM/quality and user consent. **Cherry Studio** remains fallback, and **ChatGPT Desktop local MCP** is the future second interface subject to actual feature availability, separate transfer privacy and consent. No unverified Cloud API/tunnel or model activation is authorized. Read [full architecture proposal](../03-architecture-and-tools/DUAL-SURFACE-CHAT-TOOL-CORE-PROPOSAL-20261021.md) and [D-015](DECISION-REGISTER.md).

Once/if user endorses the DESIGN, G1 readiness inspection, G2 code/adapter work, G3 local pilot and G4 ChatGPT integration require separate granular permissions, gates and actual evidence. On failure Jan must not be installed/upgraded anyway; an alternative can be proposed without sacrificing a host-independent tool schema. A/B/C remain shared future capability roles, not three separate manual applications.

## 6. Research governance and next gate

Any future Work search about interface/tool-host architecture follows the [Work Bridge protocol](../04-work-research-bridge/README.md): **read actual relevant Applied Notion library + Mission plus independent official search, merge receipts and compare alternatives**. No separate Applied Research Bridge write. User has not explicitly ordered a new Work WQ in this message; it may be proposed once the scope is agreed rather than implying Work research is already dispatched.

**Decision status summary:** `REQ-012` confirmed; `D-014` user directive that product is chat-first; `TASK-0017` proposed next bounded design/integration effort, **AWAITING SCOPE/APPROVAL**; A/B/C remain **logical capabilities**; CAP-006 remains `VERIFIED-REAL / BOUNDED`, not user-facing conversational operational.

## 2026-10-21 entitlement correction — current ChatGPT Plus, G0 accepted

The user approved the staged two-chat-surface architectural direction with `اوکی`, while correctly warning that their actual ChatGPT subscription is **Plus**, not Pro. Product docs current 2026-10-21: [OpenAI custom MCP help](https://help.openai.com/en/articles/12584461-connecting-custom-mcp-servers-in-chatgpt) lists **Pro read/fetch custom MCP**, **Business/Enterprise/Edu full MCP**, with **no verified Plus custom connector entitlement**. [ChatGPT/Codex host MCP configuration](https://learn.chatgpt.com/docs/extend/mcp) and [public installed plugins](https://learn.chatgpt.com/docs/plugins) are separate surfaces/capabilities; do not deduce that a generic config is active in this user's normal Plus chat. The shared contract remains usable irrespective of Plus limitations; **local independent chat is primary conditional pilot, ChatGPT direct local-tool adapter G4 on HOLD until proven legitimate/available**, without mandating a subscription upgrade or API key. G0 approved, G1 Windows/account feature read-only inspection, G2 code, G3 local test and G4 ChatGPT connector **each separately permission-gated**. Full source/recommendation in [dual-surface plan](../03-architecture-and-tools/DUAL-SURFACE-CHAT-TOOL-CORE-PROPOSAL-20261021.md).
