# Follow-Up Improvement Research

This is research-only. Production follow-up tracking remains fixed and still reads reports/tracking_state.json.

## Policy Summary

| policy_id   | policy_name                   | frequency   |   portfolio_size | total_return   | benchmark_total_return   | cagr   | bist100_cagr   | excess_cagr   | monthly_win_rate_vs_bist100   | average_monthly_excess_return   | max_drawdown   |   average_monthly_turnover |   average_trades_per_month | transaction_cost_impact   | worst_underperformance_month   | worst_underperformance   | best_outperformance_month   | best_outperformance   |   intervals |
|:------------|:------------------------------|:------------|-----------------:|:---------------|:-------------------------|:-------|:---------------|:--------------|:------------------------------|:--------------------------------|:---------------|---------------------------:|---------------------------:|:--------------------------|:-------------------------------|:-------------------------|:----------------------------|:----------------------|------------:|
| A           | Current baseline monthly Top3 | monthly     |                3 | 55.71%         | 53.62%                   | 16.79% | 16.24%         | 0.55%         | 44.12%                        | 0.11%                           | -19.32%        |                    1.2451  |                    3.73529 | 13.57%                    | 2024-04                        | -10.59%                  | 2025-04                     | 15.27%                |          35 |
| B           | Weekly rebalance Top3         | weekly      |                3 | -20.27%        | 53.62%                   | -7.63% | 16.24%         | -23.87%       | 40.00%                        | -1.77%                          | -42.13%        |                    3.0381  |                    9.11429 | 19.01%                    | 2024-03                        | -12.42%                  | 2025-03                     | 12.41%                |         149 |
| C           | Weekly rebalance Top5         | weekly      |                5 | 5.01%          | 53.62%                   | 1.73%  | 16.24%         | -14.51%       | 42.86%                        | -1.04%                          | -36.45%        |                    2.65714 |                   13.2857  | 21.50%                    | 2024-08                        | -9.16%                   | 2026-09                     | 6.85%                 |         149 |
| D           | Relative Strength Top3        | weekly      |                3 | -4.29%         | 53.62%                   | -1.52% | 16.24%         | -17.77%       | 40.00%                        | -1.30%                          | -39.97%        |                    4.21905 |                   12.6571  | 32.82%                    | 2026-02                        | -14.58%                  | 2026-08                     | 8.57%                 |         149 |
| E           | Benchmark-aware Top3          | weekly      |                3 | -12.47%        | 53.62%                   | -4.56% | 16.24%         | -20.80%       | 37.14%                        | -1.57%                          | -40.89%        |                    4.21905 |                   12.6571  | 30.05%                    | 2026-02                        | -11.73%                  | 2026-08                     | 8.57%                 |         149 |
| F           | Leadership Rotation Overlay   | weekly      |                3 | -14.79%        | 53.62%                   | -5.46% | 16.24%         | -21.70%       | 40.00%                        | -1.59%                          | -42.16%        |                    4.1619  |                   12.4857  | 28.84%                    | 2026-02                        | -11.73%                  | 2026-08                     | 8.44%                 |         149 |

## Decision

- Did weekly rebalance improve excess return? No. Historical excess CAGR delta vs baseline: -24.42%; recent excess delta: -0.25%.
- Did relative strength improve excess return? Recent yes, historical no, so rejected. Historical excess CAGR delta vs baseline: -18.32%; recent excess delta: 12.75%.
- Did benchmark-aware selection improve excess return? Recent yes, historical no, so rejected. Historical excess CAGR delta vs baseline: -21.36%; recent excess delta: 10.29%.
- Did any policy beat BIST100 robustly? No under the current acceptance filter.
- Next paper-trading candidate: none. No policy passed both historical and recent acceptance criteria.
- Current one-month fixed hold should be kept for tracking, while weekly/relative-strength variants remain research-only.

## Acceptance Rule

A policy is only eligible if it improves both historical walk-forward excess return and the recent 2026-06 counterfactual excess return. Policies that only fix June 2026 are rejected.
