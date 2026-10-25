import csv, json, re, pathlib, subprocess, hashlib, gzip, base64
ROOT=pathlib.Path(__file__).parent
OUT=ROOT/'deliverable'
PROJECT=ROOT/'project-source'
UP=ROOT/'upstream-source'
def head(p):return subprocess.check_output(['git','-C',str(p),'rev-parse','HEAD'],text=True).strip()
PH,UH=head(PROJECT),head(UP)
def blob(p,f):return subprocess.check_output(['git','-C',str(p),'rev-parse',f'HEAD:{f}'],text=True).strip()
BASE='06-tests-and-evidence/tools/omniroute-iran-direct-check/'
def rows(n):return list(csv.DictReader((PROJECT/BASE/n).open(encoding='utf-8-sig')))
catalog=rows('OmniRoute_v3.8.52_375_providers.csv')
snapshot=rows('OmniRoute_v3.8.52_upstream_api_snapshot.csv')
extras=rows('OmniRoute_v3.8.52_api_discovery_additions.csv')
snapshot_data=json.loads((UP/'tests/snapshots/provider/translate-path.json').read_text())
assert len(catalog)==len({p['ProviderID'] for p in catalog})==375
for x in snapshot:assert x['InferenceEndpoint'] in snapshot_data[x['ProviderID']]['url'].values()
sources=[]
paths=['PROJECT-RULES.md','SOURCES-AND-AUTHORITY.md','07-operations-and-continuity/CURRENT-STATUS.md','04-work-research-bridge/README.md','04-work-research-bridge/REPOSITORY-LOCK.md','02-project-management/DECISION-REGISTER.md','06-tests-and-evidence/plans/OMNIROUTE-WINDOWS-FIRST-PILOT-20261024.md','06-tests-and-evidence/logs/OMNIROUTE-375-DEEP-AUDIT-V2-USER-RUN-20261025.md']
paths+= [str(p.relative_to(PROJECT)) for p in sorted((PROJECT/BASE).iterdir()) if p.is_file()]
for f in paths:sources.append(dict(Repository='mohammadrezanabizadeh41-png/DJMRN-Intelligent-Assistant',HEAD=PH,Path=f,BlobSHA=blob(PROJECT,f),Bytes=len((PROJECT/f).read_bytes())))
up_paths=['docs/reference/PROVIDER_REFERENCE.md','docs/reference/FREE_TIERS.md','tests/snapshots/provider/translate-path.json','docs/architecture/RESILIENCE_GUIDE.md','src/shared/constants/providers.ts','open-sse/config/freeModelCatalog.data.ts']
registry={}
for p in sorted((UP/'open-sse/config/providers/registry').glob('*/index.ts')):
 text=p.read_text();registry[p.parent.name]=text;up_paths.append(str(p.relative_to(UP)))
for f in up_paths:sources.append(dict(Repository='cheaper-inference/OmniRoute',HEAD=UH,Path=f,BlobSHA=blob(UP,f),Bytes=len((UP/f).read_bytes())))
def official(path):return f'https://github.com/cheaper-inference/OmniRoute/blob/{UH}/{path}'
ref=official('docs/reference/PROVIDER_REFERENCE.md');snap=official('tests/snapshots/provider/translate-path.json')
targets=[];seen=set()
def add(id,kind,url,source,vetted='YES'):
 if not url.startswith('https://') or any(s in url.lower() for s in ['${','<','{','}','%7b','%7d']):return
 k=(id,kind,url)
 if k not in seen:targets.append(dict(ProviderID=id,ProbeKind=kind,URL=url,Source=source,Vetted=vetted));seen.add(k)
from urllib.parse import urlsplit
for p in catalog:
 if p['WebsiteURL'].startswith('https://'):
  u=urlsplit(p['WebsiteURL']);add(p['ProviderID'],'WEBSITE_ORIGIN',f'{u.scheme}://{u.netloc}/',ref)
for x in snapshot:
 add(x['ProviderID'],'API_HOST',x['HostOrigin'],snap)
 add(x['ProviderID'],'API_ACTUAL_ROUTE_GET',x['InferenceEndpoint'],snap)
# All literal snapshot variants, not just nonStream; no synthesized /models paths.
for id,entry in snapshot_data.items():
 if id not in {p['ProviderID'] for p in catalog}:continue
 for url in set(entry.get('url',{}).values()):add(id,'API_ACTUAL_ROUTE_GET',url,snap)
known={}
for id,text in registry.items():
 for k in ['baseUrl','modelsUrl','healthUrl','statusUrl']:
  m=re.search(r'^\s*'+k+r':\s*"(https://[^"\n]+)"',text,re.M)
  if m:known[(id,m[1])]=official(f'open-sse/config/providers/registry/{id}/index.ts')
for x in extras:
 s=known.get((x['ProviderID'],x['ProbeURL']))
 if x['ProviderID']=='openrouter' and x['ProbeURL']=='https://openrouter.ai/api/v1/models':s='https://openrouter.ai/docs/api-reference/models/get-models'
 if x['ProviderID']=='groq' and x['ProbeURL']=='https://api.groq.com/openai/v1/models':s='https://console.groq.com/docs/models'
 if not s and x['ProviderID']=='llm7' and x['ProbeKind']=='SIGNUP_DASHBOARD':s='https://docs.llm7.io/limits'
 if not s and x['ProviderID']=='openrouter' and x['ProbeKind']=='SIGNUP_DASHBOARD':s='https://openrouter.ai/pricing'
 # Preserve all old targets for offline import, but curated uncorroborated URLs are not scanned.
 add(x['ProviderID'],x['ProbeKind'],x['ProbeURL'],s or 'LEGACY_CURATED_NOT_INDEPENDENTLY_VERIFIED', 'YES' if s else 'NO')
for (id,url),source in known.items():
 if id not in {p['ProviderID'] for p in catalog}:continue
 text=registry[id]
 if re.search(r'modelsUrl:\s*"'+re.escape(url)+'"',text):
  if not any(t['ProviderID']==id and t['URL']==url and t['ProbeKind'] in ['CURATED_PUBLIC_DISCOVERY','SOURCE_REGISTRY_MODELS'] for t in targets):add(id,'API_MODELS',url,source)
 # Literal API bases may be dynamic /accounts prefixes; never call these inference.
 elif not any(t['ProviderID']==id and t['URL']==url for t in targets):add(id,'API_BASE_SOURCE_ONLY',url,source)

def f(status='FREE_PLAN_UNVERIFIED',source='UNKNOWN',quota='UNKNOWN',card='UNKNOWN',over='UNKNOWN',region='UNKNOWN',commercial='UNKNOWN',rpm='UNKNOWN',rpd='UNKNOWN',tokens='UNKNOWN',reset='UNKNOWN'):
 return dict(FreeStatus=status,Source=source,Quota=quota,CardRequired=card,Overage=over,Region=region,Commercial=commercial,RPM=rpm,RPD=rpd,Tokens=tokens,Reset=reset,CheckedAt='2026-10-25' if source!='UNKNOWN' else 'NOT_VERIFIED')
free={
 'llm7':f('FREE_POSSIBLE_ACCOUNT_REQUIRED','https://docs.llm7.io/limits; https://docs.llm7.io/guides/models-api','Free token, turbo models only; service is research/experimental',tokens='100000 input+output per rolling 24h',rpm='60; 1/s; 250/hour',reset='Rolling 24 hours'),
 'openrouter':f('FREE_POSSIBLE_ACCOUNT_REQUIRED','https://openrouter.ai/pricing','Free-model API only',card='NO',rpm='20',rpd='50',over='FREE_MODELS_ONLY; ACCOUNT_HARD_STOP_NOT_TESTED'),
 'cloudflare-ai':f('FREE_POSSIBLE_ACCOUNT_REQUIRED','https://developers.cloudflare.com/workers-ai/platform/pricing/','10000 neurons/day on Workers Free; selected models require payment',over='FREE_PLAN_REQUESTS_FAIL_AT_CAP; PAID_PLAN_HAS_OVERAGE',reset='00:00 UTC daily'),
 'uncloseai':f('FREE_POSSIBLE_AUTH_REQUIRED','https://uncloseai.com/inference.html; https://www.uncloseai.com/terms-of-use.html','Publisher describes free inference; user v2 models GET returned 401; no-auth not verified'),
 'huggingface':f('BILLING_REQUIRED','https://huggingface.co/docs/inference-providers/pricing','Current Free Users monthly credits: none; PRO credits require paid PRO',commercial='MODEL_AND_PROVIDER_SPECIFIC'),
 'cerebras':f('BILLING_REQUIRED','https://www.cerebras.ai/pricing','One-time $5 promotion expires 30 days; API inactive without payment method',card='YES',over='PROMO_PAUSES_AT_EXHAUSTION_UNLESS_SEPARATE_PAYGO_PURCHASE',reset='Nonrenewable; 30 days'),
 'together':f('BILLING_REQUIRED','https://docs.together.ai/docs/billing-credits','No free trials; initial $15 minimum credit purchase; prepaid',card='UNKNOWN',over='PREPAID_PAUSE_AT_ZERO'),
 'fireworks':f('BILLING_REQUIRED','https://docs.fireworks.ai/faq-new/billing-pricing/how-does-billing-and-credit-usage-work','Prepaid billing; free grant not independently established',card='YES',over='AUTO_RELOAD_CAN_PURCHASE; DISABLED_PAUSES_AT_ZERO'),
 'nvidia':f('FREE_POSSIBLE_ACCOUNT_REQUIRED','https://docs.api.nvidia.com/nim/docs/product','Developer Program hosted NIM endpoint prototyping; numeric quota unknown',commercial='PROTOTYPING_RESEARCH_DEVELOPMENT_TESTING_ONLY_NOT_PRODUCTION'),
 'deepseek':f('BILLING_REQUIRED','https://api-docs.deepseek.com/quick_start/pricing','Token-priced inference deducted from topped-up or granted balance; recurring free not established'),
 'siliconflow':f('FREE_PLAN_UNVERIFIED','https://docs.siliconflow.com/en/userguide/rate-limits/rate-limit-and-upgradation','Free models exist; exact live zero-price model and tier must be independently verified; no unconditional model allowlist'),
 'zai':f('FREE_PLAN_UNVERIFIED','https://docs.z.ai/guides/overview/pricing; https://docs.z.ai/guides/llm/glm-4.5','Main pricing lists paid models; separate GLM-4.5-Flash page advertises free; endpoint/account/model eligibility unknown'),
 'pollinations':f('FREE_PLAN_UNVERIFIED','https://pollinations.ai/; https://pollinations.ai/terms; https://gen.pollinations.ai/docs','Quest Pollen reward differs from recurring free tier; current zero-price model/account terms require review'),
 'sambanova':f('FREE_POSSIBLE_ACCOUNT_REQUIRED','https://docs.sambanova.ai/docs/en/models/rate-limits','Free tier without linked payment method; numeric model/account limits pending',card='NO'),
 'groq':f('FREE_POSSIBLE_ACCOUNT_REQUIRED','https://console.groq.com/docs/rate-limits','gpt-oss-20b/120b example free limits; actual organization limits may differ',rpm='30 for cited models',rpd='1000 for cited models',tokens='8000 TPM; 200000 TPD for cited models'),
 'ovhcloud':f('FREE_PLAN_UNVERIFIED','UNKNOWN','Upstream claims optional-key 2 req/min/IP/model; independent provider terms not yet verified'),
 'modelscope':f('FREE_PLAN_UNVERIFIED','UNKNOWN','Upstream documents regional identity gate; verify current vendor quota/KYC before use'),
 'openference-api':f('FREE_PLAN_UNVERIFIED','https://openference.com/pricing; https://docs.openference.com/api-reference/models','Official pricing extraction incomplete; recurring free claim not independently established'),
 'openference':f('FREE_PLAN_UNVERIFIED','https://openference.com/pricing','Same underlying service as openference-api; OAuth is separate integration, not independent free budget')
}
providers=[]
for p in catalog:
 id=p['ProviderID'];text=registry.get(id,'')
 def prop(k):
  m=re.search(r'^\s*'+k+r':\s*"([^"\n]+)"',text,re.M);return m[1] if m else 'UNKNOWN'
 ep=[x['InferenceEndpoint'] for x in snapshot if x['ProviderID']==id]
 special=bool(re.search(r'^(Local|System|Upstream|OAuth|Web Cookie|Cloud Agent|Search|Audio)',p['Group'])) or bool(re.search(r'(CLI|Playground|DuckDuckGo AI Chat|Veo AI Free|ZCode)',p['ProviderName'],re.I))
 src=official(f'open-sse/config/providers/registry/{id}/index.ts') if text else ref
 models=list(dict.fromkeys(re.findall(r'\bid:\s*"([^"\n]+)"',text)))[1:]
 providers.append(dict(ProviderID=id,Alias=p['Alias'],ProviderName=p['ProviderName'],Group=p['Group'],Endpoint=ep[0] if ep else '',Source=src,Protocol=prop('format'),AuthType=prop('authType'),ToolCalling=prop('toolCalling'),Models=';'.join(models) or 'UNKNOWN_OR_SHARED_MODEL_LIST',Chat='UPSTREAM_DOCUMENTED_ROUTE' if any('chat/completions' in e for e in ep) else 'UNKNOWN',Special='YES' if special else 'NO',AccountEligibility='NOT_VERIFIED',Free=free.get(id,f())))
research=dict(Status='PARTIAL_OFFICIAL_RESEARCH_NOT_ACCOUNT_APPROVAL',SourceManifest='SOURCE-MANIFEST.json',FreeTierCoverage=f'{len(free)} provider/integration records have independently attempted primary-source review; remaining UNKNOWN; no account eligible verified',Note='Notion fetched in full; current governing and task-relevant sections reviewed; not all historical text or child pages exhaustively reviewed')
data=dict(ProjectHEAD=PH,UpstreamHEAD=UH,Providers=providers,Targets=targets,Research=research)
raw=json.dumps(data,ensure_ascii=False,separators=(',',':'))
payload=base64.b64encode(gzip.compress(raw.encode(),mtime=0)).decode()
template=(OUT/'gate-template.ps1').read_text()
template=template.replace('@@DATAHASH@@',hashlib.sha256(raw.encode()).hexdigest()).replace('@@PAYLOAD@@',payload).replace('@@CS@@',(OUT/'DirectHttps.cs').read_text())
(OUT/'Test-DJMRN-OmniRoute-Provider-Gate-v3.ps1').write_text(template,encoding='utf-8-sig')
(OUT/'SOURCE-MANIFEST.json').write_text(json.dumps(dict(ProjectHEAD=PH,UpstreamHEAD=UH,Sources=sources),ensure_ascii=False,indent=2))
(OUT/'PINNED-DATASET.json').write_text(json.dumps(data,ensure_ascii=False,indent=2))
for name,rs in [('MERGED-CANDIDATE-MATRIX.csv',providers),('ENDPOINT-PROVENANCE.csv',targets)]:
 flat=[dict(p,Free=json.dumps(p['Free'],ensure_ascii=False)) for p in rs] if name.startswith('MERGED') else rs
 with (OUT/name).open('w',encoding='utf-8-sig',newline='') as out:
  w=csv.DictWriter(out,flat[0].keys());w.writeheader();w.writerows(flat)
print(json.dumps(dict(Providers=len(providers),Targets=len(targets),UniqueVetted=len({x['URL'] for x in targets if x['Vetted']=='YES'}),UnverifiedLegacy=len([x for x in targets if x['Vetted']=='NO']),ProjectHEAD=PH,UpstreamHEAD=UH,ScriptBytes=len(template.encode()))))
