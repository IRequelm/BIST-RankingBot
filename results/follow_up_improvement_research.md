# Follow-Up Improvement Research

This is research-only. Production follow-up tracking remains fixed and still reads reports/tracking_state.json.

## Policy Summary

| policy_id   | policy_name                   | frequency   |   portfolio_size | total_return   | benchmark_total_return   | cagr   | bist100_cagr   | excess_cagr   | monthly_win_rate_vs_bist100   | average_monthly_excess_return   | max_drawdown   |   average_monthly_turnover |   average_trades_per_month | transaction_cost_impact   | worst_underperformance_month   | worst_underperformance   | best_outperformance_month   | best_outperformance   |   intervals |
|:------------|:------------------------------|:------------|-----------------:|:---------------|:-------------------------|:-------|:---------------|:--------------|:------------------------------|:--------------------------------|:---------------|---------------------------:|---------------------------:|:--------------------------|:-------------------------------|:-------------------------|:----------------------------|:----------------------|------------:|
| A           | Current baseline monthly Top3 | monthly     |                3 | 81.73%         | 85.36%                   | 25.70% | 26.65%         | -0.96%        | 45.16%                        | 0.01%                           | -19.32%        |                    1.23656 |                    3.70968 | 14.18%                    | 2024-04                        | -10.59%                  | 2025-04                     | 15.27%                |          32 |
| B           | Weekly rebalance Top3         | weekly      |                3 | -5.91%         | 85.36%                   | -2.31% | 26.65%         | -28.96%       | 37.50%                        | -1.98%                          | -42.13%        |                    3.13542 |                    9.40625 | 21.00%                    | 2024-03                        | -12.42%                  | 2025-03                     | 12.41%                |         137 |
| C           | Weekly rebalance Top5         | weekly      |                5 | 12.43%         | 85.36%                   | 4.59%  | 26.65%         | -22.06%       | 40.62%                        | -1.48%                          | -36.45%        |                    2.68125 |                   13.4062  | 21.08%                    | 2024-08                        | -9.16%                   | 2026-03                     | 6.68%                 |         137 |
| D           | Relative Strength Top3        | weekly      |                3 | -2.06%         | 85.36%                   | -0.79% | 26.65%         | -27.44%       | 34.38%                        | -1.93%                          | -37.24%        |                    4.26042 |                   12.7812  | 30.63%                    | 2026-02                        | -14.58%                  | 2025-03                     | 6.67%                 |         137 |
| E           | Benchmark-aware Top3          | weekly      |                3 | -7.51%         | 85.36%                   | -2.94% | 26.65%         | -29.60%       | 31.25%                        | -2.12%                          | -38.70%        |                    4.28125 |                   12.8438  | 29.12%                    | 2026-02                        | -11.73%                  | 2025-03                     | 6.25%                 |         137 |
| F           | Leadership Rotation Overlay   | weekly      |                3 | -11.10%        | 85.36%                   | -4.40% | 26.65%         | -31.05%       | 37.50%                        | -2.17%                          | -42.16%        |                    4.13542 |                   12.4062  | 26.95%                    | 2026-02                        | -11.73%                  | 2024-04                     | 7.40%                 |         137 |

## Decision

- Did weekly rebalance improve excess return? Recent yes, historical no, so rejected. Historical excess CAGR delta vs baseline: -28.00%; recent excess delta: 7.51%.
- Did relative strength improve excess return? Recent yes, historical no, so rejected. Historical excess CAGR delta vs baseline: -26.49%; recent excess delta: 7.16%.
- Did benchmark-aware selection improve excess return? Recent yes, historical no, so rejected. Historical excess CAGR delta vs baseline: -28.64%; recent excess delta: 7.91%.
- Did any policy beat BIST100 robustly? No under the current acceptance filter.
- Next paper-trading candidate: none. No policy passed both historical and recent acceptance criteria.
- Current one-month fixed hold should be kept for tracking, while weekly/relative-strength variants remain research-only.

## Acceptance Rule

A policy is only eligible if it improves both historical walk-forward excess return and the recent 2026-06 counterfactual excess return. Policies that only fix June 2026 are rejected.
