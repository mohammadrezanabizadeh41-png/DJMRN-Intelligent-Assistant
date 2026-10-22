# KYNXA H0/H1 — user-reported Windows 11 read-only preflight, 2026-10-22

**Context:** DJMRN user personally downloaded and extracted official KYNXA v1.7.0 Setup ZIP. Coordinator did not execute any Windows commands. Recorded values below are direct user-pasted PowerShell JSON; ZIP hash comparison was performed locally by user with a supplied publisher digest. No credentials or private paths saved.

| Field | User result |
|---|---|
| Windows build | 26300 |
| `RAM_Physical_GB` (Win32_ComputerSystem.TotalPhysicalMemory / 1 GiB) | 5.88 |
| `RAM_Usable_GB` (OS.TotalVisibleMemorySize / 1 MiB) | 5.88 |
| `RAM_Available_GB` (OS.FreePhysicalMemory / 1 MiB) | **0.87** |
| `DriveC_Free_GB` | 117.73 |
| `ZIP_Found` | true |
| `ZIP_Hash_Match` | **true** |
| `Setup_EXE_Found` | true |
| `Setup_Signature` | **NotSigned** |

Publisher digest matched by user command: `d2e16a8b17de8e86672ff12226d4aa6719f5b4d1ffd61a910e6b333af0fa973b`. Source: https://github.com/jinpeng900/KYNXA/releases/tag/v1.7.0 . Publisher warned installer is not production signed and was built, not installation-tested. Checksum equality confirms correspondence to publisher's GitHub asset, NOT software safety, authorship, antivirus cleanliness or installer testing.

**Important interpretive correction:** The variable labeled `RAM_Physical_GB` in original script used Win32_ComputerSystem.TotalPhysicalMemory, which can represent memory visible to Windows, **not necessarily sum of installed DIMM capacities**. Do not conclude only 5.88 GiB physically installed; historically inventory indicated 8 GiB DIMMs with substantial hardware reservation. A new read-only `Win32_PhysicalMemory.Capacity` sum is the right way to independently distinguish installed RAM from OS-visible RAM; no new device execution has been observed yet.

**Status:** `H0_PARTIAL / H1_ZIP_AND_EXTRACT_VERIFIED_BY_USER / DEVICE_APP_NOT_RUN`. Free 0.87 GiB is limited headroom for adding a substantial agent application; it does not by itself prove KYNXA incompatible. Installer security risk independently requires review. Suggested next step: read-only DIMM, current process working sets, OS commit/pagefile snapshot; user may then close *chosen* unused apps normally and remeasure. **No process termination was performed or requested automatically.** Do not launch or bypass Windows warnings until separately authorized.

**Scope not tested:** Installer runtime, Defender file scan, installed KYNXA footprint, model RAM and Persian performance, auto-download behavior, tool permissions, personal filesystem, external accounts, Jan, CAP-006, G3B, goose. D-005 remains OPEN; original file guard remains CLOSED.
