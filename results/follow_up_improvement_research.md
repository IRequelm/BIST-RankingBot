# Follow-Up Improvement Research

This is research-only. Production follow-up tracking remains fixed and still reads reports/tracking_state.json.

## Policy Summary

| policy_id   | policy_name                   | frequency   |   portfolio_size | total_return   | benchmark_total_return   | cagr   | bist100_cagr   | excess_cagr   | monthly_win_rate_vs_bist100   | average_monthly_excess_return   | max_drawdown   |   average_monthly_turnover |   average_trades_per_month | transaction_cost_impact   | worst_underperformance_month   | worst_underperformance   | best_outperformance_month   | best_outperformance   |   intervals |
|:------------|:------------------------------|:------------|-----------------:|:---------------|:-------------------------|:-------|:---------------|:--------------|:------------------------------|:--------------------------------|:---------------|---------------------------:|---------------------------:|:--------------------------|:-------------------------------|:-------------------------|:----------------------------|:----------------------|------------:|
| A           | Current baseline monthly Top3 | monthly     |                3 | 73.16%         | 86.12%                   | 24.41% | 28.04%         | -3.62%        | 43.33%                        | -0.17%                          | -19.32%        |                    1.23333 |                    3.7     | 13.03%                    | 2024-04                        | -10.59%                  | 2025-04                     | 15.27%                |          31 |
| B           | Weekly rebalance Top3         | weekly      |                3 | -11.56%        | 86.12%                   | -4.77% | 28.04%         | -32.81%       | 35.48%                        | -2.27%                          | -42.13%        |                    3.17204 |                    9.51613 | 19.31%                    | 2024-03                        | -12.42%                  | 2025-03                     | 12.41%                |         132 |
| C           | Weekly rebalance Top5         | weekly      |                5 | 12.19%         | 86.12%                   | 4.68%  | 28.04%         | -23.35%       | 38.71%                        | -1.56%                          | -36.45%        |                    2.71613 |                   13.5806  | 20.61%                    | 2024-08                        | -9.16%                   | 2026-03                     | 6.68%                 |         132 |
| D           | Relative Strength Top3        | weekly      |                3 | -4.70%         | 86.12%                   | -1.90% | 28.04%         | -29.93%       | 32.26%                        | -2.10%                          | -35.17%        |                    4.29032 |                   12.871   | 28.98%                    | 2026-02                        | -14.58%                  | 2025-03                     | 6.67%                 |         132 |
| E           | Benchmark-aware Top3          | weekly      |                3 | -10.66%        | 86.12%                   | -4.38% | 28.04%         | -32.42%       | 29.03%                        | -2.32%                          | -38.70%        |                    4.31183 |                   12.9355  | 27.35%                    | 2026-02                        | -11.73%                  | 2025-03                     | 6.25%                 |         132 |
| F           | Leadership Rotation Overlay   | weekly      |                3 | -15.71%        | 86.12%                   | -6.57% | 28.04%         | -34.61%       | 35.48%                        | -2.43%                          | -42.16%        |                    4.2043  |                   12.6129  | 25.12%                    | 2026-02                        | -11.73%                  | 2024-04                     | 7.40%                 |         132 |

## Decision

- Did weekly rebalance improve excess return? No. Historical excess CAGR delta vs baseline: -29.19%; recent excess delta: -2.80%.
- Did relative strength improve excess return? Recent yes, historical no, so rejected. Historical excess CAGR delta vs baseline: -26.31%; recent excess delta: 0.26%.
- Did benchmark-aware selection improve excess return? Recent yes, historical no, so rejected. Historical excess CAGR delta vs baseline: -28.80%; recent excess delta: 0.26%.
- Did any policy beat BIST100 robustly? No under the current acceptance filter.
- Next paper-trading candidate: none. No policy passed both historical and recent acceptance criteria.
- Current one-month fixed hold should be kept for tracking, while weekly/relative-strength variants remain research-only.

## Acceptance Rule

A policy is only eligible if it improves both historical walk-forward excess return and the recent 2026-06 counterfactual excess return. Policies that only fix June 2026 are rejected.
