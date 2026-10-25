// In-process, pinned-public-IP HTTPS GET client. C# 5 / .NET Framework 4.5 APIs.
// No proxy, cookies, credentials, redirects, certificate override or response bodies.
using System;
using System.IO;
using System.Text;
using System.Net;
using System.Net.Sockets;
using System.Net.Security;
using System.Security.Authentication;
using System.Diagnostics;
using System.Collections.Generic;
namespace DJMRNGateV3 {
 public sealed class Result {
  public int HTTP; public string ErrorCode=""; public string DNS="NOT_RUN";
  public string TCP4="NOT_RUN", TCP6="NOT_RUN", TLS="NOT_RUN";
  public string ContentType="", Server="", AuthScheme="", Redirect="";
  public string RetryAfter="", ResponseOrigin="UNKNOWN_ORIGIN_CDN_WAF_GATEWAY";
  public long ElapsedMs; public int Attempts; public string TestedAt="";
  public string TimeSource="LIVE_UTC", Evidence="LIVE_LOCAL_MACHINE_GET";
 }
 public static class DirectHttps {
  // The client never consults system proxy settings; no HTTP CONNECT is used.
  public static readonly bool UseProxy = false;
  public static bool Public(IPAddress ip) {
   if(ip.IsIPv4MappedToIPv6) return Public(ip.MapToIPv4());
   byte[] b=ip.GetAddressBytes();
   if(b.Length==4) {
    if(b[0]==0 || b[0]==10 || b[0]==127 || b[0]>=224) return false;
    if(b[0]==100 && b[1]>=64 && b[1]<=127) return false;
    if(b[0]==169 && b[1]==254 || b[0]==172 && b[1]>=16 && b[1]<=31) return false;
    if(b[0]==192 && (b[1]==168 || b[1]==0 || b[1]==2)) return false;
    if(b[0]==198 && (b[1]==18 || b[1]==19 || b[1]==51 && b[2]==100)) return false;
    if(b[0]==203 && b[1]==0 && b[2]==113) return false;
    return true;
   }
   // Allow only global unicast 2000::/3; reject transition/documentation ranges.
   if((b[0]&0xe0)!=0x20) return false;
   if(b[0]==0x20 && b[1]==0x02) return false;
   if(b[0]==0x20 && b[1]==0x01 && (b[2]==0 && b[3]==0 || b[2]==0x0d && b[3]==0xb8 || b[2]==0 && b[3]==2)) return false;
   return true;
  }
  public static bool SafeUrl(string s) {
   Uri u; if(!Uri.TryCreate(s,UriKind.Absolute,out u)) return false;
   if(u.Scheme!="https" || u.Port!=443 || u.UserInfo!="" || u.Fragment!="") return false;
   if(u.HostNameType!=UriHostNameType.Dns || !u.Host.Contains(".")) return false;
   string h=u.DnsSafeHost.ToLowerInvariant();
   foreach(string x in new string[]{".localhost",".local",".internal",".lan",".home",".test",".invalid",".example"}) if(h.EndsWith(x)) return false;
   if(h=="localhost" || h.EndsWith(".onion")) return false;
   string q=u.Query.ToLowerInvariant();
   foreach(string x in new string[]{"key=","token=","secret=","password=","auth=","signature=","credential="}) if(q.Contains(x)) return false;
   return true;
  }
  public static string Error(Exception e) {
   if(e is AggregateException) e=((AggregateException)e).GetBaseException();
   for(Exception t=e;t!=null;t=t.InnerException) {
    SocketException s=t as SocketException;
    if(s!=null) {
     switch(s.SocketErrorCode) {
      case SocketError.HostNotFound: case SocketError.NoData: case SocketError.TryAgain: return "DNS_FAILURE";
      case SocketError.ConnectionReset: case SocketError.ConnectionAborted: return "CONNECTION_RESET";
      case SocketError.ConnectionRefused: return "TCP_REFUSED";
      case SocketError.TimedOut: return "TCP_TIMEOUT";
      case SocketError.NetworkDown: case SocketError.NetworkUnreachable: case SocketError.HostUnreachable: return "NETWORK_UNREACHABLE";
     }
    }
    if(t is AuthenticationException) return "TLS_ERROR";
    if(t is TimeoutException) return "TIMEOUT";
   }
   if(e is IOException) return "IO_ERROR";
   return "TRANSPORT_ERROR";
  }
  static string Clip(string v) { v=v.Replace("\r","").Replace("\n",""); return v.Length>160?v.Substring(0,160):v; }
  public static Result Probe(string url,int timeoutMs) {
   Result r=new Result(); r.TestedAt=DateTime.UtcNow.ToString("o"); r.Attempts=1;
   Stopwatch all=Stopwatch.StartNew();
   try {
    if(!SafeUrl(url)) {r.ErrorCode="SECURITY_URL_REJECTED";return r;}
    Uri u=new Uri(url); IPAddress[] ips;
    try {
     var task=Dns.GetHostAddressesAsync(u.DnsSafeHost);
     if(!task.Wait(timeoutMs)) {r.DNS="DNS_TIMEOUT";r.ErrorCode="DNS_TIMEOUT";return r;}
     ips=task.Result;
    } catch(Exception e) {r.DNS="DNS_FAILURE";r.ErrorCode=Error(e);return r;}
    if(ips.Length==0){r.DNS="DNS_EMPTY";r.ErrorCode="DNS_FAILURE";return r;}
    // Reject mixed public/private answers too; connection uses these exact addresses.
    foreach(IPAddress ip in ips) if(!Public(ip)){r.DNS="NONPUBLIC_ANSWER_REJECTED";r.ErrorCode="SECURITY_DNS_REJECTED";return r;}
    bool v4=false,v6=false; List<IPAddress> selected=new List<IPAddress>();
    foreach(IPAddress ip in ips) {
     if(ip.AddressFamily==AddressFamily.InterNetwork && !v4){selected.Add(ip);v4=true;}
     if(ip.AddressFamily==AddressFamily.InterNetworkV6 && !v6){selected.Add(ip);v6=true;}
    }
    r.DNS="PUBLIC_ONLY_V4_"+v4+"_V6_"+v6;
    // TCP observations are separate from authenticated HTTPS; at most one IP/family.
    foreach(IPAddress ip in selected) {
     bool is4=ip.AddressFamily==AddressFamily.InterNetwork;
     using(TcpClient c=new TcpClient(ip.AddressFamily)) {
      try {
       IAsyncResult a=c.BeginConnect(ip,443,null,null);
       bool ok; using(a.AsyncWaitHandle) {ok=a.AsyncWaitHandle.WaitOne(timeoutMs);}
       if(!ok) {if(is4)r.TCP4="TIMEOUT";else r.TCP6="TIMEOUT";r.ErrorCode="TCP_TIMEOUT";continue;}
       c.EndConnect(a); if(is4)r.TCP4="CONNECTED";else r.TCP6="CONNECTED";
       c.ReceiveTimeout=timeoutMs;c.SendTimeout=timeoutMs;
       // Default SslStream validation checks the requested hostname and trusted chain.
       using(SslStream ssl=new SslStream(c.GetStream(),false)) {
        var auth=ssl.BeginAuthenticateAsClient(u.DnsSafeHost,null,SslProtocols.Tls12,true,null,null);
        bool authOK; using(auth.AsyncWaitHandle){authOK=auth.AsyncWaitHandle.WaitOne(timeoutMs);}
        if(!authOK){r.TLS="TLS_TIMEOUT";r.ErrorCode="TLS_TIMEOUT";continue;}
        ssl.EndAuthenticateAsClient(auth);r.TLS="VALIDATED_TLS12";
        ssl.ReadTimeout=timeoutMs;ssl.WriteTimeout=timeoutMs;
        byte[] request=Encoding.ASCII.GetBytes("GET "+u.PathAndQuery+" HTTP/1.1\r\nHost: "+u.IdnHost+"\r\nUser-Agent: DJMRN-Provider-Gate/3.0\r\nAccept: application/json, */*\r\nAccept-Encoding: identity\r\nConnection: close\r\n\r\n");
        ssl.Write(request,0,request.Length);
        List<byte> header=new List<byte>(); int state=0; Stopwatch read=Stopwatch.StartNew();
        while(header.Count<16384) {
         if(read.ElapsedMilliseconds>=timeoutMs)throw new TimeoutException();
         ssl.ReadTimeout=Math.Max(1,timeoutMs-(int)read.ElapsedMilliseconds);
         int b=ssl.ReadByte();if(b<0)throw new IOException("EOF before HTTP headers");header.Add((byte)b);
         if((state==0 || state==2) && b==13) state++; else if((state==1 || state==3) && b==10) state++;else state=0;
         if(state==4)break;
        }
        if(state!=4){r.ErrorCode="HTTP_HEADER_LIMIT";continue;}
        string[] lines=Encoding.ASCII.GetString(header.ToArray()).Split(new string[]{"\r\n"},StringSplitOptions.None);
        string[] first=lines[0].Split(' ');int code;
        if(first.Length<2 || !first[0].StartsWith("HTTP/1.") || !Int32.TryParse(first[1],out code) || code<200 || code>599){r.ErrorCode="HTTP_PROTOCOL_UNVERIFIED";continue;}
        r.HTTP=code;r.ErrorCode="";
        foreach(string line in lines) {
         int colon=line.IndexOf(':');if(colon<1)continue;
         string key=line.Substring(0,colon).ToLowerInvariant(), value=line.Substring(colon+1).Trim();
         if(key=="content-type")r.ContentType=Clip(value.Split(';')[0]);
         // Keep only a product hint; arbitrary server strings and bodies are not retained.
         if(key=="server")r.Server=value.ToLowerInvariant().Contains("cloudflare")?"CLOUDFLARE_EDGE_HINT":value.ToLowerInvariant().Contains("nginx")?"NGINX_HINT":"OTHER_SERVER_HINT";
         if(key=="www-authenticate") {string scheme=value.Split(' ')[0];if(scheme=="Bearer" || scheme=="Basic")r.AuthScheme=scheme;else r.AuthScheme="OTHER_SCHEME";}
         if(key=="location") {Uri dest; if(Uri.TryCreate(u,value,out dest) && SafeUrl(dest.AbsoluteUri))r.Redirect=(dest.Host==u.Host?"SAME_HOST_NOT_FOLLOWED:":"CROSS_HOST_NOT_FOLLOWED:")+dest.GetLeftPart(UriPartial.Authority);else r.Redirect="UNSAFE_OR_LOGIN_REDIRECT_NOT_FOLLOWED";}
         if(key=="retry-after") {int seconds; DateTime date;if(Int32.TryParse(value,out seconds) && seconds>=0)r.RetryAfter=seconds.ToString();else if(DateTime.TryParse(value,out date))r.RetryAfter=date.ToUniversalTime().ToString("o");else r.RetryAfter="PRESENT_UNPARSED";}
        }
        // Never consume body: no raw public JSON is necessary for this conservative gate.
        return r;
       }
      }catch(Exception e){r.ErrorCode=Error(e);if(r.TLS=="NOT_RUN" && r.ErrorCode=="TLS_ERROR")r.TLS="TLS_VALIDATION_OR_HANDSHAKE_FAILED";if(is4 && r.TCP4=="NOT_RUN")r.TCP4=r.ErrorCode;if(!is4 && r.TCP6=="NOT_RUN")r.TCP6=r.ErrorCode;}
     }
    }
   }catch(Exception e){r.ErrorCode=Error(e);}
   finally {r.ElapsedMs=all.ElapsedMilliseconds;}
   return r;
  }
 }
}
