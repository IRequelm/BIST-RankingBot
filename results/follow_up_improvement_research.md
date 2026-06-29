# Follow-Up Improvement Research

This is research-only. Production follow-up tracking remains fixed and still reads reports/tracking_state.json.

## Policy Summary

| policy_id   | policy_name                   | frequency   |   portfolio_size | total_return   | benchmark_total_return   | cagr   | bist100_cagr   | excess_cagr   | monthly_win_rate_vs_bist100   | average_monthly_excess_return   | max_drawdown   |   average_monthly_turnover |   average_trades_per_month | transaction_cost_impact   | worst_underperformance_month   | worst_underperformance   | best_outperformance_month   | best_outperformance   |   intervals |
|:------------|:------------------------------|:------------|-----------------:|:---------------|:-------------------------|:-------|:---------------|:--------------|:------------------------------|:--------------------------------|:---------------|---------------------------:|---------------------------:|:--------------------------|:-------------------------------|:-------------------------|:----------------------------|:----------------------|------------:|
| A           | Current baseline monthly Top3 | monthly     |                3 | 76.35%         | 87.22%                   | 25.70% | 28.76%         | -3.07%        | 44.83%                        | -0.13%                          | -19.32%        |                    1.22989 |                    3.68966 | 12.76%                    | 2024-04                        | -10.59%                  | 2025-04                     | 15.27%                |          30 |
| B           | Weekly rebalance Top3         | weekly      |                3 | -6.77%         | 87.22%                   | -2.78% | 28.76%         | -31.55%       | 36.67%                        | -2.20%                          | -42.13%        |                    3.21111 |                    9.63333 | 19.90%                    | 2024-03                        | -12.42%                  | 2025-03                     | 12.41%                |         130 |
| C           | Weekly rebalance Top5         | weekly      |                5 | 19.23%         | 87.22%                   | 7.35%  | 28.76%         | -21.42%       | 40.00%                        | -1.43%                          | -36.45%        |                    2.76667 |                   13.8333  | 21.55%                    | 2024-08                        | -9.16%                   | 2026-03                     | 6.68%                 |         130 |
| D           | Relative Strength Top3        | weekly      |                3 | -1.51%         | 87.22%                   | -0.61% | 28.76%         | -29.37%       | 33.33%                        | -2.08%                          | -35.17%        |                    4.36667 |                   13.1     | 29.43%                    | 2026-02                        | -14.58%                  | 2025-03                     | 6.67%                 |         130 |
| E           | Benchmark-aware Top3          | weekly      |                3 | -7.66%         | 87.22%                   | -3.16% | 28.76%         | -31.93%       | 30.00%                        | -2.31%                          | -38.70%        |                    4.38889 |                   13.1667  | 27.78%                    | 2026-02                        | -11.73%                  | 2025-03                     | 6.25%                 |         130 |
| F           | Leadership Rotation Overlay   | weekly      |                3 | -12.01%        | 87.22%                   | -5.03% | 28.76%         | -33.79%       | 36.67%                        | -2.39%                          | -42.16%        |                    4.27778 |                   12.8333  | 25.76%                    | 2026-02                        | -11.73%                  | 2024-04                     | 7.40%                 |         130 |

## Decision

- Did weekly rebalance improve excess return? Recent yes, historical no, so rejected. Historical excess CAGR delta vs baseline: -28.48%; recent excess delta: 0.12%.
- Did relative strength improve excess return? Recent yes, historical no, so rejected. Historical excess CAGR delta vs baseline: -26.31%; recent excess delta: 1.28%.
- Did benchmark-aware selection improve excess return? Recent yes, historical no, so rejected. Historical excess CAGR delta vs baseline: -28.86%; recent excess delta: 1.28%.
- Did any policy beat BIST100 robustly? No under the current acceptance filter.
- Next paper-trading candidate: none. No policy passed both historical and recent acceptance criteria.
- Current one-month fixed hold should be kept for tracking, while weekly/relative-strength variants remain research-only.

## Acceptance Rule

A policy is only eligible if it improves both historical walk-forward excess return and the recent 2026-06 counterfactual excess return. Policies that only fix June 2026 are rejected.
