"""OH-10: backed-up, explicitly approved production detail import. No outbound actions."""
import argparse,hashlib,json,sqlite3,sys
from pathlib import Path
from datetime import datetime,timezone
from contextlib import closing
sys.path.insert(0,str(Path(__file__).resolve().parent))
from parse_details import parse

def snapshot(db,table):
    return hashlib.sha256(repr(db.execute("SELECT * FROM "+table+" ORDER BY rowid").fetchall()).encode()).hexdigest(),db.execute("SELECT COUNT(*) FROM "+table).fetchone()[0]

def run(a):
    dbpath=Path(a.database).resolve(strict=True)
    backups=Path(a.backups).resolve(strict=True)
    objects={}
    for path in a.details:
        obj=parse(json.loads(Path(path).read_text(encoding="utf-8-sig")))
        key=obj["official_id"]
        if key in objects and obj!=objects[key]:raise ValueError("CONFLICTING_CAPTURES")
        objects[key]=obj
    if set(objects)!={"3066213","3066185"}:raise ValueError("EXPECTED_TWO_KNOWN_PROJECTS")
    with closing(sqlite3.connect(dbpath,timeout=10)) as db:
        db.execute("PRAGMA foreign_keys=ON")
        if db.execute("PRAGMA integrity_check").fetchone()[0]!="ok":raise ValueError("DB_NOT_HEALTHY")
        if db.execute("SELECT value FROM metadata WHERE key='schema_version'").fetchone()!=("djmrn.oh.local.v1",):raise ValueError("SCHEMA_VERSION")
        before={t:snapshot(db,t) for t in ("opportunities","opportunity_history")}
        if before["opportunities"][1]!=22:raise ValueError("EXPECTED_22")
        ids={}
        for key,obj in objects.items():
            matches=db.execute("SELECT id FROM opportunities WHERE source_site=? AND (external_id=? OR external_id=? OR canonical_url=?)",(obj["site"],obj["export_external_id"],key,obj["url"])).fetchall()
            if len(matches)!=1:raise ValueError("MATCH_NOT_UNIQUE_"+key)
            ids[key]=matches[0][0]
        if len(set(ids.values()))!=2 or ids["3066185"]!=20:raise ValueError("ID_RECONCILIATION")
        backup=backups/("opportunities-pre-oh10-"+datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S%fZ")+".sqlite3")
        with closing(sqlite3.connect(backup)) as b:db.backup(b)
        with closing(sqlite3.connect(backup)) as b:
            if b.execute("PRAGMA integrity_check").fetchone()[0]!="ok" or {t:snapshot(b,t) for t in before}!=before:raise ValueError("BACKUP_VERIFICATION")
        print("OH_10_BACKUP=PASS; FILE="+str(backup),flush=True)
        try:
            db.execute("BEGIN IMMEDIATE")
            db.execute("CREATE TABLE IF NOT EXISTS opportunity_details(opportunity_id INTEGER PRIMARY KEY REFERENCES opportunities(id),official_id TEXT,structured_json TEXT NOT NULL)")
            if [x[1] for x in db.execute("PRAGMA table_info(opportunity_details)")]!=["opportunity_id","official_id","structured_json"]:raise ValueError("DETAIL_SCHEMA")
            db.execute("CREATE UNIQUE INDEX IF NOT EXISTS ux_detail_official ON opportunity_details(official_id) WHERE official_id IS NOT NULL")
            events=[]
            for key,obj in objects.items():
                oid=ids[key];payload=json.dumps(obj,sort_keys=True,ensure_ascii=False)
                old=db.execute("SELECT official_id,structured_json FROM opportunity_details WHERE opportunity_id=?",(oid,)).fetchone()
                if old is None:
                    db.execute("INSERT INTO opportunity_details VALUES(?,?,?)",(oid,key,payload));events.append("NEW")
                elif old==(key,payload):events.append("SEEN")
                elif old[0] in (None,key):
                    db.execute("UPDATE opportunity_details SET official_id=?,structured_json=? WHERE opportunity_id=?",(key,payload,oid));events.append("UPDATED")
                else:raise ValueError("DETAIL_CONFLICT")
            if {t:snapshot(db,t) for t in before}!=before:raise ValueError("ORIGINAL_ROWS_CHANGED")
            if db.execute("PRAGMA foreign_key_check").fetchall() or db.execute("PRAGMA quick_check").fetchone()[0]!="ok":raise ValueError("INTEGRITY_FAILED")
            db.commit()
        except:
            db.rollback()
            raise
        if {t:snapshot(db,t) for t in before}!=before:raise ValueError("POSTCOMMIT_ORIGINAL_ROWS_CHANGED")
        print("OH_10_PRODUCTION_IMPORT=PASS")
        print("EVENTS="+",".join(events)+"; DETAIL_ROWS="+str(db.execute("SELECT COUNT(*) FROM opportunity_details").fetchone()[0]))
        print("OPPORTUNITIES=22; HISTORY="+str(before["opportunity_history"][1])+"; ID_3066185="+str(ids["3066185"]))
        print("ORIGINAL_ROWS_UNCHANGED=YES; BACKUP_RETAINED=YES; OUTBOUND_ACTIONS=0")
if __name__=="__main__":
    p=argparse.ArgumentParser()
    p.add_argument("--database",required=True);p.add_argument("--backups",required=True)
    p.add_argument("--details",nargs="+",required=True)
    p.add_argument("--approve-production-write",action="store_true")
    a=p.parse_args()
    if not a.approve_production_write:raise SystemExit("EXPLICIT_APPROVAL_REQUIRED")
    run(a)
