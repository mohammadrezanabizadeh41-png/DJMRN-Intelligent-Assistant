"""Fail-closed Windows file boundary: G2A source ONLY / OS proof HOLD.

CAP-006 reopens a pathname even after an external guard could have opened an
approved handle. An early path/sha check followed by its later open is NOT a
guarantee of which bytes the reopened operation read (TOCTOU). This module
deliberately does not offer a 'verified' flag, permit unsafe fallback or return
a pathname that a caller can pass to CAP-006. Do not remove the HOLD without
separately reviewing a handle-to-bytes CAP change OR demonstrating and testing
a complete NTFS locking/identity proof with all parent components.
"""
from __future__ import annotations


class WindowsGuardHold(RuntimeError):
    code = "FILE_BOUNDARY_UNPROVEN"

    def __init__(self):
        super().__init__(self.code)


HOLD_REQUIREMENTS = (
    "Confirm local regular NTFS file/volume and owner SID via real handles",
    "No hardlinks, ADS, UNC, cloud placeholder or reparse-point ancestors",
    "Hold compatible file and parent directory handles through actual read",
    "Prove CAP-006 path reopen cannot access unapproved replacement bytes",
    "Deny concurrent rename/replacement/race or safely read verified handle",
    "Audit Windows sharing/identity semantics and execute negative G3 tests",
)


def require_verified_read(*_args, **_kwargs):
    """Always deny until an independently approved, tested OS-bound implementation."""
    raise WindowsGuardHold()
