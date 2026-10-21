# KB-0014 — R2/M1 source atlas for existing ready-made conversational assistant solutions

**Date:** 2026-10-22 | **Status:** CURATED / STAGE-1 SOURCE DISCOVERY ACCEPTED WITH ACCESS GAPS / NO PRODUCT TESTED, RANKED OR ADOPTED  
**Origin:** [immutable WA0007](../../04-work-research-bridge/responses/WA0007.md) = SRC-0016; [independent coordinator review](../../04-work-research-bridge/reviews/WQ0007.md), checked original [WQ0007](../../04-work-research-bridge/requests/WQ0007.md).  
**Future context:** [R2 three-stage protocol](../../02-project-management/R2-REUSE-FIRST-THREE-STAGE-DISCOVERY-PROTOCOL-20261022.md); existing TASK-0017, [Master Roadmap](../../02-project-management/MASTER-SYSTEM-ROADMAP-20261022.md).  
**Aliases/keywords:** سرچ منابع همیار, ready-made assistant, app-first, chat-to-tool, source atlas, reuse before build, GitHub catalogs, MCP registry, Python starter, C# WinUI, Hugging Face Spaces, stage 1 WQ0007, اطلس منابع.

## Outcome and credible scope

The **29 unique channels (21 observed directory/feed M + 8 official-document mechanism D) across 8 families** in [WA0007 §S3](../../04-work-research-bridge/responses/WA0007.md) are a **discovery map**, not 29 tested apps or 29 successful search queries. Different catalog owners and mirrors are not always independent maintainers. The source prioritization helps avoid writing another full UI/assistant/tool bridge without first checking maintained upstream alternatives.

| Family | Source IDs; examples, NOT product choices | What may be discovered | Coverage gate |
|---|---|---|---|
| F1 Public forges | S01 GitHub, S02 GitLab | source apps, working sample repos, release source | actual query/commit, code search auth differs |
| F2 App/component catalogs | S03 Awesome Selfhosted; S04 SourceForge; S23 Catalogs.dev; S27 AlternativeTo; S28 FossHub | full desktop/web apps vs isolated UI widgets | open upstream; ads/affiliate and OS tags ≠ fit |
| F3 Package/Windows installers | S05 PyPI; S06 npm; S07 NuGet; S08 Go; S09 crates.io; S17 WinGet; S18 Scoop | SDK/bridges vs binary Windows distributions | package metadata ≠ no-shell usable chat program |
| F4 AI/MCP/Skills | S10 Hugging Face; S11 official MCP Registry; S12 skills.sh | Spaces demo, model weights, server transport, skills | card/namespace/install count ≠ security or reliability |
| F5 Official starter/workflow galleries | S13 Vercel Templates; S14 Windows SDK Samples; S15 AI Dev Gallery; S16 Chainlit Cookbook; S24 n8n; S25 Node-RED; S26 Activepieces | source-backed starter, template, scope/approval example | approval UI ≠ enforceable policy; engine/keys/licensing distinct |
| F6 Upstream/news signals | S19 HN Show; S20 MS Foundry Blog; S29 GitHub Changelog | newly shipped/retired app/tool/SDK leads | original release or repo verifies claims |
| F7 Cross-platform metadata | S21 ecosyste.ms | discovery/dedup/metadata link | secondary aggregator, not authoritative upstream |
| F8 Papers | S22 arXiv advanced search | reference implementation/benchmark methods | preprint ≠ Windows/M1 validation |

**Stage2 highest-yield search channels from Work (§S7):**
`S01 → S27 → S03 → S13 → S16 → S14 → S07 → S05 → S10 → S11`. No vendor chosen. Include Go/Rust and less-GitHub forges as at-least-sampled alternates to prevent Python/JS and GitHub bias. Suggested Work info budget: 2 distinct native/search queries per lane if available, <=2 results pages/channel, ~40–60 raw leads before identity dedup (not mandatory hit counts), aim 15–30 materially distinct assets with actual proof. Results marked BLOCKED/PARTIAL stay explicit. Source atlas original keeps full query examples and all 29 links; do not duplicate raw copyrighted text.

## Reuse-first asset decision dimensions for later inventory

- `COMPLETE_APP`: runs as local standalone chat UI **and actually supports safe scoped read-only custom tools** (claims require code/doc evidence).
- `REFERENCE_STARTER`: forkable working multi-file application with chat + tools; adaptation burden not proven.
- `COMPONENT_SDK`: language-specific typed bridge/tool calls, approval, file search, UI, process lifecycle.
- `MCP_SERVER/CONNECTOR`: transport+metadata; permission policy separate; do not expose arbitrary shell.
- `MODEL_WEIGHTS` vs `INFERENCE_ENGINE`: totally separate objects, tool call/FA quality and RAM unknown.
- `WORKFLOW_TEMPLATE`: source code/JSON with dependency & side effect risks; not automatically runnable alone.
- `HOSTED_SAAS`: recurring cost/region/Iran/credential/cloud egress UNKNOWN until verified.
- `NO_NEW_COMPONENT`: CAP-006 existing deterministic search + minimal safe direct chat bridge as baseline; option to reuse existing controlled ChatGPT-connected tools, but Plus custom MCP unavailable/unverified and offline laptop access not implied.

## Stage2 negative evidence and missing sources

- Many npm/PyPI/HF/GitLab/MCP Registry search-query pages blocked in Work's tool: **tool access failure**, not proof the source lacks candidates or is geo-blocked.
- Independent coordinator verified [HF full-text docs](https://huggingface.co/docs/hub/search), [MS Windows App SDK samples](https://github.com/microsoft/WindowsAppSDK-Samples) and [MCP Registry UI](https://registry.modelcontextprotocol.io/); no actual model or product demo executed. Chainlit example child URL could not be fetched by the reviewer web interface and remains Work-reported/UNVETTED.
- Reddit, Codeberg, SourceHut, Gitee, Marketplace/OpenVSX and portable distribution catalogs untested or partial; look for a fallback when stage-two candidates appear overconcentrated.
- Full current product license, release freshness, dependencies, regional terms and private-data controls are **to be checked for each Stage2 artifact** and rechecked before activation.
- Hardware: 8GiB physical vs historical OS-visible RAM; no product-specific benchmark; cloud computation must not be rejected by laptop RAM, but browser/client footprint still matters.

**Next:** distinct WQ0008/WA0008 **candidate inventory only**, followed by independently reviewed WQ0009 Stage3 if authorized. No software installed or any architectural decision made by KB curation.
