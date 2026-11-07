"""BTC 4H multi-indicator HMA-forward research v1; NO orders/network/LLMs.

Twelve event-generating rule families; HMA parameter grids; rolling 12H/1D
confirmation; horizon-based targets; conservative first-hit simulation.
Historical price/volume only. Uses source-verified v0 dataset loader.
"""
import argparse
import collections
import datetime as dt
import json
import math
import statistics
from pathlib import Path
from run import load_data, ema, wilder_rsi

BARS_PER_DAY = 6
H30 = 180
H60 = 360
H90 = 540
NAN = float("nan")
COST_PER_SIDE = 0.0015


def wma(values, window):
    out = [NAN]*len(values)
    d = window*(window+1)/2
    for i in range(window-1, len(values)):
        window_values = values[i-window+1:i+1]
        if all(math.isfinite(z) for z in window_values):
            out[i] = sum((j+1)*z for j,z in enumerate(window_values))/d
    return out


def hma(values, window):
    half = wma(values, max(1, window//2))
    whole = wma(values, window)
    raw = [2*a-b if math.isfinite(a) and math.isfinite(b) else NAN
           for a,b in zip(half, whole)]
    return wma(raw, max(1, math.isqrt(window)))


def atr(rows, period=14):
    close = [r[4] for r in rows]
    tr = [r[2]-r[3] for r in rows]
    for i in range(1,len(rows)):
        tr[i] = max(rows[i][2]-rows[i][3],
                    abs(rows[i][2]-close[i-1]),
                    abs(rows[i][3]-close[i-1]))
    out = [NAN]*len(rows)
    avg = sum(tr[:period])/period
    out[period-1] = avg
    for i in range(period,len(rows)):
        avg=(avg*(period-1)+tr[i])/period
        out[i]=avg
    return out


def keltner_ema_cross(rows, period, mult):
    close=[r[4] for r in rows]
    center=ema(close,period)
    volatility=atr(rows,period)
    events=[]
    for i in range(period+1,len(rows)):
        upper=center[i]+mult*volatility[i]
        previous=center[i-1]+mult*volatility[i-1]
        if close[i]>upper and close[i-1]<=previous:
            events.append(i)
    return events


def supertrend_flip(rows, period, mult):
    volatility=atr(rows,period)
    up=down=NAN
    direction=1
    events=[]
    for i in range(period,len(rows)):
        center=(rows[i][2]+rows[i][3])/2
        upper=center+mult*volatility[i]
        lower=center-mult*volatility[i]
        prev_close=rows[i-1][4]
        up = upper if not math.isfinite(up) or upper<up or prev_close>up else up
        down = lower if not math.isfinite(down) or lower>down or prev_close<down else down
        previous=direction
        if direction<0 and rows[i][4]>up:
            direction=1
        elif direction>0 and rows[i][4]<down:
            direction=-1
        if direction==1 and previous==-1:events.append(i)
    return events


def build_events(rows, model, p, cache):
    close=cache["close"]
    high=cache["high"]
    low=cache["low"]
    volumes=cache["volume"]
    n=len(rows)
    hits=[]
    def take(i, condition):
        if condition: hits.append(i)
    if model in ("hma_turn","hma_price_cross","hma_dual","hma_pullback"):
        fast=p.get("n",p.get("fast",16))
        h=cache["hma"].setdefault(fast, hma(close,fast))
        if model=="hma_turn":
            for i in range(fast+math.isqrt(fast)+2,n):
                take(i,h[i]>h[i-1] and h[i-1]<=h[i-2] and close[i]>h[i])
        elif model=="hma_price_cross":
            for i in range(fast+math.isqrt(fast)+2,n):
                take(i,close[i]>h[i] and close[i-1]<=h[i-1] and h[i]>h[i-1])
        elif model=="hma_dual":
            slow=p["slow"]
            other=cache["hma"].setdefault(slow,hma(close,slow))
            for i in range(slow+math.isqrt(slow)+2,n):
                take(i,h[i]>other[i] and h[i-1]<=other[i-1] and h[i]>h[i-1])
        else:
            for i in range(fast+math.isqrt(fast)+4,n):
                take(i,close[i]>h[i] and close[i-1]<=h[i-1]
                     and min(close[i-4:i])<h[i-2] and h[i]>h[i-1])
    elif model=="rsi_reclaim":
        r=cache["rsi"]
        level=p["level"]
        for i in range(16,n):
            take(i,math.isfinite(r[i-1]) and r[i-1]<=level and r[i]>level)
    elif model=="rsi_oversold_rebound":
        r=cache["rsi"]
        level=p["level"]
        for i in range(17,n):
            take(i,min(r[i-6:i])<=level and r[i]>level+5 and r[i-1]<=level+5)
    elif model=="macd_positive_cross":
        m=cache["macd"]
        sig=cache["macd_signal"]
        for i in range(40,n):
            take(i,m[i]>sig[i] and m[i-1]<=sig[i-1] and
                 (m[i]>0 if p["zero_filter"] else True))
    elif model=="donchian_break":
        lookback=p["period"]
        for i in range(lookback+2,n):
            take(i,close[i]>max(high[i-lookback:i]) and
                 close[i-1]<=max(high[i-lookback-1:i-1]))
    elif model=="bollinger_reclaim":
        period=p["period"]
        k=p["sigma"]
        for i in range(period+1,n):
            old=close[i-period:i]
            current=close[i-period+1:i+1]
            oldlower=statistics.fmean(old)-k*statistics.pstdev(old)
            newlower=statistics.fmean(current)-k*statistics.pstdev(current)
            take(i,close[i-1]<oldlower and close[i]>newlower)
    elif model=="volume_hma":
        h=cache["hma"].setdefault(p["n"],hma(close,p["n"]))
        period=p["vol_period"]
        volmean=cache["volma"].setdefault(period, simple_average(volumes,period))
        for i in range(max(p["n"]+8,period+1),n):
            take(i,volumes[i]>=p["mult"]*volmean[i-1] and
                 close[i]>h[i] and h[i]>h[i-1] and
                 close[i]>close[i-1])
    elif model=="supertrend_flip":
        hits=supertrend_flip(rows,p["period"],p["mult"])
    elif model=="keltner_break":
        hits=keltner_ema_cross(rows,p["period"],p["mult"])
    else:
        raise ValueError("Undefined model "+model)
    return hits


def simple_average(arr,n):
    out=[NAN]*len(arr)
    s=0.
    for i,x in enumerate(arr):
        s+=x
        if i>=n:s-=arr[i-n]
        if i>=n-1:out[i]=s/n
    return out


def get_cache(rows):
    close=[r[4] for r in rows]
    fast=ema(close,12);slow=ema(close,26)
    macd=[x-y for x,y in zip(fast,slow)]
    return {"close":close,"high":[r[2] for r in rows],
            "low":[r[3] for r in rows],
            "volume":[r[5] for r in rows],
            "hma":{},"volma":{},
            "rsi":wilder_rsi(close,14),
            "macd":macd,"macd_signal":ema(macd,9)}


def candidates():
    return {
      "hma_turn":[{"n":x} for x in (9,16,21,34,55,89)],
      "hma_price_cross":[{"n":x} for x in (9,16,21,34,55)],
      "hma_dual":[{"fast":f,"slow":s} for f,s in ((9,21),(9,34),(16,34),(16,55),(21,55))],
      "hma_pullback":[{"n":x} for x in (16,21,34,55)],
      "rsi_reclaim":[{"level":x} for x in (40,45,50,55)],
      "rsi_oversold_rebound":[{"level":x} for x in (25,30,35)],
      "macd_positive_cross":[{"zero_filter":False},{"zero_filter":True}],
      "donchian_break":[{"period":x} for x in (12,20,30,55)],
      "bollinger_reclaim":[{"period":p,"sigma":s} for p,s in ((20,2),(30,2),(20,1.5))],
      "volume_hma":[{"n":n,"vol_period":20,"mult":1.5} for n in (9,16,21,34)],
      "supertrend_flip":[{"period":p,"mult":m} for p,m in ((10,2.0),(10,3.0),(14,3.0))],
      "keltner_break":[{"period":p,"mult":m} for p,m in ((14,1.5),(20,1.5),(20,2.0))]
    }


def unique_events(events, begin, end, min_separation=6):
    # suppress redundant alerts from same technique for 24 hours
    out=[]
    previous=-99999
    for i in events:
        if i<begin or i>=end:continue
        if i-previous<min_separation:continue
        out.append(i);previous=i
    return out


def evaluate_horizon(rows, events, begin, end, horizon, goal, stop=0.10):
    """Conservative: stop gets priority if stop and target in same 4H bar."""
    results=[]
    for i in events:
        if i+1+horizon>end:continue
        entry=rows[i+1][1]*(1+COST_PER_SIDE)
        hi_target=entry*(1+goal)
        low_stop=entry*(1-stop)
        first="none"
        max_hi=entry
        for j in range(i+1,i+1+horizon):
            max_hi=max(max_hi,rows[j][2])
            if rows[j][3]<=low_stop:
                first="stop";break
            if rows[j][2]>=hi_target:
                first="target";break
        results.append((i,first,max_hi/entry-1))
    count=len(results)
    return {"eligible":count,
            "hit_target_before_10pct_stop":sum(k=="target" for _,k,_ in results),
            "stopped_first":sum(k=="stop" for _,k,_ in results),
            "hit_rate_pct":round(100*sum(k=="target" for _,k,_ in results)/count,2) if count else None,
            "max_optimistic_excursion_pct_median":round(100*statistics.median(v for _,_,v in results),2) if count else None}


def trade_simulation(rows, entries, begin, end, hma_exit, horizon=H30, goal=.20, hard_stop=.10, trail=.08):
    """No overlapping trades; entry next OPEN, trailing from previous completed bars;
    same-bar stop/trail always wins against target; HMA downturn exits next OPEN.
    """
    s=set(i for i in entries if begin<=i<end)
    trades=[]
    equity=10000.
    i=begin
    while i<end-1:
        if i not in s:
            i+=1;continue
        enter=i+1
        if enter>=end:break
        entry_price=rows[enter][1]*(1+COST_PER_SIDE)
        stop=entry_price*(1-hard_stop)
        max_high_before=entry_price
        exit_price=None
        reason=None
        last=min(end-1,enter+horizon-1)
        for j in range(enter,last+1):
            opening=rows[j][1]
            candidate_stop=max(stop,max_high_before*(1-trail))
            if j>enter and hma_exit[j-1]:
                exit_price=opening*(1-COST_PER_SIDE);reason="HMA_turn_down";last=j;break
            if opening<=candidate_stop:
                exit_price=opening*(1-COST_PER_SIDE);reason="gap_stop";last=j;break
            if rows[j][3]<=candidate_stop:
                exit_price=candidate_stop*(1-COST_PER_SIDE);reason="stop_or_trail";last=j;break
            if rows[j][2]>=entry_price*(1+goal):
                exit_price=entry_price*(1+goal)*(1-COST_PER_SIDE);reason="take_profit";last=j;break
            max_high_before=max(max_high_before,rows[j][2])
        if exit_price is None:
            exit_price=rows[last][4]*(1-COST_PER_SIDE);reason="time_exit"
        ret=exit_price/entry_price-1
        equity*=1+ret
        trades.append({"entry_index":enter,"exit_index":last,"return_pct":100*ret,"reason":reason})
        i=last+1
    if not trades:return {"trades":0,"win_pct":None,"net_return_pct":0.0,"median_return_pct":None,
                          "profit_factor":None,"exit_reasons":{}}
    pos=sum(1 for t in trades if t["return_pct"]>0)
    gain=sum(max(0,t["return_pct"]) for t in trades)
    loss=sum(max(0,-t["return_pct"]) for t in trades)
    return {"trades":len(trades),"win_pct":round(100*pos/len(trades),2),
            "net_return_pct":round(100*(equity/10000-1),2),
            "median_return_pct":round(statistics.median(t["return_pct"] for t in trades),2),
            "profit_factor":round(gain/loss,3) if loss else None,
            "exit_reasons":dict(collections.Counter(t["reason"] for t in trades))}


def hma_derived_exit(close,n=21):
    h=hma(close,n)
    return [i>=n+math.isqrt(n)+1 and h[i]<h[i-1] for i in range(len(close))]


def higher_regimes(rows):
    # True market UTC day and 12H buckets. Only count a full group of completed 4h
    # bars. A regime value is first usable at the last 4H bar close in that group.
    regimes={}
    for timeframe,size,period in (("12h",3,16),("1d",6,20)):
        groups=collections.defaultdict(list)
        for i,r in enumerate(rows):
            when=r[0]
            date_start=dt.datetime.combine(when.date(),dt.time(0),tzinfo=dt.timezone.utc)
            slot=when.hour//12 if size==3 else 0
            key=date_start+dt.timedelta(hours=12*slot)
            groups[key].append(i)
        valid=[]
        for key,positions in sorted(groups.items()):
            required_hours=[key.hour+4*x for x in range(size)]
            if len(positions)!=size or [rows[i][0].hour for i in positions]!=required_hours:
                continue
            valid.append((positions[-1],rows[positions[-1]][4]))
        hm=hma([v for _,v in valid],period)
        gate=[None]*len(rows)
        value=None
        ix=0
        for i in range(len(rows)):
            while ix<len(valid) and valid[ix][0]<=i:
                if ix>=period+math.isqrt(period)+2 and math.isfinite(hm[ix]) and math.isfinite(hm[ix-1]):
                    value=hm[ix]>hm[ix-1]
                ix+=1
            gate[i]=value
        regimes[timeframe]=gate
    return regimes


def confluence(picked, begin, end, regimes, min_votes=2, within_bars=3):
    # At each bar only votes of distinct model families with event in last <=12h.
    lists={name:set(v) for name,v in picked.items()}
    timestamps=[]
    active_prev=False
    last_signal=-100000
    for i in range(begin,end):
        votes=[name for name,ev in lists.items() if any((i-k) in ev for k in range(within_bars+1))]
        active=len(votes)>=min_votes and regimes["12h"][i] is True and regimes["1d"][i] is True
        if active and not active_prev and i-last_signal>=6:
            timestamps.append(i);last_signal=i
        active_prev=active
    return timestamps


def rank_train(rows, event_map, split):
    all_ranked=[]
    for name,models in event_map.items():
        candidates=[]
        for params,events in models:
            train=unique_events(events,200,split)
            quality=evaluate_horizon(rows,train,200,split,H30,.05,.05)
            eligible=quality["eligible"]
            hits=quality["hit_target_before_10pct_stop"]
            # No cherry-picking 1-2 events. Targets and score preselected.
            score= (hits+2)/(eligible+4) if eligible>=16 else -1
            # Soft penalty for extremely low / high densities (only 5%-in-30d target selection).
            candidates.append((score,eligible,params,events,quality))
        winner=max(candidates,key=lambda x:(x[0],min(x[1],80)))
        all_ranked.append((name,winner))
    return all_ranked


def main():
    p=argparse.ArgumentParser()
    p.add_argument("--csv",required=True,type=Path)
    p.add_argument("--output",required=True,type=Path)
    args=p.parse_args()
    rows=load_data(args.csv)
    cache=get_cache(rows)
    split=2190
    rules=candidates()
    evaluated={}
    for name,options in rules.items():
        evaluated[name]=[(params,build_events(rows,name,params,cache)) for params in options]
    ranked=rank_train(rows,evaluated,split)
    exit_flags=hma_derived_exit(cache["close"],21)
    models=[]
    for name,(score,n,params,raw,train_quality) in ranked:
        older=unique_events(raw,200,split)
        recent=unique_events(raw,split,len(rows))
        half={
         "family":name,"selected_params":params,"train_selection_score":round(score,4),
         "train_events":len(older),"test_events":len(recent),
         "train_target_5pct_30d":train_quality,
         "test_target_5pct_30d":evaluate_horizon(rows,recent,split,len(rows),H30,.05,.05),
         "test_target_20pct_30d":evaluate_horizon(rows,recent,split,len(rows),H30,.20,.10),
         "test_target_50pct_60d":evaluate_horizon(rows,recent,split,len(rows),H60,.50,.10),
         "test_target_50pct_90d":evaluate_horizon(rows,recent,split,len(rows),H90,.50,.10),
         "test_exit_trading":trade_simulation(rows,recent,split,len(rows),exit_flags)
        }
        models.append(half)
    # Choose by TRAINING QUALITY ONLY among distinct model families.
    chosen=sorted(ranked,key=lambda p:(p[1][0],min(p[1][1],80)),reverse=True)[:5]
    named={name:unique_events(meta[3],0,len(rows)) for name,meta in chosen}
    higher=higher_regimes(rows)
    con_old=confluence(named,200,split,higher,2)
    con_new=confluence(named,split,len(rows),higher,2)
    response={
      "experiment":"DJMRN HMA-MULTI-CONFIRM V1 / exploratory only",
      "source":"Bitstamp BTC/USD 4H continuous OHLCV 2024-11-07 through 2026-11-07",
      "data_sha256":"d8f286a9b64be2b6b54b87302ef55bd5f9f7962774f3ab12b016a661190a664a",
      "train_first_bar":rows[0][0].isoformat(),
      "test_first_bar":rows[split][0].isoformat(),
      "test_last_bar":rows[-1][0].isoformat(),
      "candidate_families":len(rules),
      "candidate_variants":sum(len(x) for x in rules.values()),
      "selection":"training ONLY; 5% high before -5% low within 30d; at least 16 eligible events",
      "events_definition":"transition/crossing events, deduped >=24h apart per model, signal computed after complete 4H close",
      "event_outcome":"enter next 4H OPEN, conservative stop first if high and low hit same 4H bar; censored near end",
      "trading_exit":"20% target / 10% stop / 8% prev-high trailing / HMA21 turn down / max 30days; fee+slippage 15 bps each side",
      "models":models,
      "confirmation":{
       "picked_by_train_only":[name for name,_ in chosen],
       "rule":"at least 2 of top 5 families within last 12h + completed 12H HMA16 and daily HMA20 both rising; 1-day rearm",
       "training_events":len(con_old),"test_events":len(con_new),
       "test_goal_5pct_30d":evaluate_horizon(rows,con_new,split,len(rows),H30,.05,.05),
       "test_goal_20pct_30d":evaluate_horizon(rows,con_new,split,len(rows),H30,.20,.10),
       "test_exit":trade_simulation(rows,con_new,split,len(rows),exit_flags)
      },
      "warnings":[
       "Results are exploratory only; no calibrated probability, no live positions, no financial advice.",
       "A signal event count is not an executable trade count. Confluence does not guarantee fewer errors.",
       "Forward 20%-30d and 50%-60/90d targets are hypotheses, not parameter selection objectives.",
       "More variants and repeated inspection of the same holdout increases multiple-testing / overfitting risk.",
       "No point-in-time macro news or external fundamentals have been included; prior 40/20/40 scores are not active.",
       "Higher timeframes resampled from completed 4H data only; 1H not used.",
       "HMA periods are measured in four-hour candles, not days. Trade exit ordering is conservative where ambiguous.",
       "The horizon-metric and trading-exit metrics use different stop logic and must not be compared as identical outcomes."
      ]
    }
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(response,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    print("FAMILIES="+str(len(rules))+";VARIANTS="+str(response["candidate_variants"]))
    for x in models:
        print("MODEL="+x["family"]+";PARAMS="+str(x["selected_params"])+";TRAIN="+str(x["train_events"])+";TEST="+str(x["test_events"])+";TEST_GOAL_20_30D="+str(x["test_target_20pct_30d"]["hit_rate_pct"])+";TEST_TRADE_RETURN="+str(x["test_exit_trading"]["net_return_pct"]))
    print("CONFLUENCE_TRAIN="+str(len(con_old))+";TEST="+str(len(con_new))+";TEST_GOAL20="+str(response["confirmation"]["test_goal_20pct_30d"]["hit_rate_pct"])+";TRADING="+str(response["confirmation"]["test_exit"]["net_return_pct"]))
    print("OUTPUT="+str(args.output))


if __name__=="__main__":
    main()
