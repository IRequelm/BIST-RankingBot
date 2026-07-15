# Follow-Up Improvement Research

This is research-only. Production follow-up tracking remains fixed and still reads reports/tracking_state.json.

## Policy Summary

| policy_id   | policy_name                   | frequency   |   portfolio_size | total_return   | benchmark_total_return   | cagr   | bist100_cagr   | excess_cagr   | monthly_win_rate_vs_bist100   | average_monthly_excess_return   | max_drawdown   |   average_monthly_turnover |   average_trades_per_month | transaction_cost_impact   | worst_underperformance_month   | worst_underperformance   | best_outperformance_month   | best_outperformance   |   intervals |
|:------------|:------------------------------|:------------|-----------------:|:---------------|:-------------------------|:-------|:---------------|:--------------|:------------------------------|:--------------------------------|:---------------|---------------------------:|---------------------------:|:--------------------------|:-------------------------------|:-------------------------|:----------------------------|:----------------------|------------:|
| A           | Current baseline monthly Top3 | monthly     |                3 | 66.21%         | 84.83%                   | 22.27% | 27.52%         | -5.25%        | 43.33%                        | -0.28%                          | -19.32%        |                    1.23333 |                    3.7     | 12.53%                    | 2024-04                        | -10.59%                  | 2025-04                     | 15.27%                |          31 |
| B           | Weekly rebalance Top3         | weekly      |                3 | -15.11%        | 84.83%                   | -6.27% | 27.52%         | -33.79%       | 35.48%                        | -2.38%                          | -42.13%        |                    3.17204 |                    9.51613 | 18.55%                    | 2024-03                        | -12.42%                  | 2025-03                     | 12.41%                |         132 |
| C           | Weekly rebalance Top5         | weekly      |                5 | 7.58%          | 84.83%                   | 2.93%  | 27.52%         | -24.58%       | 38.71%                        | -1.66%                          | -36.45%        |                    2.71613 |                   13.5806  | 19.77%                    | 2024-08                        | -9.16%                   | 2026-03                     | 6.68%                 |         132 |
| D           | Relative Strength Top3        | weekly      |                3 | -8.84%         | 84.83%                   | -3.60% | 27.52%         | -31.11%       | 32.26%                        | -2.22%                          | -36.49%        |                    4.29032 |                   12.871   | 27.73%                    | 2026-02                        | -14.58%                  | 2025-03                     | 6.67%                 |         132 |
| E           | Benchmark-aware Top3          | weekly      |                3 | -14.54%        | 84.83%                   | -6.03% | 27.52%         | -33.55%       | 29.03%                        | -2.44%                          | -38.70%        |                    4.31183 |                   12.9355  | 26.17%                    | 2026-02                        | -11.73%                  | 2025-03                     | 6.25%                 |         132 |
| F           | Leadership Rotation Overlay   | weekly      |                3 | -19.08%        | 84.83%                   | -8.04% | 27.52%         | -35.55%       | 35.48%                        | -2.53%                          | -42.16%        |                    4.2043  |                   12.6129  | 24.13%                    | 2026-02                        | -11.73%                  | 2024-04                     | 7.40%                 |         132 |

## Decision

- Did weekly rebalance improve excess return? No. Historical excess CAGR delta vs baseline: -28.54%; recent excess delta: -6.32%.
- Did relative strength improve excess return? No. Historical excess CAGR delta vs baseline: -25.87%; recent excess delta: -3.72%.
- Did benchmark-aware selection improve excess return? No. Historical excess CAGR delta vs baseline: -28.30%; recent excess delta: -3.72%.
- Did any policy beat BIST100 robustly? No under the current acceptance filter.
- Next paper-trading candidate: none. No policy passed both historical and recent acceptance criteria.
- Current one-month fixed hold should be kept for tracking, while weekly/relative-strength variants remain research-only.

## Acceptance Rule

A policy is only eligible if it improves both historical walk-forward excess return and the recent 2026-06 counterfactual excess return. Policies that only fix June 2026 are rejected.
