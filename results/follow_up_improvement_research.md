# Follow-Up Improvement Research

This is research-only. Production follow-up tracking remains fixed and still reads reports/tracking_state.json.

## Policy Summary

| policy_id   | policy_name                   | frequency   |   portfolio_size | total_return   | benchmark_total_return   | cagr   | bist100_cagr   | excess_cagr   | monthly_win_rate_vs_bist100   | average_monthly_excess_return   | max_drawdown   |   average_monthly_turnover |   average_trades_per_month | transaction_cost_impact   | worst_underperformance_month   | worst_underperformance   | best_outperformance_month   | best_outperformance   |   intervals |
|:------------|:------------------------------|:------------|-----------------:|:---------------|:-------------------------|:-------|:---------------|:--------------|:------------------------------|:--------------------------------|:---------------|---------------------------:|---------------------------:|:--------------------------|:-------------------------------|:-------------------------|:----------------------------|:----------------------|------------:|
| A           | Current baseline monthly Top3 | monthly     |                3 | 68.07%         | 89.19%                   | 23.00% | 28.95%         | -5.94%        | 43.33%                        | -0.32%                          | -19.32%        |                    1.23333 |                     3.7    | 12.67%                    | 2024-04                        | -10.59%                  | 2025-04                     | 15.27%                |          31 |
| B           | Weekly rebalance Top3         | weekly      |                3 | -11.31%        | 89.19%                   | -4.67% | 28.95%         | -33.62%       | 35.48%                        | -2.32%                          | -42.13%        |                    3.12903 |                     9.3871 | 19.07%                    | 2024-03                        | -12.42%                  | 2025-03                     | 12.41%                |         131 |
| C           | Weekly rebalance Top5         | weekly      |                5 | 12.78%         | 89.19%                   | 4.91%  | 28.95%         | -24.04%       | 38.71%                        | -1.59%                          | -36.45%        |                    2.69032 |                    13.4516 | 20.50%                    | 2024-08                        | -9.16%                   | 2026-03                     | 6.68%                 |         131 |
| D           | Relative Strength Top3        | weekly      |                3 | -5.26%         | 89.19%                   | -2.13% | 28.95%         | -31.08%       | 32.26%                        | -2.17%                          | -35.17%        |                    4.26882 |                    12.8065 | 28.65%                    | 2026-02                        | -14.58%                  | 2025-03                     | 6.67%                 |         131 |
| E           | Benchmark-aware Top3          | weekly      |                3 | -11.18%        | 89.19%                   | -4.62% | 28.95%         | -33.57%       | 29.03%                        | -2.39%                          | -38.70%        |                    4.29032 |                    12.871  | 27.04%                    | 2026-02                        | -11.73%                  | 2025-03                     | 6.25%                 |         131 |
| F           | Leadership Rotation Overlay   | weekly      |                3 | -15.15%        | 89.19%                   | -6.34% | 28.95%         | -35.29%       | 35.48%                        | -2.46%                          | -42.16%        |                    4.16129 |                    12.4839 | 24.99%                    | 2026-02                        | -11.73%                  | 2024-04                     | 7.40%                 |         131 |

## Decision

- Did weekly rebalance improve excess return? No. Historical excess CAGR delta vs baseline: -27.68%; recent excess delta: -0.88%.
- Did relative strength improve excess return? Recent yes, historical no, so rejected. Historical excess CAGR delta vs baseline: -25.13%; recent excess delta: 1.33%.
- Did benchmark-aware selection improve excess return? Recent yes, historical no, so rejected. Historical excess CAGR delta vs baseline: -27.62%; recent excess delta: 1.33%.
- Did any policy beat BIST100 robustly? No under the current acceptance filter.
- Next paper-trading candidate: none. No policy passed both historical and recent acceptance criteria.
- Current one-month fixed hold should be kept for tracking, while weekly/relative-strength variants remain research-only.

## Acceptance Rule

A policy is only eligible if it improves both historical walk-forward excess return and the recent 2026-06 counterfactual excess return. Policies that only fix June 2026 are rejected.
