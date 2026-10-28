"""OH-08 offline structured parsing of Freelancermap detail exports; no database writes."""
import argparse, json, re
from pathlib import Path
from urllib.parse import urlsplit

def parse(d):
    if d.get("schema_version")!="djmrn.oh.detail.v1" or d.get("site")!="freelancermap": raise ValueError("INVALID_SCHEMA")
    u=urlsplit(d["url"])
    if u.scheme!="https" or u.hostname not in ("freelancermap.com","www.freelancermap.com") or not u.path.startswith("/project/"): raise ValueError("INVALID_URL")
    raw=d["visible_text"]
    if not isinstance(raw,str) or len(raw)<100: raise ValueError("INVALID_TEXT")
    lines=[s.strip() for s in raw.replace("\xa0"," ").splitlines() if s.strip()]
    title=d["title"].strip()
    if title not in lines or "Description" not in lines: raise ValueError("MISSING_SECTIONS")
    ix=lines.index("Description")
    end=lines.index("Application form",ix+1) if "Application form" in lines[ix+1:] else len(lines)
    description="\n".join(lines[ix+1:end]).strip()
    form="\n".join(lines[end+1:]).strip() if end<len(lines) else None
    if not description: raise ValueError("EMPTY_DESCRIPTION")
    h=re.search(r"^#(\d{5,12})$",raw,re.M)
    official=h.group(1) if h else None
    if not official:
        m=re.search(r"-(\d{5,12})/?$",u.path)
        official=m.group(1) if m else None
    pre=lines[lines.index(title)+1:ix]
    company=pre[0] if pre else None
    countries=("United Kingdom","Ireland","Germany","France","Netherlands","Belgium","Spain","Portugal","United States","Canada")
    country=next((s for s in pre if s in countries),None)
    header_modes=[m for m in ("On-site","Hybrid","Remote") if any(s.casefold()==m.casefold() for s in pre)]
    description_modes=[m for m,p in (("On-site",r"\bon[ -]?site\b"),("Hybrid",r"\bhybrid\b"),("Remote",r"\bremote\b")) if re.search(p,description,re.I)]
    duration=next((int(m.group(1)) for s in pre if (m:=re.fullmatch(r"Duration\s+(\d+)\s+months?",s,re.I))),None)
    pos=next((i for i,s in enumerate(pre) if re.fullmatch(r"Duration\s+\d+\s+months?",s,re.I)),None)
    skills=[]
    if pos is not None:
        candidate=pre[pos+1:]
        if "Save to watchlist" in candidate: candidate=candidate[candidate.index("Save to watchlist")+1:]
        skills=[s for s in candidate if s not in ("Apply now","Save to watchlist")]
    warnings=[]
    if header_modes and description_modes and not set(header_modes).intersection(description_modes): warnings.append("WORK_MODE_CONFLICT")
    if not country: warnings.append("COUNTRY_UNSPECIFIED")
    if not header_modes: warnings.append("WORK_MODE_UNSPECIFIED")
    if duration is None: warnings.append("DURATION_UNSPECIFIED")
    warnings.append("BUDGET_UNSPECIFIED")
    if d.get("truncated"): warnings.append("SOURCE_TEXT_TRUNCATED")
    return {"schema_version":"djmrn.oh.structured.v1","site":"freelancermap","official_id":official,"export_external_id":d.get("external_id"),"title":title,"url":d["url"],"company":company,"country":country,"work_mode_header":header_modes,"work_mode_description":description_modes,"duration_months":duration,"budget":None,"skills_explicit":skills,"description":description,"application_form":form,"warnings":warnings}

def main():
    p=argparse.ArgumentParser()
    p.add_argument("files",nargs="+")
    args=p.parse_args()
    seen=set()
    for filename in args.files:
        d=json.loads(Path(filename).read_text(encoding="utf-8-sig"))
        obj=parse(d)
        key=obj["official_id"] or obj["url"]
        if key in seen:
            print("DUPLICATE_CAPTURE="+key)
            continue
        seen.add(key)
        report={k:v for k,v in obj.items() if k not in ("description","application_form")}
        report["description_chars"]=len(obj["description"])
        report["application_form_chars"]=len(obj["application_form"] or "")
        print(json.dumps(report,ensure_ascii=False))
    print("OH_08_OFFLINE_PARSE=PASS; UNIQUE_PROJECTS={}; DATABASE_WRITES=0; NETWORK_ACTIONS=0".format(len(seen)))

if __name__=="__main__":main()
