# OmniRoute #001 AI Horde — user GUI evidence and first minimal Persian model proposal

**Date:** 2026-10-25. **Evidence source:** 6 user-uploaded desktop photographs in current conversation (4 overview + 2 model-dropdown screenshots), model/provider status documented by user; this note is transcription/analysis **not** access to or execution on the user's computer.

## What is actually established

- App screen shows `AI Horde`, `Enabled` toggle ON, `0 connections`, banner "No authentication required" / no signup or key required; `Add PAT` optional. This is **UI_ENABLED_NO_INFERENCE**, not proven API text generation.
- Available Models screen shows `3/3 active` built-in text candidates labelled **Free**, with `Assumed` pricing, including provider-id style `horde/google/gemma-4-31b` and role-play-model entries. They are built-in entries; live serving/true zero-cost requires actual verification.
- Playground screen shows `Model=2DN` after opening the selector and `Select key=(default)`; separate photo shows a large alphabetical list of image model IDs (`2DN`, diffusion names). Thus **current selected 2DN is an image-generation model**, inappropriate for L1 Persian chat.
- User explicitly requests: first verify one tiny chat, then describe/decide assistant architecture. User specifies a durable policy to choose role-sized free models and ration actual tokens/requests/kudos/credits, avoiding model switching at each message. See [approved role/quota policy](../../02-project-management/FREE-CLOUD-MODEL-QUOTA-AND-ROLE-ROUTING-POLICY-20261025.md).

## Source-based service accounting (not measured from user ISP)

- AI Horde anonymous access is free; internal `0000000000` key, lowest priority. Queue availability changes with volunteer workers. It is **not** a conventional measured renewing token/day balance in current official docs. Kudos is queue priority and cannot be sold; signed-in or pseudonymous API keys are optional and are not necessary for initial test.
- [Provider reference for OmniRoute v3.8.52](https://github.com/cheaper-inference/OmniRoute/blob/release/v3.8.52/docs/reference/PROVIDER_REFERENCE.md) identifies `aihorde` as `No-auth` and optional account improves priority; provider feature support does not prove native function-calling.
- [Official user/readme](https://github.com/Haidra-Org/AI-Horde/blob/main/README.md), [provider site](https://aihorde.net/), [text usage instructions](https://horde-sdk.readthedocs.io/en/stable/how-to/generate-text/), [live endpoint](https://aihorde.net/api/v2/status/models?type=text) are sources. An external live read of last endpoint in this discussion found `koboldcpp/gemma-4-E4B-it` with one worker; model counts constantly change.

## Minimal trial chosen (not yet executed)

- **Preferred L1 text model:** exact live Horde model string `koboldcpp/gemma-4-E4B-it` (if OmniRoute lists it). Don't assume it is shown unless user confirms. If absent, use model-import/list search flow; **do not accidentally choose 2DN/image**.
- **Fallback for *trial only*:** `google/gemma-4-31b` if the E4B model is not listed but real text-chat supports it; use one response and note heavier role, not adopted low-cost primary.
- **One prompt:** `سلام. فقط در یک جمله فارسی بگو: آماده دریافت دستور هستم.`
- **If GUI has relevant knobs:** output max 64; context approximately 512–1024; n=1; retries=0/at most one user-authorized retry. Do not claim these settings have been entered or are visible. Select key default. Do not toggle global flags, add PAT or change network/firewall.
- **To record after user returns:** selected actual model ID, displayed HTTP/response/error, text quality, wait time if observed, free/status/provenance, whether separate key was required. `CONNECTED_VERIFIED_FREE` only after actual correct nonbillable response through OmniRoute.

**Result currently:** `UI_ENABLED_NO_INFERENCE`. No remote model response, no agent-to-agent messages, no real quota cap measured, no server-side policy access confirmed on user's ISP.
