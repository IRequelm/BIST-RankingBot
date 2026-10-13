# Follow-Up Improvement Research

This is research-only. Production follow-up tracking remains fixed and still reads reports/tracking_state.json.

## Policy Summary

| policy_id   | policy_name                   | frequency   |   portfolio_size | total_return   | benchmark_total_return   | cagr   | bist100_cagr   | excess_cagr   | monthly_win_rate_vs_bist100   | average_monthly_excess_return   | max_drawdown   |   average_monthly_turnover |   average_trades_per_month | transaction_cost_impact   | worst_underperformance_month   | worst_underperformance   | best_outperformance_month   | best_outperformance   |   intervals |
|:------------|:------------------------------|:------------|-----------------:|:---------------|:-------------------------|:-------|:---------------|:--------------|:------------------------------|:--------------------------------|:---------------|---------------------------:|---------------------------:|:--------------------------|:-------------------------------|:-------------------------|:----------------------------|:----------------------|------------:|
| A           | Current baseline monthly Top3 | monthly     |                3 | 66.01%         | 59.37%                   | 20.03% | 18.28%         | 1.75%         | 45.45%                        | 0.19%                           | -19.32%        |                    1.24242 |                    3.72727 | 13.98%                    | 2024-04                        | -10.59%                  | 2025-04                     | 15.27%                |          34 |
| B           | Weekly rebalance Top3         | weekly      |                3 | -14.41%        | 59.37%                   | -5.45% | 18.28%         | -23.73%       | 41.18%                        | -1.71%                          | -42.13%        |                    3.04902 |                    9.14706 | 19.83%                    | 2024-03                        | -12.42%                  | 2025-03                     | 12.41%                |         145 |
| C           | Weekly rebalance Top5         | weekly      |                5 | 7.75%          | 59.37%                   | 2.72%  | 18.28%         | -15.56%       | 44.12%                        | -1.09%                          | -36.45%        |                    2.65294 |                   13.2647  | 21.34%                    | 2024-08                        | -9.16%                   | 2026-09                     | 6.85%                 |         145 |
| D           | Relative Strength Top3        | weekly      |                3 | -8.80%         | 59.37%                   | -3.26% | 18.28%         | -21.54%       | 35.29%                        | -1.58%                          | -38.81%        |                    4.22549 |                   12.6765  | 30.31%                    | 2026-02                        | -14.58%                  | 2026-08                     | 8.57%                 |         145 |
| E           | Benchmark-aware Top3          | weekly      |                3 | -14.88%        | 59.37%                   | -5.64% | 18.28%         | -23.91%       | 32.35%                        | -1.79%                          | -40.42%        |                    4.20588 |                   12.6176  | 28.17%                    | 2026-02                        | -11.73%                  | 2026-08                     | 8.57%                 |         145 |
| F           | Leadership Rotation Overlay   | weekly      |                3 | -16.17%        | 59.37%                   | -6.16% | 18.28%         | -24.44%       | 38.24%                        | -1.78%                          | -42.16%        |                    4.14706 |                   12.4412  | 27.35%                    | 2026-02                        | -11.73%                  | 2026-08                     | 8.44%                 |         145 |

## Decision

- Did weekly rebalance improve excess return? No. Historical excess CAGR delta vs baseline: -25.48%; recent excess delta: -1.43%.
- Did relative strength improve excess return? Recent yes, historical no, so rejected. Historical excess CAGR delta vs baseline: -23.29%; recent excess delta: 0.45%.
- Did benchmark-aware selection improve excess return? Recent yes, historical no, so rejected. Historical excess CAGR delta vs baseline: -25.67%; recent excess delta: 0.03%.
- Did any policy beat BIST100 robustly? No under the current acceptance filter.
- Next paper-trading candidate: none. No policy passed both historical and recent acceptance criteria.
- Current one-month fixed hold should be kept for tracking, while weekly/relative-strength variants remain research-only.

## Acceptance Rule

A policy is only eligible if it improves both historical walk-forward excess return and the recent 2026-06 counterfactual excess return. Policies that only fix June 2026 are rejected.
