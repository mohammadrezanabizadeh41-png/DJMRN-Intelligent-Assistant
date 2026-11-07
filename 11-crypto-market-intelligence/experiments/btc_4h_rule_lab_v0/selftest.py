"""Read-only regression checks for the BTC 4H experimental runner."""
import argparse
import json
from pathlib import Path
import run


def check(data: Path, config_path: Path):
    config = json.loads(config_path.read_text(encoding="utf-8"))
    rows = run.load_data(data)
    assert len(rows) == 4380
    assert all(rows[i][0] < rows[i+1][0] for i in range(len(rows)-1))
    total_checks = 0
    for model, params_list in config["candidates"].items():
        for params in params_list:
            full = run.signals(rows, model, params)
            assert len(full) == len(rows)
            assert set(full).issubset({0, 1})
            # Reject any rule that depends on data arriving after the signal candle.
            for cut in (1200, 2500):
                prefix = run.signals(rows[:cut], model, params)
                assert full[:cut] == prefix, (model, params, cut)
                total_checks += 1
            free = run.backtest(rows, full, 2190, len(rows), 0)
            priced = run.backtest(rows, full, 2190, len(rows), 15)
            assert priced["net_return_pct"] <= free["net_return_pct"] + 0.002
            total_checks += 1
    report = run.evaluate(data, config)
    assert report["train_candles"] == 2190
    assert report["holdout_candles"] == 2190
    assert len(report["strategies"]) == 6
    print("SELFTEST=PASS;CHECKS=" + str(total_checks) +
          ";RULE_FAMILIES=" + str(len(config["candidates"])) +
          ";DATA_BARS=" + str(len(rows)))


if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("--csv", type=Path, required=True)
    p.add_argument("--config", type=Path, required=True)
    a = p.parse_args()
    check(a.csv, a.config)
