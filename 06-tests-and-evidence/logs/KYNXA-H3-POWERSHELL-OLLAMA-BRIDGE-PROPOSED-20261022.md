# H3 — User requests PowerShell-controlled local model bridge into KYNXA (Ollama option)

**2026-10-22 / Proposal, NOT_RUN.** User reports PowerShell-to-model setup worked well in past, asks whether engine can be connected to KYNXA through PowerShell to avoid repeated UI/debug effort. User wants to return to main DJMRN task promptly.

## Evidence and task decision
- User's existing GGUF file was confirmed by a real user PowerShell scan: `%USERPROFILE%\.cache\huggingface\hub\models--ggml-org--gemma-3-1b-it-qat-GGUF\snapshots\c2531de7eec944fecd05bb2c23804c50d5a915c4\gemma-3-1b-it-qat-Q4_0.gguf` (0.67 GiB). Ollama installation historically present; previous `ollama list` empty. No need to redownload GGUF.
- KYNXA v1.7 official source https://github.com/jinpeng900/KYNXA/blob/v1.7.0/apps/desktop/Services/Models/ModelPresets.cs specifically lists external **Ollama** at **http://127.0.0.1:11434/v1**, and Direct OpenAI compatible provider. KYNXA's native `waiting-resource` check only applies to private managed llama.cpp engine, not generic Ollama HTTP proxy. Windows RAM constraints nevertheless remain real.
- Official Ollama import instructions https://github.com/ollama/ollama/blob/main/docs/import.mdx and https://registry.ollama.com/blog/improved-performance-and-model-support-with-gguf show Modelfile `FROM <local GGUF path>` and `ollama create -f Modelfile <name>`. This registers a local model, may copy GGUF bytes into Ollama's own model library (approx 0.67 GiB extra disk); **not** a new Internet download and not guaranteed zero-copy.
- Ollama official API https://github.com/ollama/ollama/blob/main/docs/api/introduction.mdx documents local loopback `http://localhost:11434/api` and OpenAI-compatible `http://localhost:11434/v1`, no API key for local requests.

## One-shot bounded user PowerShell script proposed
1. Read-only Test-Path on the GGUF and Get-Command ollama.exe.
2. Probe `GET http://127.0.0.1:11434/api/version`; if not running, `Start-Process ollama.exe serve` (explicitly starts user-local engine). This is an intentional **process action** in proposed user-run script, NOT executed by coordinator.
3. Probe `GET /api/tags`; if alias `djmrn-gemma3-1b:latest` absent, make a throwaway Modelfile with `FROM` the verified GGUF and `PARAMETER num_ctx 1024`; `ollama create djmrn-gemma3-1b -f <temporary Modelfile>`, then delete only **script-created** throwaway file. Ollama creates local library model data. Do not change pre-existing Jan, KYNXA or HF files or download new model weights. Idempotently skip create if alias exists.
4. Single user-local `POST http://127.0.0.1:11434/api/chat` with tiny non-sensitive message, num_ctx 1024, max new tokens 12, stream false, `keep_alive:0` to unload model after run. First model load can time out or run slowly under 8 GiB physical / 5.88 GiB OS usable RAM. No automatic retry loop or privileged/system security changes.
5. If `OLLAMA_CHAT_OK` appears, user then configures KYNXA via **Models > Add model connection > Provider Ollama > URL http://127.0.0.1:11434/v1 > Fetch models/Test > select djmrn-gemma3-1b:latest > Save**. Existing saved Jan Custom service connection remains unchanged.
6. All tools/skills/file access remain disabled/approval-gated. Don't bypass native KYNXA resource service; don't infer global host adoption on success.

## Status
- **PowerShell/Ollama approach proposed to user; no output/result pasted, no Ollama import/launch or KYNXA connection verified.**
- Native H3 KYNXA GGUF engine: still waiting-resource; External Jan provider saved but no confirmed chat reply.
- D-005 architecture decision OPEN, G3B Windows file guard CLOSED. Main DJMRN project remains priority.
