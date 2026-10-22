# G2A dependency and execution holds

- Current G2A source: Python standard library only for contract, approval, manifest and fail-closed dispatcher. No runtime dependency resolver, package installer or inference client.
- Existing CAP-006 source: stays unchanged at ../document_search_v0/docsearch_v0.py; pure legacy translation cannot substitute for secure Win32 reading.
- Exact Python version installed on user's Windows historically: 3.14.7 (not re-measured or tested in this action). Do not assume environment or Tk exists.
- Optional future MCP adapter (G2B-A) is NOT part of G2A. Python MCP SDK, its transitives/pywin32 wheel compatibility, version and hashes require a later approved source lock. No pip/uv/npx/curl allowed.
- Jan installed binary/source parity, shell disable and tool policy profile are NOT inspected on the user's machine. Jan adapter/launcher NOT IMPLEMENTED.
- G3 smoke, local model inference, Windows file guards, real timestamps/RAM/RTL and network egress tests NOT RUN.
- Required STOP: Windows CAP reopen after a guard remains an unresolved TOCTOU problem. windows_guard.require_verified_read ALWAYS denies. Any future change to CAP source or use of unverified file-path reads needs a different explicit user scope.
- This is a code review artifact, not a launch manual. No daemon, scheduler, new provider, service or real user-document grant.
