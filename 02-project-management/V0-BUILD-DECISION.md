# User-approved path and bounded V0 start — D-009 / D-011 / D-012

**Date:** 2026-10-20. User explicitly approved previous proposal: `thin contract + first no-Agent capability`, and asked to **record reasons in GitHub and begin**.

## Approved sequence (D-009)
1. Define only a **logical** job boundary: `task_id, capability, input_ref, permission_scope/owner, status, error, result/receipt`; cancellation/deadline only when needed. No shared coordinator implementation required initially.
2. Build one bounded deterministic, low-risk source-grounded local lookup/extraction capability **without Agent, LLM, manager or background processes**.
3. After real usage evidence: consider durable queue/ledger if tasks need retries/restart, direct local/remote model if deterministic output cannot suffice, resource admission/lease manager **before** unattended or concurrent resource-heavy work, and multi-role Agent only when justified.
4. Scope creep stops until new user approval; the roadmap P0–P6 is **not** automatically adopted in full.

## Approved V0 direction (D-012)
- **Purpose:** initial document lookup for future Knowledge Center / Research Curator: read explicitly listed text documents, normalize Persian letter/digit variants for search, return matching source lines and SHA256 digests with their relative paths.
- **Access:** code creation in canonical `mohammadrezanabizadeh41-png/DJMRN-Intelligent-Assistant` repo, synthetic nonsensitive sample files, controlled off-device tests **within this answer** approved. Original input files remain untouched; no customer data.
- **Exclusions:** no local Windows execution/test/benchmark, installation, moving/editing real device files, installing services or cloud tools, financial actions, account connections, email/sending, remote workload, or change to Notion/Applied research repo. **Any Windows run still requires separate scoped go-ahead.**
- **First iteration selection:** Python stdlib CLI only for CAP-006; not a project-wide language choice. Comparison in [V0-TECH-CHOICE](../03-architecture-and-tools/V0-TECH-CHOICE.md).
- **Implementation output:** [code and fixtures](../05-assistants-and-capabilities/src/document_search_v0/README.md); [test evidence](../06-tests-and-evidence/logs/NEW-V0001-20261020.md).
- **Expected response contract:** explicit root and relative file allowlist + query → JSON `contract_version/task_id/capability/status/permission_scope/searched[file,sha256,bytes]/matches[file,line,source_sha256,text,match_mode]/error`.
- **Known V0 limitations:** line-based lexical matching, no OCR/semantic RAG/no JSON field parser, no persistence, no "fully secure sandbox", relaxed matches may cross spaces, max 20 UTF-8 files up to 1MiB. No web search and no automatic reading of the private GitHub repo.

## Acceptance gates / status
| Gate | Evidence | Status |
|---|---|---|
| D-009 user approval for sequencing | user's current message and earlier proposed V0 | **APPROVED / documented** |
| D-012 user approval for starting bounded build | same message | **APPROVED FOR REPO CODE + SYNTHETIC OFF-DEVICE TEST** |
| Minimal alternative comparison | documented in 03 | COMPLETE FOR V0 SCOPE ONLY |
| Source and 16 synthetic isolated tests | exact blobs, report NEW-V0001 | **TESTED-SYNTHETIC** |
| Windows user machine / real authorized files | no new Windows commands executed | **NOT TESTED / AWAITING SEPARATE APPROVAL** |
| Production deployment / models/manager | not in scope | **NOT APPROVED** |

**Next:** receive explicit approval to run a limited **read-only smoke test using ONLY bundled synthetic fixtures** on user's Windows (if and when requested); first verify Python executable and encoding with no installation. Then consider actual non-sensitive selected documents with exact user-provided paths. No assumption of successful Windows deployment until observed.
