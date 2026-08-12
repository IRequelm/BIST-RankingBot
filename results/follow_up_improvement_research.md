# Follow-Up Improvement Research

This is research-only. Production follow-up tracking remains fixed and still reads reports/tracking_state.json.

## Policy Summary

| policy_id   | policy_name                   | frequency   |   portfolio_size | total_return   | benchmark_total_return   | cagr   | bist100_cagr   | excess_cagr   | monthly_win_rate_vs_bist100   | average_monthly_excess_return   | max_drawdown   |   average_monthly_turnover |   average_trades_per_month | transaction_cost_impact   | worst_underperformance_month   | worst_underperformance   | best_outperformance_month   | best_outperformance   |   intervals |
|:------------|:------------------------------|:------------|-----------------:|:---------------|:-------------------------|:-------|:---------------|:--------------|:------------------------------|:--------------------------------|:---------------|---------------------------:|---------------------------:|:--------------------------|:-------------------------------|:-------------------------|:----------------------------|:----------------------|------------:|
| A           | Current baseline monthly Top3 | monthly     |                3 | 70.25%         | 79.75%                   | 22.65% | 25.23%         | -2.58%        | 45.16%                        | -0.11%                          | -19.32%        |                    1.21505 |                    3.64516 | 13.08%                    | 2024-04                        | -10.59%                  | 2025-04                     | 15.27%                |          32 |
| B           | Weekly rebalance Top3         | weekly      |                3 | -10.04%        | 79.75%                   | -3.98% | 25.23%         | -29.21%       | 37.50%                        | -2.04%                          | -42.13%        |                    3.11458 |                    9.34375 | 19.94%                    | 2024-03                        | -12.42%                  | 2025-03                     | 12.41%                |         137 |
| C           | Weekly rebalance Top5         | weekly      |                5 | 8.71%          | 79.75%                   | 3.26%  | 25.23%         | -21.97%       | 40.62%                        | -1.49%                          | -36.45%        |                    2.70625 |                   13.5312  | 20.59%                    | 2024-08                        | -9.16%                   | 2026-03                     | 6.68%                 |         137 |
| D           | Relative Strength Top3        | weekly      |                3 | -7.65%         | 79.75%                   | -3.01% | 25.23%         | -28.24%       | 34.38%                        | -2.02%                          | -38.74%        |                    4.30208 |                   12.9062  | 29.20%                    | 2026-02                        | -14.58%                  | 2025-03                     | 6.67%                 |         137 |
| E           | Benchmark-aware Top3          | weekly      |                3 | -13.42%        | 79.75%                   | -5.38% | 25.23%         | -30.61%       | 31.25%                        | -2.23%                          | -39.42%        |                    4.32292 |                   12.9688  | 27.56%                    | 2026-02                        | -11.73%                  | 2025-03                     | 6.25%                 |         137 |
| F           | Leadership Rotation Overlay   | weekly      |                3 | -13.02%        | 79.75%                   | -5.21% | 25.23%         | -30.44%       | 37.50%                        | -2.14%                          | -42.16%        |                    4.13542 |                   12.4062  | 26.37%                    | 2026-02                        | -11.73%                  | 2024-04                     | 7.40%                 |         137 |

## Decision

- Did weekly rebalance improve excess return? Recent yes, historical no, so rejected. Historical excess CAGR delta vs baseline: -26.63%; recent excess delta: 2.85%.
- Did relative strength improve excess return? Recent yes, historical no, so rejected. Historical excess CAGR delta vs baseline: -25.66%; recent excess delta: 1.16%.
- Did benchmark-aware selection improve excess return? Recent yes, historical no, so rejected. Historical excess CAGR delta vs baseline: -28.03%; recent excess delta: 1.16%.
- Did any policy beat BIST100 robustly? No under the current acceptance filter.
- Next paper-trading candidate: none. No policy passed both historical and recent acceptance criteria.
- Current one-month fixed hold should be kept for tracking, while weekly/relative-strength variants remain research-only.

## Acceptance Rule

A policy is only eligible if it improves both historical walk-forward excess return and the recent 2026-06 counterfactual excess return. Policies that only fix June 2026 are rejected.
