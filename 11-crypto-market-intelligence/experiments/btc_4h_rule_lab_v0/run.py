"""DJMRN BTC 4H research sandbox. Standard library; no network or trades."""
import argparse
import csv
import datetime as dt
import hashlib
import json
import math
import statistics
from pathlib import Path

EXPECTED_SHA256 = "d8f286a9b64be2b6b54b87302ef55bd5f9f7962774f3ab12b016a661190a664a"


def load_data(path):
    digest = hashlib.sha256(path.read_bytes()).hexdigest()
    if digest != EXPECTED_SHA256:
        raise ValueError("Bitstamp dataset hash mismatch; do not use altered data: " + digest)
    with path.open(encoding="utf-8", newline="") as f:
        records = list(csv.DictReader(f))
    rows = []
    for rec in records:
        t = dt.datetime.fromisoformat(rec["timestamp_utc"].replace("Z", "+00:00"))
        vals = [float(rec[key]) for key in ("open_usd", "high_usd", "low_usd", "close_usd", "volume_btc")]
        o, h, l, c, v = vals
        if not all(map(math.isfinite, vals)) or not (0 < l <= min(o, c) <= max(o, c) <= h) or v <= 0:
            raise ValueError("Invalid OHLCV: " + str(t))
        if t.minute or t.second or t.hour % 4 or (rows and t-rows[-1][0] != dt.timedelta(hours=4)):
            raise ValueError("Non-continuous UTC 4H candle at " + str(t))
        rows.append((t, o, h, l, c, v))
    if len(rows) != 4380: raise ValueError("Expected 4380 complete bars")
    return rows


def ema(data, period):
    alpha = 2 / (period + 1)
    out = []
    z = data[0]
    for x in data:
        z += alpha * (x-z)
        out.append(z)
    return out


def ma(data, period):
    out = [float("nan")]*len(data)
    total = 0.0
    for i, x in enumerate(data):
        total += x
        if i >= period: total -= data[i-period]
        if i >= period-1: out[i] = total/period
    return out


def wilder_rsi(data, period):
    out = [float("nan")]*len(data)
    gain = loss = 0.0
    for i in range(1, len(data)):
        delta = data[i]-data[i-1]
        up, down = max(0.0, delta), max(0.0, -delta)
        if i <= period:
            gain += up
            loss += down
            if i != period: continue
            gain /= period
            loss /= period
        else:
            gain = (gain*(period-1)+up)/period
            loss = (loss*(period-1)+down)/period
        out[i] = 100.0 if loss == 0 else 100-100/(1+gain/loss)
    return out


def signals(rows, model, p):
    close = [r[4] for r in rows]
    high = [r[2] for r in rows]
    low = [r[3] for r in rows]
    n = len(rows)
    out = [0]*n
    if model == "sma":
        fast, slow = p["fast"], p["slow"]
        a, b = ma(close, fast), ma(close, slow)
        for i in range(slow-1, n): out[i] = int(a[i]>b[i] and close[i]>b[i])
    elif model == "ema":
        fast, slow = p["fast"], p["slow"]
        a, b = ema(close, fast), ema(close, slow)
        for i in range(slow+10, n): out[i] = int(a[i]>b[i] and close[i]>b[i])
    elif model == "macd":
        fast, slow, period = p["fast"], p["slow"], p["signal"]
        a, b = ema(close, fast), ema(close, slow)
        macd = [x-y for x,y in zip(a,b)]
        s = ema(macd, period)
        for i in range(slow+period, n): out[i] = int(macd[i]>s[i] and macd[i]>0)
    elif model == "rsi":
        r = wilder_rsi(close, p["period"])
        state = 0
        for i in range(p["period"], n):
            if r[i] <= p["buy"]: state = 1
            elif r[i] >= p["sell"]: state = 0
            out[i] = state
    elif model == "bollinger":
        period, sigma = p["period"], p["sigma"]
        state = 0
        for i in range(period-1, n):
            group = close[i-period+1:i+1]
            middle = statistics.fmean(group)
            if close[i] < middle-sigma*statistics.pstdev(group): state = 1
            elif close[i]>=middle: state = 0
            out[i] = state
    elif model == "breakout":
        lookback, exit_period = p["lookback"], p["exit"]
        state = 0
        for i in range(lookback, n):
            if close[i]>max(high[i-lookback:i]): state=1
            elif close[i]<min(low[i-exit_period:i]): state=0
            out[i]=state
    else: raise ValueError("Unknown model "+model)
    return out


def backtest(rows, positions, start, end, per_side_bps):
    """End-of-candle t signal, NEXT bar t+1 OPEN fill. Long/flat only."""
    cost=per_side_bps/10000
    cash=10000.0
    units=0.0
    entry_equity=0
    round_trips=[]
    curve=[cash]
    for i in range(start,end):
        wanted=positions[i-1]
        op=rows[i][1]
        if wanted and units==0:
            entry_equity=cash
            units=cash/(op*(1+cost))
            cash=0
        elif not wanted and units:
            cash=units*op*(1-cost)
            round_trips.append(cash/entry_equity-1)
            units=0
        curve.append(cash+units*rows[i][4])
    if units:
        cash=units*rows[end-1][4]*(1-cost)
        round_trips.append(cash/entry_equity-1)
        curve[-1]=cash
    peak=curve[0]
    dd=0.0
    for v in curve:
        peak=max(v,peak)
        dd=max(dd, 1-v/peak)
    buy_hold=(rows[end-1][4]/rows[start][1])*(1-cost)/(1+cost)-1
    return {
      "net_return_pct":round(100*(curve[-1]/10000-1),3),
      "max_drawdown_pct":round(100*dd,3),
      "closed_trades":len(round_trips),
      "trade_win_rate_pct":round(100*sum(r>0 for r in round_trips)/len(round_trips),2) if round_trips else None,
      "buy_hold_net_pct":round(100*buy_hold,3),
      "long_exposure_pct":round(100*sum(positions[start-1:end-1])/(end-start),2)
    }


def evaluate(csv_path, config):
    rows=load_data(csv_path)
    holdout=dt.datetime.fromisoformat(config["holdout_start_utc"].replace("Z","+00:00"))
    split=next(i for i,row in enumerate(rows) if row[0]>=holdout)
    if split<1000 or len(rows)-split<1000: raise ValueError("Chronological split too small")
    per_side_bps=float(config["fee_bps"])+float(config["slippage_bps"])
    results=[]
    for model, opts in config["candidates"].items():
        candidates=[]
        for params in opts:
            rule=signals(rows,model,params)
            train=backtest(rows,rule,100,split,per_side_bps)
            score=(train["net_return_pct"]-.5*train["max_drawdown_pct"]) if train["closed_trades"]>=4 else -1e9
            candidates.append((score,params,train))
        _, best, train=max(candidates,key=lambda x:x[0])
        rule=signals(rows,model,best)
        test=backtest(rows,rule,split,len(rows),per_side_bps)
        results.append({"strategy":model,"chosen_by_train_only":best,"train":train,"holdout":test})
    results.sort(key=lambda x:x["strategy"])
    return {
     "label":"DJMRN RESEARCH-ONLY BTC/USD 4H deterministic rule experiment v0",
     "source":"Bitstamp historical OHLCV; fixed dataset SHA256",
     "sha256":EXPECTED_SHA256,
     "candles":len(rows),
     "train_candles":split,
     "holdout_candles":len(rows)-split,
     "train_begin_utc":rows[100][0].isoformat(),
     "train_end_before_utc":rows[split][0].isoformat(),
     "holdout_begin_utc":rows[split][0].isoformat(),
     "last_candle_utc":rows[-1][0].isoformat(),
     "cost_bps_each_entry_and_exit":per_side_bps,
     "execution":"Rule evaluated after close; fill at next 4H bar OPEN",
     "selection":"training net return - 0.5*max drawdown, at least 4 closed trades",
     "warnings":["TEST year untouched in parameter selection; ranking test winners retroactively is not live validation",
                 "Model means fixed technical rules, not neural-network ML",
                 "Trade win rate is not calibrated probability of profit",
                 "No news, fundamental, annual-range 40/20/40 scoring, stop-loss or short selling yet"],
     "strategies":results
    }


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--csv",required=True,type=Path)
    parser.add_argument("--config",required=True,type=Path)
    parser.add_argument("--output",required=True,type=Path)
    args=parser.parse_args()
    config=json.loads(args.config.read_text(encoding="utf-8"))
    report=evaluate(args.csv,config)
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(report,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    print("DATA=VERIFIED;TRAIN="+str(report["train_candles"])+";HOLDOUT="+str(report["holdout_candles"]))
    for r in report["strategies"]:
        t=r["holdout"]
        print(r["strategy"]+";NET_PCT="+str(t["net_return_pct"])+";WIN_PCT="+str(t["trade_win_rate_pct"])+";TRADES="+str(t["closed_trades"])+";MAX_DD_PCT="+str(t["max_drawdown_pct"]))
    print("RESULT="+str(args.output))


if __name__=="__main__":
    main()
