# Goose G4 — local Gemma3 1B replies in Persian but self-introduction is incoherent; narrow 4B comparison

**Recorded:** 2026-10-22. **Evidence:** directly user-uploaded screenshot of the Goose chat. The user message in screenshot is **«خودتو معرفی کن؟»**. This is a distinct prompt from a previously suggested one-sentence prompt; preserve actual input and don't claim the proposed prompt was run.

## Observed
- Goose produced a substantial response in Persian. It begins as a self-introduction, but devolves into a long, semantically disordered discussion of instructions, configuration, resources, reading documentation, descriptions, prompts and priorities. It does **not** satisfy a normal concise self-introduction. Apparent internal operational/instruction concepts make it into user output.
- Unlike G3 greeting, **no literal `<turn-context>` markup, `<current-time>` XML or personal working-directory string is visible in this screenshot**. This does not prove internal prompt isolation is generally fixed.
- Current model attributed to native local **Gemma3 1B Q4_0** on basis of G2 saved selection and G3 followed by screenshot; the cropped G4 screenshot does not itself show a model selector or process-level model identity. No tool calls, disk access, model change, memory figure or KYNXA/Jan/Ollama action evidenced.
- Result: **TEXT_GENERATION_PASS**, **PERSIAN_SELF_INTRO_QUALITY_FAIL**, **RELIABLE_AGENT_TOOL_CALLING_NOT_TESTED**; no claim of data exposure beyond the G3 user-home-field shown in prior test (which was redacted when logged).

## Lowest-friction next step and stopping rule
- Official provider docs https://goose.vcorp.ai/docs/getting-started/providers/ show **Goose Desktop sidebar > Settings > Models > Switch models**. A shortcut is the current model label near app bottom > `Change Model`; model changes may take effect in new session. No command line or long-running external daemon required for the switch.
- The native Goose G2 GUI already showed **Gemma3 4B Q4_0 2.4GB Ready** in pre-existing HF cache; try at most **one short self-introduction in a new session** on 4B if GUI allows switch and Windows remains responsive. **Don't run Gemma 3 12B Q2_K (4.4GB)** on this limited headroom. Don't download another model or launch Jan/Ollama/KYNXA concurrently for this test.
- Windows machine: physical 8 GiB RAM, OS visible ~5.88GiB, recent available RAM heavily constrained; a 2.4GB model plus KV/runtime and Goose UI **might fail to load, swap heavily or freeze**. If switching to 4B is not built into GUI, or causes memory pressure, **PARK GOOSE** rather than spend more sessions troubleshooting. The user specifically forbids recurring manual launch/shell setup. No permissions/extensions/commands/files authorized.
- A working 4B model's brief Persian answer does **not** establish correct tool calling, durable restart or trustworthy Windows controls; keep D-005 undecided, G3B file access guard CLOSED.

**Status:** GOOSE_G4_USER_SCREENSHOT_INFERENCE_PERSIAN_QUALITY_FAIL / 4B TEST_PROPOSED_NOT_RUN / G3B_CLOSED / D-005_OPEN.
References: [G3 prior greeting with literal raw context](GOOSE-G3-LOCAL-GEMMA1B-FIRST-RESPONSE-20261022.md), [G2 existing Gemma models ready](GOOSE-G2-USER-LOCAL-CACHED-MODELS-READY-20261022.md), [permanent GGUF paths](../../07-operations-and-continuity/LOCAL-ENGINE-AND-MODEL-PATH-REGISTER.md).
