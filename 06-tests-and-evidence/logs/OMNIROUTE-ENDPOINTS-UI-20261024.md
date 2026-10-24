# OmniRoute v3.8.52 — Endpoints UI read-only snapshot (three actual user screenshots)

**Date:** 2026-10-24. **Project:** DJMRN-Intelligent-Assistant `main`. **Status:** USER_SCREENSHOT_UI_OBSERVED, **NOT** API authentication, request success, real free-provider quota or model inference validation.

## Raw image preservation and provenance
- Three **unaltered original screenshot PNGs** were saved together with per-file SHA-256 manifest as **a private Library ZIP**, not to public GitHub: `/DJMRN/OmniRoute/2026-10-24/DJMRN_OmniRoute_Endpoints_Screenshots_20261024.zip`
- Library identifier: `libfile_3c1be637e36c8191ae114a4a196ea92a`; ZIP SHA-256: `241847cceb2bdbf1b33786aa5905900a90c57a72d05f5e37256bc48eff1c2448`.
- Images, in order (unchanged bytes, hashes below):
  1. `screenshots/01-endpoint-and-tunnels-top.png` SHA-256 `2bcac84e36d1569926c73967099bc91b3856de3b840247e1c29da0f9353f01fc`
  2. `screenshots/02-model-endpoint-catalog.png` SHA-256 `d0df8de98eb68af6b6a172672f4de8a913ec1ec8439054c01aac6e3f0c7d43df`
  3. `screenshots/03-search-utility-vscode-endpoint.png` SHA-256 `3da07a02203f7337cde5f346f428986c7ac229e08d17392a3aef2d5b72dd87e3`
- To avoid exposing a household/device LAN address or device name in the **public GitHub repo**, that identifying detail is redacted in written report; originals are only in private Library.

## UI observations (facts from screenshots, not provider availability)
- **Local OpenAI-compatible base URL:** `http://localhost:20128/v1` (displayed, not yet proven via actual `/v1/chat/completions` request). API Endpoint includes a `Test endpoint →` action **not invoked**.
- **Active Endpoint → Local**, and **Local Server → Running** green status. UI also shows an **RFC1918 private LAN address** for the server on the same port. **Important:** this is a reason to inspect network binding, not conclusive evidence external devices can connect.
- Protocol tabs: **APIs** selected; **MCP**, **A2A**, **Context Sources** available but their functionality/invocation not tested.
- **Tunnel status: 0/3 active**: Cloud OmniRoute disabled/not configured (cloud sync, not local backups); Cloudflare Quick Tunnel not installed; Tailscale Tunnel not installed; ngrok Tunnel says Needs Auth. No tunnel setup or cloud reachability authorized.
- **Custom System Prompt** toggle OFF.
- **Core APIs**: Chat Completions `/v1/chat/completions`, Responses `/v1/responses`, Completions Legacy `/v1/completions` show **0 models**; Messages/Anthropic `/v1/messages` shows a dash. Headline `0 models across 4 endpoints`.
- **Media / multimodal**: Embeddings, image generation/edits, audio transcription/text-to-speech, music generation, video generation: all visible **0 models**. Visible URL fragments are catalog/navigation, not functioning free providers.
- **Search & Discovery**: Web Search `/v1/search` shows **28 models** as its own category. **This is not a real free-tier entitlement or a verified working web search provider**.
- **Utility & Management**: Rerank 0, Moderations 0, Batch API/File API display dashes, List Models `/v1/models` displays 0.
- **VS Code token alias**: Base/Models/Chat placeholder URLs use `{token}`, not real keys. No extension/provider installed or configured based on this.
- There is **no supported claim** of any real model invocation, free token balance or billable/zero-cost activity.

## Specific security warning and stop gate
Prior screenshot from `Configuration → Security`: `Require login` ON, UI says password updated; `IP Access Control` **Disabled**. This protects dashboard access but is **not evidence** `/v1/*` requires an API key. Official vendor [User Guide](https://github.com/cheaper-inference/OmniRoute/wiki/User-Guide) documents `REQUIRE_API_KEY` with default `false` for some environments; the maintainers explicitly note [some local-first deployments bind to `0.0.0.0` and do not require an API key](https://github.com/cheaper-inference/OmniRoute/discussions/11645), allowing untrusted LAN callers to exhaust billed provider quotas. **These documented defaults are NOT independently verified as the Windows Desktop configuration on this device**.

**Before adding any provider/real key**, confirm:
1. HTTP listener scope: localhost only (`127.0.0.1` / `::1`) or an intentional restricted network exposure; independently inspect without requesting secrets. If an all-interface listener is found, restrict to loopback via approved reversible documented setting or validated OS firewall.
2. `REQUIRE_API_KEY` behavior for `/v1` (or equivalent verified product setting). Strong dashboard password alone is not sufficient proof.
3. Free-only provider allowlist, account billing/off and quotas, and authenticated routing to each assistant, before any actual inference.
4. Do not turn on any Quick Tunnel, Tailscale, ngrok, system proxy, public endpoints, root CA or custom Agentic feature now; no paid provider connection or model call.

## Next GUI action
User currently uses OmniRoute Desktop UI (browser localhost is alternative, not second server). Inspect **Configuration → Advanced** or relevant Security lower subsections in read-only mode, looking for `REQUIRE_API_KEY`, bind/host, LAN access and endpoint permissions. **Do not copy secrets or post any server.env file**. If UI lacks a definitive bind display, a single optional read-only Windows shell command can confirm the listener later.

**State:** `LOCAL_API_ADVERTISED`, `LOCAL_SERVER_RUNNING_UI`, `MODELS_CORE_ZERO`, `SEARCH_CATALOG_28_UNVERIFIED`, `TUNNELS_NONE`, `IP_ACL_DISABLED`, `LAN_BIND_UNKNOWN`, `API_KEY_AUTH_UNKNOWN`, `PROVIDER_REAL_NOT_CONNECTED`. D-005 OPEN; G3B/M1 CLOSED.
