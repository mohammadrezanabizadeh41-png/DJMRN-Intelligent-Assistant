# DJMRN — software installation and deployment statistics snapshot (2026-10-23)

## Follow-up 2026-10-23 — complete direct Windows download (LATEST)
- New direct official HTTPS Windows x64 v2.3.2 binary **134305792/134305792** expected bytes, user-computed SHA256 `430D365584D6F47CC8167AC65A747163AB6FB1ECCF666978F37B263E63C377B2`.
- Windows Authenticode **NotSigned**; no publisher hash for this exact file independently verified. **EXECUTION NOT_ATTEMPTED**, so native Bifrost is still NOT operational and is NOT an installation success. [User command evidence](../06-tests-and-evidence/logs/WINDOWS-BIFROST-FULL-SIZE-DOWNLOAD-20261023.md).
- Original NPX-cache file **57943 bytes**, `EFTYPE`, and earlier rename-only repair remain historical failure and must NOT be launched. Current snapshot 21 items, chronological events 15; no real Groq or Jan communication.

## 2026-10-23 latest — device pre-execution security check, no launch yet
- User's fresh PowerShell preflight: `FILE_SIZE_SHA256: PASS`, `PE64_FORMAT: PASS`, `DEFENDER_SCAN: COMPLETED_WITHOUT_COMMAND_ERROR`, `BIFROST_EXECUTION: NOT_ATTEMPTED`. **Only 16 observed chronological events, not 16 installations.** [Bounded Defender/PE64 check](../06-tests-and-evidence/logs/WINDOWS-BIFROST-USER-DEFENDER-PE-PREFLIGHT-20261023.md).
- No execution, localhost health, Groq request, Jan connection, signed publisher binary proof or malware-free certification. Windows Authenticode remains **NotSigned**; local SHA/size check is not a publisher digest.
- Next user-controlled step: run verified downloaded full binary deliberately (unsigned-file risk acknowledged), **not** broken npx cache; loopback only, new secret in-process. No automatic services, startup task, network firewall permission, or cloud provider activation.

## 2026-10-23 — first native Windows Bifrost execution observed, exit code 1
- User explicitly typed `RUN` to launch **Bifrost v2.3.2** full native binary. Process started, read saved `config.json` and completed SQLite schema migrations; **real execution was achieved**, superseding prior `NOT_ATTEMPTED` state.
- Startup blocked on initial pricing model catalog fetch `https://getbifrost.ai/datasheet` with `context deadline exceeded` after ~61 sec; native process exited **code 1**. **Local gateway remains NOT_OPERATIONAL, no localhost health PASS, no first admin setup, no real Groq or Jan call.** [Sanitized device boot log](../06-tests-and-evidence/logs/WINDOWS-BIFROST-USER-NATIVE-BOOT-PRICING-TIMEOUT-20261023.md).
- New event `DJMRN-I017`. **21 classified components, 17 operation/download/check events (not 17 installs)**. Proposed vendor-supported offline `file://` pricing/model-parameter samples strictly for UI bootstrap; must not treat the samples as full authoritative model prices or free account quota. No local fix executed yet.

## Interpretation
**Historical device claims ≠ installed right now; downloaded ≠ installed; package created in ChatGPT ≠ program executed; Github CI PASS ≠ user Windows installed.** This snapshot is a time-bounded register with explicit evidence. Do not sum all rows as simultaneously active programs. Sources are pinned as per-row relative repository paths and original past observation dates; no private username/keys/token in the CSV.

## Snapshot metrics (derived from CSV at creation)
- Software/OS/provider components individually classified: **21**.
- Chronological action/evidence ledger records: **17**.
- **Current direct user PowerShell CLI**: Node.js v24.22.1 **VERIFIED**; Windows x64 **VERIFIED**. Other current versions not blanket revalidated.
- **Bifrost v2.3.2 on user's Windows:** one FAILED NPX start (`EFTYPE/-4028`), one 57,943-byte `CACHED_TRUNCATED` file, **zero observed successful user-device Bifrost health checks**, **zero observed Groq real inference**, **zero observed Jan-to-Bifrost successful conversations**.
- **Official Bifrost Windows amd64 HEAD**: HTTP 200, Content-Length 134,305,792 bytes. Local fraction **0.0431%**; missing **134,247,849** advertised bytes. `MZ/PE/AMD64/PE32+` headers validate superficial structure only, not full binary.
- **CI-only synthetic**: Bifrost pinned OCI on Linux GitHub Actions P2C/P2D/P2E/P2F passed prior scopes. Highest *single* cumulative unit-regression run **73/73 PASS**, NOT 73 distinct new installations or provider calls; prior first failed runs preserved. These are **not added to user-device installation successes**.
- **Prepared conversation ZIP artifacts:** live-start package, PE suffix-fix attempt. Artifacts were created by assistant; the first launcher was user executed and failed; suffix-fix ZIP **NOT reported executed and now DO NOT RUN** because binary is incomplete. No repo-hosted binary or secret.
- **Known other historical user software:** Python, Git, Winget, VS Code, Jan Desktop/Agent, Ollama, LM Studio and Bionic, LlamaApp, KYNXA, Goose, ChatGPT Desktop, with different proof levels and possibly outdated versions. **Goose launched and locally generated Persian output 2026-10-22; older note of not installed on same day is superseded.** Local-Gemma text exists but quality FAIL, not production assistant acceptance.

## Classification counts

| Snapshot `state` | Number of rows |
|---|---:|
| `NATIVE_STARTED_EXIT1_PRICING_TIMEOUT_NOT_OPERATIONAL` | 1 |
| `FEATURE_PRESENT_HISTORICAL` | 1 |
| `INSTALLED_CLI_HISTORICAL` | 4 |
| `INSTALLED_CLI_VERIFIED_CURRENT` | 1 |
| `INSTALLED_CURRENT_ARCH_VERIFIED` | 1 |
| `INSTALLED_HISTORICAL` | 1 |
| `INSTALLED_LAUNCHED_HISTORICAL` | 1 |
| `INVOKED_VERSION_UNKNOWN` | 1 |
| `NOT_CONNECTED` | 1 |
| `NOT_PRESENT` | 1 |
| `UNVERIFIED` | 1 |
| `USER_INSTALLED_HISTORICAL` | 4 |
| `USER_INSTALLED_LAUNCHED_HISTORICAL` | 2 |
| `USER_LAUNCHED_MODEL_RESPONDED_HISTORICAL` | 1 |

**Scope clarifier:** these row counts include the OS, services, unknown/bundled features, historical applications and actual local tests. Only facts with dated user-run evidence support present operational status. The primary quantitative source for reproducible statistics is [component inventory CSV](installed-software-snapshot-20261023.csv); historical operations are in [append-only event ledger CSV](installation-events.csv). Follow [Windows truncated PE evidence](../06-tests-and-evidence/logs/WINDOWS-BIFROST-TRUNCATED-PE-20261023.md).

## Next real deployment acceptance criteria
1. Confirm new full official Windows executable downloaded and verified (official HEAD size + compatible executable format; vendor checksum/signature when available).
2. Bound native Bifrost to local loopback `127.0.0.1:18080`, first-admin account with fresh local setup token and auth; validate health on Windows.
3. Verify *actual user* Groq Free allowance/billing/no-overage before touching its API; configure only one approved free model with no paid fallback.
4. Configure Jan local custom endpoint; observe **one** non-sensitive Persian chat result with provider response; record wall-time/RAM and request count if available without leaking secrets.
5. Keep G3B/M1 personal-file guard CLOSED, D-005 architecture OPEN until separately decided.

**Data minimization:** This snapshot deliberately does not store account name, private directory names, first-admin token, key, user-specific identifier or credential. Reconcile future snapshots rather than replacing historical outcomes.
