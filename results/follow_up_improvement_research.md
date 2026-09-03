# Follow-Up Improvement Research

This is research-only. Production follow-up tracking remains fixed and still reads reports/tracking_state.json.

## Policy Summary

| policy_id   | policy_name                   | frequency   |   portfolio_size | total_return   | benchmark_total_return   | cagr   | bist100_cagr   | excess_cagr   | monthly_win_rate_vs_bist100   | average_monthly_excess_return   | max_drawdown   |   average_monthly_turnover |   average_trades_per_month | transaction_cost_impact   | worst_underperformance_month   | worst_underperformance   | best_outperformance_month   | best_outperformance   |   intervals |
|:------------|:------------------------------|:------------|-----------------:|:---------------|:-------------------------|:-------|:---------------|:--------------|:------------------------------|:--------------------------------|:---------------|---------------------------:|---------------------------:|:--------------------------|:-------------------------------|:-------------------------|:----------------------------|:----------------------|------------:|
| A           | Current baseline monthly Top3 | monthly     |                3 | 84.67%         | 84.29%                   | 25.86% | 25.77%         | 0.10%         | 46.88%                        | 0.09%                           | -19.32%        |                    1.21875 |                    3.65625 | 14.70%                    | 2024-04                        | -10.59%                  | 2025-04                     | 15.27%                |          33 |
| B           | Weekly rebalance Top3         | weekly      |                3 | -2.89%         | 84.29%                   | -1.09% | 25.77%         | -26.86%       | 39.39%                        | -1.80%                          | -42.13%        |                    3.06061 |                    9.18182 | 21.83%                    | 2024-03                        | -12.42%                  | 2025-03                     | 12.41%                |         140 |
| C           | Weekly rebalance Top5         | weekly      |                5 | 13.52%         | 84.29%                   | 4.87%  | 25.77%         | -20.90%       | 42.42%                        | -1.39%                          | -36.45%        |                    2.70909 |                   13.5455  | 22.25%                    | 2024-08                        | -9.16%                   | 2026-03                     | 6.68%                 |         140 |
| D           | Relative Strength Top3        | weekly      |                3 | 1.88%          | 84.29%                   | 0.70%  | 25.77%         | -25.06%       | 36.36%                        | -1.72%                          | -38.81%        |                    4.17172 |                   12.5152  | 32.21%                    | 2026-02                        | -14.58%                  | 2026-08                     | 8.57%                 |         140 |
| E           | Benchmark-aware Top3          | weekly      |                3 | -4.66%         | 84.29%                   | -1.77% | 25.77%         | -27.54%       | 33.33%                        | -1.93%                          | -39.49%        |                    4.21212 |                   12.6364  | 30.51%                    | 2026-02                        | -11.73%                  | 2026-08                     | 8.57%                 |         140 |
| F           | Leadership Rotation Overlay   | weekly      |                3 | -6.24%         | 84.29%                   | -2.39% | 25.77%         | -28.15%       | 39.39%                        | -1.91%                          | -42.16%        |                    4.05051 |                   12.1515  | 28.75%                    | 2026-02                        | -11.73%                  | 2026-08                     | 8.44%                 |         140 |

## Decision

- Did weekly rebalance improve excess return? Recent yes, historical no, so rejected. Historical excess CAGR delta vs baseline: -26.96%; recent excess delta: 9.16%.
- Did relative strength improve excess return? Recent yes, historical no, so rejected. Historical excess CAGR delta vs baseline: -25.16%; recent excess delta: 9.62%.
- Did benchmark-aware selection improve excess return? Recent yes, historical no, so rejected. Historical excess CAGR delta vs baseline: -27.64%; recent excess delta: 9.43%.
- Did any policy beat BIST100 robustly? No under the current acceptance filter.
- Next paper-trading candidate: none. No policy passed both historical and recent acceptance criteria.
- Current one-month fixed hold should be kept for tracking, while weekly/relative-strength variants remain research-only.

## Acceptance Rule

A policy is only eligible if it improves both historical walk-forward excess return and the recent 2026-06 counterfactual excess return. Policies that only fix June 2026 are rejected.
