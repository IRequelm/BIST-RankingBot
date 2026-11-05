# Follow-Up Improvement Research

This is research-only. Production follow-up tracking remains fixed and still reads reports/tracking_state.json.

## Policy Summary

| policy_id   | policy_name                   | frequency   |   portfolio_size | total_return   | benchmark_total_return   | cagr   | bist100_cagr   | excess_cagr   | monthly_win_rate_vs_bist100   | average_monthly_excess_return   | max_drawdown   |   average_monthly_turnover |   average_trades_per_month | transaction_cost_impact   | worst_underperformance_month   | worst_underperformance   | best_outperformance_month   | best_outperformance   |   intervals |
|:------------|:------------------------------|:------------|-----------------:|:---------------|:-------------------------|:-------|:---------------|:--------------|:------------------------------|:--------------------------------|:---------------|---------------------------:|---------------------------:|:--------------------------|:-------------------------------|:-------------------------|:----------------------------|:----------------------|------------:|
| A           | Current baseline monthly Top3 | monthly     |                3 | 54.14%         | 50.55%                   | 16.46% | 15.50%         | 0.96%         | 44.12%                        | 0.14%                           | -19.32%        |                    1.2451  |                    3.73529 | 13.44%                    | 2024-04                        | -10.59%                  | 2025-04                     | 15.27%                |          35 |
| B           | Weekly rebalance Top3         | weekly      |                3 | -21.07%        | 50.55%                   | -8.00% | 15.50%         | -23.50%       | 40.00%                        | -1.74%                          | -42.13%        |                    3.0381  |                    9.11429 | 18.82%                    | 2024-03                        | -12.42%                  | 2025-03                     | 12.41%                |         149 |
| C           | Weekly rebalance Top5         | weekly      |                5 | 1.11%          | 50.55%                   | 0.39%  | 15.50%         | -15.11%       | 42.86%                        | -1.09%                          | -36.45%        |                    2.65714 |                   13.2857  | 20.71%                    | 2024-08                        | -9.16%                   | 2026-09                     | 6.85%                 |         149 |
| D           | Relative Strength Top3        | weekly      |                3 | -10.82%        | 50.55%                   | -3.95% | 15.50%         | -19.45%       | 37.14%                        | -1.45%                          | -39.97%        |                    4.21905 |                   12.6571  | 30.60%                    | 2026-02                        | -14.58%                  | 2026-08                     | 8.57%                 |         149 |
| E           | Benchmark-aware Top3          | weekly      |                3 | -17.32%        | 50.55%                   | -6.48% | 15.50%         | -21.98%       | 34.29%                        | -1.68%                          | -40.89%        |                    4.21905 |                   12.6571  | 28.40%                    | 2026-02                        | -11.73%                  | 2026-08                     | 8.57%                 |         149 |
| F           | Leadership Rotation Overlay   | weekly      |                3 | -19.51%        | 50.55%                   | -7.36% | 15.50%         | -22.86%       | 37.14%                        | -1.69%                          | -42.16%        |                    4.1619  |                   12.4857  | 27.26%                    | 2026-02                        | -11.73%                  | 2026-08                     | 8.44%                 |         149 |

## Decision

- Did weekly rebalance improve excess return? Recent yes, historical no, so rejected. Historical excess CAGR delta vs baseline: -24.46%; recent excess delta: 0.36%.
- Did relative strength improve excess return? Recent yes, historical no, so rejected. Historical excess CAGR delta vs baseline: -20.42%; recent excess delta: 7.40%.
- Did benchmark-aware selection improve excess return? Recent yes, historical no, so rejected. Historical excess CAGR delta vs baseline: -22.94%; recent excess delta: 6.37%.
- Did any policy beat BIST100 robustly? No under the current acceptance filter.
- Next paper-trading candidate: none. No policy passed both historical and recent acceptance criteria.
- Current one-month fixed hold should be kept for tracking, while weekly/relative-strength variants remain research-only.

## Acceptance Rule

A policy is only eligible if it improves both historical walk-forward excess return and the recent 2026-06 counterfactual excess return. Policies that only fix June 2026 are rejected.
