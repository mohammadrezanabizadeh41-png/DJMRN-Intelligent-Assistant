"""DJMRN OH-23 source: offline Freelancermap detail extractor.

Additive structured-field extension of OH-08. Reads JSON files only; stdout only;
never opens SQLite or a network connection. Original capture remains canonical.
GitHub source readiness does not imply Windows deployment or DB-write approval.
"""
import argparse
import hashlib
import json
import re
from pathlib import Path
from urllib.parse import urlsplit

CURRENCIES = {"£": "GBP", "$": "USD", "€": "EUR", "GBP": "GBP", "USD": "USD", "EUR": "EUR"}
CURRENCY_PATTERN = r"(?:£|\$|€|GBP|USD|EUR)"
RATE_RE = re.compile(
    rf"(?P<currency>{CURRENCY_PATTERN})\s*(?P<amount>\d[\d,]*(?:\.\d{{1,2}})?)\s*"
    r"(?:per\s+|/\s*)(?P<unit>hour|day|week|month|project|hr|daily|hourly|annum|year)\b",
    re.I,
)
SC_MENTION_RE = re.compile(r"\bSC\b|\bsecurity\s+(?:check|clearance)\b", re.I)
SC_HARD_RE = re.compile(
    r"\b(?:mandatory|required|essential|cannot\s+be\s+considered)\b"
    r"|\bmust\s+(?:already\s+)?(?:hold|have)\s+"
    r"(?:(?:current|valid|existing)\s+)?(?:SC|security\s+(?:check|clearance))\b", re.I
)
SC_SOFT_RE = re.compile(
    r"\b(?:advantage|desirable|preferred|would\s+be\s+beneficial|"
    r"eligible\s+and\s+willing\s+to\s+undergo)\b", re.I
)
SC_NOT_REQUIRED_RE = re.compile(
    r"\b(?:not\s+(?:currently\s+)?(?:mandatory|required|essential)"
    r"|no\s+(?:(?:SC|security)\s+)?clearance\s+required)\b", re.I
)
DURATION_RE = re.compile(r"\b(?:initial\s+)?(?P<count>\d{1,2})\s*[- ]\s*(?P<unit>months?|weeks?|days?)\b", re.I)
ONSITE_DAYS_RE = re.compile(r"\b(?P<low>\d)\s*(?:-|to)\s*(?P<high>\d)\s*days?\s*per\s*week\s*on\s*[- ]?site\b", re.I)
ONE_ONSITE_DAY_RE = re.compile(r"\b(?P<count>\d)\s*days?\s*per\s*week\s*on\s*[- ]?site\b", re.I)


def _excerpt(s, limit=220):
    return re.sub(r"\s+", " ", s).strip()[:limit]


def _money(description):
    """Rate is NOT a total contract budget. Conflicting rates are not guessed."""
    candidates = []
    for line in description.splitlines():
        for match in RATE_RE.finditer(line):
            token = match.group("currency")
            unit = match.group("unit").casefold()
            unit = {"hr": "hour", "hourly": "hour", "daily": "day", "annum": "year"}.get(unit, unit)
            amount = float(match.group("amount").replace(",", ""))
            if amount <= 0:
                continue
            amount = int(amount) if amount.is_integer() else amount
            item = {"kind": "rate", "amount": amount, "currency": CURRENCIES[token.upper()] if token.upper() in CURRENCIES else CURRENCIES[token],
                    "unit": unit, "is_total_budget": False, "evidence": _excerpt(line)}
            candidates.append(item)
    unique = {(x["amount"], x["currency"], x["unit"]): x for x in candidates}
    if len(unique) == 1:
        return next(iter(unique.values())), []
    if len(unique) > 1:
        return None, ["RATE_CONFLICT_REVIEW"]
    for line in description.splitlines():
        m = re.search(rf"(?P<currency>{CURRENCY_PATTERN})\s*competitive\b|\bcompetitive\s+(?:rate|salary)\b", line, re.I)
        if m:
            symbol = m.group("currency")
            currency = CURRENCIES.get(symbol.upper(), CURRENCIES.get(symbol)) if symbol else None
            return {"kind": "qualitative_rate", "amount": None, "currency": currency,
                    "unit": None, "is_total_budget": False, "qualifier": "competitive", "evidence": _excerpt(line)}, ["RATE_UNQUANTIFIED"]
    return None, ["BUDGET_UNSPECIFIED"]


def _clearance(description):
    """Apply cues only within a clause mentioning SC; preserve supporting text."""
    chunks = re.split(r"(?<=[.!?;])\s+|\n+", description)
    categorized = []
    for chunk in chunks:
        evidence = _excerpt(chunk)
        if not SC_MENTION_RE.search(evidence):
            continue
        if SC_NOT_REQUIRED_RE.search(evidence):
            status = "NOT_REQUIRED"
        elif SC_SOFT_RE.search(evidence):
            status = "PREFERRED_OR_ELIGIBLE"
        elif SC_HARD_RE.search(evidence):
            status = "REQUIRED_CURRENT"
        else:
            status = "MENTIONED_ONLY"
        categorized.append((status, evidence))
    statuses = {status for status, _ in categorized}
    if "REQUIRED_CURRENT" in statuses and statuses.intersection(
        {"NOT_REQUIRED", "PREFERRED_OR_ELIGIBLE"}
    ):
        status = "AMBIGUOUS"
    else:
        status = next((x for x in (
            "REQUIRED_CURRENT", "PREFERRED_OR_ELIGIBLE", "NOT_REQUIRED", "MENTIONED_ONLY"
        ) if x in statuses), "NOT_MENTIONED")
    evidence = next((x for s, x in categorized if s == status),
                    categorized[0][1] if categorized else None)
    warnings = ["SC_REQUIREMENT_CONFLICT"] if status == "AMBIGUOUS" else []
    return {"status": status, "current_clearance_mandatory": status == "REQUIRED_CURRENT",
            "evidence": evidence}, warnings


def _modes(s):
    return [name for name, pat in (("On-site", r"\bon[ -]?site\b"),
                                  ("Hybrid", r"\bhybrid\b"), ("Remote", r"\bremote(?:ly)?\b"))
            if re.search(pat, s, re.I)]


def _duration(pre, description):
    header = next((int(m.group(1)) for s in pre if (m := re.fullmatch(r"Duration\s+(\d+)\s+months?", s, re.I))), None)
    matches = list(DURATION_RE.finditer(description))
    durations = [m for m in matches if ("contract" in description[max(0, m.start()-30):m.end()+30].casefold()
                or "duration" in description[max(0, m.start()-30):m.end()+30].casefold())]
    info = None
    if header is not None:
        info = {"count": header, "unit": "month", "source": "header"}
    elif durations:
        m = durations[0]
        info = {"count": int(m.group("count")), "unit": m.group("unit").casefold().rstrip("s"), "source": "description"}
    extension = bool(re.search(r"\b(?:potential\s+extension|option\s+to\s+extend|possible\s+extension)\b", description, re.I))
    return header if header is not None else (info["count"] if info and info["unit"] == "month" else None), {
        "term": info, "extension_mentioned": extension
    }


def parse(d):
    if d.get("schema_version") != "djmrn.oh.detail.v1" or d.get("site") != "freelancermap":
        raise ValueError("INVALID_SCHEMA")
    url = d.get("url")
    if not isinstance(url, str):
        raise ValueError("INVALID_URL")
    u = urlsplit(url)
    if u.scheme != "https" or u.hostname not in ("freelancermap.com", "www.freelancermap.com") or not u.path.startswith("/project/"):
        raise ValueError("INVALID_URL")
    raw = d.get("visible_text")
    if not isinstance(raw, str) or len(raw) < 100:
        raise ValueError("INVALID_TEXT")
    lines = [s.strip() for s in raw.replace("\xa0", " ").splitlines() if s.strip()]
    title_raw = d.get("title")
    if not isinstance(title_raw, str):
        raise ValueError("MISSING_TITLE")
    title = title_raw.strip()
    if title not in lines or "Description" not in lines:
        raise ValueError("MISSING_SECTIONS")
    ix = lines.index("Description")
    end = lines.index("Application form", ix + 1) if "Application form" in lines[ix + 1:] else len(lines)
    description = "\n".join(lines[ix + 1:end]).strip()
    if not description:
        raise ValueError("EMPTY_DESCRIPTION")
    if end < len(lines):
        form_end = lines.index("Similar projects", end + 1) if "Similar projects" in lines[end + 1:] else len(lines)
        form = "\n".join(lines[end + 1:form_end]).strip()
    else:
        form = None
    official_match = re.search(r"^#(\d{5,12})$", raw, re.M)
    official = official_match.group(1) if official_match else None
    if not official:
        tail_match = re.search(r"-(\d{5,12})/?$", u.path)
        official = tail_match.group(1) if tail_match else None
    pre = lines[lines.index(title) + 1:ix]
    company = pre[0] if pre else None
    countries = ("United Kingdom", "Ireland", "Germany", "France", "Netherlands", "Belgium", "Spain", "Portugal", "United States", "Canada")
    country = next((s for s in pre if s in countries), None)
    header_modes = [x for x in ("On-site", "Hybrid", "Remote") if any(s.casefold() == x.casefold() for s in pre)]
    description_modes = _modes(description)
    duration, contract_duration = _duration(pre, description)
    pos = next((i for i, s in enumerate(pre) if re.fullmatch(r"Duration\s+\d+\s+months?", s, re.I)), None)
    skills = []
    if pos is not None:
        candidate = pre[pos + 1:]
        if "Save to watchlist" in candidate:
            candidate = candidate[candidate.index("Save to watchlist") + 1:]
        skills = [s for s in candidate if s not in ("Apply now", "Save to watchlist")]
    warnings = []
    if header_modes and description_modes and not set(header_modes).intersection(description_modes):
        warnings.append("WORK_MODE_CONFLICT")
    elif header_modes == ["On-site"] and "Hybrid" in description_modes:
        warnings.append("ON_SITE_HEADER_WITH_HYBRID_DETAILS")
    if not country:
        warnings.append("COUNTRY_UNSPECIFIED")
    if not header_modes:
        warnings.append("WORK_MODE_UNSPECIFIED")
    if contract_duration["term"] is None:
        warnings.append("DURATION_UNSPECIFIED")
    rate, rate_warnings = _money(description)
    warnings.extend(rate_warnings)
    clearance, sc_warnings = _clearance(description)
    warnings.extend(sc_warnings)
    onsite = ONSITE_DAYS_RE.search(description) or ONE_ONSITE_DAY_RE.search(description)
    days = None
    if onsite:
        days = {"min": int(onsite.group("low")), "max": int(onsite.group("high"))} if "low" in onsite.groupdict() else {"min": int(onsite.group("count")), "max": int(onsite.group("count"))}
        if days["max"] > 7 or days["min"] > days["max"]:
            days = None
            warnings.append("ONSITE_FREQUENCY_AMBIGUOUS")
    if d.get("truncated"):
        warnings.append("SOURCE_TEXT_TRUNCATED")
    return {
        "schema_version": "djmrn.oh.structured.v1", "site": "freelancermap",
        "official_id": official, "export_external_id": d.get("external_id"),
        "title": title, "url": url, "company": company, "country": country,
        "work_mode_header": header_modes, "work_mode_description": description_modes,
        "work_arrangement": {"header": header_modes, "description": description_modes,
                             "onsite_days_per_week": days, "remote_mentioned": "Remote" in description_modes},
        "duration_months": duration, "contract_duration": contract_duration,
        "budget": rate, "security_clearance": clearance,
        "skills_explicit": skills, "description": description, "application_form": form,
        "source_evidence": {"visible_text_sha256": hashlib.sha256(raw.encode("utf-8")).hexdigest(),
                            "extracted_at_utc": d.get("extracted_at_utc"),
                            "truncated": bool(d.get("truncated"))},
        "warnings": warnings,
    }


def main():
    p = argparse.ArgumentParser(description="OH-23 offline parser; no DB/network")
    p.add_argument("files", nargs="+")
    args = p.parse_args()
    seen = set()
    for filename in args.files:
        d = json.loads(Path(filename).read_text(encoding="utf-8-sig"))
        obj = parse(d)
        key = obj["official_id"] or obj["url"]
        if key in seen:
            print("DUPLICATE_CAPTURE=" + key)
            continue
        seen.add(key)
        report = {k: v for k, v in obj.items() if k not in ("description", "application_form")}
        report["description_chars"] = len(obj["description"])
        report["application_form_chars"] = len(obj["application_form"] or "")
        print(json.dumps(report, ensure_ascii=False))
    print(f"OH_23_OFFLINE_PARSE=PASS; UNIQUE_PROJECTS={len(seen)}; DATABASE_WRITES=0; NETWORK_ACTIONS=0")


if __name__ == "__main__":
    main()
