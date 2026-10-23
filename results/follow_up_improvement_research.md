# Follow-Up Improvement Research

This is research-only. Production follow-up tracking remains fixed and still reads reports/tracking_state.json.

## Policy Summary

| policy_id   | policy_name                   | frequency   |   portfolio_size | total_return   | benchmark_total_return   | cagr   | bist100_cagr   | excess_cagr   | monthly_win_rate_vs_bist100   | average_monthly_excess_return   | max_drawdown   |   average_monthly_turnover |   average_trades_per_month | transaction_cost_impact   | worst_underperformance_month   | worst_underperformance   | best_outperformance_month   | best_outperformance   |   intervals |
|:------------|:------------------------------|:------------|-----------------:|:---------------|:-------------------------|:-------|:---------------|:--------------|:------------------------------|:--------------------------------|:---------------|---------------------------:|---------------------------:|:--------------------------|:-------------------------------|:-------------------------|:----------------------------|:----------------------|------------:|
| A           | Current baseline monthly Top3 | monthly     |                3 | 58.50%         | 47.17%                   | 17.86% | 14.78%         | 3.08%         | 45.45%                        | 0.25%                           | -19.32%        |                    1.24242 |                    3.72727 | 13.36%                    | 2024-04                        | -10.59%                  | 2025-04                     | 15.27%                |          34 |
| B           | Weekly rebalance Top3         | weekly      |                3 | -18.32%        | 47.17%                   | -6.96% | 14.78%         | -21.74%       | 41.18%                        | -1.62%                          | -42.13%        |                    3.08824 |                    9.26471 | 19.20%                    | 2024-03                        | -12.42%                  | 2025-03                     | 12.41%                |         147 |
| C           | Weekly rebalance Top5         | weekly      |                5 | 3.57%          | 47.17%                   | 1.26%  | 14.78%         | -13.52%       | 44.12%                        | -0.99%                          | -36.45%        |                    2.68824 |                   13.4412  | 20.81%                    | 2024-08                        | -9.16%                   | 2026-09                     | 6.85%                 |         147 |
| D           | Relative Strength Top3        | weekly      |                3 | -9.75%         | 47.17%                   | -3.59% | 14.78%         | -18.37%       | 38.24%                        | -1.39%                          | -38.81%        |                    4.30392 |                   12.9118  | 30.64%                    | 2026-02                        | -14.58%                  | 2026-08                     | 8.57%                 |         147 |
| E           | Benchmark-aware Top3          | weekly      |                3 | -15.76%        | 47.17%                   | -5.93% | 14.78%         | -20.71%       | 35.29%                        | -1.60%                          | -40.42%        |                    4.28431 |                   12.8529  | 28.49%                    | 2026-02                        | -11.73%                  | 2026-08                     | 8.57%                 |         147 |
| F           | Leadership Rotation Overlay   | weekly      |                3 | -17.82%        | 47.17%                   | -6.76% | 14.78%         | -21.54%       | 38.24%                        | -1.61%                          | -42.16%        |                    4.22549 |                   12.6765  | 27.40%                    | 2026-02                        | -11.73%                  | 2026-08                     | 8.44%                 |         147 |

## Decision

- Did weekly rebalance improve excess return? No. Historical excess CAGR delta vs baseline: -24.82%; recent excess delta: -1.45%.
- Did relative strength improve excess return? Recent yes, historical no, so rejected. Historical excess CAGR delta vs baseline: -21.45%; recent excess delta: 3.71%.
- Did benchmark-aware selection improve excess return? Recent yes, historical no, so rejected. Historical excess CAGR delta vs baseline: -23.79%; recent excess delta: 3.30%.
- Did any policy beat BIST100 robustly? No under the current acceptance filter.
- Next paper-trading candidate: none. No policy passed both historical and recent acceptance criteria.
- Current one-month fixed hold should be kept for tracking, while weekly/relative-strength variants remain research-only.

## Acceptance Rule

A policy is only eligible if it improves both historical walk-forward excess return and the recent 2026-06 counterfactual excess return. Policies that only fix June 2026 are rejected.
