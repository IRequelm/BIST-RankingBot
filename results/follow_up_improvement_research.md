# Follow-Up Improvement Research

This is research-only. Production follow-up tracking remains fixed and still reads reports/tracking_state.json.

## Policy Summary

| policy_id   | policy_name                   | frequency   |   portfolio_size | total_return   | benchmark_total_return   | cagr   | bist100_cagr   | excess_cagr   | monthly_win_rate_vs_bist100   | average_monthly_excess_return   | max_drawdown   |   average_monthly_turnover |   average_trades_per_month | transaction_cost_impact   | worst_underperformance_month   | worst_underperformance   | best_outperformance_month   | best_outperformance   |   intervals |
|:------------|:------------------------------|:------------|-----------------:|:---------------|:-------------------------|:-------|:---------------|:--------------|:------------------------------|:--------------------------------|:---------------|---------------------------:|---------------------------:|:--------------------------|:-------------------------------|:-------------------------|:----------------------------|:----------------------|------------:|
| A           | Current baseline monthly Top3 | monthly     |                3 | 64.73%         | 79.73%                   | 21.25% | 25.40%         | -4.15%        | 45.16%                        | -0.21%                          | -19.32%        |                    1.21505 |                    3.64516 | 12.66%                    | 2024-04                        | -10.59%                  | 2025-04                     | 15.27%                |          32 |
| B           | Weekly rebalance Top3         | weekly      |                3 | -12.76%        | 79.73%                   | -5.13% | 25.40%         | -30.54%       | 37.50%                        | -2.13%                          | -42.13%        |                    3.09375 |                    9.28125 | 19.19%                    | 2024-03                        | -12.42%                  | 2025-03                     | 12.41%                |         136 |
| C           | Weekly rebalance Top5         | weekly      |                5 | 5.51%          | 79.73%                   | 2.09%  | 25.40%         | -23.31%       | 37.50%                        | -1.58%                          | -36.45%        |                    2.70625 |                   13.5312  | 19.98%                    | 2024-08                        | -9.16%                   | 2026-03                     | 6.68%                 |         136 |
| D           | Relative Strength Top3        | weekly      |                3 | -11.46%        | 79.73%                   | -4.59% | 25.40%         | -29.99%       | 31.25%                        | -2.15%                          | -38.81%        |                    4.26042 |                   12.7812  | 27.70%                    | 2026-02                        | -14.58%                  | 2025-03                     | 6.67%                 |         136 |
| E           | Benchmark-aware Top3          | weekly      |                3 | -16.99%        | 79.73%                   | -6.94% | 25.40%         | -32.34%       | 28.12%                        | -2.36%                          | -39.49%        |                    4.28125 |                   12.8438  | 26.14%                    | 2026-02                        | -11.73%                  | 2025-03                     | 6.25%                 |         136 |
| F           | Leadership Rotation Overlay   | weekly      |                3 | -18.26%        | 79.73%                   | -7.49% | 25.40%         | -32.89%       | 34.38%                        | -2.34%                          | -42.16%        |                    4.13542 |                   12.4062  | 24.79%                    | 2026-02                        | -11.73%                  | 2024-04                     | 7.40%                 |         136 |

## Decision

- Did weekly rebalance improve excess return? No. Historical excess CAGR delta vs baseline: -26.39%; recent excess delta: -5.01%.
- Did relative strength improve excess return? No. Historical excess CAGR delta vs baseline: -25.84%; recent excess delta: -7.71%.
- Did benchmark-aware selection improve excess return? No. Historical excess CAGR delta vs baseline: -28.19%; recent excess delta: -7.71%.
- Did any policy beat BIST100 robustly? No under the current acceptance filter.
- Next paper-trading candidate: none. No policy passed both historical and recent acceptance criteria.
- Current one-month fixed hold should be kept for tracking, while weekly/relative-strength variants remain research-only.

## Acceptance Rule

A policy is only eligible if it improves both historical walk-forward excess return and the recent 2026-06 counterfactual excess return. Policies that only fix June 2026 are rejected.
