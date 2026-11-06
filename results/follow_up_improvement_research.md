# Follow-Up Improvement Research

This is research-only. Production follow-up tracking remains fixed and still reads reports/tracking_state.json.

## Policy Summary

| policy_id   | policy_name                   | frequency   |   portfolio_size | total_return   | benchmark_total_return   | cagr   | bist100_cagr   | excess_cagr   | monthly_win_rate_vs_bist100   | average_monthly_excess_return   | max_drawdown   |   average_monthly_turnover |   average_trades_per_month | transaction_cost_impact   | worst_underperformance_month   | worst_underperformance   | best_outperformance_month   | best_outperformance   |   intervals |
|:------------|:------------------------------|:------------|-----------------:|:---------------|:-------------------------|:-------|:---------------|:--------------|:------------------------------|:--------------------------------|:---------------|---------------------------:|---------------------------:|:--------------------------|:-------------------------------|:-------------------------|:----------------------------|:----------------------|------------:|
| A           | Current baseline monthly Top3 | monthly     |                3 | 54.14%         | 48.65%                   | 16.45% | 14.97%         | 1.48%         | 44.12%                        | 0.17%                           | -19.32%        |                    1.2451  |                    3.73529 | 13.44%                    | 2024-04                        | -10.59%                  | 2025-04                     | 15.27%                |          35 |
| B           | Weekly rebalance Top3         | weekly      |                3 | -21.07%        | 48.65%                   | -7.99% | 14.97%         | -22.96%       | 40.00%                        | -1.70%                          | -42.13%        |                    3.0381  |                    9.11429 | 18.82%                    | 2024-03                        | -12.42%                  | 2025-03                     | 12.41%                |         149 |
| C           | Weekly rebalance Top5         | weekly      |                5 | 1.11%          | 48.65%                   | 0.39%  | 14.97%         | -14.58%       | 42.86%                        | -1.05%                          | -36.45%        |                    2.65714 |                   13.2857  | 20.71%                    | 2024-08                        | -9.16%                   | 2026-09                     | 6.85%                 |         149 |
| D           | Relative Strength Top3        | weekly      |                3 | -10.82%        | 48.65%                   | -3.95% | 14.97%         | -18.92%       | 37.14%                        | -1.41%                          | -39.97%        |                    4.21905 |                   12.6571  | 30.60%                    | 2026-02                        | -14.58%                  | 2026-08                     | 8.57%                 |         149 |
| E           | Benchmark-aware Top3          | weekly      |                3 | -17.32%        | 48.65%                   | -6.47% | 14.97%         | -21.44%       | 34.29%                        | -1.64%                          | -40.89%        |                    4.21905 |                   12.6571  | 28.40%                    | 2026-02                        | -11.73%                  | 2026-08                     | 8.57%                 |         149 |
| F           | Leadership Rotation Overlay   | weekly      |                3 | -19.51%        | 48.65%                   | -7.35% | 14.97%         | -22.32%       | 37.14%                        | -1.66%                          | -42.16%        |                    4.1619  |                   12.4857  | 27.26%                    | 2026-02                        | -11.73%                  | 2026-08                     | 8.44%                 |         149 |

## Decision

- Did weekly rebalance improve excess return? Recent yes, historical no, so rejected. Historical excess CAGR delta vs baseline: -24.43%; recent excess delta: 0.36%.
- Did relative strength improve excess return? Recent yes, historical no, so rejected. Historical excess CAGR delta vs baseline: -20.39%; recent excess delta: 7.40%.
- Did benchmark-aware selection improve excess return? Recent yes, historical no, so rejected. Historical excess CAGR delta vs baseline: -22.92%; recent excess delta: 6.37%.
- Did any policy beat BIST100 robustly? No under the current acceptance filter.
- Next paper-trading candidate: none. No policy passed both historical and recent acceptance criteria.
- Current one-month fixed hold should be kept for tracking, while weekly/relative-strength variants remain research-only.

## Acceptance Rule

A policy is only eligible if it improves both historical walk-forward excess return and the recent 2026-06 counterfactual excess return. Policies that only fix June 2026 are rejected.
