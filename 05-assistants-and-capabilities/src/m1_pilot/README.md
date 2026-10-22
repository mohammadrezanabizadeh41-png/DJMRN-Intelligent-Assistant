# DJMRN M1 pilot — G2A source-only, fail-closed foundation

Status: G2A FOUNDATION COMMITTED FOR REVIEW; NOT A WORKING ASSISTANT; WINDOWS G3 HOLD.

This source was created under the user's limited G2A permission. It uses Python standard-library-only contracts and a model-independent session permission controller. It does NOT grant access to any files by itself. The Windows file identity / CAP-006 reopen race is unresolved. windows_guard.require_verified_read() intentionally denies every real file read. There is no automatic unlock, fallback search, shell, API, model, network listener, Jan configuration or executable installer.

Implementation order: strict v1 tool schema -> operator-side non-persistent manifest and approval -> deterministic receipt format -> dispatcher -> Windows verified-by-handle boundary (HOLD) -> existing CAP-006 integration after a separate security decision. A separately approved additive CAP-006 source update now provides search_preloaded_bytes; legacy path search and CLI remain unchanged. The new function does not validate user grants or OS file identity, and the M1 dispatcher still never calls it.

Only one tool may ever be offered to a model: search_approved_documents. Model input may contain query, file_ids and max_matches, never root, path, command, script, URL or permission. The trusted program—not model prompts or Jan's "Always allow"—must bind approved file IDs. An ordinary process running with a Windows user's privileges is NOT an OS sandbox against hostile same-user software.

Readiness matrix:
- Parser, immutable test manifest structure, grant/revoke state machine and receipt constructors: SOURCE IMPLEMENTED; mock verification still required.
- Real Windows handle/read guard: FAIL CLOSED / NOT IMPLEMENTED / NEVER CLAIM SAFE.
- CAP-006 adapter: mapping and validation only; no live search dispatch permitted.
- Independent local human-approval window: NOT BUILT.
- Jan MCP adapter, any local chat GUI or model: NOT BUILT.
- Synthetic tests: SOURCE ONLY; no device test. Fixtures can be added under the same reviewed G2A scope; fixture hashes must be computed from actual bytes, never invented.
- G3 hardware/RTL/performance/model/egress: NOT RUN.
- Any need to refactor CAP-006 requires a separate user approval.

All future test runs/installs/network/model work on the user's Windows require separate G3 authorization. The default state is BLOCKED.
