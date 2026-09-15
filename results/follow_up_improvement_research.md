# Follow-Up Improvement Research

This is research-only. Production follow-up tracking remains fixed and still reads reports/tracking_state.json.

## Policy Summary

| policy_id   | policy_name                   | frequency   |   portfolio_size | total_return   | benchmark_total_return   | cagr   | bist100_cagr   | excess_cagr   | monthly_win_rate_vs_bist100   | average_monthly_excess_return   | max_drawdown   |   average_monthly_turnover |   average_trades_per_month | transaction_cost_impact   | worst_underperformance_month   | worst_underperformance   | best_outperformance_month   | best_outperformance   |   intervals |
|:------------|:------------------------------|:------------|-----------------:|:---------------|:-------------------------|:-------|:---------------|:--------------|:------------------------------|:--------------------------------|:---------------|---------------------------:|---------------------------:|:--------------------------|:-------------------------------|:-------------------------|:----------------------------|:----------------------|------------:|
| A           | Current baseline monthly Top3 | monthly     |                3 | 90.81%         | 86.72%                   | 27.04% | 26.02%         | 1.02%         | 46.88%                        | 0.17%                           | -19.32%        |                    1.21875 |                    3.65625 | 15.17%                    | 2024-04                        | -10.59%                  | 2025-04                     | 15.27%                |          33 |
| B           | Weekly rebalance Top3         | weekly      |                3 | 0.74%          | 86.72%                   | 0.27%  | 26.02%         | -25.75%       | 39.39%                        | -1.73%                          | -42.13%        |                    3.08081 |                    9.24242 | 22.80%                    | 2024-03                        | -12.42%                  | 2025-03                     | 12.41%                |         141 |
| C           | Weekly rebalance Top5         | weekly      |                5 | 18.24%         | 86.72%                   | 6.40%  | 26.02%         | -19.62%       | 42.42%                        | -1.30%                          | -36.45%        |                    2.70909 |                   13.5455  | 23.17%                    | 2024-08                        | -9.16%                   | 2026-03                     | 6.68%                 |         141 |
| D           | Relative Strength Top3        | weekly      |                3 | 5.87%          | 86.72%                   | 2.14%  | 26.02%         | -23.89%       | 36.36%                        | -1.64%                          | -38.81%        |                    4.19192 |                   12.5758  | 33.65%                    | 2026-02                        | -14.58%                  | 2026-08                     | 8.57%                 |         141 |
| E           | Benchmark-aware Top3          | weekly      |                3 | -1.10%         | 86.72%                   | -0.41% | 26.02%         | -26.43%       | 33.33%                        | -1.85%                          | -39.49%        |                    4.23232 |                   12.697   | 31.82%                    | 2026-02                        | -11.73%                  | 2026-08                     | 8.57%                 |         141 |
| F           | Leadership Rotation Overlay   | weekly      |                3 | -2.73%         | 86.72%                   | -1.02% | 26.02%         | -27.04%       | 39.39%                        | -1.84%                          | -42.16%        |                    4.07071 |                   12.2121  | 29.98%                    | 2026-02                        | -11.73%                  | 2026-08                     | 8.44%                 |         141 |

## Decision

- Did weekly rebalance improve excess return? Recent yes, historical no, so rejected. Historical excess CAGR delta vs baseline: -26.77%; recent excess delta: 5.43%.
- Did relative strength improve excess return? Recent yes, historical no, so rejected. Historical excess CAGR delta vs baseline: -24.91%; recent excess delta: 6.10%.
- Did benchmark-aware selection improve excess return? Recent yes, historical no, so rejected. Historical excess CAGR delta vs baseline: -27.45%; recent excess delta: 5.71%.
- Did any policy beat BIST100 robustly? No under the current acceptance filter.
- Next paper-trading candidate: none. No policy passed both historical and recent acceptance criteria.
- Current one-month fixed hold should be kept for tracking, while weekly/relative-strength variants remain research-only.

## Acceptance Rule

A policy is only eligible if it improves both historical walk-forward excess return and the recent 2026-06 counterfactual excess return. Policies that only fix June 2026 are rejected.
