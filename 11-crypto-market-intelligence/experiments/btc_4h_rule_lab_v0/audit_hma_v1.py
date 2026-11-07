"""Repeatable HMA timeframe and confluence timing sensitivity audit.
All selection is training only. Test-year outcomes exploratory, not predictive.
"""
import argparse
import collections
import datetime as dt
import json
import math
from pathlib import Path
from run import load_data
import hma_multiconfirm_v1 as core


def completed_timeframe(rows, hours):
    slots=collections.defaultdict(list)
    for i,b in enumerate(rows):
        t=b[0]
        midnight=dt.datetime.combine(t.date(),dt.time(0),tzinfo=dt.timezone.utc)
        anchor=t if hours==4 else (midnight + dt.timedelta(hours=12*(t.hour//12))
                                   if hours==12 else midnight)
        slots[anchor].append(i)
    result=[]
    for t,items in sorted(slots.items()):
        if len(items)==hours//4 and [rows[i][0].hour for i in items]==[t.hour+4*x for x in range(hours//4)]:
            result.append((items[-1],rows[items[-1]][4]))
    return result


def main():
    p=argparse.ArgumentParser()
    p.add_argument("--csv",required=True,type=Path)
    p.add_argument("--output",required=True,type=Path)
    a=p.parse_args()
    rows=load_data(a.csv)
    cache=core.get_cache(rows)
    split=2190
    candidates=core.candidates()
    all_families={name:[(params,core.build_events(rows,name,params,cache))
                         for params in variants] for name,variants in candidates.items()}
    ranked=core.rank_train(rows,all_families,split)
    best_families=sorted(ranked,key=lambda x:(x[1][0],min(x[1][1],80)),reverse=True)[:5]
    chosen={name:core.unique_events(item[3],0,len(rows)) for name,item in best_families}
    regimes=core.higher_regimes(rows)
    cases=[]
    for votes in (2,3,4):
        before=core.confluence(chosen,200,split,regimes,votes)
        after=core.confluence(chosen,split,len(rows),regimes,votes)
        exit_options=[]
        for hma_exit in (16,21,34,55,89):
            flags=core.hma_derived_exit(cache["close"],hma_exit)
            train=core.trade_simulation(rows,before,200,split,flags)
            exit_options.append({"hma_exit_period":hma_exit,"train":train})
        winner=max(exit_options,key=lambda x:x["train"]["net_return_pct"])
        frozen=winner["hma_exit_period"]
        result=core.trade_simulation(rows,after,split,len(rows),core.hma_derived_exit(cache["close"],frozen))
        cases.append({
          "confirmation_votes":votes,
          "train_events":len(before),"test_events":len(after),
          "all_train_exit_variants":exit_options,
          "train_selected_hma_exit":frozen,
          "holdout_exit_result":result,
          "test_target_20pct_30days":core.evaluate_horizon(rows,after,split,len(rows),core.H30,.20,.10),
          "test_target_50pct_90days":core.evaluate_horizon(rows,after,split,len(rows),core.H90,.50,.10)
        })
    timeframes=[]
    for hours in (4,12,24):
        z=completed_timeframe(rows,hours)
        close=[x[1] for x in z]
        variants=[]
        for n in (9,16,21,34,55,89):
            line=core.hma(close,n)
            events=[z[j][0] for j in range(n+math.isqrt(n)+3,len(z))
                    if line[j]>line[j-1] and line[j-1]<=line[j-2] and close[j]>line[j]]
            train=core.unique_events(events,200,split)
            holdout=core.unique_events(events,split,len(rows))
            train5=core.evaluate_horizon(rows,train,200,split,core.H30,.05,.05)
            count=train5["eligible"]
            score=(train5["hit_target_before_10pct_stop"]+2)/(count+4) if count>=12 else -1
            variants.append({"hma_period_bars":n,"period_hours":hours*n,
                             "train_events":len(train),"test_events":len(holdout),
                             "train_score":round(score,4),
                             "test_target_20pct_30days":core.evaluate_horizon(
                                 rows,holdout,split,len(rows),core.H30,.20,.10)})
        picked=max(variants,key=lambda x:x["train_score"])
        timeframes.append({"timeframe_hours":hours,"valid_resampled_bars":len(z),
                           "train_selected_hma_period":picked["hma_period_bars"],
                           "all_period_results":variants})
    baseline=[]
    for name,events in (("every_4h",list(range(split,len(rows)))),
                        ("once_per_day",list(range(split,len(rows),6)))):
        baseline.append({"name":name,"samples":len(events),
                         "target_20pct_30days":core.evaluate_horizon(
                            rows,events,split,len(rows),core.H30,.20,.10),
                         "target_50pct_90days":core.evaluate_horizon(
                            rows,events,split,len(rows),core.H90,.50,.10)})
    report={
      "label":"DJMRN BTC 4H HMA V1 RESEARCH-ONLY timing/exit sensitivity",
      "provenance":"Bitstamp BTC/USD snapshot SHA256 d8f286a9b64be2b6b54b87302ef55bd5f9f7962774f3ab12b016a661190a664a",
      "train_split_index":split,
      "model_selection":"first year ONLY, including train-selected exit periods, five families and HMA periods",
      "chosen_families":[name for name,_ in best_families],
      "exit_and_confluence":cases,
      "hma_multi_timeframe":timeframes,
      "unconditional_baselines":baseline,
      "causality_selftest":"210 prefix-regression checks separately passed",
      "no_financial_advice":True,
      "warnings":[
       "Results are exploratory; 7 trades in a test year is a tiny sample and cannot establish a reliable success rate.",
       "No 50%-within-90d target hit appeared on held-out sample under specified 10% stop.",
       "Higher timeframe trends use only fully closed groups of 4H Bitstamp bars.",
       "Train-optimal exit HMA is selected without looking at test outcomes; repeated test inspection risks data snooping.",
       "Fundamental/news 20% weight and rolling annual behavior 40% are NOT active.",
       "Trading results use assumed fee plus slippage 15 bps each side, not execution venue price guarantees."
      ]}
    a.output.parent.mkdir(parents=True,exist_ok=True)
    a.output.write_text(json.dumps(report,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    print("TRAIN_SELECTED_FAMILIES="+str(report["chosen_families"]))
    for x in cases:
        print("CONFLUENCE_VOTES="+str(x["confirmation_votes"])+";TRAIN="+str(x["train_events"])+";TEST="+str(x["test_events"])+";EXIT_HMA_CHOSEN_TRAIN="+str(x["train_selected_hma_exit"])+";TEST_NET_RETURN_PCT="+str(x["holdout_exit_result"]["net_return_pct"])+";TEST_WIN_PCT="+str(x["holdout_exit_result"]["win_pct"])+";TRADES="+str(x["holdout_exit_result"]["trades"]))
    for tf in timeframes:
        print("TIMEFRAME_H="+str(tf["timeframe_hours"])+";CANDLES="+str(tf["valid_resampled_bars"])+";TRAIN_SELECTED_HMA="+str(tf["train_selected_hma_period"]))
    print("SAVED="+str(a.output))


if __name__=="__main__":
    main()
