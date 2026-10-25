"""Development-only test runner. No user prerequisites and no network calls."""
import pathlib,subprocess,tempfile,csv,json,shutil,sys
R=pathlib.Path(__file__).parent; D=R/'deliverable';pwsh='/tmp/djmrn-pwsh/pwsh'
root=pathlib.Path(tempfile.mkdtemp(prefix='djmrn-gate-validation-'))
script=D/'Test-DJMRN-OmniRoute-Provider-Gate-v3.ps1';harness=D/'Test-Gate-Fixtures.ps1'
checks=[]
def check(name,ok):
 checks.append(dict(Test=name,Status='PASS' if ok else 'FAIL'));assert ok,name
def run(file,*args):
 p=subprocess.run([pwsh,'-NoProfile','-File',str(file),*map(str,args)],capture_output=True,text=True,timeout=150)
 (root/f'run-{len(list(root.glob("run-*")))}.txt').write_text(p.stdout+p.stderr)
 check('Process exit '+str(args[0:2]),p.returncode==0)
 return p
def read(path):return json.loads(path.read_text(encoding='utf-8-sig'))
st=root/'selftest';run(script,'-SelfTest','-OutputDirectory',st)
selftest=read(st/'SELFTEST-RESULTS.json');fixture=pathlib.Path(selftest['FixtureDirectory'])/'input'
check('SelfTest all passed',selftest['Failed']==0)
# Add input secrets only in fields that must not be retained. No real credentials.
f=fixture/'01_ALL_ADDRESSES_AND_REASONS.csv';rs=list(csv.DictReader(f.open(encoding='utf-8-sig')))
for r in rs:r['ErrorDetail']='Bearer SYNTHETICSECRET12345';r['Server']='SECRET_SENTINEL_NOT_TO_EXPORT';r['ArbitraryPrivateColumn']='SECRET_SENTINEL_NOT_TO_EXPORT'
with f.open('w',encoding='utf-8-sig',newline='') as w:
 c=csv.DictWriter(w,rs[0].keys());c.writeheader();c.writerows(rs)
offline=root/'offline';run(script,'-InputDirectory',fixture,'-OutputDirectory',offline)
o=read(offline/'10_FULL_AUDIT_RESULTS.json');check('Offline zero requests',o['Metadata']['Queues']['A']==0 and o['Metadata']['Mode']=='AnalyzeExisting')
for p in offline.iterdir():check('No synthetic secret in '+p.name,'SYNTHETICSECRET' not in p.read_text(encoding='utf-8-sig') and 'SECRET_SENTINEL' not in p.read_text(encoding='utf-8-sig'))
check('12 mandatory outputs',len([p for p in offline.iterdir() if p.name[:2].isdigit()])==12)
check('375 rows in CSV',len(list(csv.DictReader((offline/'01_ALL_375_PROVIDERS.csv').open(encoding='utf-8-sig'))))==375)
check('375 unique IDs JSON',len({r['ProviderID'] for r in o['Providers']})==375)
ex=root/'export';run(script,'-Mode','ExportShortlist','-InputDirectory',fixture,'-OutputDirectory',ex)
check('ExportShortlist same queues',read(ex/'10_FULL_AUDIT_RESULTS.json')['Metadata']['Queues']==o['Metadata']['Queues'])
ex3=root/'export-v3';run(script,'-Mode','ExportShortlist','-InputDirectory',offline,'-OutputDirectory',ex3)
check('V3 offline evidence reused',read(ex3/'10_FULL_AUDIT_RESULTS.json')['Metadata']['InputSource']=='offline' and len(read(ex3/'10_FULL_AUDIT_RESULTS.json')['ImportedEndpointEvidence'])==len(rs))
network=root/'full';run(harness,'-OutputDirectory',network,'-InputDirectory',fixture,'-NoDelay')
n=read(network/'10_FULL_AUDIT_RESULTS.json');check('Mock full kept375',len(n['Providers'])==375)
check('Mock full actually completes',n['Metadata']['RunStatus'] in ['COMPLETE','COMPLETE_WITH_GAPS'])
check('Mock 429 retained',any(r['HTTP']==429 for r in n['Endpoints']))
check('Unvetted legacy not fresh tested',all(r['Evidence']!='SYNTHETIC_TRANSPORT' for r in n['Endpoints'] if r['Vetted']=='NO' and not any(t['URL']==r['URL'] and t['Vetted']=='YES' for t in n['Endpoints'])))
partial=root/'partial';run(harness,'-OutputDirectory',partial,'-InputDirectory',fixture,'-StopAfter','15','-NoDelay')
p=read(partial/'10_FULL_AUDIT_RESULTS.json');check('Interrupted yields PARTIAL and 375',p['Metadata']['RunStatus']=='PARTIAL' and len(p['Providers'])==375)
cp=read(partial/'checkpoint.json');completed={x['URL'] for x in cp['Results']}
run(harness,'-OutputDirectory',partial,'-InputDirectory',fixture,'-Resume','-NoDelay')
after=read(partial/'checkpoint.json');check('Resume retains completed results',completed.issubset({x['URL'] for x in after['Results']}))
check('Resume no duplicate URLs',len(after['Results'])==len({x['URL'] for x in after['Results']}))
retest=root/'retest';run(harness,'-Mode','RetestFailed','-OutputDirectory',retest,'-InputDirectory',fixture,'-NoDelay')
rt=read(retest/'10_FULL_AUDIT_RESULTS.json');check('Retest controls recorded',len(rt['Controls'])==3)
check('Synthetic cannot earn D',not any(r['Queue']=='D' for r in rt['Providers']))
check('Retest only previous noHTTP or controls',all(r['URL'] in {'https://api.llm7.io/v1/models','https://openrouter.ai/api/v1/models','https://hermes.ai.unturf.com/v1/models'} or any(x['URL']==r['URL'] and x['HTTP']=='0' for x in rs) for r in read(retest/'checkpoint.json')['Results']))
bad=root/'bad-input';bad.mkdir();(bad/'01_ALL_ADDRESSES_AND_REASONS.csv').write_text('corrupt')
badout=root/'bad-output';run(script,'-InputDirectory',bad,'-OutputDirectory',badout)
check('Malformed input gets report',len(read(badout/'10_FULL_AUDIT_RESULTS.json')['Providers'])==375)
empty=root/'empty';run(script,'-InputDirectory',root/'missing','-OutputDirectory',empty)
check('Missing input stays offline',read(empty/'checkpoint.json')['Results']==[])
result=dict(Environment='Linux PowerShell 7.4.6 (.NET 8), NOT Windows PowerShell 5.1',Tests=checks,SelfTest=selftest['Tests'],NetworkRequests=0,WindowsPS51Parser='NOT_RUN',WindowsRealNetwork='NOT_RUN',TestDirectory=str(root))
(D/'VALIDATION-RESULTS.json').write_text(json.dumps(result,ensure_ascii=False,indent=2))
sample=D/'SYNTHETIC-SAMPLE-OUTPUT';sample.mkdir(exist_ok=True)
for p in offline.iterdir():
 if p.name[:2].isdigit():shutil.copyfile(p,sample/p.name)
print(json.dumps(dict(Checks=len(checks),SelfTest=len(selftest['Tests']),Status='PASS',Directory=str(root))))
