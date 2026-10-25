# Synthetic transport ONLY; never opens network sockets. Run this harness in a fresh
# process so its fake DJMRNGateV3 type cannot affect a later real audit process.
#requires -Version 5.1
[CmdletBinding()]
param([Parameter(Mandatory=$true)][string]$OutputDirectory,[string]$InputDirectory='',
 [ValidateSet('FullNetworkAudit','RetestFailed','AnalyzeExisting','ExportShortlist')][string]$Mode='FullNetworkAudit',
 [int]$StopAfter=0,[switch]$Resume,[switch]$NoDelay)
$ErrorActionPreference='Stop'
$mock=@'
using System;
namespace DJMRNGateV3 {
 public class Result {
 public int HTTP,Attempts; public string URL,ErrorCode="",DNS="SIMULATED_PUBLIC",TCP4="SIMULATED",TCP6="NOT_RUN",TLS="SIMULATED";
 public string ContentType="application/json",Server="MOCK",AuthScheme="",Redirect="",RetryAfter="",ResponseOrigin="MOCK_ONLY",TestedAt="2026-10-25T00:00:00Z",TimeSource="SYNTHETIC",Evidence="SYNTHETIC_TRANSPORT";
 public long ElapsedMs=1;
 }
 public static class DirectHttps {
 public static int Count=0,StopAfter=0;
 public static Result Probe(string url,int timeout) {
  Count++; if(StopAfter>0 && Count>StopAfter)throw new OperationCanceledException("SYNTHETIC_INTERRUPTION");
  Result r=new Result(); r.URL=url;
  Uri u=new Uri(url);
  if(u.Host.Contains("llm7"))r.HTTP=401;
  else if(u.Host.Contains("groq")){r.HTTP=0;r.ErrorCode="TIMEOUT";}
  else if(u.Host.Contains("openrouter"))r.HTTP=200;
  else if(u.Host.Contains("siliconflow"))r.HTTP=429;
  else if(u.Host.Contains("deepseek"))r.HTTP=403;
  else if(u.Host.Contains("unturf"))r.HTTP=200;
  else if(u.Host.Contains("jina"))r.HTTP=451;
  else if(u.AbsolutePath.Contains("chat/completions"))r.HTTP=405;
  else r.HTTP=200;
  return r;
 }
}
}
'@
Add-Type -TypeDefinition $mock -Language CSharp
[DJMRNGateV3.DirectHttps]::StopAfter=$StopAfter
if($NoDelay){function Start-Sleep {param($Milliseconds,$Seconds)}}
$arguments=@{Mode=$Mode;OutputDirectory=$OutputDirectory;RetryCount=1;TimeoutSeconds=2}
if($InputDirectory){$arguments.InputDirectory=$InputDirectory};if($Resume){$arguments.Resume=$true}
& (Join-Path $PSScriptRoot 'Test-DJMRN-OmniRoute-Provider-Gate-v3.ps1') @arguments
Write-Host ('SYNTHETIC_TRANSPORT_CALLS='+[DJMRNGateV3.DirectHttps]::Count)
