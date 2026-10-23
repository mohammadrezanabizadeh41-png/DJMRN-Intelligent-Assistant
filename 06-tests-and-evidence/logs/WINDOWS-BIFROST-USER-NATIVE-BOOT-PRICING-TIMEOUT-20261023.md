# Windows 11 Bifrost 2.3.2 — first real native boot, SQLite migrations success, fatal pricing data timeout

**Date:** 2026-10-23 22:39–22:40 (+03:30, per user console). **Source:** user provided complete 745-line PowerShell/native Bifrost output. Sanitized: no user profile name, secret, access token, session key or raw sensitive paths copied.

## Actual observations
- User typed `RUN` after verifying full downloaded EXE. `File verification: PASS`, `Gateway: 127.0.0.1:18080`, `Authenticode: NotSigned`.
- Fresh `BIFROST_SETUP_TOKEN` generated and placed in local Windows clipboard, not printed in console; **not captured or committed**.
- Native Bifrost v2.3.2 **really started to initialize** (ASCII release banner). Configuration loaded from `%LOCALAPPDATA%\DJMRN\Bifrost\config.json`.
- SQLite config store migrations completed (numerous table/index migrations). Final `config store initialized (default SQLite)`.
- Start `initializing model catalog...`. Approx 61 seconds later: `failed to initialize pricing manager: failed to sync pricing data: failed to load pricing data from URL and no existing data available: context deadline exceeded (last attempt: failed to download pricing data: Get "https://getbifrost.ai/datasheet": context deadline exceeded)`.
- PowerShell `BIFROST_EXIT_CODE: 1`. Gateway startup **FAIL**. No `listening/healthy` status, admin account, provider key, Groq API request or Jan-to-gateway inference demonstrated; database migrations do not establish overall operational readiness.

## Diagnosis and planned intervention
Official 2.3.2 vendor air-gapped guide and pinned examples explicitly support local `file://` `framework.pricing.pricing_url` and `model_parameters_url` to prevent first-boot datasheet HTTP timeouts:
- https://github.com/maximhq/bifrost/blob/a05ea20e68bf116a35e9f05b1a3d749624b3935e/docs/deployment-guides/how-to/airgapped.mdx
- https://github.com/maximhq/bifrost/blob/a05ea20e68bf116a35e9f05b1a3d749624b3935e/examples/configs/withlocalpricingfiles/README.md
- https://github.com/maximhq/bifrost/blob/a05ea20e68bf116a35e9f05b1a3d749624b3935e/examples/configs/withlocalpricingfiles/config.json
- https://github.com/maximhq/bifrost/blob/a05ea20e68bf116a35e9f05b1a3d749624b3935e/docs/providers/custom-pricing.mdx

**NEXT (NOT RUN):** fetch the two *vendor sample* datasheets to private local app-dir from a pinned official GitHub tree; validate JSON; backup current user `config.json` locally (not GitHub); add only `framework.pricing.pricing_url="file:./pricing.json"` and `model_parameters_url="file:./model-parameters.json"` (process working dir app-dir on restart) while preserving all existing providers/config. User must intentionally run local preparation script. No cloud keys, paid plans, Windows Defender changes or host-wide proxy changes. Vendor sample catalog covers only a few example models, **NOT authoritative for the intended Groq Free model**; do not route production models or assert actual free allowance based on it.

**Safety and acceptance:** Confirm first a local re-start reaches healthy loopback and dashboard administration is protected with a NEW setup token (last attempt's token was deleted from process on exit). Before any actual Groq traffic, confirm user's account Free tier, model access and no charge/overage, plus correct model catalog and virtual-key authorization. Keep G3B/M1 user-file access guard CLOSED. No need to repeat install/NPX/binary downloads, and do not classify as installed working gateway until actual health checked.

## Statistical classification
- Runtime launch **REAL_NATIVE_BINARY_STARTED_BUT_FATAL_PRICING_TIMEOUT**.
- SQLite first-boot migrations **USER_LOG_CONFIRMED_SUCCESS**.
- Gateway health **NOT_REACHED**, exit 1.
- Provider call **NOT_RUN**.
