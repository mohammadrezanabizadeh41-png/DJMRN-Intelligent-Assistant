# DJMRN | Offline-safe provider census shell launcher, v3.8.52 | PowerShell 5.1
# No user credentials; no model calls; 375 source provider IDs; 51 API probe candidates.
# HTTPS GET headers only. Network reachability is not free-tier eligibility.
[CmdletBinding()]
param([int]$TimeoutSeconds=8,[int]$BatchSize=16)
$ErrorActionPreference='Stop'
if($BatchSize -lt 1 -or $BatchSize -gt 24){throw 'BatchSize must be 1..24'}
$dir=Join-Path ([Environment]::GetFolderPath('Desktop')) ('DJMRN-375-RESULT-' + (Get-Date -Format 'yyyyMMdd-HHmmss'))
New-Item -ItemType Directory -Path $dir -Force | Out-Null
$catalogUrl='https://raw.githubusercontent.com/mohammadrezanabizadeh41-png/DJMRN-Intelligent-Assistant/main/06-tests-and-evidence/tools/omniroute-iran-direct-check/OmniRoute_v3.8.52_375_providers.csv'
$csvFile=Join-Path $PSScriptRoot 'OmniRoute_v3.8.52_375_providers.csv'
if(-not(Test-Path -LiteralPath $csvFile)){
    Invoke-WebRequest -Uri $catalogUrl -OutFile $csvFile -TimeoutSec 20 -UseBasicParsing
}
$catalog=@(Import-Csv -LiteralPath $csvFile -Encoding UTF8)
if($catalog.Count -ne 375){throw ('Catalog mismatch; expected 375, got ' + $catalog.Count)}
$api=@{
'openai'='https://api.openai.com/v1/models'
'anthropic'='https://api.anthropic.com/v1/models'
'gemini'='https://generativelanguage.googleapis.com/v1beta/models'
'groq'='https://api.groq.com/openai/v1/models'
'openrouter'='https://openrouter.ai/api/v1/models'
'ovhcloud'='https://oai.endpoints.kepler.ai.cloud.ovh.net/v1/models'
'cloudflare-ai'='https://api.cloudflare.com/client/v4/'
'deepseek'='https://api.deepseek.com/models'
'mistral'='https://api.mistral.ai/v1/models'
'cohere'='https://api.cohere.com/v1/models'
'nvidia'='https://integrate.api.nvidia.com/v1/models'
'cerebras'='https://api.cerebras.ai/v1/models'
'fireworks'='https://api.fireworks.ai/inference/v1/models'
'together'='https://api.together.xyz/v1/models'
'huggingface'='https://router.huggingface.co/v1/models'
'sambanova'='https://api.sambanova.ai/v1/models'
'siliconflow'='https://api.siliconflow.cn/v1/models'
'zai'='https://api.z.ai/api/paas/v4/models'
'glm'='https://open.bigmodel.cn/api/paas/v4/models'
'bigmodel'='https://open.bigmodel.cn/api/paas/v4/models'
'qwen-cloud'='https://dashscope.aliyuncs.com/compatible-mode/v1/models'
'alibaba'='https://dashscope.aliyuncs.com/compatible-mode/v1/models'
'kimi'='https://api.moonshot.ai/v1/models'
'moonshot'='https://api.moonshot.ai/v1/models'
'minimax'='https://api.minimax.io/v1/models'
'minimax-cn'='https://api.minimaxi.com/v1/models'
'xai'='https://api.x.ai/v1/models'
'chutes'='https://llm.chutes.ai/v1/models'
'nebius'='https://api.studio.nebius.com/v1/models'
'hyperbolic'='https://api.hyperbolic.xyz/v1/models'
'novita'='https://api.novita.ai/v3/openai/models'
'llm7'='https://api.llm7.io/v1/models'
'requesty'='https://router.requesty.ai/v1/models'
'venice'='https://api.venice.ai/api/v1/models'
'deepinfra'='https://api.deepinfra.com/v1/openai/models'
'aimlapi'='https://api.aimlapi.com/v1/models'
'perplexity'='https://api.perplexity.ai/'
'modelscope'='https://api-inference.modelscope.cn/v1/models'
'openference-api'='https://api.openference.com/v1/models'
'reka'='https://api.reka.ai/v1/models'
'ollama-cloud'='https://ollama.com/api/tags'
'jina-ai'='https://api.jina.ai/v1/embeddings'
'jina-reader'='https://r.jina.ai/'
'pollinations'='https://gen.pollinations.ai/'
'clova-studio'='https://clovastudio.stream.ntruss.com/'
'stability-ai'='https://api.stability.ai/v2beta/'
'fal-ai'='https://fal.run/'
'baseten'='https://api.baseten.co/'
'liquid'='https://api.liquid.ai/'
'elevenlabs'='https://api.elevenlabs.io/v1/models'
'assemblyai'='https://api.assemblyai.com/v2/'
}
$targets=New-Object 'System.Collections.Generic.List[object]'
foreach($p in $catalog){
    if($p.Group -notmatch '^Local|^System|^Upstream' -and $p.WebsiteURL -match '^https://'){
        try {
            $u=[uri]$p.WebsiteURL
            if($u.Host -notmatch '^(localhost|127\.|10\.|192\.168\.|172\.(1[6-9]|2[0-9]|3[01])\.|.*\.local$)'){
                $targets.Add([pscustomobject]@{Id=$p.ProviderID;Kind='WEBSITE';Url=($u.GetLeftPart([UriPartial]::Authority) + '/')})
            }
        }catch{}
    }
    if($api.ContainsKey($p.ProviderID)){$targets.Add([pscustomobject]@{Id=$p.ProviderID;Kind='API';Url=$api[$p.ProviderID]})}
}
$unique=@($targets | Group-Object Url | ForEach-Object { $_.Name })
Write-Host ('DJMRN: 375 providers; HTTPS destinations=' + $unique.Count + '; GET only; NO VPN/proxy or API keys') -ForegroundColor Cyan
Add-Type -AssemblyName System.Net.Http
$handler=New-Object System.Net.Http.HttpClientHandler
$handler.UseProxy=$false
$handler.UseCookies=$false
$handler.AllowAutoRedirect=$false
$http=New-Object -TypeName System.Net.Http.HttpClient -ArgumentList $handler
$http.Timeout=[timespan]::FromSeconds($TimeoutSeconds)
$http.DefaultRequestHeaders.UserAgent.ParseAdd('DJMRN-Reachability/1.0')
$cache=@{}
try{
for($i=0;$i -lt $unique.Count;$i+=$BatchSize){
    $last=[math]::Min($unique.Count-1,$i+$BatchSize-1)
    $tasks=@()
    foreach($url in $unique[$i..$last]){
        try{$task=$http.GetAsync($url,[System.Net.Http.HttpCompletionOption]::ResponseHeadersRead)
            $tasks+= [pscustomobject]@{Url=$url;Task=$task}
        }catch{$cache[$url]='ERROR'}
    }
    foreach($t in $tasks){
        try{$response=$t.Task.GetAwaiter().GetResult();$cache[$t.Url]=[string]([int]$response.StatusCode);$response.Dispose()}
        catch{
            $m=$_.Exception.GetBaseException().Message
            $cache[$t.Url]=if($m -match 'timed out|timeout|cancelled|canceled'){'TIMEOUT'}
            elseif($m -match 'reset|closed|forcibly'){'RESET'}
            elseif($m -match 'SSL|TLS|certificate'){'TLS'}
            elseif($m -match 'resolve|name|DNS'){'DNS'}
            else{'NO_HTTP'}
        }
    }
    Write-Host ('Checked ' + [math]::Min($i+$BatchSize,$unique.Count) + ' / ' + $unique.Count)
}
}finally{$http.Dispose();$handler.Dispose()}
$results=New-Object 'System.Collections.Generic.List[object]'
foreach($p in $catalog){
    $pt=@($targets|Where-Object Id -eq $p.ProviderID)
    if($pt.Count -eq 0){$results.Add([pscustomobject]@{Id=$p.ProviderID;Kind='SKIP';Http='';Url='';State='LOCAL_OR_NO_HTTPS'})}
    else{foreach($t in $pt){
        $code=[string]$cache[$t.Url]
        $state=if($code -match '^\d{3}$'){'HTTP_RESPONSE'}else{'NO_HTTP'}
        $results.Add([pscustomobject]@{Id=$p.ProviderID;Kind=$t.Kind;Http=$code;Url=$t.Url;State=$state})
    }}
}
$full=Join-Path $dir 'DJMRN_ALL_375_provider_test_results.csv'
$results|Export-Csv -LiteralPath $full -NoTypeInformation -Encoding UTF8
$apiResults=@($results|Where-Object Kind -eq 'API')
$apiUp=@($apiResults|Where-Object State -eq 'HTTP_RESPONSE')
$apiDown=@($apiResults|Where-Object State -ne 'HTTP_RESPONSE')
$webUp=@($results|Where-Object { $_.Kind -eq 'WEBSITE' -and $_.State -eq 'HTTP_RESPONSE' })
$summary=@(
    ('DJMRN_375_SCAN=' + (Get-Date -Format yyyy-MM-dd))
    ('PROVIDERS=' + $catalog.Count + '; UNIQUE_HTTPS=' + $unique.Count + '; WEBSITES_HTTP=' + $webUp.Count + '; API_HTTP=' + $apiUp.Count + '/' + $apiResults.Count)
    ('API_HTTP_RESPONDED=' + (($apiUp|ForEach-Object { $_.Id + '(' + $_.Http + ')' }) -join ', '))
    ('API_NO_HTTP=' + (($apiDown|ForEach-Object { $_.Id + '(' + $_.Http + ')' }) -join ', '))
)
$summaryPath=Join-Path $dir 'DJMRN_COPY_THIS_RESULT.txt'
$summary|Set-Content -LiteralPath $summaryPath -Encoding UTF8
Write-Host '';Write-Host '========== COPY THE NEXT FOUR LINES INTO CHAT ==========' -ForegroundColor Green
$summary|ForEach-Object{Write-Host $_}
Write-Host '============= END OF RESULTS =============' -ForegroundColor Green
Write-Host ('Full CSV saved: '+$full)
Write-Host 'Network status only: no proof of API usability, free pricing or region eligibility.' -ForegroundColor Yellow
