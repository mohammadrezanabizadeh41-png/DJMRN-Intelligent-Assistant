# GOOSE-G1 — Windows desktop launched; Welcome/choose-model onboarding confirmed

**Date:** 2026-10-22. **Observation:** user supplied direct screenshot of native Windows goose Desktop running (title bar "Goose", File/Edit/View/Window menus) and welcome panel. App shows **"Welcome to goose"**, **"Your local AI agent. Connect an AI model provider to get started."**, two user choice tiles:
1. **Use a Local Model** — "Download a model and run it on this device. No API key or account needed."
2. **Connect to a Provider** — "Connect OpenAI, Anthropic, Google, etc".

**Verified from screenshot:** user extracted/launched a Goose Windows Desktop binary enough for onboarding UI. **NOT verified:** exact running version by Help/About, archive SHA for user download, actual local inference backend/available models, tool-calling, API/cloud billing or permissions. No new user model download or chat response has been reported.

**Official docs check 2026-10-22:** https://goose-docs.ai/blog/2026/04/24/use-goose-with-built-in-local-inference/ — goose Desktop ships built-in llama.cpp local inference, no separate Ollama/Jan service or daemon necessary. Goose local-provider flow downloads a quantized GGUF from Hugging Face into HF shared cache, with automatic unloading and CPU/GPU decisions. **Use Local Model tile** is the direct low-friction route, but it may require a NEW download. Whether this specific version discovers/reuses user's nine existing GGUF files in HF/Jan/LM Studio cache **not independently verified**, must not claim it. Alternative Connect to Provider may need extra provider auth/manual service, so not preferred initially. Official docs https://goose-docs.ai/docs/getting-started/providers/ — local inference can generate conversation but tool-calling reliability depends on model.

**Next proposed user step (NOT YET OBSERVED):** click **Use a Local Model** only; STOP before model download/install/account/extension/shell permissions. Inspect next screen, prefer already present HF-cached GGUF or very small feasible model for Ryzen 3500U, 8 GiB physical but ~5.88 GiB OS usable and limited free RAM. Do not configure external endpoints or auto-install anything. Single reliable Persian chat with normal program start, no daily shell, is required before subsequent tool-access testing.

**Status:** GOOSE-G1 UI_LAUNCHED_BY_USER / MODEL_NOT_SELECTED / DOWNLOAD_NOT_RUN / INFERENCE_NOT_VERIFIED / G3B FILE GUARD CLOSED / D-005 OPEN; KYNXA remains PARKED.
