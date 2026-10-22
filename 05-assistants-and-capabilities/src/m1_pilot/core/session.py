"""Serialized, in-memory, deny-by-default tool dispatcher (NO real file reads)."""
from __future__ import annotations

from threading import RLock

from .approval import LocalApprovalControl, PermissionDenied
from .contract import ContractError, parse_envelope
from .manifest import Manifest
from .receipt import error_receipt
from .windows_guard import WindowsGuardHold, require_verified_read


class SearchSession:
    def __init__(self, manifest: Manifest, approvals: LocalApprovalControl,
                 connection_id: str):
        self.manifest = manifest
        self.approvals = approvals
        self.connection_id = connection_id
        self._lock = RLock()
        self._seen: set[str] = set()
        self._closed = False

    def close(self):
        with self._lock:
            self._closed = True
            self.approvals.revoke()

    def dispatch(self, raw_trusted_envelope: str) -> dict:
        """Never execute CAP on an unproven Windows path; negative test path only."""
        try:
            request = parse_envelope(raw_trusted_envelope)
        except ContractError as e:
            return error_receipt(None, "INVALID", e.code)
        with self._lock:
            if self._closed:
                return error_receipt(request.request_id, "BLOCKED", "SESSION_CLOSED")
            if request.request_id in self._seen:
                return error_receipt(request.request_id, "BLOCKED", "REPLAY")
            if len(self._seen) >= 256:
                self.close()
                return error_receipt(request.request_id, "BLOCKED", "REPLAY_LIMIT")
            self._seen.add(request.request_id)
            try:
                self.approvals.require(self.manifest, self.connection_id,
                                       request.args.file_ids,
                                       request.manifest_revision)
            except PermissionDenied as e:
                return error_receipt(request.request_id, "BLOCKED", e.code)
            try:
                require_verified_read(self.manifest, request.args)
            except WindowsGuardHold as e:
                return error_receipt(request.request_id, "BLOCKED", e.code)
            # Refuse fail-open if a later implementation returns unexpectedly.
            return error_receipt(request.request_id, "BLOCKED", "UNEXPECTED_GUARD_RETURN")
