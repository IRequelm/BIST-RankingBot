# Follow-Up Improvement Research

This is research-only. Production follow-up tracking remains fixed and still reads reports/tracking_state.json.

## Policy Summary

| policy_id   | policy_name                   | frequency   |   portfolio_size | total_return   | benchmark_total_return   | cagr   | bist100_cagr   | excess_cagr   | monthly_win_rate_vs_bist100   | average_monthly_excess_return   | max_drawdown   |   average_monthly_turnover |   average_trades_per_month | transaction_cost_impact   | worst_underperformance_month   | worst_underperformance   | best_outperformance_month   | best_outperformance   |   intervals |
|:------------|:------------------------------|:------------|-----------------:|:---------------|:-------------------------|:-------|:---------------|:--------------|:------------------------------|:--------------------------------|:---------------|---------------------------:|---------------------------:|:--------------------------|:-------------------------------|:-------------------------|:----------------------------|:----------------------|------------:|
| A           | Current baseline monthly Top3 | monthly     |                3 | 67.94%         | 81.15%                   | 22.03% | 25.63%         | -3.60%        | 45.16%                        | -0.18%                          | -19.32%        |                    1.21505 |                    3.64516 | 12.91%                    | 2024-04                        | -10.59%                  | 2025-04                     | 15.27%                |          32 |
| B           | Weekly rebalance Top3         | weekly      |                3 | -11.06%        | 81.15%                   | -4.40% | 25.63%         | -30.03%       | 37.50%                        | -2.10%                          | -42.13%        |                    3.09375 |                    9.28125 | 19.57%                    | 2024-03                        | -12.42%                  | 2025-03                     | 12.41%                |         136 |
| C           | Weekly rebalance Top5         | weekly      |                5 | 6.20%          | 81.15%                   | 2.34%  | 25.63%         | -23.30%       | 37.50%                        | -1.59%                          | -36.45%        |                    2.70625 |                   13.5312  | 20.11%                    | 2024-08                        | -9.16%                   | 2026-03                     | 6.68%                 |         136 |
| D           | Relative Strength Top3        | weekly      |                3 | -8.16%         | 81.15%                   | -3.22% | 25.63%         | -28.85%       | 34.38%                        | -2.06%                          | -38.81%        |                    4.26042 |                   12.7812  | 28.72%                    | 2026-02                        | -14.58%                  | 2025-03                     | 6.67%                 |         136 |
| E           | Benchmark-aware Top3          | weekly      |                3 | -13.91%        | 81.15%                   | -5.59% | 25.63%         | -31.22%       | 31.25%                        | -2.27%                          | -39.49%        |                    4.28125 |                   12.8438  | 27.11%                    | 2026-02                        | -11.73%                  | 2025-03                     | 6.25%                 |         136 |
| F           | Leadership Rotation Overlay   | weekly      |                3 | -15.22%        | 81.15%                   | -6.15% | 25.63%         | -31.78%       | 37.50%                        | -2.25%                          | -42.16%        |                    4.13542 |                   12.4062  | 25.71%                    | 2026-02                        | -11.73%                  | 2024-04                     | 7.40%                 |         136 |

## Decision

- Did weekly rebalance improve excess return? Recent yes, historical no, so rejected. Historical excess CAGR delta vs baseline: -26.43%; recent excess delta: 0.20%.
- Did relative strength improve excess return? No. Historical excess CAGR delta vs baseline: -25.25%; recent excess delta: -0.91%.
- Did benchmark-aware selection improve excess return? No. Historical excess CAGR delta vs baseline: -27.62%; recent excess delta: -0.91%.
- Did any policy beat BIST100 robustly? No under the current acceptance filter.
- Next paper-trading candidate: none. No policy passed both historical and recent acceptance criteria.
- Current one-month fixed hold should be kept for tracking, while weekly/relative-strength variants remain research-only.

## Acceptance Rule

A policy is only eligible if it improves both historical walk-forward excess return and the recent 2026-06 counterfactual excess return. Policies that only fix June 2026 are rejected.
