# Experiment Log

Permanent record of controlled improvement cycles for BIST-RankingBot.

Each future cycle must append one entry using the format defined in `AGENT_TASK.md`.

## Log Format

```markdown
## YYYY-MM-DD HH:MM TZ - Short experiment name

- Timestamp: YYYY-MM-DD HH:MM TZ
- Hypothesis: ...
- Biggest weakness: ...
- Improvement implemented: ...
- Files changed:
  - `path/to/file.py`
- Metrics before:
  - Best validation model / size: ...
  - Validation selection_score: ...
  - Validation strategy_total_return: ...
  - Validation excess_return_over_benchmark: ...
  - Validation strategy_max_drawdown: ...
  - Validation win_rate: ...
  - Out-of-sample selection_score: ...
  - Out-of-sample strategy_total_return: ...
  - Out-of-sample excess_return_over_benchmark: ...
  - Out-of-sample strategy_max_drawdown: ...
  - Out-of-sample win_rate: ...
  - Paper trading total return: ...
  - Paper trading benchmark return: ...
- Validation command: `python main.py`
- Validation result: passed/failed
- Metrics after:
  - Best validation model / size: ...
  - Validation selection_score: ...
  - Validation strategy_total_return: ...
  - Validation excess_return_over_benchmark: ...
  - Validation strategy_max_drawdown: ...
  - Validation win_rate: ...
  - Out-of-sample selection_score: ...
  - Out-of-sample strategy_total_return: ...
  - Out-of-sample excess_return_over_benchmark: ...
  - Out-of-sample strategy_max_drawdown: ...
  - Out-of-sample win_rate: ...
  - Paper trading total return: ...
  - Paper trading benchmark return: ...
- Decision: accepted/rejected
- Reasoning: ...
```

## 2026-06-03 11:34 +03:00 - Fix factor rank direction

- Timestamp: 2026-06-03 11:34 +03:00
- Hypothesis: Correcting `_cross_sectional_score` so higher-is-better factors receive higher percentile scores and lower-is-better volatility receives higher scores for lower raw volatility will make ranking outputs logically correct and improve the validated ranking framework, even if historical model leadership changes.
- Biggest weakness: The latest ranking audit showed factor normalization was inverted: momentum, volume increase, and MA trend were penalized when high, while higher volatility was rewarded. This made current recommendations explainability-invalid even when some backtest metrics looked strong.
- Improvement implemented: Changed `_cross_sectional_score` to use `ascending=higher_is_better`.
- Files changed:
  - `src/ranking.py`
  - Generated validation outputs under `results/`
  - Generated paper trading outputs under `paper_trading/`
- Metrics before:
  - Best validation model / size: low_volatility / 5
  - Validation selection_score: 1.170089
  - Validation strategy_total_return: 4.353909
  - Validation excess_return_over_benchmark: 1.112345
  - Validation strategy_max_drawdown: -0.148211
  - Validation win_rate: 0.708333
  - Out-of-sample selection_score: 0.316395
  - Out-of-sample strategy_total_return: 0.925429
  - Out-of-sample excess_return_over_benchmark: 0.312559
  - Out-of-sample strategy_max_drawdown: -0.144634
  - Out-of-sample win_rate: 0.586207
  - Paper trading total return: 0.00%
  - Paper trading benchmark return: 0.00%
  - Regime policy avg_robustness_score, best policy: defensive_mode 0.243895
  - Factor direction check: momentum/volume/trend correlations were negative; volatility correlation was positive.
- Validation command: `.venv\Scripts\python.exe main.py`
- Validation result: passed. Yahoo Finance returned no valid data for `KOZAL.IS`, which the project recorded as a missing ticker. Pandas emitted future warnings in paper trading, but the run completed.
- Metrics after:
  - Best validation model / size: trend_following / 3
  - Validation selection_score: 2.210031
  - Validation strategy_total_return: 5.372737
  - Validation excess_return_over_benchmark: 2.131174
  - Validation strategy_max_drawdown: -0.116821
  - Validation win_rate: 0.625000
  - Out-of-sample selection_score: -0.213398
  - Out-of-sample strategy_total_return: 0.442529
  - Out-of-sample excess_return_over_benchmark: -0.170341
  - Out-of-sample strategy_max_drawdown: -0.176701
  - Out-of-sample win_rate: 0.620690
  - Paper trading total return: 0.00%
  - Paper trading benchmark return: 0.00%
  - Regime policy avg_robustness_score, best policy: baseline 0.315792
  - Factor direction check: `momentum_1m` 0.8028, `momentum_3m` 0.9762, `momentum_6m` 0.8946, `volume_increase` 0.9541, `above_ma` 0.9892, `volatility` -0.9912.
- Decision: accepted
- Reasoning: Accepted despite the selected validation winner's out-of-sample score worsening because the previous system had a fundamental sign-direction bug that made rankings and explanations invalid. The fix restores correct factor semantics, validation score improves from 1.170089 to 2.210031, validation drawdown improves from -0.148211 to -0.116821, and the best regime policy average robustness improves from 0.243895 to 0.315792. The remaining validation/out-of-sample winner mismatch is now the biggest weakness for the next cycle.

## 2026-06-03 15:23 +03:00 - Add cash allocation threshold

- Timestamp: 2026-06-03 15:23 +03:00
- Hypothesis: Adding an opportunity threshold and leaving weak slots in `CASH` will reduce forced exposure when expected returns are unattractive, improving risk control even if return participation falls.
- Biggest weakness: The system forced 100% stock allocation even when the current opportunity set was weak.
- Improvement implemented: Tested 2%, 5%, 8%, 10%, and 12% thresholds, selected 5%, added `CASH` as a portfolio asset, and updated investor reports to show cash allocation and qualified opportunity count.
- Files changed:
  - `config.py`
  - `main.py`
  - `src/current_portfolio.py`
  - `src/investor_report.py`
  - `src/cash_allocation.py`
  - `src/real_return_report.py`
  - `results/cash_allocation_report.md`
  - `results/cash_allocation_comparison.csv`
  - `results/monthly_investor_report.xlsx`
  - `results/monthly_investor_report.md`
  - `results/real_return_report.md`
  - Generated validation and paper trading outputs under `results/` and `paper_trading/`
- Metrics before:
  - Best validation model / size: trend_following / 3
  - Validation selection_score: 2.210031
  - Validation strategy_total_return: 5.372737
  - Validation excess_return_over_benchmark: 2.131174
  - Validation strategy_max_drawdown: -0.116821
  - Validation win_rate: 0.625000
  - Out-of-sample selection_score: -0.213398
  - Out-of-sample strategy_total_return: 0.442529
  - Out-of-sample excess_return_over_benchmark: -0.170341
  - Out-of-sample strategy_max_drawdown: -0.176701
  - Out-of-sample win_rate: 0.620690
  - Baseline avg cash weight: 0.00%
- Validation command: `.venv\Scripts\python.exe main.py`
- Validation result: passed. Yahoo Finance returned no valid data for `KOZAL.IS`, which the project recorded as a missing ticker. Pandas emitted future warnings in paper trading and investor report row concatenation, but the run completed.
- Metrics after:
  - Selected threshold: 5.00%
  - Current cash allocation: 80.00%
  - Current qualified opportunities: 2
  - Validation selection_score: -2.973929
  - Validation strategy_total_return: 0.228055
  - Validation excess_return_over_benchmark: -3.013509
  - Validation strategy_max_drawdown: -0.032294
  - Validation win_rate: 0.208333
  - Validation avg cash weight: 81.94%
  - Out-of-sample selection_score: -0.412659
  - Out-of-sample strategy_total_return: 0.155657
  - Out-of-sample excess_return_over_benchmark: -0.457213
  - Out-of-sample strategy_max_drawdown: -0.063930
  - Out-of-sample win_rate: 0.344828
  - Out-of-sample avg cash weight: 70.11%
- Decision: accepted
- Reasoning: Accepted under the stated rule because out-of-sample drawdown improved materially from -17.67% to -6.39%, an 11.28 percentage-point reduction. The tradeoff is lower out-of-sample return, excess return, win rate, and selection_score, so the next weakness is that the cash filter is defensive but too return-sacrificing.

## 2026-06-03 15:43 +03:00 - Calibrate opportunity filter

- Timestamp: 2026-06-03 15:43 +03:00
- Hypothesis: Replacing the fixed 5% opportunity threshold with a non-negative percentile filter will reduce excessive cash allocation and materially improve out-of-sample return while keeping drawdown better than the full-invested baseline.
- Biggest weakness: The selected 5% fixed threshold produced about 70.11% average out-of-sample cash allocation and reduced out-of-sample total return to 15.57%.
- Improvement implemented: Added a calibrated opportunity filter that requires expected return to be non-negative and at or above the current opportunity set's 50th percentile. Cash allocation support remains active.
- Files changed:
  - `config.py`
  - `main.py`
  - `src/current_portfolio.py`
  - `src/investor_report.py`
  - `src/cash_allocation.py`
  - `results/opportunity_filter_calibration.md`
  - `results/monthly_investor_report.xlsx`
  - `results/monthly_investor_report.md`
  - `results/recommendation_audit_report.md`
  - Generated validation and paper trading outputs under `results/` and `paper_trading/`
- Metrics before:
  - Current filter: fixed 5.00% expected-return threshold
  - Best validation model / size: trend_following / 3
  - Validation selection_score: -2.973929
  - Validation strategy_total_return: 0.228055
  - Validation excess_return_over_benchmark: -3.013509
  - Validation strategy_max_drawdown: -0.032294
  - Validation win_rate: 0.208333
  - Validation avg cash weight: 81.94%
  - Out-of-sample selection_score: -0.412659
  - Out-of-sample strategy_total_return: 0.155657
  - Out-of-sample excess_return_over_benchmark: -0.457213
  - Out-of-sample strategy_max_drawdown: -0.063930
  - Out-of-sample win_rate: 0.344828
  - Out-of-sample avg cash weight: 70.11%
  - Full-invested baseline out-of-sample strategy_total_return: 0.442529
  - Full-invested baseline out-of-sample strategy_max_drawdown: -0.176701
  - Paper trading total return: 280.00%
  - Paper trading benchmark return: 0.00%
- Validation command: `.venv\Scripts\python.exe main.py`
- Validation result: passed. Yahoo Finance returned no valid data for `KOZAL.IS`, which the project recorded as a missing ticker. Pandas emitted future warnings in paper trading and investor report row concatenation, but the run completed.
- Metrics after:
  - Selected filter: percentile_positive_p50
  - Current effective BUY threshold: 1.50%
  - Current cash allocation: 50.00%
  - Current qualified opportunities: 5
  - Validation selection_score: -1.403081
  - Validation strategy_total_return: 1.680045
  - Validation excess_return_over_benchmark: -1.561519
  - Validation strategy_max_drawdown: -0.077031
  - Validation win_rate: 0.625000
  - Validation avg cash weight: 38.89%
  - Out-of-sample selection_score: 0.101305
  - Out-of-sample strategy_total_return: 0.640525
  - Out-of-sample excess_return_over_benchmark: 0.027655
  - Out-of-sample strategy_max_drawdown: -0.109727
  - Out-of-sample win_rate: 0.586207
  - Out-of-sample avg cash weight: 35.63%
  - Paper trading total return: 420.00%
  - Paper trading benchmark return: 0.00%
- Decision: accepted
- Reasoning: Accepted because out-of-sample return improved materially versus the current 5% threshold, from 15.57% to 64.05%, and drawdown remained improved versus the full-invested baseline, at -10.97% versus -17.67%. The filter also reduced average out-of-sample cash from 70.11% to 35.63%, keeping cash support without starving the strategy of exposure.
