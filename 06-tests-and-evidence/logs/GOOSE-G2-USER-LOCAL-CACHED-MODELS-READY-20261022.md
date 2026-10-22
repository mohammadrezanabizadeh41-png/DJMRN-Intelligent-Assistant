# GOOSE-G2 — Built-in local model picker detects pre-existing cached Gemma GGUFs

**Date:** 2026-10-22. **Evidence:** direct user-supplied screenshot of Goose Windows Desktop after selecting `Use a Local Model`. **User's hardware:** Ryzen 5 3500U, 8GiB physical / ~5.88GiB OS-usable RAM (previous snapshot).

## What actual screenshot shows (not inference claims)
- `Use a Local Model` section expanded, radio selection `ggml-org/gemma-3-1b-it-qat-GGUF:Q4_0`, `687MB`, green **Ready**, label **Best for your machine**.
- `ggml-org/gemma-3-4b-it-qat-GGUF:Q4_0`, `2.4GB`, green **Ready**.
- `tensorblock/gemma-3-12b-it-GGUF:Q2_K`, `4.4GB`, green **Ready**.
- Main blue action `Use ggml-org/gemma-3-1b-it-qat-GGUF:Q4_0`.
- `Search HuggingFace` optional field; no indication of any new model download or cloud provider account needed to move forward.

## Analysis and controlled next step
- This is strong **UI evidence** that Goose recognized three Gemma GGUFs previously reported in local HuggingFace cache ([permanent paths registry](../../07-operations-and-continuity/LOCAL-ENGINE-AND-MODEL-PATH-REGISTER.md)). Model duplication/network download **not observed or required by UI** at this point. Green `Ready` means UI considers listed model ready, **not proof** that a process successfully loaded weights, answered text, or respects resource budget.
- For only first smoke test, keep selected `Gemma 3 1B Q4_0` (Goose recommends it for user's machine); user to click main blue Use button **once**, wait for setup result and show screenshot. No 4B/12B load, provider accounts, MCP extensions, shell/fs permissions. Next small non-sensitive Persian greeting test ONLY if chat opens.
- Compare against KYNXA H3 failure: goose built-in local model picker finds existing small Gemma GGUFs directly, so at least this stage avoids manual external HTTP server and model path hunting. Not yet evidence for routine start/recovery or overall host adoption.

**Status:** GOOSE G2 LOCAL_CACHE_READY_UI_USER_VERIFIED / MODEL_START_NOT_YET_REPORTED / INFERENCE_NOT_VERIFIED / DOWNLOAD_NOT_PERFORMED_IN_SCREENSHOT / G3B FILE GUARD CLOSED / D-005 OPEN.
