# Follow-Up Improvement Research

This is research-only. Production follow-up tracking remains fixed and still reads reports/tracking_state.json.

## Policy Summary

| policy_id   | policy_name                   | frequency   |   portfolio_size | total_return   | benchmark_total_return   | cagr   | bist100_cagr   | excess_cagr   | monthly_win_rate_vs_bist100   | average_monthly_excess_return   | max_drawdown   |   average_monthly_turnover |   average_trades_per_month | transaction_cost_impact   | worst_underperformance_month   | worst_underperformance   | best_outperformance_month   | best_outperformance   |   intervals |
|:------------|:------------------------------|:------------|-----------------:|:---------------|:-------------------------|:-------|:---------------|:--------------|:------------------------------|:--------------------------------|:---------------|---------------------------:|---------------------------:|:--------------------------|:-------------------------------|:-------------------------|:----------------------------|:----------------------|------------:|
| A           | Current baseline monthly Top3 | monthly     |                3 | 67.81%         | 60.88%                   | 20.57% | 18.74%         | 1.82%         | 45.45%                        | 0.19%                           | -19.32%        |                    1.24242 |                    3.72727 | 14.13%                    | 2024-04                        | -10.59%                  | 2025-04                     | 15.27%                |          34 |
| B           | Weekly rebalance Top3         | weekly      |                3 | -14.12%        | 60.88%                   | -5.35% | 18.74%         | -24.09%       | 38.24%                        | -1.73%                          | -42.13%        |                    3.04902 |                    9.14706 | 19.90%                    | 2024-03                        | -12.42%                  | 2025-03                     | 12.41%                |         145 |
| C           | Weekly rebalance Top5         | weekly      |                5 | 7.88%          | 60.88%                   | 2.78%  | 18.74%         | -15.96%       | 44.12%                        | -1.12%                          | -36.45%        |                    2.65294 |                   13.2647  | 21.36%                    | 2024-08                        | -9.16%                   | 2026-09                     | 6.85%                 |         145 |
| D           | Relative Strength Top3        | weekly      |                3 | -7.78%         | 60.88%                   | -2.88% | 18.74%         | -21.63%       | 35.29%                        | -1.58%                          | -38.81%        |                    4.22549 |                   12.6765  | 30.64%                    | 2026-02                        | -14.58%                  | 2026-08                     | 8.57%                 |         145 |
| E           | Benchmark-aware Top3          | weekly      |                3 | -13.92%        | 60.88%                   | -5.27% | 18.74%         | -24.01%       | 32.35%                        | -1.79%                          | -40.42%        |                    4.20588 |                   12.6176  | 28.49%                    | 2026-02                        | -11.73%                  | 2026-08                     | 8.57%                 |         145 |
| F           | Leadership Rotation Overlay   | weekly      |                3 | -15.23%        | 60.88%                   | -5.80% | 18.74%         | -24.54%       | 38.24%                        | -1.77%                          | -42.16%        |                    4.14706 |                   12.4412  | 27.65%                    | 2026-02                        | -11.73%                  | 2026-08                     | 8.44%                 |         145 |

## Decision

- Did weekly rebalance improve excess return? No. Historical excess CAGR delta vs baseline: -25.91%; recent excess delta: -0.19%.
- Did relative strength improve excess return? Recent yes, historical no, so rejected. Historical excess CAGR delta vs baseline: -23.45%; recent excess delta: 2.43%.
- Did benchmark-aware selection improve excess return? Recent yes, historical no, so rejected. Historical excess CAGR delta vs baseline: -25.84%; recent excess delta: 2.01%.
- Did any policy beat BIST100 robustly? No under the current acceptance filter.
- Next paper-trading candidate: none. No policy passed both historical and recent acceptance criteria.
- Current one-month fixed hold should be kept for tracking, while weekly/relative-strength variants remain research-only.

## Acceptance Rule

A policy is only eligible if it improves both historical walk-forward excess return and the recent 2026-06 counterfactual excess return. Policies that only fix June 2026 are rejected.
