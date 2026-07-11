# Follow-Up Improvement Research

This is research-only. Production follow-up tracking remains fixed and still reads reports/tracking_state.json.

## Policy Summary

| policy_id   | policy_name                   | frequency   |   portfolio_size | total_return   | benchmark_total_return   | cagr   | bist100_cagr   | excess_cagr   | monthly_win_rate_vs_bist100   | average_monthly_excess_return   | max_drawdown   |   average_monthly_turnover |   average_trades_per_month | transaction_cost_impact   | worst_underperformance_month   | worst_underperformance   | best_outperformance_month   | best_outperformance   |   intervals |
|:------------|:------------------------------|:------------|-----------------:|:---------------|:-------------------------|:-------|:---------------|:--------------|:------------------------------|:--------------------------------|:---------------|---------------------------:|---------------------------:|:--------------------------|:-------------------------------|:-------------------------|:----------------------------|:----------------------|------------:|
| A           | Current baseline monthly Top3 | monthly     |                3 | 67.46%         | 87.84%                   | 22.71% | 28.44%         | -5.72%        | 43.33%                        | -0.31%                          | -19.32%        |                    1.23333 |                    3.7     | 12.62%                    | 2024-04                        | -10.59%                  | 2025-04                     | 15.27%                |          31 |
| B           | Weekly rebalance Top3         | weekly      |                3 | -14.98%        | 87.84%                   | -6.24% | 28.44%         | -34.68%       | 35.48%                        | -2.42%                          | -42.13%        |                    3.17204 |                    9.51613 | 18.58%                    | 2024-03                        | -12.42%                  | 2025-03                     | 12.41%                |         132 |
| C           | Weekly rebalance Top5         | weekly      |                5 | 8.26%          | 87.84%                   | 3.20%  | 28.44%         | -25.24%       | 38.71%                        | -1.69%                          | -36.45%        |                    2.71613 |                   13.5806  | 19.89%                    | 2024-08                        | -9.16%                   | 2026-03                     | 6.68%                 |         132 |
| D           | Relative Strength Top3        | weekly      |                3 | -8.52%         | 87.84%                   | -3.47% | 28.44%         | -31.91%       | 32.26%                        | -2.26%                          | -36.27%        |                    4.29032 |                   12.871   | 27.82%                    | 2026-02                        | -14.58%                  | 2025-03                     | 6.67%                 |         132 |
| E           | Benchmark-aware Top3          | weekly      |                3 | -14.24%        | 87.84%                   | -5.92% | 28.44%         | -34.35%       | 29.03%                        | -2.48%                          | -38.70%        |                    4.31183 |                   12.9355  | 26.26%                    | 2026-02                        | -11.73%                  | 2025-03                     | 6.25%                 |         132 |
| F           | Leadership Rotation Overlay   | weekly      |                3 | -18.96%        | 87.84%                   | -8.01% | 28.44%         | -36.45%       | 35.48%                        | -2.58%                          | -42.16%        |                    4.2043  |                   12.6129  | 24.16%                    | 2026-02                        | -11.73%                  | 2024-04                     | 7.40%                 |         132 |

## Decision

- Did weekly rebalance improve excess return? No. Historical excess CAGR delta vs baseline: -28.95%; recent excess delta: -4.01%.
- Did relative strength improve excess return? No. Historical excess CAGR delta vs baseline: -26.19%; recent excess delta: -1.21%.
- Did benchmark-aware selection improve excess return? No. Historical excess CAGR delta vs baseline: -28.63%; recent excess delta: -1.21%.
- Did any policy beat BIST100 robustly? No under the current acceptance filter.
- Next paper-trading candidate: none. No policy passed both historical and recent acceptance criteria.
- Current one-month fixed hold should be kept for tracking, while weekly/relative-strength variants remain research-only.

## Acceptance Rule

A policy is only eligible if it improves both historical walk-forward excess return and the recent 2026-06 counterfactual excess return. Policies that only fix June 2026 are rejected.
