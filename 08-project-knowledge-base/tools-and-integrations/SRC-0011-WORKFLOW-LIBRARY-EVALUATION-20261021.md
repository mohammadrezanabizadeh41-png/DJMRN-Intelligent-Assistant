# SRC-0011 — Zie619/n8n-workflows: evidence-based workflow-template source evaluation

**Date checked:** 2026-10-21  
**Repo:** `mohammadrezanabizadeh41-png/DJMRN-Intelligent-Assistant`, main  
**Verdict:** **ACCEPT AS A FUTURE READ-ONLY WORKFLOW DISCOVERY / REUSE / INSPIRATION SOURCE (CONDITIONAL)**, **NOT** an approved workflow, security authority, adopted n8n runtime, deployed API, production-ready software or committed installation.  
**Full, byte-identical user source:** [SRC-0011, 885 original lines](../inbox/SRC-0011-n8n-workflows-template-library-reuse-discovery-20261021.md), original file `Pasted text(20261021-004424).txt`, **24,578 bytes**, SHA256 `f4aae663d5409866cd3e6e77c77e2e59e7f8ad4e79ed149d11a9ec8be5e97454`, verified Git blob `03436a0c5e6d264e2cd7f3a06ca8adec034c064a`.  
**Related canonical future capability:** [REQ-WFR-001 workflow pattern discovery/reuse](../../02-project-management/WORKFLOW-PATTERN-DISCOVERY-REUSE-REQUIREMENT.md) / [TASK-0019](../../02-project-management/TASK-REGISTER.md); links existing [REQ-TDR-001 Radar](../../02-project-management/TECHNOLOGY-DISCOVERY-RADAR-REQUIREMENT.md), [KB-0007 workflow products](KB-0007-ready-made-workflow-products.md) and [REQ-MPA-001 logical assistants](../../02-project-management/MULTI-PERSONA-SPECIALIST-ASSISTANTS-REQUIREMENT.md). **Active G1 stays untouched.**

## 1. Project authority and current practical context

DJMRN user's ordinary UX must eventually be `natural Persian message → trusted assistant/tool choice → authorized background action → source-cited understandable reply`, not per-task manual PowerShell. The current engineering milestone is [TASK-0017](../../02-project-management/TASK-REGISTER.md), G1 read-only Jan/ChatGPT readiness **PARTIAL** after real RAM snapshot and Jan shortcut basename discovery. CAP-006 already has a real two-source read-only technical PASS but no chat→tool implementation. System **8 GiB physically installed, ~5.88 GiB Windows usable, latest user snapshot only ~1.73 GiB available**, no current local n8n benchmark or approved install.

For future automations, first check **existing DJMRN capabilities + native workflow logic + trustworthy external template sources**; reusable templates are *external untrusted examples*, never authority over GitHub decisions, permits, credentials or architecture. n8n JSON logic can potentially be **translated into Python, Node-RED, Activepieces or simple bounded DJMRN code**, not necessarily imported into n8n. Avoid rebuilding an existing Workflow Discovery catalog or creating a second Technology Radar: the new capability's distinct job is matching **user task → reusable automation pattern → review/adaptation recommendation**, whereas Radar's job is **monitoring technology/sources and idea signals**.

## 2. Actual upstream evidence / precision about published counts

**Primary source**: [Zie619/n8n-workflows GitHub repository](https://github.com/Zie619/n8n-workflows), observed branch `main`, upstream commit **`94007c1445d9258a7da116646b79473e7c7c3282`**. GitHub REST response on 2026-10-21 showed real PUBLIC, NOT archived repository, MIT repository-level license ([upstream LICENSE](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/LICENSE)), and an active main Git tree. License for the **template-collection repository** does not settle rights to imported third-party assets or commercial licensing for the **n8n runtime**.

- [Upstream README at that revision](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/README.md) **publishes**: **4,343 workflows / 365 integrations / 29,445 nodes / 15 categories**, `100% Import Success`, `Production-Ready`, `<50MB RAM` and `<100ms search`. These are **upstream README claims**, not independently audited DJMRN observations or guarantees of security/performance on the Lenovo.
- **Independent Git tree count** from the **same upstream `main` commit**: **2,061 tracked `.json` files directly under `workflows/`** (all recursive subdirectories), across **188 distinct immediate integration-named subdirectories** in this tree. These are a **different counting unit** than the README's 15 topical categories. README's 4,343 could include an external/generated collection, a larger deployed DB or an earlier claim; **the difference is unresolved**. Do not claim 4,343 individually inspectable checked JSON files exist in the current Git tree. `2,061` is an observed **tracked-path count**, **not** a validated count of unique, runnable, safe, nonduplicate automations.
- README documents a public **[browser-facing GitHub Pages catalog](https://zie619.github.io/n8n-workflows/)**, local Python/FastAPI + SQLite FTS5 search API (`/api/search`, `/api/workflow/{id}`, etc.), possible Docker install, and online discovery. Official source [api_server.py](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/api_server.py) contains FastAPI paths and workflow database handling; [workflow_db.py](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflow_db.py) shows SQLite FTS5 indexing. **Reading repository source/README does NOT independently test deployed site's availability, authorization, returned corpus count, API quotas, speed, completeness or request egress**. Browser Pages UI and local FastAPI **are distinct deployment paths**; do not assume a remote Pages site directly exposes the local Python API or automatically gets private credentials.
- GitHub repo-level MIT license confirmed by real `LICENSE` content and GitHub metadata. n8n **engine** is separately a **fair-code/Sustainable Use License** product according to [official n8n documentation](https://docs.n8n.io/), and some engine features are tier-gated. A library MIT label does **not** grant unrestricted hosted n8n services/commercial licensing or free credentials/API access.
- GitHub repository `pushed_at` observed `2026-06-24T14:16:03Z`; `updated_at` reflects other repository activity and is not proof new workflows appeared today. Current README's "Latest Updates (November 2025)" is author text, not today's revision date. **No automatic update feed was checked or monitoring activated.**

## 3. Independent source-JSON spot inspection (READ-ONLY; 3 samples, no execution/import)

Pinned upstream sample workflow records under exact reviewed upstream ref `94007c1445d9258a7da116646b79473e7c7c3282`:

| Tracked JSON sample | File/node observations from actual parsed JSON | Implication |
|---|---|---|
| [Code/GitHub/scheduled](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Code/0667_Code_GitHub_Create_Scheduled.json) | `23` nodes incl `manualTrigger`, `scheduleTrigger`, `github`, `httpRequest`, `code`, other workflow calls; `credentials` metadata present; displayed JSON name = `Manualtrigger Workflow` (not equivalent to filename). | Relevant to future GitHub discovery ideas but multiple trigger/HTTP/code/credential behaviors need per-node inspection. File name is NOT a reliable canonical functional spec. |
| [Filter/RSS scheduled monitor](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Filter/1772_Filter_Rssfeedread_Monitor_Scheduled.json) | `18` nodes incl `rssFeedRead`, `scheduleTrigger`, `filter`, `gmail`, `jira`, `n8nTrainingCustomerDatastore`; credential metadata; `active=false`. | Example reusable feed/filter pattern but contains integration-specific/possibly demonstration nodes, nontrivial account dependencies; **not directly usable** as a no-credential pure RSS alert. |
| [Execute Command/Webhook/Mailgun](https://github.com/Zie619/n8n-workflows/blob/94007c1445d9258a7da116646b79473e7c7c3282/workflows/Executecommand/0097_Executecommand_Mailgun_Automation_Webhook.json) | `10` nodes incl `webhook`, `executeCommand`, `mailgun`, `if`; credential metadata; `active=false`. | Concrete high-risk pattern: incoming network trigger plus possible OS shell process plus outgoing provider. **DO NOT import/execute** without explicit dedicated approval/security containment. |

**Spot-check only:** parsing three JSON files proves presence of these nodes/metadata, not that arbitrary sample code is malware, actually executes any command, sends external data, has exposed raw passwords, or works on any particular n8n release. We did not inspect all node parameter payloads for embedded secrets (nor replicate them to private repo). The official n8n [community-node risks](https://docs.n8n.io/integrations/community-nodes/risks.md) warn about arbitrary code and data access; [JSON export/import](https://docs.n8n.io/build/manage-workflows/export-and-import.md) explicitly warns that credential names/IDs and sometimes HTTP auth headers can remain in exported workflows. These support DJMRN's **deny-by-default credential and code review policy**.

## 4. Same-role alternatives / neutral source comparison

| Source for finding existing flow patterns | How to use as REFERENCE | Strength | Caveat |
|---|---|---|---|
| **Zie619 n8n JSON catalog** | Public GitHub Pages search or directly inspect a **small number** of pinned JSONs from GitHub. | Repository-path/commit provenance, full node graph examples; MIT repository code. | Self-reported 4,343 != observed 2,061 tracked workflow JSONs; no auto trust, old node versions/third-party API/cost/credentials. |
| [Official n8n workflow templates](https://n8n.io/workflows/) | Compare maintained examples with specific workflow needs. | Official first-party ecosystem and node documentation. | Still n8n-shaped; templates may invoke paid providers, and engine has separate license/hosting requirements. |
| [Activepieces template library](https://www.activepieces.com/docs/flows/template-library) | Search by description/category; preview apps/pieces and steps. | Official ready-to-customize template previews and explicit setup information; alternative flow engine. | Requires distinct platform/pieces/hosting entitlements for execution; not interoperable JSON and not proof of free services. |
| [Node-RED Flow Library](https://flows.nodered.org/) | Browse nodes, flows and collections for reusable pattern ideas. | Open community ecosystem and direct importable flow examples. | External nodes and credentials, Node-RED-specific flow semantics and license/security review. |
| Dify/Flowise/Langflow galleries and DJMRN native patterns | Additional **candidate** sources for LLM/app templates, use only if matched to need. | Potential AI automation examples. | In this round **not independently audited**; cannot assert quality/size/permissions. |

**No vendor winner** from the catalog-only comparison, and no claim n8n should replace existing D-015 chat core, Windows Scheduler, cloud tools, B/C capability interfaces or future Agent/Workflow selection.

## 5. Exact per-candidate security, compatibility and cost intake

For a future **user-authorized READ-ONLY** match/search result, capture:
`source_id, upstream_repo, source_commit, path, file_blob_sha, workflow_original_name, stated_intent, category_tags, node_type_versions, triggers, accounts/credentials_metadata, endpoints/external_destinations, webhooks, community/custom nodes, code/executeCommand/FileSystem operations, data egress, persistent_state, retries/idempotency, rate_limits, estimated_cost, provider_region_and_access, commercial/license, n8n_runtime_version, alternatives, reimplementation_effort, synthetic_test_plan, evidence, reviewed_at, reviewer, verdict`.

Required reject/review gates:
- **External JSON is untrusted data**, not instructions from the user or an import script. No user email/credentials/cookies/OAuth/API keys added to GitHub or taken from downloaded snippets. Untrusted expressions, commands, package installs and templated HTTP URLs must be inspected before any execution; `CredentialMetadataFound` by itself is not proof of secret leakage.
- Network webhooks, external API calls, Code nodes, Execute Command, third-party/community nodes, filesystem writes and any `download+execute` remain **BLOCKED UNTIL EXPLICIT APPROVAL**. No control-plane/agent auto-run from these sources.
- Validate node availability, version, expression syntax, credential schema and API deprecation. In a non-n8n implementation, **translate conceptual sequence, not blindly transplant JSON nodes**, preserving error/retry/limits and data rights.
- Regional/legal availability and renewable Free Tier/card/overage constraints must be **rechecked for EACH provider**. Repo MIT != free remote OpenAI/Gmail/CRM usage or n8n engine license.
- Template match coverage `60/80/90%` in user source is an **illustrative hypothetical score, not computed evidence**; matching/effort must use explicit review and provenance. No silently generated confidence scores.
- API search, Pages browsing, clones, code mirrors and local indexes have distinct exposure/performance; a future catalog crawler/index must comply with source licensing and rate limits and be explicitly authorized. With recent laptop G1 **1.73GiB available**, prefer **selective remote/GitHub read-only inspection** first, no clone/Docker/n8n/search-server at this stage.

## 6. Practical DJMRN-specific use cases, benefits and limits

Potential near-term value (when explicitly requested, *not an executed/working job now*):
1. Build a **GitHub RSS release/watch → deduplicate → inspect official announcement → optional AI summary → approval → notify** automation using existing (sanitized) pattern(s), rather than composing every connection from nothing. Fits REQ-TDR-001; historical DJMRN cloud schedule is **separate older project** and not an approved migrated runtime.
2. For freelance client requests such as **Telegram lead intake → CRM update → quality filter → drafted response**, find existing patterns and estimate provider permissions/fees, then submit a proposal; never silently connect customer credentials or violate messaging platform policies.
3. Curate low-cost **audio/video/content/YouTube workflow ideas** using metadata and proven official third-party APIs; **actual commercial demand/profit** is speculative, not established by many templates.
4. Assistant roles `Automation Scout, Compatibility Reviewer, Security Reviewer, Cost Reviewer, Adapter` are **logical workflow steps or specialist profiles**, not a mandate for multiple Agent OS processes/models.

**A plausible smallest future acceptance test (NOT AUTHORIZED OR EXECUTED):**
- User chooses **one actual need** as a Persian chat message.
- Using online/GitHub read-only sources, retrieve **up to three relevant candidates** and their actual pinned JSONs/commit/path; no installation/clone.
- Extract trigger/actions/code/credentials/providers, compare one candidate to simple native flow and one official alternative. Produce `REUSE / TRANSLATE / BUILD / REJECT` verdict with specific red flags, source and manual time/complexity estimates as estimates.
- **PASS** only if real relevant pattern and evidence-backed time/cost/compatibility benefit emerge, with manageable paid/region/privacy/security requirements. **FAIL/DEFER** if source mismatch, no relevant candidate, unreviewable execution, excessive dependencies, no real savings.
- **No JSON execution, API credentials, workflow import or background monitor** in that pilot; running even a synthetic imported workflow is separate later permission.

## 7. Current decision and handoff

**Source-level value: CONDITIONAL YES.** Register Zie619/n8n-workflows as a **discovered/official-repo-spotchecked candidate source** of workflow patterns, plus official n8n template gallery, Activepieces Template Library and Node-RED Flow Library as comparators. This is **not** automatically an indexed source, monitored Radar feed or an adopted external trust authority.

**Immediate benefit:** low-cost **lookup/learning/reference** for future user tasks; no local memory overhead or installation if using existing browser/GitHub read-only research.  
**Unproven:** deployment/resource use, real import success, 4,343 distinct available workflows, 365 provider current validity, up-to-date APIs, execution correctness and saved time on a real DJMRN workload.  
**Status:** `SOURCE REGISTERED / RESEARCH SPOT-CHECKED / FUTURE WORKFLOW PATTERN DISCOVERY CANDIDATE / NO RUN / G1 UNCHANGED`.  
**The approved active task is still G1:** verify current Jan executable/version and available ChatGPT Plus UI features without running models or changing settings. The new source does **not** block or change G0/G1/TASK-0017. Any long-running future discovery, Agent management, local n8n runtime or cloud connection needs its **own user approval**.
