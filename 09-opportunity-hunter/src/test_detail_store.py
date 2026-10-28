"""OH-09 disposable SQLite detail-store test; never writes to operational DB."""
import argparse, json, sqlite3, sys, tempfile
from contextlib import closing
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parent))
from parse_details import parse

def init(db):
    db.execute("""CREATE TABLE IF NOT EXISTS opportunity_details (
        opportunity_id INTEGER PRIMARY KEY REFERENCES opportunities(id),
        official_id TEXT, structured_json TEXT NOT NULL)""")
    db.execute("""CREATE UNIQUE INDEX IF NOT EXISTS ux_detail_official
        ON opportunity_details(official_id) WHERE official_id IS NOT NULL""")

def attach(db, obj):
    site=obj["site"]
    matches=db.execute("""SELECT id FROM opportunities WHERE source_site=?
        AND (external_id=? OR canonical_url=? OR external_id=?)""",
        (site,obj["export_external_id"],obj["url"],obj["official_id"])).fetchall()
    ids={x[0] for x in matches}
    if len(ids)!=1: raise RuntimeError("OPPORTUNITY_MATCH_COUNT_"+str(len(ids)))
    oid=ids.pop()
    existing=db.execute("SELECT official_id,structured_json FROM opportunity_details WHERE opportunity_id=?",(oid,)).fetchone()
    if existing and existing[0] not in (None,obj["official_id"]):raise RuntimeError("OFFICIAL_ID_CONFLICT")
    other=db.execute("SELECT opportunity_id FROM opportunity_details WHERE official_id=?",(obj["official_id"],)).fetchone()
    if other and other[0]!=oid:raise RuntimeError("OFFICIAL_ID_ALREADY_ASSIGNED")
    data=json.dumps(obj,ensure_ascii=False,sort_keys=True)
    if existing:
        if existing[1]==data:return "SEEN",oid
        db.execute("UPDATE opportunity_details SET official_id=?,structured_json=? WHERE opportunity_id=?",(obj["official_id"],data,oid))
        return "UPDATED",oid
    db.execute("INSERT INTO opportunity_details(opportunity_id,official_id,structured_json) VALUES(?,?,?)",(oid,obj["official_id"],data))
    return "NEW",oid

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--database",required=True)
    p.add_argument("--details",nargs="+",required=True)
    a=p.parse_args()
    source=Path(a.database).resolve(strict=True)
    objects={}
    for file in a.details:
        obj=parse(json.loads(Path(file).read_text(encoding="utf-8-sig")))
        key=obj["official_id"] or obj["url"]
        if key in objects and objects[key]!=obj:raise RuntimeError("DUPLICATE_CAPTURE_CONFLICT")
        objects[key]=obj
    if len(objects)!=2:raise RuntimeError("EXPECTED_TWO_UNIQUE_PROJECTS")
    with tempfile.TemporaryDirectory(prefix="djmrn-oh09-") as td:
        target=Path(td)/"test.sqlite3"
        with closing(sqlite3.connect("file:"+source.as_posix()+"?mode=ro",uri=True)) as live,closing(sqlite3.connect(target)) as copy:
            if live.execute("PRAGMA integrity_check").fetchone()[0]!="ok":raise RuntimeError("SOURCE_INTEGRITY")
            version=live.execute("SELECT value FROM metadata WHERE key='schema_version'").fetchone()
            if not version or version[0]!="djmrn.oh.local.v1":raise RuntimeError("UNEXPECTED_SCHEMA")
            before=live.execute("SELECT COUNT(*) FROM opportunities").fetchone()[0]
            live.backup(copy)
        with closing(sqlite3.connect(target)) as db:
            db.execute("PRAGMA foreign_keys=ON")
            init(db)
            results=[]
            for _ in range(2):
                batch=[]
                for obj in objects.values():
                    with db:
                        batch.append(attach(db,obj)[0])
                results.append(batch)
            count=db.execute("SELECT COUNT(*) FROM opportunity_details").fetchone()[0]
            opportunities=db.execute("SELECT COUNT(*) FROM opportunities").fetchone()[0]
            health=db.execute("PRAGMA integrity_check").fetchone()[0]
            fk=db.execute("PRAGMA foreign_key_check").fetchall()
            ids=dict(db.execute("SELECT official_id,opportunity_id FROM opportunity_details"))
        if sorted(results[0])!=["NEW","NEW"] or sorted(results[1])!=["SEEN","SEEN"] or count!=2 or opportunities!=before or health!="ok" or fk or set(ids)!={"3066213","3066185"}:
            raise RuntimeError("OH09_ASSERTION_FAILED "+str((results,count,opportunities,health,ids)))
        print("OH_09_TEMP_DETAIL_STORE=PASS")
        print("FIRST_NEW=2; SECOND_SEEN=2; DETAIL_ROWS=2")
        print("OPPORTUNITIES_BEFORE={}; OPPORTUNITIES_AFTER={}".format(before,opportunities))
        print("OFFICIAL_ID_3066185_LINKED_TO_EXISTING_ID="+str(ids["3066185"]))
        print("INTEGRITY=ok; FOREIGN_KEYS=ok; OPERATIONAL_DB_WRITES=0; OUTBOUND_ACTIONS=0")
    print("TEMP_CLEANUP=PASS")

if __name__=="__main__":main()
