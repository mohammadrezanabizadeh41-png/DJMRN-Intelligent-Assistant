"""Strict tool input and trusted envelope parsing; no filesystem, model or network."""
from __future__ import annotations

from dataclasses import dataclass
import json
import re
from uuid import UUID

from . import SCHEMA_VERSION, TOOL_NAME

_ID_RE = re.compile(r"^[a-z][a-z0-9-]{1,31}$", re.ASCII)
MAX_MESSAGE_CHARS = 8192


class ContractError(ValueError):
    def __init__(self, code: str):
        super().__init__(code)
        self.code = code


def _pairs_no_duplicates(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ContractError("DUPLICATE_JSON_KEY")
        result[key] = value
    return result


def _constant_forbidden(_):
    raise ContractError("NONFINITE_NUMBER")


def strict_json_object(raw: str) -> dict:
    if type(raw) is not str or len(raw) > MAX_MESSAGE_CHARS:
        raise ContractError("MESSAGE_SIZE")
    try:
        data = json.loads(raw, object_pairs_hook=_pairs_no_duplicates,
                          parse_constant=_constant_forbidden)
    except ContractError:
        raise
    except (ValueError, TypeError, RecursionError):
        raise ContractError("MALFORMED_JSON") from None
    if type(data) is not dict:
        raise ContractError("NOT_OBJECT")
    return data


def _valid_text(value: object) -> bool:
    return type(value) is str and not any(
        ord(c) < 32 or ord(c) == 127 or 0xD800 <= ord(c) <= 0xDFFF
        for c in value
    )


@dataclass(frozen=True)
class SearchArgs:
    query: str
    file_ids: tuple[str, ...]
    max_matches: int = 8


def parse_model_args(data: dict) -> SearchArgs:
    if type(data) is not dict:
        raise ContractError("ARGUMENTS_NOT_OBJECT")
    if not {"query", "file_ids"}.issubset(data) or (
        set(data) - {"query", "file_ids", "max_matches"}
    ):
        raise ContractError("ARGUMENT_FIELDS")
    query = data["query"]
    if not _valid_text(query) or not query.strip() or len(query) > 512:
        raise ContractError("QUERY_INVALID")
    ids = data["file_ids"]
    if type(ids) is not list or not 1 <= len(ids) <= 2:
        raise ContractError("FILE_COUNT")
    if any(type(fid) is not str or not _ID_RE.fullmatch(fid) for fid in ids):
        raise ContractError("FILE_ID_INVALID")
    if len(set(ids)) != len(ids):
        raise ContractError("FILE_ID_DUPLICATE")
    limit = data.get("max_matches", 8)
    if type(limit) is not int or not 1 <= limit <= 8:
        raise ContractError("MATCH_LIMIT")
    return SearchArgs(query=query, file_ids=tuple(ids), max_matches=limit)


@dataclass(frozen=True)
class Envelope:
    request_id: str
    manifest_revision: int
    args: SearchArgs


def parse_envelope(raw: str) -> Envelope:
    obj = strict_json_object(raw)
    if set(obj) != {
        "schema_version", "request_id", "operation", "manifest_revision", "arguments"
    }:
        raise ContractError("ENVELOPE_FIELDS")
    if obj["schema_version"] != SCHEMA_VERSION or obj["operation"] != TOOL_NAME:
        raise ContractError("UNKNOWN_TOOL")
    rid = obj["request_id"]
    if type(rid) is not str:
        raise ContractError("REQUEST_ID")
    try:
        parsed = UUID(rid)
    except (ValueError, AttributeError):
        raise ContractError("REQUEST_ID") from None
    if str(parsed) != rid or parsed.version != 4:
        raise ContractError("REQUEST_ID")
    revision = obj["manifest_revision"]
    if type(revision) is not int or revision <= 0:
        raise ContractError("MANIFEST_REVISION")
    return Envelope(rid, revision, parse_model_args(obj["arguments"]))
