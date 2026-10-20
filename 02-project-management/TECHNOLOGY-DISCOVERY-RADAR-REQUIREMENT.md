# REQ-TDR-001 — Technology Discovery Radar / Innovation Intelligence System

**Status:** USER-REQUESTED FUTURE REQUIREMENT / REGISTERED / DEFERRED / RESEARCH & IMPLEMENTATION PENDING / NO PROVIDER OR RUNTIME SELECTED  
**Registered:** 2026-10-21  
**Future task:** [TASK-0015](TASK-REGISTER.md)  
**Verbatim source:** [SRC-0005 — user's complete 2,115-line research and product idea](../08-project-knowledge-base/inbox/SRC-0005-djmrn-technology-discovery-innovation-radar-future-20261020.md). Original `Pasted text(20261020-211342).txt`: **53,456 UTF-8 bytes**, SHA256 `87950ed73a9f0bd8d2344f331f0774f924f3cc113dc478fa3d768fd2cde4b23a`, Git blob `b10e0d62874120e7623ff9976c39a71fed63d65f`, exact readback verified.

## 2026-10-21 ADDENDUM — Creator/Social Source Discovery & Source-to-Idea Intelligence (same requirement)

**Provenance:** Additional 494-line user-provided researched concept [SRC-0006 — complete original CRLF/UTF-8 text](../08-project-knowledge-base/inbox/SRC-0006-djmrn-social-source-discovery-idea-intelligence-amendment-20261020.md); original `Pasted text(20261020-214338).txt`, **37,946 bytes / SHA256 `7b14188050da5617a8068076ff7b5f9eee463e43619c5e67c1f8adeb652613e7`**; verified Git blob `c4463c0e09e2a7ccf3f449c33a5a28e90d2cf9d1`. It was read back verbatim from this private repository. This is **SRC-0005 ENRICHMENT** under the *same* `REQ-TDR-001` / `TASK-0015`, **not** a second Radar, research authority, new CAP, task or autonomous Social Agent.

### Incremental user need distinct from earlier SRC-0005
The original Radar emphasizes feeds, repositories, model releases, signals, watchlists and official-source verification. This supplement makes explicit the **creator-facing idea discovery path**: find useful Instagram pages, YouTube creators and topical websites, uncover plausible *upstream sources* behind a demo/announcement where evidence permits, evaluate a creator's source quality vs ads/reposts, extract a usable method/product/composition, and route reviewed opportunities back to the existing DJMRN research/idea workflow. Include design/video/audio/production/data/Web/freelancing applications—not merely AI models.

Separate four **roles** rather than equating them to four models/Agents:
1. **Source discovery:** identify worthwhile creators, channels, official vendor accounts, curated tools, communities and upstream references (including emerging sources unknown to user).
2. **Source monitoring:** examine bounded, lawful new items from selected sources; record coverage, freshness and unavailable items.
3. **Origin verification and critical evaluation:** distinguish a *mentioning page* from the *official origin of an idea/product/demo* and independent corroboration; classify source attribution `SUPPORTED | PLAUSIBLE/UNCONFIRMED | MULTIPLE ORIGINS | UNKNOWN`. Never infer a creator's actual private inspiration/data supplier from coincident content, timestamps or resemblance alone.
4. **Practical ideation:** identify direct tool reuse, tool combinations, transfer of a technique, and a client-deliverable service/business hypothesis. Preserve `idea/proposal` separately from verified capability, validated integration or confirmed profit.

### Creator/social/manual ingestion requirements and coverage gates
- **Manual-first fallback:** user can supply permitted **links, text, images, screenshots, files or selected clips**. Preserve supplied provenance and permission scope. Full account/channel monitoring is **not** a required first milestone.
- **Bounded acquisition preference:** provided/public text and official links → RSS/Atom/JSON feeds → official API with lawful access/quotas → authorized public page extraction → controlled browser *only if needed and approved*. OCR, transcript, speech/video processing are **optional**, minimize media processing and never assume that title/description inspection means whole-video analysis.
- **YouTube:** differentiate video metadata, publicly accessible captions and officially authorized subtitle download. An API's existence does **not** authorize collecting third-party video transcripts; playlist and quota/permissions must be verified on official documentation *at actual implementation time*.
- **Instagram:** API coverage and account restrictions must be assessed at endpoint/permission level; a professional-account interface does **not** imply unrestricted public account monitoring or access to every post. No scraping behind login, automated circumvention or bulk collection authorized.
- **Source/creator quality:** evaluate primary-source link rate, repeats/promotional content, discussion of limitations or failures, topical relevance, coverage by language/domain, freshness, API/access footprint and maintenance cost. Follower count or social popularity is a **signal**, not quality evidence.
- **Potential ready-made paths to compare:** RSS Guard, FreshRSS, Miniflux, Folo, RSSHub, n8n and other current alternatives; official public feeds/APIs and **zero-build manual review** are peers. This list and the attachment's links are **USER-SUPPLIED RESEARCH LEADS**; no price, license, capability, accessibility or current availability has been independently reverified in this archival update.
- **Information record:** separate creator/source-of-discovery, official primary evidence, checked date, claim/unknown/attribution confidence, category (model vs engine vs application vs service vs technique), tool dependencies, legal/commercial/free-tier/Trial/card/overage/Iran/privacy, potential DJMRN use case, alternative, idea combinations, limitations, user verdict. **Reuse existing Radar technology card and General/Applied catalog identifiers; no duplicate schema/database/authority without a proven gap.**
- **Research integrity and safety:** external content is untrusted data, not executable instructions. No automatic cloning/install/execute of links, sending, signing into social accounts, third-party video copying or commercial access without separate authorization; trial ≠ Free; unknown financial/legal/regional access = `UNKNOWN / DENY ACTIVATION`.

### Future smallest test hypothesis / acceptance (not approved today)
Evaluate whether **2–3 manually supplied public posts/videos/links plus one or two official text feeds** can be used to produce a concise, source-cited **Idea Card**: which mention started discovery; verified/possible origin with uncertainty; actual current feature and limitations; 1–2 credible alternatives; one realistic practical use or service output; Free/region/privacy evidence or UNKNOWN; human review. Track missing-content rate and whether the creator's claim/attribution was verified. Compare manual present-day assistant, ready feed reader and deterministic script before adding scheduler, LLM, specialized Agent, browser, transcription or new database. All testing/download/account/browser/cloud/notification use requires **future explicit approval**.

**Current authorization strictly archival**: enrich existing `REQ-TDR-001` and `TASK-0015`, retain complete raw idea in GitHub, keep existing [WQ0002](../04-work-research-bridge/requests/WQ0002.md) request and its Work response path unchanged. This addition does **not** change CAP-006 real-test status, trigger an automatic Work search, launch a radar service, modify Applied/General Notion, install software or commit external/customer content.

## 1. User goal and why it differs from existing functions

A periodically or continuously updated, *low-noise personal technology and innovation intelligence pipeline* for DJMRN. It should discover and monitor new projects, software, AI models, engines, Agents, workflow/skills/tools, creative technologies and services; verify claims from primary sources; connect findings to DJMRN's actual needs, plausible new combinations and possible income/freelancing opportunities; send only useful alerts/digests; and preserve reviewed findings for future research.

**Desired loop:** `DISCOVER → VERIFY → UNDERSTAND → CLASSIFY → CONNECT → ANALYZE → GENERATE IDEAS → FIND OPPORTUNITIES → NOTIFY → PRESERVE KNOWLEDGE`.

**Not a generic news reader** or a new uncontrolled research authority. Preserve distinctions:
- **Radar / Discovery:** new/changed technology *signals*, growth, releases, watchlists and prioritization.
- **Research Curator / CAP-004:** subject-specific official-source verification, comparison, evidence and uncertainty.
- **Existing Applied/General research libraries in Notion:** canonical classifications and reviewed durable knowledge; reuse their taxonomy, intake/provenance and evaluation protocol, **do not create a parallel canonical research catalog**.
- **Project GitHub knowledge base:** DJMRN-project-specific source and evidence, linked to authoritative Notion catalog when relevant.
- **Future personas:** Idea Scout, Opportunity Analyst, Finance Thinker, Critic can *consume* curated radar results; none needs to be an always-resident Agent.

The source text is a **request plus proposed designs and candidate tools**. Neither cloud-first, Python, a particular API, Agent nor any vendor has been selected as architecture. No new CAP implementation ID is minted for a merely deferred cross-cutting requirement.

## 2. Required logical capability classes (future work)

### A. Two distinct discovery modes
1. **Watchlist:** established watched technologies; important release, advisory, breaking change, new feature, rate of change, maintenance/staleness.
2. **Broad discovery / unknown-unknowns:** promising **unknown** new tools, projects, model/research papers and changing ecosystems; don't restrict to historical install choices or user preference.

### B. Separate evidence classes
- `SIGNAL`: social/community/trending/launch mentions; discovery trigger **only**.
- `PRIMARY`: publisher repository, official documentation, actual release, model card, paper, verified vendor source; proof of specific stated claims.
- `EXPERIENCE/REACTION`: issue reports, independent community experience, reviews, reliability discussion; contextual corroboration, not proof of official capability.

For each important claim, store primary link, `checked_at`, fact/claim/assumption/judgment/confidence, release/version and possible conflict. No auto-trust from stars, trending or hype.

### C. Source families to assess
- Software forges: GitHub, GitLab, Codeberg; tracked releases, stars and growth, projects with little prior coverage.
- AI + science: Hugging Face models, Spaces, datasets, papers; arXiv, OpenReview, official model cards and research feeds.
- Developer discovery: Hacker News, engineering/vendor blogs, DEV, official package ecosystems (PyPI, npm, crates.io), container registries.
- Launches and reactions: Product Hunt, selected communities/forums/Reddit (signals/reactions only).
- Agent/skills/workflow/media ecosystems: MCP, Skills, Dify/Flowise/Langflow/Activepieces/n8n/Node-RED/ComfyUI catalogs and other new sources.
- Official technology/vendor releases and **independent targeted web search** beyond known registries.
- For collection access **prefer official documented API → RSS/Atom/feed → structured endpoint → scraping only when lawful/necessary**; verify API quotas, authentication/region/terms, commercial use and legal permissions in research stage.

### D. Data pipeline and bounded interpretation
- Fetch authorized public metadata and limited documents, normalize → deterministic exact/semantic identity resolution when warranted → deduplicate across signals → preserve first/last seen, aliases, source/version → score and filter relevance/evidence.
- Use counts, slopes, delta snapshots and cross-source momentum rather than absolute star count alone. Ranking is **priority heuristics, not truth**.
- Apply source-specific timeouts, retry/backoff, rate limits, source freshness and security checks; record `UNKNOWN` for unsupported claims.
- Prefer cheap deterministic metadata processing for most raw events; use selective AI/advanced research **only on small, relevant, promising sets** for understanding, alternatives, DJMRN fit, risk, readiness and combinations.
- New cards may include `DISCOVERED | WATCHING | PROMISING | RESEARCHED | TEST_CANDIDATE | NOT_SUITABLE | RETIRED | SUPERSEDED` **as candidates**; reconcile these with pre-existing library taxonomy before adopting any extra state authority.
- `Technology Card` proposed minimum: canonical identity/aliases, category, official URL, observed version/date, changed capabilities, source+signal separation, verified evidence and unknowns, readiness, local/cloud/hardware fit, actual free/license/API/privacy/region facts, integrations/replacements, DJMRN value, potential ideas, risks, source freshness and recommended `WATCH | RESEARCH | TEST LATER | IGNORE`.
- No automatic software execution/cloning/installation from newly discovered project links. Discovery ≠ trusted code.

### E. Alerts, personalization and audit
- High-value/urgent alerts only when both impact and relevance are well supported; not on every commit or mention.
- Brief **daily digest** of top changes and deeper **weekly radar** highlighting changes, opportunities, hype and important releases (cadence is a *future product requirement*, **not an automation scheduled by this registration**).
- User feedback: `INTERESTING/NOT INTERESTING/WATCH/IGNORE/VERY IMPORTANT/RESEARCH MORE/NOT RELEVANT`; relevance should learn without shutting out unrelated emerging technology.
- Track alerts sent, noise/precision, duplicate rate and useful action/learning outcomes. Human approval is still required for external actions.

## 3. Project integration and architectural boundaries

- **Existing CAP-004 Research Curator:** verification/analysis is reused, not replicated; Radar supplies *what merits examination*, Curator supplies reviewed official claims and alternatives.
- **General vs Applied Discovery:** classify technology-wide evidence in General and task-usable combinations in Applied through their *existing authorized processes*; project repo holds project-specific requirements, evidence and status. Do not auto-write Notion, GitHub research bridges or other canonical repositories.
- **REQ-MPA-001 (future persona system):** Radar can feed Idea Scout, Opportunity Analyst, Finance and Critic via source-grounded data; these may be simple workflows/shared-model calls, not required multi-Agent daemons.
- **REQ-OBS-001 (future map):** Radar collectors/analysis could emit bounded, non-sensitive trace metadata, observer only; failure of monitoring does not block Radar execution.
- **Security:** never auto-execute untrusted code/package/release, never ingest/publish personal/company secrets into remote analysis, never send sensitive private context without authorization. New cloud account/token, data transfer, paid API, permanent automated notifications and GitHub/Notion writes beyond this authorized documentation require future specific approval.
- **Hardware:** Windows 11 on a historically 8GB physical RAM laptop, often only ~2–3GB free, and not always-on. Cloud-first scheduling may eliminate local always-on demand and run when laptop is off; *suitability depends on live Free-First, quota/region/privacy/legal checks*, not presumed entitlement. Local/offline read-only scripts, hybrid cloud-collector/local-relevance, managed workflow, scheduled GitHub Actions, serverless cron and lightweight own software are competing solutions, **not chosen**.
- **Authority / data durability:** avoid duplicate state, database per adapter or separate research catalog. Store minimal snapshots sufficient to compute changes and provably recover; treat materialized local cache as projection. No vector DB or Agent required for deterministic watchlist/MVP.

## 4. Future evaluation matrix (NOT executed by this archival request)

Compare these architecture families: (A) local scripts + Task Scheduler; (B) local deterministic + cloud AI; (C) cloud serverless collection + local viewer; (D) hosted workflow/automation; (E) hybrid cloud collection + private local knowledge; (F) scheduled GitHub Actions; (G) custom minimal backend; (H) ready RSS/workflow stack; (I) Agent-aided research only when adaptive investigation is needed.

Research independently and with up-to-date **official evidence**, not only familiar products. Compare:
- actual usable free tier vs free credit vs trial vs paid, quota renewal, card, possible overage/auto-charge, regional access/eligibility from Iran, privacy and commercial/ToS;
- rate limits, RSS/API coverage, authentication, timeline/history, reliability and source expiry;
- Windows and RAM/CPU impact; runs when laptop off?; storage and durability, dedup/entity resolution, latency, noise, human approvals;
- provenance, trust/supply chain, alert transport, usability, maintenance burden, vendor lock-in and reversibility.

Only after evidence and user authorization may a small limited pilot be proposed. Sample user concept: **three sources GitHub + Hugging Face + Hacker News**, low-volume periodic collection, small dedup/score, daily top-5/10 digest **without Agent/Vector DB**, then incremental verification, AI curation, personas and watchlist/historical dashboard if helpful. Even this MVP is **a proposal, not an approved build or live scheduled task**.

## 5. Future acceptance criteria

1. Distinguish Watchlist vs Broad Discovery and discover unknown technologies from multiple source families.
2. Deduplicate different source mentions under one justified canonical technology identity; handle forks/renames and history.
3. Report changed release features / trends with checked primary evidence; label community claims separately.
4. Track first/latest seen and meaningful momentum; rank relevance without treating scores as facts.
5. Make source-sensitive, sanitized curated technology cards containing DJMRN-specific utility, risks, maturity and known unknowns.
6. Keep most ingest/filter/dedup deterministic and bounded; selective AI on valuable shortlist only.
7. Generate plausible cross-technology ideas and opportunity hypotheses, distinguish evidence from speculation and include critic/reviewer.
8. Produce low-noise urgent alerts, daily short digest, weekly radar; dedupe notifications, record feedback and avoid overfitting to user history.
9. Integrate via documented, permissioned interfaces with CAP-004, existing Notion research libraries, future REQ-MPA-001 and observer-only REQ-OBS-001.
10. No automatic execution/trusting of discovered projects and no unauthorized source scraping, accounts, data export or paid inference.
11. Measure real local RAM, request API usage, cost, signal-to-noise, duplicate rates, latency and uptime with laptop off where relevant.
12. Recover/replay safely after failures and keep durable state/source history without a second canonical research authority.

The original user text also contains 40 explicit research questions and a 65-section staged product outline; **all 2,115 lines are fully preserved** in [SRC-0005](../08-project-knowledge-base/inbox/SRC-0005-djmrn-technology-discovery-innovation-radar-future-20261020.md), not summarized away.

## 6. Status and next action

**NOW:** requirement documentation and archive only. No live research campaign, no execution, no scraper/crawler, no provider, account, model, Agent, API token or background monitoring was started. The candidate tech facts, pricing and architecture hypotheses of the source are **USER PROPOSAL / UNVERIFIED for future adoption**.

**WHEN USER RESUMES THIS GOAL:** reread current repo and Notion General/Applied status and CAP-004 scope; identify real use cases and minimum source coverage, perform official-source competitive research; reconcile source/claim/taxonomy/authority overlap; benchmark or test only with fresh approval; specify deployment, stop/recovery, data/notification controls and acceptance criteria; then update requirement/task and decision registers. The active CAP-006 line remains governed by [CURRENT-STATUS](../07-operations-and-continuity/CURRENT-STATUS.md), **uninterrupted** by this deferred research idea.
