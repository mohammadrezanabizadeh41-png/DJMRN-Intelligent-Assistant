# Goose G3 — First real on-device chat generation observed (Gemma 3 1B), with context-tag leakage

**Date:** 2026-10-22. **Source:** direct user screenshot of native Goose Desktop chat UI, message sent at **11:23 PM** local, following G2 built-in local model selection. This report documents the screenshot as user-run evidence, not code execution by the coordinator. Sensitive personal directory username has been **redacted**; do not store unredacted screenshots or file paths from the rendered response in public/project logs.

## Inputs / visible results
- User sent simple Persian greeting: **«سلام»** in native Goose chat.
- Goose displayed a model-generated assistant bubble consisting of Persian **«سلام»** followed by raw context tags: `<turn-context>`, `<current-time>2026-10-22 23:23:00 +03:30</current-time>`, `<working-directory>[LOCAL_USER_HOME_REDACTED]</working-directory>`, closing `</turn-context>`.
- This is the first **user-observed actual text-generation result in Goose** after the native local-model picker had marked `ggml-org/gemma-3-1b-it-qat-GGUF:Q4_0` (687 MB) **Ready**. Generation works at least for a tiny prompt. The model/backend provenance in this particular screenshot is inferred from the immediately preceding G2 selected model + click, not exposed in the cropped chat screenshot itself; do not claim cryptographic process-level confirmation.
- **Quality defect:** unexpected raw conversation-context tags and local working-directory metadata appear in model answer. Most likely a mismatch between 1B model instruction-following/chat-template behavior and Goose agent context formatting, **hypothesis only** (root cause not verified). The fact a current-working-directory field appears is **not evidence the model read any user file**; no tool execution visible.
- No file-system/shell/MCP plugin access, model tool-calling success, broader Persian reasoning, prompt isolation, data exfiltration, durable auto-restart, or performance/memory baseline is verified by the screenshot.

## Interpretation / acceptance
- Upgrade goose from `G2_LOCAL_CACHE_READY_UI` to `G3_BASIC_TEXT_GENERATION_USER-VERIFIED`, but **not** `PRODUCTION_CHAT_PASS` or `TOOL_PERMISSION_PASS`.
- This eliminates immediate need for Jan/Ollama/custom llama-server bridging just to get *some* text in Goose. It **does not yet demonstrate acceptable natural-language UX**, because an end-user greeting should not include internal metadata. Maintain minimum permissions (no shells, broad workspaces, new extensions, external accounts or personal file grants), G3B Windows file guard CLOSED.
- **Next smallest GUI-only test:** in same Goose chat, send one innocuous short Persian prompt: `فقط در یک جمله بگو چه کمکی می‌توانی بکنی. هیچ برچسب یا اطلاعات سیستمی ننویس.` Check text quality and whether raw context tags recur; do not tune extensions/providers or launch multiple large models yet. If raw system tags recur, classify model-in-Goose chat quality failure and evaluate a model with better instruction-following/tool competence *only after low-RAM feasibility*, or park candidate without repeated troubleshooting.
- User decision: maintain preference for **zero recurring manual PowerShell/server startup**. Do not install dependencies or auto-run scripts just to fix Goose during candidate evaluation.

**Status:** G3 BASIC LOCAL INFERENCE VERIFIED BY USER SCREENSHOT / CHAT QUALITY LIMITED / INTERNAL CONTEXT LEAK VISIBLE / SECURITY ACTION NOT PROVEN / D-005 OPEN / KYNXA PARKED / G3B CLOSED.

Related [G2 local-cache model chooser evidence](GOOSE-G2-USER-LOCAL-CACHED-MODELS-READY-20261022.md), [permanent models paths](../../07-operations-and-continuity/LOCAL-ENGINE-AND-MODEL-PATH-REGISTER.md), [ready-made host candidate queue](../../03-architecture-and-tools/READY-MADE-HOST-EVALUATION-QUEUE-20261022.md).
