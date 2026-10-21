# REQ-WFR-001 — Reuse-first Workflow Pattern Discovery and Adaptation (FUTURE)

**Registered:** 2026-10-21  
**User demand:** Before building a new automation, DJMRN should examine existing capabilities/tools and **search safe, ready-made workflow/template catalogs** for reusable design patterns, then evaluate whether to **reuse, adapt, translate or build** with evidence and permission. Product interactions later must be **message-first**, not PowerShell.  
**Status:** **USER-PROPOSED FUTURE CAPABILITY / REGISTERED / RESEARCH CANDIDATE ACCEPTED AS SOURCE / DEFERRED / NOT DESIGNED, BUILT OR RUN**.  
**Task:** [TASK-0019](TASK-REGISTER.md).  
**Complete primary source:** [SRC-0011, user-provided 885-line complete research](../08-project-knowledge-base/inbox/SRC-0011-n8n-workflows-template-library-reuse-discovery-20261021.md), byte-sha `f4aae663d5409866cd3e6e77c77e2e59e7f8ad4e79ed149d11a9ec8be5e97454`, Git blob `03436a0c5e6d264e2cd7f3a06ca8adec034c064a`.  
**Independent source evaluation:** [Zie619 catalog dossier](../08-project-knowledge-base/tools-and-integrations/SRC-0011-WORKFLOW-LIBRARY-EVALUATION-20261021.md).  
**Related existing capabilities and authorities:** [KB-0007 ready workflow products](../08-project-knowledge-base/tools-and-integrations/KB-0007-ready-made-workflow-products.md), [REQ-TDR-001 Technology Radar](TECHNOLOGY-DISCOVERY-RADAR-REQUIREMENT.md) / TASK-0015, [REQ-MPA-001 logical assistants](MULTI-PERSONA-SPECIALIST-ASSISTANTS-REQUIREMENT.md) / TASK-0014, [REQ-012 conversation-first](CHAT-FIRST-ASSISTANT-INTERACTION-REQUIREMENT.md) / [D-015 shared UI/tool core](../03-architecture-and-tools/DUAL-SURFACE-CHAT-TOOL-CORE-PROPOSAL-20261021.md), [Tool Governance](https://app.notion.com/p/3edc8c68469081cc90abdd5183f1bdb1).

## 1. Why this is DISTINCT, but must reuse existing ownership

**REQ-WFR-001 owns the future user-task-to-WORKFLOW-REUSE recommendation**, not a new Radar/technology search crawler and not a runtime/Agent engine. Its future user-facing outcome: `"برای این کار Workflow آمادهٔ معتبر پیدا کن؛ ریسک و هزینه را بسنج و قبل از ساخت از صفر گزینهٔ اقتباس پیشنهاد بده."` The assistant should search already reviewed reference sources, compare candidate flows with existing DJMRN capabilities, give attributable JSON/path/commit evidence and request permission before changing or running anything.

**Existing [REQ-TDR-001](TECHNOLOGY-DISCOVERY-RADAR-REQUIREMENT.md) remains owner of** discovering new public technology/integration trends, future lawful workflow-source update signals, creator pages and ideas. [KB-0007](../08-project-knowledge-base/tools-and-integrations/KB-0007-ready-made-workflow-products.md) retains the product/runtime candidate landscape. This future Workflow Pattern Reuse feature **does not rewrite those** or require a second source authority or new Applied branch.

**Existing assistant/multiagent persona requirements** can support logical roles `Automation Scout, Technical Reviewer, Security Reviewer, Cost Reviewer, Workflow Adapter`, but they may be **one assistant's analysis stages**; not five background Agents or resident AI models.

## 2. Scope and minimal future contract (NOT IMPLEMENTED)

**Input (future):** natural-language Persian task, explicitly permitted data class and optional tools/provider constraints; never arbitrary credential or executable from a template.  
**Workflow:**
```text
user goal
  → current DJMRN capabilities and permitted tools check
  → approved reference-source/online workflow search
  → inspect up to 3 attributable pinned candidate JSONs (NO execution/import)
  → parse node graph, trigger/action/dependencies/security/permissions/egress/cost/region
  → compare against simple native and at least one alternative template
  → recommendation: REUSE / ADAPT / TRANSLATE / CUSTOM-BUILD / REJECT
  → optional distinct user approval for code/test/real execution
```
**Output (future):** `name, source_provider, source_commit/blob, workflow_path, purpose, nodes/triggers, credential_types, risky_nodes, network, data_egress, provider_region, actual_free_quota/cost, compatibility, maintenance, security_notes, estimated_savings_basis, recommendation, confidence_evidence, unanswered_questions, requested_approval`. Avoid pseudo-exact match percentages without an evaluation rubric. Preserve HTML/JSON from public repos as untrusted data, not instructions.

**Data/provenance:** GitHub commit SHA and workflow path *for exact inspected revision*, original node type/name, user request scope, transformed logic and reason for each change. Distinguish template workflow **concept** from source n8n **engine**; engine licensing/credentials remain separate from template license.

**Security:** No arbitrary `HTTP Request`, Code/Function/ExecuteCommand/Shell, untrusted Community Nodes, file writes, webhook exposure, API credentials, OAuth, paid services, cloud upload or cron schedule based on a fetched sample. Unknown major dependency = `UNKNOWN / REVIEW REQUIRED`; generic publisher `production-ready` claims are not DJMRN approval. No secret/config content copied to source control.

## 3. Candidate source roles and factual status (2026-10-21)

- **First newly proposed source:** [Zie619/n8n-workflows](https://github.com/Zie619/n8n-workflows): real, public, unarchived upstream main `94007c1445d9258a7da116646b79473e7c7c3282`, MIT *repository*; searchable [public catalog](https://zie619.github.io/n8n-workflows/), FastAPI+SQLite FTS5 source present. Claims **4,343** workflows, while a direct `main` Git tree inspection showed **2,061 actual tracked `workflows/**/*.json` paths**; counts have distinct scopes and are unreconciled. Three specific JSONs inspected read-only, confirming sample useful RSS/GitHub flows **and** credential/code/shell/webhook hazards. Mark **REFERENCE SOURCE ACCEPTED AS RESEARCH CANDIDATE, NOT APPROVED TO RUN**; see [detailed evidence](../08-project-knowledge-base/tools-and-integrations/SRC-0011-WORKFLOW-LIBRARY-EVALUATION-20261021.md).
- **Official n8n templates:** [n8n.io/workflows](https://n8n.io/workflows/), alternative reference in same n8n ecosystem; separate n8n fair-code engine/license.
- **Independent engine/template family:** [Activepieces Template Library](https://www.activepieces.com/docs/flows/template-library), [Node-RED Flow Library](https://flows.nodered.org/); real official template indexes, not universal imports.
- **Possible additional categories:** Dify, Flowise, Langflow, GitHub workflow/template repos, DJMRN own proven workflow patterns; research specific current source URLs/licensing/maintained semantics when actually needed, not a mandatory large catalog mirror.

**Source update policy:** research on demand, not periodic full clone or automatic `watch all workflows`; keep `last_checked/upstream_sha/changed? ` only for actual used/adapted workflows. Future Radar may suggest that a source changed but must not mutate canonical accepted DJMRN patterns without review and explicit permission.

## 4. Future acceptance gates and comparative test

**Before any practical activation** pick one actual DJMRN or freelance automation problem. In read-only-only scope, inspect **≤3** relevant patterns, compare at least one non-n8n candidate or clean direct-code design, report detected risks, version mismatch, real-cost/region and concrete time-saving estimate with assumptions. This research **cannot** demonstrate actual production reliability or model speed.

Success: the tool identifies a genuinely relevant, lawfully reusable and maintainable pattern **and** shows a plausible time/cost/security benefit over building simple automation from scratch; accepts unknowns honestly; keeps project state/credentials intact. Failure: incompatible/stale code, mandatory paid/unavailable API, unclear provenance, unacceptable privileges, or no actual benefit — output **REJECT/NO MATCH/BUILD SIMPLE**.

Separate later approvals needed for automated catalog ingestion/indexing, creating new Source adapters, importing/rewriting JSON, installing n8n/Activepieces/Node-RED, running any workflow, entering accounts/keys, creating webhooks, scheduling/notifications or copying private data to cloud. **No silent execution.**

## 5. Current priorities / nothing changed in G1

**This intake is documentation/research only.** The user's already approved Windows/Jan/ChatGPT read-only **G1** remains **PARTIAL**, awaiting actual Jan executable version and real MCP menu evidence. At last user output the shortcut target was `Jan-Desktop.exe`, not `Jan.exe`; RAM available one snapshot ~1.73GiB out of 5.88GiB usable; 8GiB physical installed historical. **G2 chat-to-CAP-006 adapter and G3 real chat tool pilot not yet authorized**. This future workflow-source catalog research does not require cloning, n8n runtime, Docker, new DB, API server, assistant framework, cloud or model workload.
