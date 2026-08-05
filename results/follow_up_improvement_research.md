# Follow-Up Improvement Research

This is research-only. Production follow-up tracking remains fixed and still reads reports/tracking_state.json.

## Policy Summary

| policy_id   | policy_name                   | frequency   |   portfolio_size | total_return   | benchmark_total_return   | cagr   | bist100_cagr   | excess_cagr   | monthly_win_rate_vs_bist100   | average_monthly_excess_return   | max_drawdown   |   average_monthly_turnover |   average_trades_per_month | transaction_cost_impact   | worst_underperformance_month   | worst_underperformance   | best_outperformance_month   | best_outperformance   |   intervals |
|:------------|:------------------------------|:------------|-----------------:|:---------------|:-------------------------|:-------|:---------------|:--------------|:------------------------------|:--------------------------------|:---------------|---------------------------:|---------------------------:|:--------------------------|:-------------------------------|:-------------------------|:----------------------------|:----------------------|------------:|
| A           | Current baseline monthly Top3 | monthly     |                3 | 62.65%         | 79.53%                   | 20.68% | 25.38%         | -4.70%        | 41.94%                        | -0.25%                          | -19.32%        |                    1.21505 |                    3.64516 | 12.51%                    | 2024-04                        | -10.59%                  | 2025-04                     | 15.27%                |          32 |
| B           | Weekly rebalance Top3         | weekly      |                3 | -13.86%        | 79.53%                   | -5.60% | 25.38%         | -30.98%       | 34.38%                        | -2.17%                          | -42.13%        |                    3.09375 |                    9.28125 | 18.95%                    | 2024-03                        | -12.42%                  | 2025-03                     | 12.41%                |         136 |
| C           | Weekly rebalance Top5         | weekly      |                5 | 3.87%          | 79.53%                   | 1.48%  | 25.38%         | -23.90%       | 37.50%                        | -1.63%                          | -36.45%        |                    2.70625 |                   13.5312  | 19.68%                    | 2024-08                        | -9.16%                   | 2026-03                     | 6.68%                 |         136 |
| D           | Relative Strength Top3        | weekly      |                3 | -12.28%        | 79.53%                   | -4.94% | 25.38%         | -30.32%       | 31.25%                        | -2.17%                          | -38.89%        |                    4.26042 |                   12.7812  | 27.44%                    | 2026-02                        | -14.58%                  | 2025-03                     | 6.67%                 |         136 |
| E           | Benchmark-aware Top3          | weekly      |                3 | -17.77%        | 79.53%                   | -7.28% | 25.38%         | -32.66%       | 28.12%                        | -2.39%                          | -39.57%        |                    4.28125 |                   12.8438  | 25.90%                    | 2026-02                        | -11.73%                  | 2025-03                     | 6.25%                 |         136 |
| F           | Leadership Rotation Overlay   | weekly      |                3 | -19.02%        | 79.53%                   | -7.83% | 25.38%         | -33.21%       | 34.38%                        | -2.37%                          | -42.16%        |                    4.13542 |                   12.4062  | 24.56%                    | 2026-02                        | -11.73%                  | 2024-04                     | 7.40%                 |         136 |

## Decision

- Did weekly rebalance improve excess return? No. Historical excess CAGR delta vs baseline: -26.29%; recent excess delta: -4.52%.
- Did relative strength improve excess return? No. Historical excess CAGR delta vs baseline: -25.62%; recent excess delta: -6.88%.
- Did benchmark-aware selection improve excess return? No. Historical excess CAGR delta vs baseline: -27.97%; recent excess delta: -6.88%.
- Did any policy beat BIST100 robustly? No under the current acceptance filter.
- Next paper-trading candidate: none. No policy passed both historical and recent acceptance criteria.
- Current one-month fixed hold should be kept for tracking, while weekly/relative-strength variants remain research-only.

## Acceptance Rule

A policy is only eligible if it improves both historical walk-forward excess return and the recent 2026-06 counterfactual excess return. Policies that only fix June 2026 are rejected.
