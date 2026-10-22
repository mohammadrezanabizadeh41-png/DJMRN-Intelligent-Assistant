"""Operator-side in-memory approval state. No model/JSON endpoint can grant it."""
from __future__ import annotations

from dataclasses import dataclass
from threading import RLock
from time import monotonic
from .manifest import Manifest


class PermissionDenied(ValueError):
    def __init__(self, code: str):
        super().__init__(code)
        self.code = code


@dataclass(frozen=True)
class GrantView:
    owner_sid: str
    connection_id: str
    manifest_revision: int
    manifest_digest: str
    ids: frozenset[str]
    expires_at: float


class LocalApprovalControl:
    """For use inside a future trusted native control plane, NOT an RPC tool.

    Tests may call grant_by_operator to exercise state transitions; this is not
    Windows OS authentication. A caller with arbitrary same-user Python code
    execution is outside the claimed protection. File reads remain separately
    blocked until Windows guard proof and G3 review.
    """
    def __init__(self):
        self._lock = RLock()
        self._grant: GrantView | None = None
        self._generation = 0

    def grant_by_operator(self, manifest: Manifest, connection_id: str,
                          ttl_seconds: int = 900) -> None:
        if (type(connection_id) is not str or not connection_id or
                type(ttl_seconds) is not int or not 1 <= ttl_seconds <= 900):
            raise PermissionDenied("INVALID_GRANT")
        with self._lock:
            self._grant = GrantView(manifest.owner_sid, connection_id,
                                    manifest.revision, manifest.digest,
                                    manifest.ids, monotonic() + ttl_seconds)
            self._generation += 1

    def revoke(self) -> None:
        with self._lock:
            self._grant = None
            self._generation += 1

    def require(self, manifest: Manifest, connection_id: str,
                file_ids: tuple[str, ...], revision: int) -> int:
        with self._lock:
            g = self._grant
            if g is None:
                raise PermissionDenied("NO_GRANT")
            if monotonic() >= g.expires_at:
                self._grant = None
                raise PermissionDenied("EXPIRED")
            if (g.owner_sid != manifest.owner_sid or
                g.connection_id != connection_id or
                g.manifest_revision != revision or
                g.manifest_revision != manifest.revision or
                g.manifest_digest != manifest.digest):
                raise PermissionDenied("STALE_MANIFEST")
            if not file_ids or not set(file_ids).issubset(g.ids):
                raise PermissionDenied("UNKNOWN_FILE_ID")
            return self._generation

    def still_valid(self, generation: int) -> bool:
        with self._lock:
            g = self._grant
            return (g is not None and generation == self._generation
                    and monotonic() < g.expires_at)
