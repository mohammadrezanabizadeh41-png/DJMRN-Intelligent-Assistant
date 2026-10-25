#requires -Version 5.1
<#
DJMRN v2 / 2026-10-25 / OmniRoute release v3.8.52.
One complete, non-invasive direct-ISP census; NOT proof of usable or free inference.
All probes use GET and NO credentials / model calls / installations / Windows settings.
Data: canonical 375 providers, 280 documented API routes, 54 discovery additions.
Outputs detailed per-address, per-provider, diagnosis, next-step and shareable summary.
#>
[CmdletBinding()]
param([int]$TimeoutSeconds=8,[int]$Parallel=12,[switch]$SkipWebsite)
$ErrorActionPreference="Stop"
$ProgressPreference="SilentlyContinue"
if($TimeoutSeconds -lt 3 -or $TimeoutSeconds -gt 30){throw "TimeoutSeconds must be 3..30"}
if($Parallel -lt 1 -or $Parallel -gt 24){throw "Parallel must be 1..24"}
$P=$PSScriptRoot
$catalog=Join-Path $P "OmniRoute_v3.8.52_375_providers.csv"
$reg=Join-Path $P "OmniRoute_v3.8.52_upstream_api_snapshot.csv"
$extras=Join-Path $P "OmniRoute_v3.8.52_api_discovery_additions.csv"
foreach($f in @($catalog,$reg,$extras)){if(!(Test-Path -LiteralPath $f)){throw "Missing official pinned input: $f"}}
$providers=@(Import-Csv -LiteralPath $catalog -Encoding UTF8)
$registered=@(Import-Csv -LiteralPath $reg -Encoding UTF8)
$discovery=@(Import-Csv -LiteralPath $extras -Encoding UTF8)
if($providers.Count -ne 375){throw "Not full 375: $($providers.Count)"}
if((@($providers.ProviderID|Select-Object -Unique)).Count -ne 375){throw "Duplicate provider IDs: abort"}
if($registered.Count -lt 280 -or $discovery.Count -lt 54){throw "Incomplete API input files; refusing incomplete scan"}
$ids=@{};foreach($p0 in $providers){$ids[$p0.ProviderID]=$true}
foreach($r0 in $registered){if(!$ids.ContainsKey($r0.ProviderID)){throw "Unknown registry ID: $($r0.ProviderID)"}}
foreach($r0 in $discovery){if(!$ids.ContainsKey($r0.ProviderID)){throw "Unknown discovered ID: $($r0.ProviderID)"}}
$desktop=[Environment]::GetFolderPath("Desktop")
if(!$desktop){$desktop=$env:USERPROFILE}
$out=Join-Path $desktop ("DJMRN-DEEP-375-"+(Get-Date -Format "yyyyMMdd-HHmmss"))
New-Item -Path $out -ItemType Directory -Force | Out-Null
Copy-Item -LiteralPath $catalog,$reg,$extras -Destination $out -Force
$raw=New-Object "System.Collections.Generic.List[object]"
function Add-Target([string]$id,[string]$kind,[string]$url,[string]$origin){
  if(!$url -or $url -notmatch '^https://'){return}
  try{$uri=[Uri]$url}catch{return}
  if($uri.Scheme -ne 'https' -or !$uri.Host){return}
  if($uri.Host -match '(^localhost$|\.localhost$|\.local$|^127\.|^0\.0\.0\.0$|^10\.|^192\.168\.|^169\.254\.|^172\.(1[6-9]|2[0-9]|3[01])\.)'){return}
  $raw.Add([pscustomobject]@{ProviderID=$id;ProbeKind=$kind;Url=$url;Host=$uri.Host;Source=$origin})
}
foreach($p0 in $providers){
  if(!$SkipWebsite -and $p0.WebsiteURL -match '^https://'){
    try{$u=[Uri]$p0.WebsiteURL;Add-Target $p0.ProviderID 'WEBSITE_ORIGIN' ($u.GetLeftPart([UriPartial]::Authority)+'/') 'Official_provider_reference'}catch{}
  }
}
foreach($x in $registered){
  Add-Target $x.ProviderID 'API_HOST' $x.HostOrigin 'Official_registry_snapshot'
  Add-Target $x.ProviderID 'API_ACTUAL_ROUTE_GET' $x.InferenceEndpoint 'Official_registry_snapshot_GET_not_POST'
}
foreach($x in $discovery){Add-Target $x.ProviderID $x.ProbeKind $x.ProbeURL $x.Origin}
$rawRows=@($raw.ToArray())
$uniqueUrls=@($rawRows | Select-Object -ExpandProperty Url -Unique)
if($uniqueUrls.Count -lt 250){throw "Unexpectedly few probes: $($uniqueUrls.Count)"}
Write-Host ("DJMRN DEEP: "+$providers.Count+" IDs; "+$registered.Count+" real API mappings; "+$discovery.Count+" discovery URLs; "+$uniqueUrls.Count+" distinct HTTPS GETs.") -ForegroundColor Cyan
Write-Host "Direct connection (proxy bypass), GET only, no secrets, no logins, no payments, no model inference." -ForegroundColor Cyan
Add-Type -AssemblyName System.Net.Http
$handler=New-Object System.Net.Http.HttpClientHandler
$handler.UseProxy=$false
$handler.UseCookies=$false
$handler.AllowAutoRedirect=$false
$http=New-Object -TypeName System.Net.Http.HttpClient -ArgumentList $handler
$http.Timeout=[TimeSpan]::FromSeconds($TimeoutSeconds)
$http.DefaultRequestHeaders.UserAgent.ParseAdd("DJMRN-Provider-Audit/2.0")
$net=@{}
try {
  for($i=0;$i -lt $uniqueUrls.Count;$i+=$Parallel){
    $last=[Math]::Min($uniqueUrls.Count-1,$i+$Parallel-1)
    $todo=New-Object "System.Collections.Generic.List[object]"
    foreach($url in $uniqueUrls[$i..$last]){
      $sw=[Diagnostics.Stopwatch]::StartNew()
      try{
        $t=$http.GetAsync($url,[System.Net.Http.HttpCompletionOption]::ResponseHeadersRead)
        $todo.Add([pscustomobject]@{Url=$url;Task=$t;Clock=$sw})
      }catch{
        $sw.Stop()
        $net[$url]=[pscustomobject]@{HttpCode=0;Error=$_.Exception.GetBaseException().Message;Ms=$sw.ElapsedMilliseconds;ContentType='';Server='';RedirectHost='';AuthHint=''}
      }
    }
    foreach($request in $todo){
      $code=0;$err='';$ctype='';$server='';$redir='';$auth=''
      try{
        $resp=$request.Task.GetAwaiter().GetResult()
        $code=[int]$resp.StatusCode
        if($resp.Content -and $resp.Content.Headers.ContentType){$ctype=[string]$resp.Content.Headers.ContentType.MediaType}
        if($resp.Headers.Server){$server=[string]$resp.Headers.Server}
        if($resp.Headers.WwwAuthenticate){$auth=(@($resp.Headers.WwwAuthenticate | ForEach-Object {$_.Scheme}) -join ',')}
        if($resp.Headers.Location){
          $l=$resp.Headers.Location
          if($l.IsAbsoluteUri){$redir=$l.GetLeftPart([UriPartial]::Authority)}
          else{$redir='RELATIVE_REDIRECT'}
        }
        $resp.Dispose()
      }catch{$err=$_.Exception.GetBaseException().Message}
      $request.Clock.Stop()
      $net[$request.Url]=[pscustomobject]@{HttpCode=$code;Error=$err;Ms=$request.Clock.ElapsedMilliseconds;ContentType=$ctype;Server=$server;RedirectHost=$redir;AuthHint=$auth}
    }
    Write-Host ("PROGRESS "+([Math]::Min($i+$Parallel,$uniqueUrls.Count))+"/"+$uniqueUrls.Count)
  }
}finally{$http.Dispose();$handler.Dispose()}
function Classify([int]$status,[string]$err,[string]$kind,[string]$ctype){
 if($status -eq 200){if($kind -like 'API*' -and $ctype -match 'text/html'){return 'HTTP_200_HTML_NOT_API_PROOF'};return 'HTTP_200_ONLY_NO_INFERENCE_PROOF'}
 if($status -ge 200 -and $status -le 299){return 'HTTP_2XX_RESPONDED'}
 if($status -ge 300 -and $status -le 399){return 'HTTP_REDIRECT_NOT_ENDPOINT_PASS'}
 if($status -eq 400){return 'HTTP_400_INVALID_REQUEST_OR_ROUTE'}
 if($status -eq 401){return 'HTTP_401_AUTH_REQUIRED'}
 if($status -eq 403){return 'HTTP_403_DENIED_CAUSE_UNKNOWN'}
 if($status -eq 404){return 'HTTP_404_GET_PATH_MISSING_OR_UNSUPPORTED'}
 if($status -eq 405){return 'HTTP_405_GET_NOT_ALLOWED_EXPECTED_ON_POST_ROUTE'}
 if($status -eq 408){return 'HTTP_408_SERVER_TIMEOUT'}
 if($status -eq 429){return 'HTTP_429_THROTTLED'}
 if($status -eq 451){return 'HTTP_451_EXPLICIT_LEGAL_RESTRICTION'}
 if($status -ge 400 -and $status -lt 500){return 'HTTP_OTHER_CLIENT_ERROR'}
 if($status -ge 500){return 'HTTP_5XX_UPSTREAM_SERVER_FAILURE'}
 if($err -match '(timed out|timeout|cancell?ed)'){return 'NO_HTTP_TIMEOUT'}
 if($err -match '(reset|forcibly closed|existing connection was forcibly|connection was closed|connection aborted)'){return 'NO_HTTP_CONNECTION_RESET'}
 if($err -match '(certificate|SSL|TLS|secure channel|handshake|authentication failed)'){return 'NO_HTTP_TLS_ERROR'}
 if($err -match '(resolve|name or service|no such host|DNS|remote name could not be resolved)'){return 'NO_HTTP_DNS_ERROR'}
 if($err -match '(refused|actively refused)'){return 'NO_HTTP_TCP_REFUSED'}
 return 'NO_HTTP_UNCLASSIFIED_INSPECT_DIAGNOSTIC'
}
# Extra per-host DNS/TCP diagnosis on failed HTTP only, never touch private/loopback target IPs.
$failedHosts=@($rawRows|Where-Object {$net[$_.Url].HttpCode -eq 0}|Select-Object -ExpandProperty Host -Unique)
$dns=@{};$tcp=@{}
foreach($h in $failedHosts){
 $dns[$h]='UNKNOWN';$tcp[$h]='NOT_TESTED';$ips=@()
 try{
   $task=[Net.Dns]::GetHostAddressesAsync($h)
   if($task.Wait(3500)){
      $ips=@($task.Result|ForEach-Object {$_.ToString()})
      $dns[$h]=if($ips.Count -gt 0){'RESOLVED:'+(($ips|Select-Object -First 4)-join ',')}else{'DNS_EMPTY'}
   }else{$dns[$h]='DNS_TIMEOUT'}
 }catch{$dns[$h]='DNS_ERROR:'+$_.Exception.GetBaseException().Message}
 if($ips.Count -eq 0){continue}
 $publicIPs=@($ips|Where-Object {$_ -notmatch '^(127\.|10\.|192\.168\.|169\.254\.|172\.(1[6-9]|2[0-9]|3[01])\.|::1$|fe80:)'})
 if($publicIPs.Count -eq 0){$tcp[$h]='DNS_ONLY_PRIVATE_IPS_SKIP';continue}
 $socket=New-Object Net.Sockets.TcpClient
 try{
   $ar=$socket.BeginConnect(([Net.IPAddress]::Parse($publicIPs[0])),443,$null,$null)
   if($ar.AsyncWaitHandle.WaitOne(2500)){$socket.EndConnect($ar);$tcp[$h]='TCP443_CONNECTED_HTTP_OR_TLS_FAILED'}
   else{$tcp[$h]='TCP443_TIMEOUT'}
 }catch{$tcp[$h]='TCP443_ERROR:'+$_.Exception.GetBaseException().Message}
 finally{$socket.Close()}
}
$endpointRows=New-Object 'System.Collections.Generic.List[object]'
foreach($r in $rawRows){
 $z=$net[$r.Url];if($null -eq $z){throw "missing network result $($r.Url)"}
 $why=Classify $z.HttpCode $z.Error $r.ProbeKind $z.ContentType
 $hostDns=if($z.HttpCode -eq 0){$dns[$r.Host]}else{'HTTP_RESPONDED_DNS_TCP_TLS_IMPLIED'}
 $hostTcp=if($z.HttpCode -eq 0){$tcp[$r.Host]}else{'HTTP_RESPONDED_TCP_TLS_IMPLIED'}
 $endpointRows.Add([pscustomobject]@{
  ProviderID=$r.ProviderID;ProbeKind=$r.ProbeKind;URL=$r.Url;Host=$r.Host
  HTTP=$z.HttpCode;ReasonCode=$why;ErrorDetail=($z.Error -replace '[\r\n]',' ')
  DNS=$hostDns;TCP443=$hostTcp;ContentType=$z.ContentType;Server=$z.Server
  RedirectHost=$z.RedirectHost;AuthScheme=$z.AuthHint;ElapsedMs=$z.Ms;Source=$r.Source
 })
}
$all=@($endpointRows.ToArray())
$all|Export-Csv -Path (Join-Path $out '01_ALL_ADDRESSES_AND_REASONS.csv') -NoTypeInformation -Encoding UTF8
$all|ConvertTo-Json -Depth 4|Set-Content -Path (Join-Path $out '01_ALL_ADDRESSES_AND_REASONS.json') -Encoding UTF8
$summaryRows=New-Object 'System.Collections.Generic.List[object]'
foreach($p0 in $providers){
 $items=@($all|Where-Object ProviderID -eq $p0.ProviderID)
 function Summ([string]$k){
   $x=@($items|Where-Object ProbeKind -eq $k)
   if($x.Count -eq 0){return 'NOT_DOCUMENTED_OR_NOT_APPLICABLE'}
   return (($x|ForEach-Object { $_.HTTP.ToString()+':'+$_.ReasonCode }) -join ';')
 }
 $apiRows=@($items|Where-Object {$_.ProbeKind -like 'API*' -or $_.ProbeKind -match 'DISCOVERY' -or $_.ProbeKind -eq 'SOURCE_REGISTRY_MODELS'})
 $ok=@($apiRows|Where-Object {$_.HTTP -ge 200})
 $known=@($items|Where-Object {$_.ProbeKind -eq 'API_ACTUAL_ROUTE_GET'})
 $status='NO_FIXED_PUBLIC_API_IN_SNAPSHOT'
 if($known.Count -gt 0){$status='API_DEFINED_NO_HTTP'}
 if($known.Count -gt 0 -and @($known|Where-Object {$_.HTTP -ge 200}).Count -gt 0){$status='API_ROUTE_RESPONDS_GET_ONLY_AUTH_OR_METHOD_PENDING'}
 if($ok.Count -gt 0){$status='API_HTTP_NETWORK_RESPONSE_NOT_INFERENCE'}
 if($ok.Count -eq 0 -and $apiRows.Count -gt 0){$status='API_NO_HTTP_NETWORK_FAIL'}
 if($p0.Group -match '^(Local|System|Upstream)'){ $status='LOCAL_SYSTEM_OR_ACCOUNT_DEPENDENT_SKIP_INTERNET_GATE' }
 $summaryRows.Add([pscustomobject]@{
   ProviderID=$p0.ProviderID;Name=$p0.ProviderName;Category=$p0.Group;Tags=$p0.Tags;Website=$p0.WebsiteURL
   WebsiteResult=(Summ 'WEBSITE_ORIGIN');ApiHostResult=(Summ 'API_HOST')
   ActualApiRouteResult=(Summ 'API_ACTUAL_ROUTE_GET')
   DiscoveryResult=(Summ 'CURATED_PUBLIC_DISCOVERY')
   PublicModelsResult=(Summ 'SOURCE_REGISTRY_MODELS');RegistrationDashboard=(Summ 'SIGNUP_DASHBOARD')
   ProviderAssessment=$status;ApiTargets=$apiRows.Count
   RespondingApiTargets=$ok.Count
   FreePlanVerified='NO';IranAccountEligibilityVerified='NO';ActualInferenceVerified='NO'
 })
}
$providersOut=@($summaryRows.ToArray())
$providersOut|Export-Csv -Path (Join-Path $out '02_ALL_375_PROVIDER_DECISIONS.csv') -NoTypeInformation -Encoding UTF8
$all|Group-Object ProbeKind,ReasonCode|Sort-Object Count -Descending|Select-Object Count,Name|Export-Csv -Path (Join-Path $out '03_REASON_COUNTS.csv') -NoTypeInformation -Encoding UTF8
$all|Where-Object {$_.ProbeKind -ne 'WEBSITE_ORIGIN' -and $_.HTTP -ge 200}|Export-Csv -Path (Join-Path $out '04_API_HTTP_RESPONDED_NOT_YET_USABLE.csv') -NoTypeInformation -Encoding UTF8
$all|Where-Object {$_.HTTP -eq 0 -or $_.HTTP -eq 451 -or $_.HTTP -eq 403}|Export-Csv -Path (Join-Path $out '05_FAILURE_OR_RESTRICTION_DETAILS.csv') -NoTypeInformation -Encoding UTF8
$all|Where-Object {$_.ProbeKind -eq 'SIGNUP_DASHBOARD'}|Export-Csv -Path (Join-Path $out '06_REGISTRATION_DASHBOARDS.csv') -NoTypeInformation -Encoding UTF8
$apiHosts=@($all|Where-Object ProbeKind -eq 'API_HOST')
$apiUp=@($apiHosts|Where-Object HTTP -ge 200)
$apiBad=@($apiHosts|Where-Object HTTP -eq 0)
$apiRoute=@($all|Where-Object ProbeKind -eq 'API_ACTUAL_ROUTE_GET')
$apiRouteUp=@($apiRoute|Where-Object HTTP -ge 200)
$web=@($all|Where-Object ProbeKind -eq 'WEBSITE_ORIGIN')
$webUp=@($web|Where-Object HTTP -ge 200)
$unclose=@($all|Where-Object {$_.ProviderID -eq 'uncloseai' -and $_.ProbeKind -eq 'SOURCE_REGISTRY_MODELS'})
$llm7=@($all|Where-Object {$_.ProviderID -eq 'llm7' -and $_.ProbeKind -eq 'SIGNUP_DASHBOARD'})
$plan=@(
 '# DJMRN: connection roadmap based on network scan'
 ''
 'This report proves only direct unproxied HTTPS reachability. It NEVER proves a free account, Iran eligibility, inference, model use or billing safety.'
 ''
 '1. Examine 04_API_HTTP_RESPONDED_NOT_YET_USABLE.csv; require actual inference endpoint evidence, not website 200.'
 '2. Prioritize built-in No-auth providers with responding API route and legitimate anonymous terms, e.g. UncloseAI if its /v1/models endpoint responds.'
 '3. Next choose official Free-plan API-key vendors whose API hosts and registration dashboards respond on this actual ISP. Verify no payment card/renewal/paid fallback.'
 '4. Confirm user-eligibility in Iran, model IDs and zero-price quotas on actual account BEFORE first tiny completion.'
 '5. Add to OmniRoute only explicitly confirmed free model allowlist; route weak/medium/strong tasks; quota caps per DJMRN assistant, 429 failover among confirmed free routes only.'
 '6. Any HTTP 200/401/403/405/429 without a real completion remains PROBE_ONLY, never CONNECTED or FREE_VERIFIED.'
 ''
 ('375 provider catalog records; '+$registered.Count+' documented HTTPS inference routes; '+$discovery.Count+' discovery extra URLs.')
 ('API host HTTP responded: '+$apiUp.Count+'/'+$apiHosts.Count)
 ('Actual inference GET route HTTP responded (NO POST): '+$apiRouteUp.Count+'/'+$apiRoute.Count)
 ('Web origins responded: '+$webUp.Count+'/'+$web.Count)
 ('UncloseAI public models: '+(($unclose|ForEach-Object {$_.HTTP.ToString()+' '+$_.ReasonCode}) -join ';'))
 ('LLM7 dashboard: '+(($llm7|ForEach-Object {$_.HTTP.ToString()+' '+$_.ReasonCode}) -join ';'))
)
$plan|Set-Content -Path (Join-Path $out '07_NEXT_CONNECTION_ROADMAP.md') -Encoding UTF8
$lineTop=@($apiUp|Where-Object {$_.ProviderID -match 'uncloseai|llm7|openrouter|huggingface|cloudflare-ai|pollinations|zai|siliconflow|deepseek|gemini|groq|modelsco|chutes|openference-api'}|ForEach-Object {$_.ProviderID+'='+$_.HTTP})
$lines=@(
 "DJMRN_DEEP_SCAN_DATE=$(Get-Date -Format yyyy-MM-dd)"
 "CATALOG_PROVIDERS=$($providers.Count); DOCUMENTED_API_ROUTES=$($registered.Count); EXTRA_TARGETS=$($discovery.Count); UNIQUE_HTTPS=$($uniqueUrls.Count)"
 "WEB_HTTP=$($webUp.Count)/$($web.Count); API_HOST_HTTP=$($apiUp.Count)/$($apiHosts.Count); API_ROUTE_GET_HTTP=$($apiRouteUp.Count)/$($apiRoute.Count)"
 "API_HOST_NO_HTTP=$($apiBad.Count); HTTP_403=$(@($all|Where-Object HTTP -eq 403).Count); HTTP_451=$(@($all|Where-Object HTTP -eq 451).Count)"
 "IMPORTANT_API_HTTP=$($lineTop -join ',')"
 "UNCLOSEAI_MODELS=$(@($unclose|ForEach-Object {$_.HTTP.ToString()+':'+$_.ReasonCode}) -join ','); LLM7_DASHBOARD=$(@($llm7|ForEach-Object {$_.HTTP.ToString()+':'+$_.ReasonCode}) -join ',')"
 "DATA_FOLDER=$out"
 "NEXT_SEND=02_ALL_375_PROVIDER_DECISIONS.csv + 01_ALL_ADDRESSES_AND_REASONS.csv (if full map and reasons needed)"
)
$lines|Set-Content -Path (Join-Path $out '00_COPY_SUMMARY_TO_CHAT.txt') -Encoding UTF8
Write-Host ''
Write-Host '===== COPY THESE LINES TO CHAT =====' -ForegroundColor Green
$lines|ForEach-Object {Write-Host $_}
Write-Host '===== END =====' -ForegroundColor Green
Write-Host "Full evidence folder: $out" -ForegroundColor Cyan
