#requires -Version 5.1
<# DJMRN-OMNIROUTE-PROVIDER-GATE-V3-20261025
Offline by default. Read-only HTTPS GETs only in explicitly selected network modes.
Self-contained pinned dataset; no downloads, keys, login, inference POST or config edits.
#>
[CmdletBinding()]
param(
 [ValidateSet('AnalyzeExisting','FullNetworkAudit','RetestFailed','ExportShortlist')][string]$Mode='AnalyzeExisting',
 [string]$InputDirectory='', [string]$OutputDirectory='',
 [ValidateRange(2,30)][int]$TimeoutSeconds=6,
 [ValidateRange(0,2)][int]$RetryCount=1,
 [switch]$Resume, [switch]$SelfTest
)
$ErrorActionPreference='Stop'
$script:Version='3.0.0'
$script:Mission='DJMRN-OMNIROUTE-PROVIDER-GATE-V3-20261025'
$script:Started=[DateTime]::UtcNow.ToString('o')
$script:Warnings=New-Object 'System.Collections.Generic.List[string]'
$script:DatasetHash='@@DATAHASH@@'
$payload='@@PAYLOAD@@'
$bytes=[Convert]::FromBase64String($payload)
$mem=New-Object IO.MemoryStream(,$bytes)
$gz=New-Object IO.Compression.GZipStream($mem,[IO.Compression.CompressionMode]::Decompress)
$reader=New-Object IO.StreamReader($gz,[Text.Encoding]::UTF8)
try { $json=$reader.ReadToEnd() } finally { $reader.Dispose();$gz.Dispose();$mem.Dispose() }
$sha=[Security.Cryptography.SHA256]::Create()
try {$hash=([BitConverter]::ToString($sha.ComputeHash([Text.Encoding]::UTF8.GetBytes($json)))).Replace('-','').ToLowerInvariant()}finally{$sha.Dispose()}
if($hash -ne $script:DatasetHash){throw 'Embedded dataset integrity failure'}
$script:Data=$json|ConvertFrom-Json
$script:Providers=@($script:Data.Providers)
function Assert-Catalog($rows) {
 if(@($rows).Count -ne 375){throw 'Catalog must contain exactly 375 records'}
 $seen=@{};foreach($p in $rows){if(!$p.ProviderID -or $p.ProviderID -notmatch '^[a-zA-Z0-9_-]+$' -or $seen.ContainsKey($p.ProviderID)){throw 'Invalid or duplicate provider ID'};$seen[$p.ProviderID]=$true}
}
Assert-Catalog $script:Providers
$script:IDs=@{};foreach($p in $script:Providers){$script:IDs[$p.ProviderID]=$p}
$script:Targets=@($script:Data.Targets)
$script:Allowed=@{};foreach($t in $script:Targets){$script:Allowed[$t.URL]=$true}
function Safe-Text($value) {
 $s=[string]$value
 # Only explicit fields are imported; never export arbitrary CSV columns or errors.
 $s=$s -replace '[\x00-\x1f\x7f]',' '
 $s=$s -replace '(?i)(Bearer\s+|sk-|ghp_|hf_)[A-Za-z0-9_\-\.]{6,}','[REDACTED]'
 $s=$s -replace '(?i)[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}','[REDACTED_EMAIL]'
 if($s.Length -gt 4096){$s=$s.Substring(0,4096)}
 return $s
}
function Export-SafeCsv($rows,[string]$name,[string[]]$columns) {
 $items=@($rows)
 $file=Join-Path $script:Out $name
 if($items.Count -eq 0){ ('"'+($columns -join '","')+'"')|Set-Content -LiteralPath $file -Encoding UTF8;return }
 $safe=@(foreach($r in $items){$o=[ordered]@{};foreach($prop in $r.PSObject.Properties){$v=Safe-Text $prop.Value;if($v -match '^\s*[=+\-@]'){$v="'"+$v};$o[$prop.Name]=$v};[pscustomobject]$o})
 $safe|Export-Csv -LiteralPath $file -NoTypeInformation -Encoding UTF8
}
function Get-NetworkState([int]$code,[string]$kind,[string]$errorCode,[int]$attempts=1) {
 if($code -eq 401){return 'API_HTTP_REACHED_AUTH_PENDING'}
 if($code -eq 403){return 'API_HTTP_REACHED_POLICY_UNKNOWN'}
 if($code -eq 405){return 'API_HTTP_REACHED_METHOD_MISMATCH'}
 if($code -eq 429){return 'API_HTTP_REACHED_RATE_LIMITED'}
 if($code -eq 451){return 'API_HTTP_REACHED_REGION_RESTRICTED'}
 if($code -ge 500){return 'API_HTTP_REACHED_SERVER_ERROR'}
 if($code -eq 404 -or ($code -ge 300 -and $code -lt 400) -or $kind -eq 'API_HOST'){return 'API_PATH_UNVERIFIED'}
 if($code -ge 200){return 'API_HTTP_REACHED'}
 if($errorCode -match '^SECURITY|^NOT_TESTED|^MISSING'){return 'UNVERIFIED'}
 return 'NETWORK_NO_HTTP_TRANSIENT'
}
function Get-Reason([int]$code,[string]$errorCode) {
 switch($code) {
  200 {return 'HTTP_200_GET_ONLY_NO_INFERENCE_PROOF'}
  400 {return 'HTTP_400_REQUEST_OR_PATH_UNVERIFIED'}
  401 {return 'HTTP_401_AUTH_REQUIRED_KEEP_CANDIDATE'}
  403 {return 'HTTP_403_AUTH_POLICY_REGION_OR_WAF_UNKNOWN'}
  404 {return 'HTTP_404_PATH_OR_GET_UNSUPPORTED_KEEP_PROVIDER'}
  405 {return 'HTTP_405_GET_DISALLOWED_POST_NOT_TESTED'}
  429 {return 'HTTP_429_RATE_OR_QUOTA_LIMIT_NO_AUTORETRY'}
  451 {return 'HTTP_451_RESPONDER_LEGAL_RESTRICTION_ORIGIN_UNKNOWN'}
 }
 if($code -ge 300 -and $code -lt 400){return 'HTTP_REDIRECT_NOT_FOLLOWED'}
 if($code -ge 500){return 'HTTP_5XX_SERVER_OR_GATEWAY_ERROR'}
 if($code -ge 200){return 'HTTP_RESPONSE_GET_ONLY'}
 return $errorCode
}
function Legacy-Error($r) {
 $s=([string]$r.ReasonCode)+' '+([string]$r.ErrorDetail)
 if($s -match 'DNS|resolve|no such host'){return 'DNS_FAILURE'}
 if($s -match 'TLS|SSL|certificate|secure channel|handshake'){return 'TLS_ERROR'}
 if($s -match 'RESET|forcibly closed|aborted'){return 'CONNECTION_RESET'}
 if($s -match 'REFUSED'){return 'TCP_REFUSED'}
 if($s -match 'TIMEOUT|timed out|cancel'){return 'TIMEOUT'}
 return 'LEGACY_NO_HTTP_UNCLASSIFIED'
}
function Hash-File([string]$path){return (Get-FileHash -LiteralPath $path -Algorithm SHA256).Hash.ToLowerInvariant()}
function Read-Legacy([string]$dir) {
 $a=Join-Path $dir '01_ALL_ADDRESSES_AND_REASONS.csv';$b=Join-Path $dir '02_ALL_375_PROVIDER_DECISIONS.csv'
 foreach($f in @($a,$b)){if(!(Test-Path -LiteralPath $f -PathType Leaf)){throw 'Legacy pair missing'};if((Get-Item -LiteralPath $f).Length -gt 40MB){throw 'CSV exceeds 40 MiB limit'}}
 $pr=@(Import-Csv -LiteralPath $b -Encoding UTF8);Assert-Catalog $pr
 foreach($p in $pr){if(!$script:IDs.ContainsKey($p.ProviderID)){throw 'Legacy provider IDs differ from pinned version'}}
 $rr=@(Import-Csv -LiteralPath $a -Encoding UTF8)
 if($rr.Count -eq 0 -or $rr.Count -gt 20000){throw 'Invalid endpoint CSV size'}
 foreach($col in @('ProviderID','ProbeKind','URL','HTTP','ReasonCode')){if($col -notin $rr[0].PSObject.Properties.Name){throw ('Missing CSV column: '+$col)}}
 $stamp=(Get-Item -LiteralPath $a).LastWriteTimeUtc.ToString('o')
 # v2 contains no per-request timestamp: do NOT pretend the file time is a measurement time.
 $mapped=New-Object 'System.Collections.Generic.List[object]';$seen=@{}
 foreach($r in $rr){
  if(!$script:IDs.ContainsKey([string]$r.ProviderID)){throw 'Unknown legacy endpoint ProviderID'}
  $code=0;if(![int]::TryParse([string]$r.HTTP,[ref]$code) -or ($code -ne 0 -and ($code -lt 200 -or $code -gt 599))){throw 'Invalid HTTP value in legacy CSV'}
  $url=[string]$r.URL
  # Whitelist exact pinned provider/kind/URL triplets. Unknown addresses are not requested/exported.
  $t=@($script:Targets|Where-Object {$_.ProviderID -eq $r.ProviderID -and $_.URL -ceq $url -and $_.ProbeKind -eq $r.ProbeKind}|Select-Object -First 1)
  if($t.Count -eq 0){$script:Warnings.Add('UNMATCHED_LEGACY_ROW_OMITTED:'+ $r.ProviderID);continue}
  $key=$r.ProviderID+'|'+$r.ProbeKind+'|'+$url
  if($seen.ContainsKey($key)){throw 'Duplicate legacy endpoint row'};$seen[$key]=$true
  $err=if($code -eq 0){Legacy-Error $r}else{''}
  $mapped.Add([pscustomobject]@{ProviderID=$r.ProviderID;ProbeKind=$r.ProbeKind;URL=$url;Source=$t[0].Source;Vetted=$t[0].Vetted;HTTP=$code;ErrorCode=$err;Reason=(Get-Reason $code $err);NetworkStatus=(Get-NetworkState $code $r.ProbeKind $err);DNS='LEGACY_DIAGNOSTIC_NOT_REVALIDATED';TCP4='NOT_RUN';TCP6='NOT_RUN';TLS='NOT_RUN';ContentType=(iftext $r.ContentType);Server='NOT_RETAINED';Redirect='LEGACY_REDIRECT_NOT_REVALIDATED';RetryAfter='UNKNOWN';ResponseOrigin='UNKNOWN_ORIGIN_CDN_WAF_GATEWAY';Attempts=1;TestedAt='UNKNOWN_LEGACY_PER_REQUEST_TIME';TimeSource=('INPUT_FILE_MTIME_UTC:'+ $stamp);Evidence='USER_V2_IMPORTED';Confidence='HTTP_OBSERVATION_ONLY';Action='Verify free plan, account eligibility and intended method before approved connection'})
 }
 return [pscustomobject]@{Rows=@($mapped.ToArray());Hashes=@((Hash-File $a),(Hash-File $b));SourceFolder=(Split-Path $dir -Leaf);LegacyDecisionRows=$pr.Count}
}
function iftext($v){if([string]$v -match '^application/(json|problem\+json)$'){return [string]$v};if([string]$v -match '^text/html'){return 'text/html'};return 'UNKNOWN'}
function Read-Evidence([string]$dir) {
 $v3=Join-Path $dir '10_FULL_AUDIT_RESULTS.json'
 if(!(Test-Path -LiteralPath $v3)){return Read-Legacy $dir}
 if((Get-Item -LiteralPath $v3).Length -gt 40MB){throw 'JSON exceeds 40 MiB limit'}
 $j=Get-Content -LiteralPath $v3 -Raw -Encoding UTF8|ConvertFrom-Json
 if($j.Metadata.DatasetSHA256 -cne $script:DatasetHash){throw 'V3 input dataset mismatch'}
 Assert-Catalog @($j.Providers)
 foreach($p in $j.Providers){if(!$script:IDs.ContainsKey([string]$p.ProviderID)){throw 'V3 provider IDs differ from pinned catalog'}}
 $result=New-Object 'System.Collections.Generic.List[object]';$seen=@{}
 foreach($r in @($j.Endpoints)){
  if($r.ErrorCode -eq 'NOT_TESTED'){continue}
  $t=@($script:Targets|Where-Object {$_.ProviderID -ceq $r.ProviderID -and $_.ProbeKind -ceq $r.ProbeKind -and $_.URL -ceq $r.URL}|Select-Object -First 1)
  if($t.Count -eq 0){throw 'V3 endpoint identity mismatch'}
  $code=0;if(![int]::TryParse([string]$r.HTTP,[ref]$code) -or ($code -ne 0 -and ($code -lt 200 -or $code -gt 599))){throw 'Invalid V3 HTTP status'}
  $key=$r.ProviderID+'|'+$r.ProbeKind+'|'+$r.URL;if($seen.ContainsKey($key)){throw 'Duplicate V3 endpoint'};$seen[$key]=$true
  $err=if($code -gt 0){''}elseif([string]$r.ErrorCode -match '^[A-Z0-9_]{1,80}$'){[string]$r.ErrorCode}else{'TRANSPORT_ERROR'}
  $ts=[DateTime]::MinValue;$time=if([DateTime]::TryParse([string]$r.TestedAt,[ref]$ts)){$ts.ToUniversalTime().ToString('o')}else{'UNKNOWN_IMPORTED_TIME'}
  $evidence=if([string]$r.Evidence -match 'SYNTHETIC'){'SYNTHETIC_IMPORTED'}else{'V3_IMPORTED_NOT_RETESTED'}
  $result.Add([pscustomobject]@{ProviderID=$r.ProviderID;ProbeKind=$r.ProbeKind;URL=$t[0].URL;Source=$t[0].Source;Vetted=$t[0].Vetted;HTTP=$code;ErrorCode=$err;Reason=(Get-Reason $code $err);NetworkStatus=(Get-NetworkState $code $r.ProbeKind $err);DNS='IMPORTED_NOT_REVALIDATED';TCP4='NOT_RUN';TCP6='NOT_RUN';TLS='NOT_RUN';ContentType=(iftext $r.ContentType);Server='NOT_RETAINED';Redirect='IMPORTED_NOT_REVALIDATED';RetryAfter='UNKNOWN';ResponseOrigin='UNKNOWN_ORIGIN_CDN_WAF_GATEWAY';Attempts=1;TestedAt=$time;TimeSource='V3_IMPORTED';Evidence=$evidence;Confidence='IMPORTED_OBSERVATION_ONLY';Action='Revalidate before connection; no account or inference proven'})
 }
 return [pscustomobject]@{Rows=@($result.ToArray());Hashes=@((Hash-File $v3));SourceFolder=(Split-Path $dir -Leaf);LegacyDecisionRows=375}
}
function Locate-Legacy {
 if($InputDirectory){try{return Read-Evidence $InputDirectory}catch{$script:Warnings.Add('EXPLICIT_INPUT_INVALID: no evidence imported; inspect original schema, dataset and 375 IDs');return [pscustomobject]@{Rows=@();Hashes=@();SourceFolder='INVALID_EXPLICIT_INPUT';LegacyDecisionRows=0}}}
 $roots=New-Object 'System.Collections.Generic.List[string]'
 foreach($r in @([Environment]::GetFolderPath('Desktop'),$(if($env:USERPROFILE){Join-Path $env:USERPROFILE 'Desktop'}),$(if($env:OneDrive){Join-Path $env:OneDrive 'Desktop'}),$(if($env:OneDriveConsumer){Join-Path $env:OneDriveConsumer 'Desktop'}))){if($r -and (Test-Path -LiteralPath $r) -and !$roots.Contains($r)){$roots.Add($r)}}
 $dirs=@(foreach($r in $roots){Get-ChildItem -LiteralPath $r -Directory -Filter 'DJMRN-DEEP-375-*' -ErrorAction SilentlyContinue})
 foreach($d in @($dirs|Sort-Object LastWriteTimeUtc -Descending)){try{return Read-Legacy $d.FullName}catch{$script:Warnings.Add('INVALID_LEGACY_FOLDER_SKIPPED:'+ $d.Name)}}
 return [pscustomobject]@{Rows=@();Hashes=@();SourceFolder='NOT_FOUND';LegacyDecisionRows=0}
}
function Atomic-Json($obj,[string]$path) {
 $tmp=$path+'.tmp';$obj|ConvertTo-Json -Depth 20|Set-Content -LiteralPath $tmp -Encoding UTF8
 # Keep previous committed checkpoint so interruption during replacement is recoverable.
 if(Test-Path -LiteralPath $path){Copy-Item -LiteralPath $path -Destination ($path+'.bak') -Force}
 Move-Item -LiteralPath $tmp -Destination $path -Force
}
function Load-Checkpoint([string]$path,[string]$identity) {
 foreach($f in @($path,($path+'.bak'))){if(Test-Path -LiteralPath $f){try{$c=Get-Content -LiteralPath $f -Raw -Encoding UTF8|ConvertFrom-Json;if($c.Identity -cne $identity){throw 'Checkpoint identity mismatch'};return $c}catch{if($_.Exception.Message -match 'identity mismatch'){throw};$script:Warnings.Add('CHECKPOINT_PARSE_FAILED_TRY_BACKUP')}}}
 throw 'No valid checkpoint to resume'
}
function Save-Checkpoint {Atomic-Json ([pscustomobject]@{Identity=$script:Identity;Mode=$Mode;DatasetHash=$script:DatasetHash;Results=@($script:Cache.Values);UpdatedAt=[DateTime]::UtcNow.ToString('o')}) (Join-Path $script:Out 'checkpoint.json')}
function Load-Transport {
 if('DJMRNGateV3.DirectHttps' -as [type]){return}
 $cs=@'
@@CS@@
'@
 Add-Type -TypeDefinition $cs -Language CSharp
}
function Invoke-Target([string]$url) {
 if(!$script:Allowed.ContainsKey($url)){throw 'Endpoint absent from pinned manifest'}
 $attempt=0
 do {
  $attempt++;$r=[DJMRNGateV3.DirectHttps]::Probe($url,$TimeoutSeconds*1000);$r.Attempts=$attempt
  # Any HTTP response, TLS/policy/security failure is terminal for this bounded test.
  $transient=$r.ErrorCode -match '^(DNS_FAILURE|DNS_TIMEOUT|TCP_TIMEOUT|TIMEOUT|CONNECTION_RESET|NETWORK_UNREACHABLE|IO_ERROR)$'
  if($r.HTTP -gt 0 -or !$transient -or $attempt -gt $RetryCount){break}
  Start-Sleep -Milliseconds ([int](500*[Math]::Pow(2,$attempt-1)))
 }while($true)
 return $r
}
function Row-FromResult($t,$r) {
 $ns=Get-NetworkState ([int]$r.HTTP) $t.ProbeKind $r.ErrorCode ([int]$r.Attempts)
 [pscustomobject]@{ProviderID=$t.ProviderID;ProbeKind=$t.ProbeKind;URL=$t.URL;Source=$t.Source;Vetted=$t.Vetted;HTTP=[int]$r.HTTP;ErrorCode=$r.ErrorCode;Reason=(Get-Reason ([int]$r.HTTP) $r.ErrorCode);NetworkStatus=$ns;DNS=$r.DNS;TCP4=$r.TCP4;TCP6=$r.TCP6;TLS=$r.TLS;ContentType=$r.ContentType;Server=$r.Server;Redirect=$r.Redirect;RetryAfter=$r.RetryAfter;ResponseOrigin=$r.ResponseOrigin;Attempts=$r.Attempts;TestedAt=$r.TestedAt;TimeSource=$r.TimeSource;Evidence=$r.Evidence;AuthScheme=$r.AuthScheme;ElapsedMs=$r.ElapsedMs;Confidence='HTTP_OBSERVATION_ONLY';Action='Check endpoint-specific auth, free model, region and billing; no inference tested'}
}
function Summarize-Providers($endpointRows,[bool]$controlOK) {
 foreach($p in $script:Providers){
  $rows=@($endpointRows|Where-Object ProviderID -eq $p.ProviderID)
  $api=@($rows|Where-Object {$_.ProbeKind -in @('API_ACTUAL_ROUTE_GET','SOURCE_REGISTRY_MODELS','API_MODELS','CURATED_PUBLIC_DISCOVERY','API_HOST')})
  $path=@($api|Where-Object {$_.ProbeKind -ne 'API_HOST' -and $_.Vetted -eq 'YES'})
  $http=@($path|Where-Object HTTP -ge 200)
  $chosen=$null;$ns='UNVERIFIED';$queue='PENDING_EVIDENCE';$why='No per-path evidence; run explicit network mode only if needed';$on='FREE_PLAN_UNVERIFIED'
  if($p.Special -eq 'YES'){$ns='LOCAL_OR_SPECIAL_INTEGRATION';$queue='E';$on='NO_SUITABLE_INFERENCE_API';$why='Local, browser, cookie, OAuth, search, audio or special integration; separate workflow required'}
  elseif($http.Count -gt 0){
   # Prefer actual inference-path observation; report all conflicting paths alongside it.
   $chosen=@($http|Sort-Object @{Expression={if($_.ProbeKind -eq 'API_ACTUAL_ROUTE_GET'){0}else{1}}}, @{Expression={if($_.HTTP -in @(403,451,429)){1}else{0}}})[0]
   $ns=$chosen.NetworkStatus;$queue='B';$on='REGION_ELIGIBILITY_UNKNOWN';$why='HTTP observed; signup/auth/free-model/eligibility still required'
   if(@($path|Where-Object {$_.HTTP -in @(403,429,451) -or ($_.HTTP -ge 300 -and $_.HTTP -lt 400) -or $_.HTTP -ge 500}).Count -gt 0){$queue='C';$why='Path-level policy, redirect, rate or gateway evidence needs review; inspect all endpoint rows'}
   if($chosen.HTTP -eq 401){$on='FREE_POSSIBLE_AUTH_REQUIRED'}
   if($chosen.HTTP -eq 451){$on='REGION_ELIGIBILITY_UNKNOWN'}
  }
  elseif($path.Count -gt 0){
   $attempted=@($path|Where-Object {$_.HTTP -eq 0 -and $_.ErrorCode -notmatch '^NOT_TESTED|^SECURITY|^MISSING'})
   if($attempted.Count -gt 0){$ns='NETWORK_NO_HTTP_TRANSIENT';$why='No HTTP on attempted API path; limited RetestFailed needed'}
   $repeated=@($attempted|Where-Object {$_.Evidence -eq 'LIVE_LOCAL_MACHINE_GET' -and $_.Attempts -ge 2})
   $noUntested=@($path|Where-Object {$_.ErrorCode -eq 'NOT_TESTED' -or $_.HTTP -gt 0}).Count -eq 0
   if($Mode -eq 'RetestFailed' -and $controlOK -and $repeated.Count -eq $path.Count -and $noUntested){$ns='NETWORK_UNAVAILABLE_ON_TESTED_PATH';$queue='D';$why='Repeated no-HTTP on every documented tested API path with controls reached; temporary path-specific hold'}
   $chosen=$path[0]
  }
  elseif(@($api|Where-Object HTTP -ge 200).Count -gt 0){$ns='API_PATH_UNVERIFIED';$queue='B';$why='Only API host or unverified curated path responded; actual API route still unverified'}
  elseif(@($script:Targets|Where-Object {$_.ProviderID -eq $p.ProviderID -and $_.ProbeKind -match 'API|MODELS' -and $_.Vetted -eq 'YES'}).Count -eq 0){$ns='NO_STATIC_PUBLIC_API';$queue='E';$why='No fixed public inference path established in this pinned source; not proof none exists'}
  $free=$p.Free
  if($free.CardRequired -eq 'YES' -or $free.FreeStatus -eq 'BILLING_REQUIRED'){$on='CARD_OR_BILLING_REQUIRED'}
  if($free.Region -eq 'RESTRICTED'){$on='REGION_ACCOUNT_RESTRICTED';if($queue -ne 'E'){$queue='C'}}
  # Queue A cannot be earned from reachability or a catalog free tag.
  if($queue -eq 'B' -and $free.FreeStatus -eq 'FREE_VERIFIED_ELIGIBLE' -and $free.Region -eq 'ELIGIBLE' -and $free.CardRequired -eq 'NO' -and $free.Overage -eq 'HARD_STOP_VERIFIED' -and $p.AccountEligibility -eq 'VERIFIED' -and $http.Count -gt 0){$queue='A';$on='READY_FOR_APPROVED_CONNECTION_TEST'}
  $codes=($path|ForEach-Object {$_.ProbeKind+':'+$_.HTTP}) -join ';'
  $other=($rows|Where-Object {$_.ProbeKind -in @('WEBSITE_ORIGIN','SIGNUP_DASHBOARD','API_HOST')}|ForEach-Object {$_.ProbeKind+':'+$_.HTTP}) -join ';'
  $priority=50;$basis='Insufficient evidence; no intelligence score inferred'
  if($queue -eq 'A'){$priority=0;$basis='All independent connection gates verified; permission still required'}
  elseif($queue -eq 'B'){$priority=20;$basis='HTTP path or host observed; free/eligibility pending';if($free.FreeStatus -in @('FREE_POSSIBLE_ACCOUNT_REQUIRED','FREE_POSSIBLE_AUTH_REQUIRED')){$priority=10;$basis='HTTP plus current primary-source free-plan lead; account eligibility unknown'}}
  elseif($queue -eq 'C'){$priority=60;$basis='Resolve path policy/rate/redirect/conflict before onboarding'}
  elseif($queue -eq 'D'){$priority=70;$basis='Hold tested path until network/time changes'}
  elseif($queue -eq 'E'){$priority=90;$basis='Separate integration or missing static public API'}
  if($on -eq 'CARD_OR_BILLING_REQUIRED'){$priority=80;$basis='Current billing/card gate blocks free-first connection'}
  [pscustomobject]@{ProviderID=$p.ProviderID;Name=$p.ProviderName;Alias=$p.Alias;Group=$p.Group;Queue=$queue;ReviewPriority=$priority;PriorityBasis=$basis;NetworkStatus=$ns;OnboardingStatus=$on;Endpoint=$(if($chosen){$chosen.URL}else{$p.Endpoint});EndpointSource=$p.Source;HTTP=$(if($chosen){$chosen.HTTP}else{'UNKNOWN'});Reason=$why;PathEvidence=$codes;WebsiteHostDashboardEvidence=$other;ConnectionType=$p.AuthType;Protocol=$p.Protocol;OmniRouteCompatibility='PINNED_REGISTRY_ONLY_NOT_RUNTIME_TESTED';FreeStatus=$free.FreeStatus;Quota=$free.Quota;RPM=$free.RPM;RPD=$free.RPD;Tokens=$free.Tokens;Reset=$free.Reset;CardRequired=$free.CardRequired;Overage=$free.Overage;RegionEligibility=$free.Region;CommercialUse=$free.Commercial;FreeSource=$free.Source;FreeCheckedAt=$free.CheckedAt;Models=$p.Models;ModelFreshness='PINNED_SOURCE_NOT_LIVE';ChatCompletion=$p.Chat;Reasoning='MODEL_SPECIFIC_UNVERIFIED';Coding='MODEL_SPECIFIC_UNVERIFIED';ToolCalling=$p.ToolCalling;StructuredOutput='MODEL_SPECIFIC_UNVERIFIED';Embeddings='MODEL_SPECIFIC_UNVERIFIED';Vision='MODEL_SPECIFIC_UNVERIFIED';Audio='MODEL_SPECIFIC_UNVERIFIED';Confidence='BOUNDED_SOURCE_AND_HTTP_ONLY';NextAction=$(if($queue -eq 'D'){'Revisit after network/time changes; no countrywide filtering conclusion'}elseif($queue -eq 'E'){'Separate integration research; do not connect as direct free chat API'}else{'Verify official free plan, live model ID, account region, no-card and hard stop; obtain approval before tiny connection test'});TestedAt=$(if($chosen){$chosen.TestedAt}else{'NOT_TESTED'});InferenceVerified='NO';ActualAccountVerified='NO'}
 }
}
function Write-Reports($rows,[bool]$controlOK,[string]$runStatus) {
 $all=@(Summarize-Providers $rows $controlOK);Assert-Catalog $all
 $schema=@('ProviderID','Endpoint','Source','NetworkStatus','HTTP','Reason','Confidence','NextAction','TestedAt')
 Export-SafeCsv $all '01_ALL_375_PROVIDERS.csv' $schema
 Export-SafeCsv $rows '02_ALL_API_ENDPOINT_TESTS.csv' @('ProviderID','ProbeKind','URL','Source','HTTP','ErrorCode','Reason','NetworkStatus','Evidence','TestedAt')
 Export-SafeCsv @($all|Where-Object {$_.Queue -in @('A','B','C')}) '03_REACHABLE_API_CANDIDATES.csv' $schema
 Export-SafeCsv @($all|Where-Object Queue -eq 'B') '04_AUTH_OR_SIGNUP_PENDING.csv' $schema
 Export-SafeCsv @($all|Where-Object Queue -eq 'C') '05_POLICY_REGION_OR_WAF_REVIEW.csv' $schema
 Export-SafeCsv @($all|Where-Object Queue -eq 'D') '06_NETWORK_UNAVAILABLE.csv' $schema
 Export-SafeCsv $all '07_FREE_TIER_VERIFICATION.csv' $schema
 Export-SafeCsv @($all|Sort-Object ReviewPriority,Queue,ProviderID) '08_OMNIROUTE_CONNECTION_QUEUE.csv' $schema
 $counts=@($rows|Group-Object ProbeKind,Reason|ForEach-Object {[pscustomobject]@{ProbeKindAndReason=$_.Name;Count=$_.Count}})
 Export-SafeCsv $counts '09_DIAGNOSTIC_REASON_COUNTS.csv' @('ProbeKindAndReason','Count')
 $q=@{};foreach($k in @('A','B','C','D','E','PENDING_EVIDENCE')){$q[$k]=@($all|Where-Object Queue -eq $k).Count}
 $meta=[pscustomobject]@{Mission=$script:Mission;Version=$script:Version;Mode=$Mode;RunStatus=$runStatus;StartedAt=$script:Started;FinishedAt=[DateTime]::UtcNow.ToString('o');PowerShell=$PSVersionTable.PSVersion.ToString();CLR=[Environment]::Version.ToString();Platform=[Environment]::OSVersion.Platform.ToString();ProviderVersion='3.8.52';DatasetSHA256=$script:DatasetHash;ProjectHEAD=$script:Data.ProjectHEAD;UpstreamHEAD=$script:Data.UpstreamHEAD;TimeoutSeconds=$TimeoutSeconds;RetryCount=$RetryCount;Concurrency=1;Proxy='DISABLED_IN_PINNED_SOCKET_CLIENT';VPN='NOT_DETECTABLE_BY_USEPROXY_FALSE';CertificateValidation='DEFAULT_TRUST_HOSTNAME_CHAIN_TLS12';Redirects='NEVER_FOLLOWED';Requests='HTTPS_GET_HEADERS_ONLY';ControlsReached=$controlOK;InputSource=$script:Legacy.SourceFolder;InputSHA256=$script:Legacy.Hashes;Queues=$q;Warnings=@($script:Warnings.ToArray());WindowsPS51RealTest=$(if($PSVersionTable.PSVersion.Major -eq 5 -and $PSVersionTable.PSVersion.Minor -eq 1 -and [Environment]::OSVersion.Platform -eq 'Win32NT'){'CURRENT_RUN_ON_WINDOWS_PS51'}else{'NOT_RUN_ON_WINDOWS_PS51'})}
 Atomic-Json ([pscustomobject]@{Metadata=$meta;Providers=$all;Endpoints=@($rows);ImportedEndpointEvidence=@($script:Legacy.Rows);Controls=@($script:Controls);Research=$script:Data.Research}) (Join-Path $script:Out '10_FULL_AUDIT_RESULTS.json')
 $lines=@('DJMRN_PROVIDER_GATE_V3='+$script:Version;"MODE=$Mode; RUN_STATUS=$runStatus; PROVIDERS=375";"QUEUE_A=$($q.A); QUEUE_B=$($q.B); QUEUE_C=$($q.C); QUEUE_D=$($q.D); QUEUE_E=$($q.E); PENDING_EVIDENCE=$($q.PENDING_EVIDENCE)";"NEW_UNIQUE_URL_TESTS=$($script:Cache.Count); IMPORTED_ROWS=$($script:Legacy.Rows.Count); HTTP_ROWS=$(@($rows|Where-Object HTTP -ge 200).Count)";'INFERENCE=NOT_TESTED; FREE_ACCOUNT_ELIGIBILITY=NOT_VERIFIED; NO_KEYS_NO_POST_NO_BILLING';"WARNINGS=$($script:Warnings.Count); INPUT=$($script:Legacy.SourceFolder)";'SEND=12_COPY_SUMMARY_TO_CHAT.txt and optionally 01_ALL_375_PROVIDERS.csv + 02_ALL_API_ENDPOINT_TESTS.csv')
 $lines|Set-Content -LiteralPath (Join-Path $script:Out '12_COPY_SUMMARY_TO_CHAT.txt') -Encoding UTF8
 $fa=@('# گزارش غربال APIهای OmniRoute';'';"نسخه فهرست: 3.8.52 — تعداد دقیق: ۳۷۵ — حالت: $Mode — وضعیت اجرا: $runStatus";'';"صف A: $($q.A) | صف B: $($q.B) | صف C: $($q.C) | صف D: $($q.D) | صف E: $($q.E) | شواهد ناکافی: $($q.PENDING_EVIDENCE)";'';'A آماده آزمون کوچک با مجوز پس از تأیید مستقل حساب و هزینه؛ B پیگیری endpoint/ثبت‌نام/کلید؛ C بررسی سیاست، منطقه، WAF، redirect، سهمیه یا سرور؛ D عدم پاسخ مکرر در مسیر آزموده‌شده؛ E خارج از API مستقیم یا فاقد مسیر ثابت تأییدشده.';'';'وجود پاسخ HTTP فقط رسیدن به پاسخ‌دهنده را نشان می‌دهد؛ Origin، موفقیت inference، مجوز منطقه‌ای، رایگان بودن و پذیرش حساب اثبات نشده‌اند. پاسخ وب‌سایت، میزبان و مسیر API جدا در CSV ثبت است. ۴۰۱ و ۴۰۵ حذف نمی‌شوند؛ ۴۰۳ علت قطعی ندارد؛ ۴۰۴ به معنی قطع شبکه نیست.';'';'پیش‌فرض کاملاً آفلاین است. این ابزار حساب یا Provider را فعال نمی‌کند. هیچ مدل پولی، POST، Cookie یا Credential ارسال نمی‌شود. خطای TLS با گواهی نامعتبر دور زده نمی‌شود. بدنه پاسخ ذخیره نمی‌شود؛ علت ۴۰۳ در نبود شواهد مستقل UNKNOWN است.';'';'Proxy در کلاینت مستقیم خاموش است؛ این امر VPN در سطح TUN، واسطه شفاف ISP یا CDN را نفی نمی‌کند. آزمون TLS به TLS 1.2 محدود است؛ اختلاف سیستم‌عامل، trust store و IPv4/IPv6 می‌تواند نتیجه را تغییر دهد.';'';'ردیف‌های تاریخی v2 زمان دقیق هر درخواست را ندارند؛ زمان فایل صرفاً منشأ جانبی است. داده قبلی ادغام می‌شود و فقط FullNetworkAudit همه مقصدهای رسمی واجد شرایط را دوباره می‌آزماید. RetestFailed فقط URLهای قبلاً بدون HTTP را به‌علاوه کنترل‌های صریح بررسی می‌کند.';'';'اطلاعات طرح‌های رایگان برای تمام نامزدها کامل نشده است؛ UNKNOWN به معنی تأیید نیست. نام و مدل در registry به معنی مجوز رایگان بودن آن مدل نیست. پژوهش عمومی و داده نسخه ثابت جای بررسی حساب را نمی‌گیرد.';'';"پوشه ورودی: $($script:Legacy.SourceFolder)";"درخواست یکتای جدید/ازسرگرفته: $($script:Cache.Count)";'';'## اخطارهای داده و اجرای ناقص';(@($script:Warnings.ToArray()) -join "`n"))
 $fa|Set-Content -LiteralPath (Join-Path $script:Out '11_PERSIAN_EXECUTIVE_REPORT.md') -Encoding UTF8
 Write-Host '';Write-Host '===== COPY TO CHAT =====' -ForegroundColor Green;$lines|ForEach-Object {Write-Host $_};Write-Host '===== END =====';Write-Host ('OUTPUT: '+$script:Out)
}
function Invoke-SelfTest {
 Load-Transport
 $tests=New-Object 'System.Collections.Generic.List[object]'
 function Check([string]$name,[bool]$pass){$tests.Add([pscustomobject]@{Test=$name;Status=$(if($pass){'PASS'}else{'FAIL'})})}
 $expect=@{200='API_HTTP_REACHED';301='API_PATH_UNVERIFIED';400='API_HTTP_REACHED';401='API_HTTP_REACHED_AUTH_PENDING';403='API_HTTP_REACHED_POLICY_UNKNOWN';404='API_PATH_UNVERIFIED';405='API_HTTP_REACHED_METHOD_MISMATCH';429='API_HTTP_REACHED_RATE_LIMITED';451='API_HTTP_REACHED_REGION_RESTRICTED';500='API_HTTP_REACHED_SERVER_ERROR'}
 foreach($n in $expect.Keys){Check ('HTTP_'+$n) ((Get-NetworkState $n 'API_ACTUAL_ROUTE_GET' '') -eq $expect[$n])}
 foreach($case in @(@('NO_HTTP_DNS_ERROR','DNS_FAILURE'),@('NO_HTTP_TIMEOUT','TIMEOUT'),@('NO_HTTP_TLS_ERROR','TLS_ERROR'),@('NO_HTTP_CONNECTION_RESET','CONNECTION_RESET'),@('NO_HTTP_TCP_REFUSED','TCP_REFUSED'))){Check ('Legacy_'+$case[1]) ((Legacy-Error ([pscustomobject]@{ReasonCode=$case[0];ErrorDetail=''})) -eq $case[1])}
 Check 'Offline_network_failure' ((Get-NetworkState 0 'API_ACTUAL_ROUTE_GET' 'NETWORK_UNREACHABLE') -eq 'NETWORK_NO_HTTP_TRANSIENT')
 foreach($socketCase in @(@(11001,'DNS_FAILURE'),@(10060,'TCP_TIMEOUT'),@(10054,'CONNECTION_RESET'),@(10061,'TCP_REFUSED'),@(10051,'NETWORK_UNREACHABLE'))){$ex=New-Object Net.Sockets.SocketException -ArgumentList ([int]$socketCase[0]);Check ('DotNetException_'+$socketCase[1]) ([DJMRNGateV3.DirectHttps]::Error($ex) -eq $socketCase[1])}
 $ex=New-Object Security.Authentication.AuthenticationException -ArgumentList 'Synthetic TLS validation failure';Check 'DotNetException_TLS' ([DJMRNGateV3.DirectHttps]::Error($ex) -eq 'TLS_ERROR')
 foreach($ip in @('127.0.0.1','10.0.0.1','172.16.0.1','192.168.0.1','169.254.169.254','100.64.0.1','::1','fc00::1','fe80::1','::ffff:127.0.0.1','2001:db8::1')){Check ('Reject_IP_'+$ip) (![DJMRNGateV3.DirectHttps]::Public([Net.IPAddress]::Parse($ip)))}
 Check 'Public_IPv4' ([DJMRNGateV3.DirectHttps]::Public([Net.IPAddress]::Parse('1.1.1.1')))
 foreach($u in @('http://example.com/','https://localhost/','https://127.0.0.1/','https://a.internal/','https://a.com:8443/','https://u:p@a.com/','https://a.com/?api_key=fixture')){Check 'Reject_unsafe_URL' (![DJMRNGateV3.DirectHttps]::SafeUrl($u))}
 $root=Join-Path ([IO.Path]::GetTempPath()) ('DJMRN-GATE-SELFTEST-'+[Guid]::NewGuid().ToString('N'));New-Item -Path $root -ItemType Directory|Out-Null
 $input=Join-Path $root 'input';New-Item -Path $input -ItemType Directory|Out-Null
 $script:Providers|Select-Object ProviderID|Export-Csv -LiteralPath (Join-Path $input '02_ALL_375_PROVIDER_DECISIONS.csv') -NoTypeInformation -Encoding UTF8
 $fixture=@(foreach($t in $script:Targets){[pscustomobject]@{ProviderID=$t.ProviderID;ProbeKind=$t.ProbeKind;URL=$t.URL;HTTP=$(if($t.ProviderID -eq 'llm7'){401}elseif($t.ProviderID -eq 'groq'){0}else{200});ReasonCode=$(if($t.ProviderID -eq 'groq'){'NO_HTTP_TIMEOUT'}else{'HTTP_FIXTURE'});ErrorDetail='';ContentType='application/json'}})
 $fixture|Export-Csv -LiteralPath (Join-Path $input '01_ALL_ADDRESSES_AND_REASONS.csv') -NoTypeInformation -Encoding UTF8
 $legacyTest=Read-Legacy $input;Check 'ImportCsv_fixture_all_rows' ($legacyTest.Rows.Count -eq $fixture.Count)
 $bad=@($script:Providers);$bad[1]=$bad[0];$caught=$false;try{Assert-Catalog $bad}catch{$caught=$true};Check 'Duplicate_ID_rejected' $caught
 $map=@(Summarize-Providers $legacyTest.Rows $false);Check '375_preserved_including_no_endpoint' ($map.Count -eq 375)
 Check '401_not_removed' (@($map|Where-Object {$_.ProviderID -eq 'llm7' -and $_.Queue -eq 'B'}).Count -eq 1)
 Check 'No_false_QueueA' (@($map|Where-Object Queue -eq 'A').Count -eq 0)
 $savedOut=$script:Out;$script:Out=$root
 Export-SafeCsv @([pscustomobject]@{ProviderID='fixture';Value='=1+1'}) 'csv-test.csv' @('ProviderID','Value')
 $csv=Import-Csv -LiteralPath (Join-Path $root 'csv-test.csv') -Encoding UTF8;Check 'CSV_injection_escaped' ($csv.Value -eq "'=1+1")
 Export-SafeCsv @() 'empty.csv' @('ProviderID','HTTP');Check 'Empty_CSV_header' ((Get-Content (Join-Path $root 'empty.csv')) -eq '"ProviderID","HTTP"')
 $cp=Join-Path $root 'checkpoint-test.json';Atomic-Json ([pscustomobject]@{Identity='fixture';Results=@([pscustomobject]@{URL='https://api.llm7.io/v1/models';HTTP=401})}) $cp
 $c=Load-Checkpoint $cp 'fixture';Check 'Resume_checkpoint_recovery' ($c.Results[0].HTTP -eq 401)
 Atomic-Json ([pscustomobject]@{Identity='fixture';Results=@()}) $cp
 'CORRUPT'|Set-Content -LiteralPath $cp; $c=Load-Checkpoint $cp 'fixture';Check 'Resume_backup_after_truncation' ($c.Results[0].HTTP -eq 401)
 $caught=$false;try{Load-Checkpoint ($cp+'.bak') 'wrong'|Out-Null}catch{$caught=$true};Check 'Resume_identity_mismatch_denied' $caught
 Check 'Credential_text_redacted' ((Safe-Text 'Bearer abcdefghijklmnop') -eq '[REDACTED]')
 $script:Out=$savedOut
 $result=[pscustomobject]@{Environment=$PSVersionTable.PSVersion.ToString();NetworkRequests=0;Tests=@($tests.ToArray());Failed=@($tests|Where-Object Status -eq 'FAIL').Count;WindowsPS51=$(if($PSVersionTable.PSVersion.Major -eq 5 -and $PSVersionTable.PSVersion.Minor -eq 1 -and [Environment]::OSVersion.Platform -eq 'Win32NT'){'SELFTEST_RUN_ON_WINDOWS_PS51'}else{'NOT_RUN_ON_WINDOWS_PS51'});RealDNS_TCP_TLS_Reset_Offline='NOT_RUN_SIMULATED_MAPPING_ONLY';CheckpointInterruptedProcess='NOT_RUN_STORAGE_RECOVERY_ONLY';FixtureDirectory=$root}
 Atomic-Json $result (Join-Path $script:Out 'SELFTEST-RESULTS.json');$tests|Format-Table -AutoSize|Out-Host
 if($result.Failed -gt 0){throw ('SelfTest FAIL: '+$result.Failed)};Write-Host ('SELFTEST PASS; '+$tests.Count+' assertions; network requests=0') -ForegroundColor Green
}
if(!$OutputDirectory){$desktop=[Environment]::GetFolderPath('Desktop');if(!$desktop){$desktop=(Get-Location).Path};$OutputDirectory=Join-Path $desktop ('DJMRN-PROVIDER-GATE-V3-'+(Get-Date -Format 'yyyyMMdd-HHmmss-fff'))}
$script:Out=[IO.Path]::GetFullPath($OutputDirectory)
if((Test-Path -LiteralPath $script:Out) -and !$Resume -and @(Get-ChildItem -LiteralPath $script:Out -Force).Count -gt 0){throw 'Output directory not empty; use a new directory or -Resume'}
New-Item -Path $script:Out -ItemType Directory -Force|Out-Null
if($SelfTest){Invoke-SelfTest;return}
$script:Legacy=Locate-Legacy
if($script:Legacy.Rows.Count -eq 0){$script:Warnings.Add('NO_VALID_V2_PAIR_FOUND: specify -InputDirectory; offline mode will report evidence gaps, never silently scan')}
$script:Cache=@{};$script:Controls=@();$controlOK=$false
$script:Identity=$script:Version+'|'+$script:DatasetHash+'|'+$Mode+'|'+$TimeoutSeconds+'|'+$RetryCount+'|'+($script:Legacy.Hashes -join ',')
if($Resume){$c=Load-Checkpoint (Join-Path $script:Out 'checkpoint.json') $script:Identity;foreach($r in @($c.Results)){if(!$script:Allowed.ContainsKey([string]$r.URL)){throw 'Unsafe checkpoint URL'};if($script:Cache.ContainsKey($r.URL)){throw 'Duplicate checkpoint URL'};$script:Cache[$r.URL]=$r}}
$old=@{};foreach($r in $script:Legacy.Rows){$old[$r.ProviderID+'|'+$r.ProbeKind+'|'+$r.URL]=$r}
$testUrls=@()
if($Mode -eq 'FullNetworkAudit'){$testUrls=@($script:Targets|Where-Object Vetted -eq 'YES'|Select-Object -ExpandProperty URL -Unique)}
if($Mode -eq 'RetestFailed'){
 if($script:Legacy.Rows.Count -eq 0){throw 'RetestFailed needs valid local v2 CSVs; use -InputDirectory or FullNetworkAudit explicitly'}
 $failed=@($script:Legacy.Rows|Where-Object {$_.HTTP -eq 0 -and $_.Vetted -eq 'YES'}|Select-Object -ExpandProperty URL -Unique)
 $testUrls=@($failed)
 # Controls from independently official source URLs, not arbitrary inferred health routes.
 $script:ControlUrls=@('https://api.llm7.io/v1/models','https://openrouter.ai/api/v1/models','https://hermes.ai.unturf.com/v1/models')
 if($failed.Count -gt 0){$testUrls=@($script:ControlUrls+$failed|Select-Object -Unique)}
}
$status='COMPLETE';$endpointRows=@()
try {
 if($testUrls.Count -gt 0){
  Load-Transport;$i=0;$blockedHosts=@{}
  foreach($done in $script:Cache.Values){if([int]$done.HTTP -eq 429){$blockedHosts[([Uri]$done.URL).DnsSafeHost]=$true}}
  foreach($url in $testUrls){
   $i++;Write-Progress -Activity 'DJMRN bounded HTTPS GET audit' -Status ($i.ToString()+'/'+$testUrls.Count) -PercentComplete (100*$i/$testUrls.Count)
   if($script:Cache.ContainsKey($url)){continue}
   try{$hostKey=([Uri]$url).DnsSafeHost}catch{$script:Warnings.Add('INVALID_ENDPOINT_SKIPPED');continue}
   if($blockedHosts.ContainsKey($hostKey)){$script:Warnings.Add('HOST_429_SKIP_UNTESTED_PATH:'+ $hostKey);continue}
   try{$r=Invoke-Target $url}catch{
    if($_.Exception.GetBaseException() -is [OperationCanceledException]){throw}
    $r=[pscustomobject]@{HTTP=0;ErrorCode='TRANSPORT_RUNTIME_ERROR';DNS='UNKNOWN';TCP4='NOT_RUN';TCP6='NOT_RUN';TLS='NOT_RUN';ContentType='';Server='';AuthScheme='';Redirect='';RetryAfter='';ResponseOrigin='UNKNOWN';ElapsedMs=0;Attempts=1;TestedAt=[DateTime]::UtcNow.ToString('o');TimeSource='LIVE_UTC';Evidence='LIVE_LOCAL_MACHINE_GET'}
   }
   $record=[pscustomobject]@{URL=$url;HTTP=$r.HTTP;ErrorCode=$r.ErrorCode;DNS=$r.DNS;TCP4=$r.TCP4;TCP6=$r.TCP6;TLS=$r.TLS;ContentType=$r.ContentType;Server=$r.Server;AuthScheme=$r.AuthScheme;Redirect=$r.Redirect;RetryAfter=$r.RetryAfter;ResponseOrigin=$r.ResponseOrigin;ElapsedMs=$r.ElapsedMs;Attempts=$r.Attempts;TestedAt=$r.TestedAt;TimeSource=$r.TimeSource;Evidence=$r.Evidence}
   $script:Cache[$url]=$record
   if($r.HTTP -eq 429){$blockedHosts[$hostKey]=$true} # stop this host for run; no wait/retry consumption
   Save-Checkpoint
   if($i%10 -eq 0){Write-Host ('PROGRESS '+$i+'/'+$testUrls.Count)}
   Start-Sleep -Milliseconds 150
  }
  Write-Progress -Activity 'DJMRN bounded HTTPS GET audit' -Completed
 }
}catch{$status='PARTIAL';$script:Warnings.Add('RUN_INTERRUPTED_OR_FAILED: completed endpoint checkpoints retained; use -Resume');Write-Verbose ($_.Exception.ToString()+' '+$_.ScriptStackTrace)}
finally {
 foreach($t in $script:Targets){
  $key=$t.ProviderID+'|'+$t.ProbeKind+'|'+$t.URL
  if($script:Cache.ContainsKey($t.URL)){$endpointRows+=Row-FromResult $t $script:Cache[$t.URL]}
  elseif($old.ContainsKey($key)){$endpointRows+=$old[$key]}
  else {$endpointRows+=[pscustomobject]@{ProviderID=$t.ProviderID;ProbeKind=$t.ProbeKind;URL=$t.URL;Source=$t.Source;Vetted=$t.Vetted;HTTP=0;ErrorCode='NOT_TESTED';Reason='NOT_TESTED';NetworkStatus='UNVERIFIED';DNS='NOT_RUN';TCP4='NOT_RUN';TCP6='NOT_RUN';TLS='NOT_RUN';ContentType='';Server='';Redirect='';RetryAfter='';ResponseOrigin='UNKNOWN';Attempts=0;TestedAt='NOT_TESTED';TimeSource='NONE';Evidence='NONE';Confidence='UNVERIFIED';Action='Preserve unknown; do not infer filtering or eligibility'}}
 }
 if($Mode -eq 'RetestFailed'){
  $script:Controls=@(foreach($url in $script:ControlUrls){if($script:Cache.ContainsKey($url)){$script:Cache[$url]}})
  $controlOK=@($script:Controls|Where-Object HTTP -ge 200).Count -ge 2
  if(!$controlOK){$script:Warnings.Add('CONTROL_COMPARISON_INCONCLUSIVE: do not label network-unavailable; internet/controls may be impaired')}
 }
 if($script:Warnings.Count -gt 0 -and $status -eq 'COMPLETE'){$status='COMPLETE_WITH_GAPS'}
 Save-Checkpoint
 Write-Reports $endpointRows $controlOK $status
}
