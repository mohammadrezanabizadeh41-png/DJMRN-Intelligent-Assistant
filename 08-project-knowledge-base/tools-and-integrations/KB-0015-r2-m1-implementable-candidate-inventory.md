# KB-0015 — R2/M1 Existing Implementable Candidate Inventory (WA0008)

**Date:** 2026-10-22 | **Status:** CURATED / STAGE2 DISCOVERED 18 IDENTITIES / ACCEPTED WITH GAPS / NO ARCHITECTURE SELECTED  
**Raw authority:** [WA0008 immutable source](../../04-work-research-bridge/responses/WA0008.md), [independent review](../../04-work-research-bridge/reviews/WQ0008.md); [WA0007 Source Atlas](../../04-work-research-bridge/responses/WA0007.md) and [KB-0014](KB-0014-r2-m1-ready-solution-source-atlas.md); Source Register pointer SRC-0017.  
**Keywords:** R2/M1, first chat, M1, ready-made assistant, آماده, اقتباس, build vs adopt, Jan, Cherry Studio, AnythingLLM, Conduit, 5ire, Chainlit, Vercel chatbot, AI Dev Gallery, MCP SDK, CAP-006, ripgrep, Qwen3.

## User-relevant conclusion

**A source-backed menu exists, but the complete M1 workflow has not been demonstrated by any candidate**: Persian user message → independent local chat UI on Windows → *actual policy on executor* restricting tool to exactly 1–2 user-chosen Markdown files → deterministic source line/hash evidence or fail-closed refusal → no daily PowerShell → acceptable measured on-device RAM. Source-verified means **the upstream source/docs exist and were inspected**, NOT tested, safe or recommended. Marketing citation or MCP annotation is not proof of the file-level boundary.

| Family | IDs | Identifiable artifacts (official upstream) | Stage3 priority and caveats |
|---|---|---|---|
| **Complete apps** (5) | CAND-0001..0005 | [Jan](https://github.com/janhq/jan), [Cherry Studio](https://github.com/CherryHQ/cherry-studio), [AnythingLLM](https://github.com/Mintplex-Labs/anything-llm), [Conduit](https://github.com/runningpixels/conduit), [5ire](https://github.com/nanbingxyz/5ire) | Existing app UI reduces UI construction; check real tool policy/approval, local provider and Windows binaries, app/version risks, AGPL/custom license. 5ire **LICENSE HOLD** for adapted/commercial redistribution until conditions assessed. |
| **Reference starters** (4) | CAND-0006..0009 | [Chainlit cookbook](https://github.com/Chainlit/cookbook) (one collection of 3 demos), [Vercel chatbot](https://github.com/vercel/chatbot), [MS AI Dev Gallery](https://github.com/microsoft/ai-dev-gallery) C# chat sample, [Desktop Assistant](https://github.com/jrubiosainz/desktop-assistant) | Not full deployed product; Chainlit sample action UI **not gate** and cookbook root license UNKNOWN (copy/redistribute HOLD); Node/cloud or shell/process risks need inspection. |
| **Tool transport SDKs** (4) | CAND-0010..0013 | MCP [Python](https://github.com/modelcontextprotocol/python-sdk), [C#](https://github.com/modelcontextprotocol/csharp-sdk), [Go](https://github.com/modelcontextprotocol/go-sdk), [Rust](https://github.com/modelcontextprotocol/rust-sdk) | Transport only; do not mistake availability for default-deny or a chat UI. Compare direct typed command/JSON without MCP too. |
| **MCP filesystem server** (1) | CAND-0014 | [MCP filesystem reference](https://github.com/modelcontextprotocol/servers) | Allows many operations incl write/move/delete and allowed directories, NOT exact 2-file permission boundary; should not be plugged unrestricted. |
| **Text search** (1) | CAND-0015 | [ripgrep](https://github.com/BurntSushi/ripgrep) | Can return lines/paths but not whole chat/scope/hash; inspect fixed argv versus existing CAP-006 (no shell fallback). |
| **Inference engine** (1) | CAND-0016 | [llama.cpp](https://github.com/ggml-org/llama.cpp) | Model engine only; tool template/RAM/Windows CPU resource testing NOT RUN. |
| **Project baseline** (1) | CAND-0017 | [CAP-006 pinned source](../../05-assistants-and-capabilities/src/document_search_v0/docsearch_v0.py), [NEW-V0004](../../06-tests-and-evidence/logs/NEW-V0004-20261021.md) | Real bounded past Windows file search (user-run) with source+line/hash, no local standalone conversational UI, not a secure general sandbox. Keep as baseline in all comparisons. |
| **Model weight** (1) | CAND-0018 | [Qwen3-1.7B](https://huggingface.co/Qwen/Qwen3-1.7B) | Documentation-only, exact revision/GGUF/tool-call/Persian/8GiB fitness unverified; model is not assistant app. |

**Count check:** 5 + 4 + 4 + 1 + 1 + 1 + 1 + 1 = 18 distinct `CAND` IDs; `SOURCE_VERIFIED=17`, `DOC_ONLY=1` under Work's evidence nomenclature. No new product/runtime selection. Raw WA S4 has each exact commit/tag, license blob/version and upstream evidence; this KB is a curated navigation summary, not a second copy.

## Research caveats checked by coordinator

- Actual Git blob and the complete 67,337-char WA0008 were identical; one added Work file on GitHub main with no unrelated modifications. Three live Notion source versions/edits match Work's reported source snapshots.
- Targeted upstream pinned primary sources independently confirm Jan Apache-2, Conduit AGPL-3, **5ire explicitly modified Apache-2.0 plus additional commercial restrictions**, Chainlit sample Continue/Cancel UI without execution protection, and MCP filesystem reference listing mutation tools and directory authorization. Remaining source/version/security/maintenance claims in WA are **not all independently reverified**.
- The report shows only **8 bounded results from four native GitHub repository queries**, with a subset relevant; different catalog pages and direct upstream source reads supported remaining identities. No complete per-channel native search coverage, no tested apps, and no regional/provider rights verified.
- Model weight size/real RAM, UI Persian, offline behavior, dynamic tool-policy enforcement and third-party account privacy remain UNKNOWN. No user device or email involved.

## Conditional Stage3 comparison bundles (not preselected)

WA S5 hypothesized seven diverse routes: (1) ready MCP desktop host Cherry or Conduit with private scoped tool; (2) document-focused AnythingLLM; (3) conditional installed Jan + CAP-006; (4) Chainlit+Python MCP+CAP-006 with cookbook permission HOLD; (5) MS .NET chat sample + C# MCP+CAP-006; (6) existing capability without new app (not yet full M1); (7) Vercel browser/web app + private tool bridge with privacy/hosting cost gates. 5ire maintained as conditional license-held candidate, smaller `desktop-assistant` requires shell scrutiny; neither excluded merely by popularity. These are **assemblies and review paths**, NOT seven already-existing complete systems.

**Next:** [WQ0009 Stage3 comparator](../../04-work-research-bridge/requests/WQ0009.md) after coordinator acceptance; Work report-only `WA0009` will examine adopt/adapt/build, estimated burden with uncertainty, user-safe implementation decision packet and optional minimal **future** real test scope. User and coordinator choose. No approval to install or execute.
