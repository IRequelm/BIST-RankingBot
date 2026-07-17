# Follow-Up Improvement Research

This is research-only. Production follow-up tracking remains fixed and still reads reports/tracking_state.json.

## Policy Summary

| policy_id   | policy_name                   | frequency   |   portfolio_size | total_return   | benchmark_total_return   | cagr   | bist100_cagr   | excess_cagr   | monthly_win_rate_vs_bist100   | average_monthly_excess_return   | max_drawdown   |   average_monthly_turnover |   average_trades_per_month | transaction_cost_impact   | worst_underperformance_month   | worst_underperformance   | best_outperformance_month   | best_outperformance   |   intervals |
|:------------|:------------------------------|:------------|-----------------:|:---------------|:-------------------------|:-------|:---------------|:--------------|:------------------------------|:--------------------------------|:---------------|---------------------------:|---------------------------:|:--------------------------|:-------------------------------|:-------------------------|:----------------------------|:----------------------|------------:|
| A           | Current baseline monthly Top3 | monthly     |                3 | 67.58%         | 86.92%                   | 22.59% | 27.98%         | -5.40%        | 43.33%                        | -0.29%                          | -19.32%        |                    1.23333 |                    3.7     | 12.63%                    | 2024-04                        | -10.59%                  | 2025-04                     | 15.27%                |          31 |
| B           | Weekly rebalance Top3         | weekly      |                3 | -14.82%        | 86.92%                   | -6.13% | 27.98%         | -34.11%       | 35.48%                        | -2.40%                          | -42.13%        |                    3.19355 |                    9.58065 | 18.75%                    | 2024-03                        | -12.42%                  | 2025-03                     | 12.41%                |         133 |
| C           | Weekly rebalance Top5         | weekly      |                5 | 7.21%          | 86.92%                   | 2.78%  | 27.98%         | -25.20%       | 38.71%                        | -1.71%                          | -36.45%        |                    2.74194 |                   13.7097  | 19.90%                    | 2026-07                        | -9.26%                   | 2026-03                     | 6.68%                 |         133 |
| D           | Relative Strength Top3        | weekly      |                3 | -8.65%         | 86.92%                   | -3.51% | 27.98%         | -31.49%       | 32.26%                        | -2.25%                          | -36.49%        |                    4.33333 |                   13       | 28.10%                    | 2026-02                        | -14.58%                  | 2025-03                     | 6.67%                 |         133 |
| E           | Benchmark-aware Top3          | weekly      |                3 | -14.36%        | 86.92%                   | -5.93% | 27.98%         | -33.92%       | 29.03%                        | -2.47%                          | -38.70%        |                    4.35484 |                   13.0645  | 26.52%                    | 2026-02                        | -11.73%                  | 2025-03                     | 6.25%                 |         133 |
| F           | Leadership Rotation Overlay   | weekly      |                3 | -18.81%        | 86.92%                   | -7.89% | 27.98%         | -35.87%       | 35.48%                        | -2.56%                          | -42.16%        |                    4.22581 |                   12.6774  | 24.35%                    | 2026-02                        | -11.73%                  | 2024-04                     | 7.40%                 |         133 |

## Decision

- Did weekly rebalance improve excess return? No. Historical excess CAGR delta vs baseline: -28.72%; recent excess delta: -8.11%.
- Did relative strength improve excess return? No. Historical excess CAGR delta vs baseline: -26.09%; recent excess delta: -5.63%.
- Did benchmark-aware selection improve excess return? No. Historical excess CAGR delta vs baseline: -28.52%; recent excess delta: -5.63%.
- Did any policy beat BIST100 robustly? No under the current acceptance filter.
- Next paper-trading candidate: none. No policy passed both historical and recent acceptance criteria.
- Current one-month fixed hold should be kept for tracking, while weekly/relative-strength variants remain research-only.

## Acceptance Rule

A policy is only eligible if it improves both historical walk-forward excess return and the recent 2026-06 counterfactual excess return. Policies that only fix June 2026 are rejected.
