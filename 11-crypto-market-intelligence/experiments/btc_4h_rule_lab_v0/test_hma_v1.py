"""Causality regression for HMA multi-timeframe BTC research sandbox.

No data beyond candle t may influence a signal emitted at candle t.
This file tests prefix invariance of all 46 parameter variants and 12H/1D
regime data, using the full existing Bitstamp snapshot.
"""
import argparse
import math
from pathlib import Path
from run import load_data
import hma_multiconfirm_v1 as m


def run_checks(csv_path):
    rows=load_data(csv_path)
    cache=m.get_cache(rows)
    checks=0
    for model,variants in m.candidates().items():
        for params in variants:
            full=m.build_events(rows,model,params,cache)
            for cut in (300,900,2000,3400):
                part=rows[:cut]
                expected=[i for i in full if i<cut]
                actual=m.build_events(part,model,params,m.get_cache(part))
                if actual!=expected:
                    raise AssertionError("Future-data leak "+model+" "+str(params)+" cut="+str(cut))
                checks+=1
    full=m.higher_regimes(rows)
    for cut in (400,1000,2200,3400):
        part=m.higher_regimes(rows[:cut])
        for tf in ("12h","1d"):
            if part[tf]!=full[tf][:cut]:
                raise AssertionError("Future regime data leaked "+tf+" cut="+str(cut))
            checks+=1
    close=[r[4] for r in rows]
    for n in (9,16,21,34,55,89):
        full_hma=m.hma(close,n)
        for cut in (200,900,2000):
            prefix=m.hma(close[:cut],n)
            for a,b in zip(full_hma[:cut],prefix):
                if math.isfinite(a):
                    if not (math.isfinite(b) and abs(a-b)<1e-8):
                        raise AssertionError("HMA prefix inconsistency: period "+str(n))
            checks+=1
    print("CAUSALITY_CHECKS=PASS;COUNT="+str(checks)+";MODELS="+str(len(m.candidates()))+
          ";VARIANTS="+str(sum(len(x) for x in m.candidates().values())))


if __name__=="__main__":
    arg=argparse.ArgumentParser()
    arg.add_argument("--csv",required=True,type=Path)
    parsed=arg.parse_args()
    run_checks(parsed.csv)
