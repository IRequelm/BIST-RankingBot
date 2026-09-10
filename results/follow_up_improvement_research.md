# Follow-Up Improvement Research

This is research-only. Production follow-up tracking remains fixed and still reads reports/tracking_state.json.

## Policy Summary

| policy_id   | policy_name                   | frequency   |   portfolio_size | total_return   | benchmark_total_return   | cagr   | bist100_cagr   | excess_cagr   | monthly_win_rate_vs_bist100   | average_monthly_excess_return   | max_drawdown   |   average_monthly_turnover |   average_trades_per_month | transaction_cost_impact   | worst_underperformance_month   | worst_underperformance   | best_outperformance_month   | best_outperformance   |   intervals |
|:------------|:------------------------------|:------------|-----------------:|:---------------|:-------------------------|:-------|:---------------|:--------------|:------------------------------|:--------------------------------|:---------------|---------------------------:|---------------------------:|:--------------------------|:-------------------------------|:-------------------------|:----------------------------|:----------------------|------------:|
| A           | Current baseline monthly Top3 | monthly     |                3 | 88.49%         | 90.25%                   | 26.62% | 27.06%         | -0.44%        | 46.88%                        | 0.06%                           | -19.32%        |                    1.21875 |                    3.65625 | 14.99%                    | 2024-04                        | -10.59%                  | 2025-04                     | 15.27%                |          33 |
| B           | Weekly rebalance Top3         | weekly      |                3 | -2.02%         | 90.25%                   | -0.76% | 27.06%         | -27.82%       | 36.36%                        | -1.87%                          | -42.13%        |                    3.08081 |                    9.24242 | 22.18%                    | 2024-03                        | -12.42%                  | 2025-03                     | 12.41%                |         141 |
| C           | Weekly rebalance Top5         | weekly      |                5 | 16.90%         | 90.25%                   | 5.99%  | 27.06%         | -21.07%       | 42.42%                        | -1.39%                          | -36.45%        |                    2.70909 |                   13.5455  | 22.91%                    | 2024-08                        | -9.16%                   | 2026-03                     | 6.68%                 |         141 |
| D           | Relative Strength Top3        | weekly      |                3 | 2.97%          | 90.25%                   | 1.10%  | 27.06%         | -25.96%       | 36.36%                        | -1.78%                          | -38.81%        |                    4.19192 |                   12.5758  | 32.73%                    | 2026-02                        | -14.58%                  | 2026-08                     | 8.57%                 |         141 |
| E           | Benchmark-aware Top3          | weekly      |                3 | -3.81%         | 90.25%                   | -1.44% | 27.06%         | -28.49%       | 30.30%                        | -2.00%                          | -39.49%        |                    4.23232 |                   12.697   | 30.95%                    | 2026-02                        | -11.73%                  | 2026-08                     | 8.57%                 |         141 |
| F           | Leadership Rotation Overlay   | weekly      |                3 | -5.39%         | 90.25%                   | -2.04% | 27.06%         | -29.10%       | 36.36%                        | -1.98%                          | -42.16%        |                    4.07071 |                   12.2121  | 29.17%                    | 2026-02                        | -11.73%                  | 2026-08                     | 8.44%                 |         141 |

## Decision

- Did weekly rebalance improve excess return? Recent yes, historical no, so rejected. Historical excess CAGR delta vs baseline: -27.38%; recent excess delta: 2.64%.
- Did relative strength improve excess return? Recent yes, historical no, so rejected. Historical excess CAGR delta vs baseline: -25.52%; recent excess delta: 3.30%.
- Did benchmark-aware selection improve excess return? Recent yes, historical no, so rejected. Historical excess CAGR delta vs baseline: -28.05%; recent excess delta: 2.92%.
- Did any policy beat BIST100 robustly? No under the current acceptance filter.
- Next paper-trading candidate: none. No policy passed both historical and recent acceptance criteria.
- Current one-month fixed hold should be kept for tracking, while weekly/relative-strength variants remain research-only.

## Acceptance Rule

A policy is only eligible if it improves both historical walk-forward excess return and the recent 2026-06 counterfactual excess return. Policies that only fix June 2026 are rejected.
