"""OH-18: read-only comparison of exported listings with local SQLite."""
import argparse,json,sqlite3
from pathlib import Path
from contextlib import closing
from collections import Counter

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--database",required=True)
    p.add_argument("--export",required=True)
    a=p.parse_args()
    payload=json.loads(Path(a.export).read_text(encoding="utf-8-sig"))
    if payload.get("schema_version")!="djmrn.oh.export.v1":raise ValueError("INVALID_EXPORT")
    rows=payload.get("opportunities")
    if not isinstance(rows,list) or len(rows)>1000:raise ValueError("INVALID_ROWS")
    uri="file:"+Path(a.database).resolve(strict=True).as_posix()+"?mode=ro"
    with closing(sqlite3.connect(uri,uri=True)) as db:
        db.execute("PRAGMA query_only=ON")
        old=db.execute("SELECT external_id,title,canonical_url FROM opportunities WHERE source_site='freelancermap'").fetchall()
    known={r[0]:r for r in old}
    known_urls={r[2]:r for r in old}
    counts=Counter()
    seen=set()
    for row in rows:
        if row.get("site")!="freelancermap":raise ValueError("INVALID_SITE")
        eid,title,url=row["external_id"],row["title"],row["url"]
        if (eid,url) in seen:raise ValueError("DUPLICATE_EXPORT")
        seen.add((eid,url))
        previous=known.get(eid) or known_urls.get(url)
        status="NEW" if previous is None else ("UPDATED_TITLE" if previous[1]!=title else "SEEN")
        counts[status]+=1
        print(json.dumps({"status":status,"title":title,"url":url},ensure_ascii=False))
    print("OH_18_READ_ONLY=PASS; TOTAL={}; NEW={}; SEEN={}; UPDATED_TITLE={}; DB_WRITES=0; SENDS=0".format(len(rows),counts["NEW"],counts["SEEN"],counts["UPDATED_TITLE"]))
if __name__=="__main__":main()
