"""Bounded and truthful status receipts; never let a model author a citation."""
from __future__ import annotations

from . import SCHEMA_VERSION

STATUS = frozenset({
    "OK", "NOT_FOUND", "INVALID", "BLOCKED",
    "CANCELLED", "TOOL_ERROR", "INTERRUPTED"
})


def error_receipt(request_id: str | None, status: str, code: str) -> dict:
    if status not in STATUS - {"OK", "NOT_FOUND"}:
        raise ValueError("INVALID_STATUS")
    # Do not leak file paths, owner SID, stack traces or secret content.
    if not code.isascii() or not code.replace("_", "").isalnum():
        code = "UNSPECIFIED"
    return {
        "schema_version": SCHEMA_VERSION, "request_id": request_id,
        "status": status, "searched": [], "matches": [],
        "match_count_returned": 0, "truncated": False,
        "error": {"code": code, "message_fa": {
            "BLOCKED": "دسترسی به فایل مجاز یا قابل تأیید نیست.",
            "INVALID": "درخواست معتبر نیست.",
            "CANCELLED": "درخواست لغو شد.",
            "TOOL_ERROR": "جست‌وجو با خطا متوقف شد.",
            "INTERRUPTED": "پایان عملیات قابل تأیید نیست."
        }[status], "retry_allowed": False}
    }
