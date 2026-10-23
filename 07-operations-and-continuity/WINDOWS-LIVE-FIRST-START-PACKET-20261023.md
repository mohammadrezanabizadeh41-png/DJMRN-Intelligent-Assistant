# DJMRN — User-authorized Windows LIVE rollout, first-start packet (2026-10-23)

## IMPORTANT 2026-10-23 corrected real-device result
First-start was **attempted on user's Windows but failed**. Current user read-only PowerShell: Node.js v24.22.1 works; Bifrost cache `bifrost-http.exe-0` is 57,943 bytes versus official 134,305,792. **Do not rename or run the incomplete cached binary, nor the previously prepared rename-only ZIP.** [Latest evidence](../06-tests-and-evidence/logs/WINDOWS-BIFROST-TRUNCATED-PE-20261023.md) and [software statistics](../01-system-inventory/INSTALLATION-AND-DEPLOYMENT-STATISTICS-20261023.md). User-device startup remains BLOCKED; synthetic Github Bifrost tests are separate.

**Stage: PREPARED FOR USER EXECUTION / USER WINDOWS RUN NOT YET OBSERVED. NOT production deployed; NO provider/account credentials entered, NO real Groq request attempted, NO installer executed on the user's PC by the coordinator.**

The user explicitly concluded the P2C–P2F synthetic evaluation is sufficient for proceeding to actual installation and use on their existing Windows 11 Pro 8GiB Ryzen 5 3500U laptop. They want a lightweight Cloud-First assistant via official Maxim Bifrost local gateway and their already-installed Jan Desktop.

## Exact prepared assistant-generated conversation artifact

**Filename:** `DJMRN-Windows-Live-Start-20261023.zip` (available as an attached file in the 2026-10-23 ChatGPT conversation; NOT in GitHub itself). **SHA256:** `524d11aa627d4ad4b2bdcf805923a81c8052720bf20193be3e8269a72fc47d43` (local ZIP bytes); size **7,043 bytes**, integrity check ZIP PASS. This reference is NOT a download URL; open the generating chat to retrieve the attachment. Do not infer GitHub contains the ZIP or that an executable ran on Windows.

Its five source files: `Start-DJMRN.ps1`, `START-DJMRN.cmd`, `Check-DJMRN.ps1`, `CHECK-DJMRN.cmd`, `README-FA.md`. No external compiled binaries, no credentials, no real API endpoints entered. ZIP verified in assistant Linux container; **PowerShell 5.1 Windows execution NOT_RUN**.

## Installation/activation design
1. User extracts ZIP and launches local `START-DJMRN.cmd`. This starts PowerShell with *process-scoped* script execution policy, not permanent global policy modification. Checks native x64 Windows, `npx.cmd`, port 18080. If Node.js missing, offers a visible explicit `INSTALL` confirmation before Windows Package Manager installs official Node.js LTS; otherwise stops safely.
2. First start uses official `npx -y @maximhq/bifrost --transport-version v2.3.2 -host 127.0.0.1 -port 18080 -app-dir %LOCALAPPDATA%\DJMRN\Bifrost`. No Docker, WSL, startup service, background scheduling, firewall exception, broad file access. Local on-disk Bifrost config is created only if absent and requires virtual keys on inference by default with `allow_direct_keys=false`, logs store disabled. UI config-store SQLite default is retained.
3. Script generates random 256-bit `BIFROST_SETUP_TOKEN` for first-admin local setup **only in process memory and user console**, not committed, transmitted to ChatGPT or saved in artifact. Initial Dashboard at `http://127.0.0.1:18080`: user must configure Workspace → Config → Security → Password protect dashboard using token and self-chosen strong admin password. User supplies NO secrets to assistant or repository.
4. First real provider technical candidate **Groq Free**; *account tier not accessed or verified*. Before ANY real API call user must confirm their account is FREE and pay-as-you-go/auto-recharge not enabled and see actual model quota; then separately create a provider key at `https://console.groq.com/keys` and paste solely into protected local Bifrost. Configure exact allowlist of live `openai/gpt-oss-120b` and Groq provider only; no paid fallback or `*` wildcard. Official [Free Plan FAQ](https://community.groq.com/t/do-i-get-charged-for-anything-on-the-groq-free-plan/832) states Free is unbilled and over-limit 429, but individual account/terms/status UNKNOWN until user checks. This is **not** proof of any universal bill-free route.
5. Create restricted Bifrost **Virtual Key** just for Groq + model. `Enforce Virtual Keys on Inference` enabled. Jan Desktop Add Custom OpenAI Provider: `http://127.0.0.1:18080/v1` and Bifrost virtual key, NOT Groq API key. Bifrost dashboard basic authentication and Jan Bearer-only authorization are separate settings; consult [exact tagged vendor virtual-key/auth docs](https://github.com/maximhq/bifrost/blob/a05ea20e68bf116a35e9f05b1a3d749624b3935e/docs/quickstart/gateway/setting-up-auth.mdx), and avoid placing both Basic and VK in one Jan Bearer header.
6. First live chat sends *one harmless nonsensitive message* only after account-level verification. This message will be processed remotely; no confidential material. Windows device results, actual success, observed idle/peak RAM, latency, provider API availability, account quota and cost all PENDING user evidence. `CHECK-DJMRN.cmd` offers read-only host health/bind checks without exposing secrets.

**Governance:** Prior P2F [successful synthetic genuine-gateway run 39966632465](https://github.com/mohammadrezanabizadeh41-png/DJMRN-Intelligent-Assistant/actions/runs/39966632465) is NOT a production cost or actual Groq guarantee. Do not automatically install all of P2D/P2E/P2F test code on Windows, since those test harnesses hardcode fake providers/dates. D-016 bounded router candidate continues into user-authorized **single-provider initial live pilot**, NOT full validated production adoption; D-005 architecture open, G3B/M1 sensitive-file access guards closed.

**Vendor evidence (fetched 2026-10-23):**
- [Maxim release Windows/NPX and v2.3.2](https://www.getmaxim.ai/bifrost/releases)
- [Exact version vendor gateway setup guide](https://github.com/maximhq/bifrost/blob/a05ea20e68bf116a35e9f05b1a3d749624b3935e/docs/quickstart/gateway/setting-up.mdx)
- [Exact version provider Groq adapter](https://github.com/maximhq/bifrost/blob/a05ea20e68bf116a35e9f05b1a3d749624b3935e/docs/providers/supported-providers/groq.mdx)
- [Groq Free Limits](https://console.groq.com/docs/rate-limits) / [Groq models/deprecations](https://console.groq.com/docs/models) / [Groq Free billing](https://console.groq.com/docs/billing-faqs)
- [Jan Desktop Custom Endpoints](https://docs.jan.ai/desktop/remote-models/custom-endpoint)

**Immediate continuation:** user should run the provided ZIP on Windows, secure Bifrost dashboard, and share sanitized **status only** (healthy page/error code), without any setup token, API key, virtual key, password, personal data or unmasked secret. If Node install fails, diagnose exact error, never claim success or install remotely. User may need to permit Node installer UAC.

