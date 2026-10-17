# Follow-Up Improvement Research

This is research-only. Production follow-up tracking remains fixed and still reads reports/tracking_state.json.

## Policy Summary

| policy_id   | policy_name                   | frequency   |   portfolio_size | total_return   | benchmark_total_return   | cagr   | bist100_cagr   | excess_cagr   | monthly_win_rate_vs_bist100   | average_monthly_excess_return   | max_drawdown   |   average_monthly_turnover |   average_trades_per_month | transaction_cost_impact   | worst_underperformance_month   | worst_underperformance   | best_outperformance_month   | best_outperformance   |   intervals |
|:------------|:------------------------------|:------------|-----------------:|:---------------|:-------------------------|:-------|:---------------|:--------------|:------------------------------|:--------------------------------|:---------------|---------------------------:|---------------------------:|:--------------------------|:-------------------------------|:-------------------------|:----------------------------|:----------------------|------------:|
| A           | Current baseline monthly Top3 | monthly     |                3 | 66.36%         | 53.74%                   | 20.04% | 16.69%         | 3.35%         | 45.45%                        | 0.28%                           | -19.32%        |                    1.24242 |                    3.72727 | 14.01%                    | 2024-04                        | -10.59%                  | 2025-04                     | 15.27%                |          34 |
| B           | Weekly rebalance Top3         | weekly      |                3 | -14.99%        | 53.74%                   | -5.66% | 16.69%         | -22.35%       | 41.18%                        | -1.63%                          | -42.13%        |                    3.06863 |                    9.20588 | 19.84%                    | 2024-03                        | -12.42%                  | 2025-03                     | 12.41%                |         146 |
| C           | Weekly rebalance Top5         | weekly      |                5 | 7.65%          | 53.74%                   | 2.68%  | 16.69%         | -14.01%       | 44.12%                        | -0.99%                          | -36.45%        |                    2.67647 |                   13.3824  | 21.52%                    | 2024-08                        | -9.16%                   | 2026-09                     | 6.85%                 |         146 |
| D           | Relative Strength Top3        | weekly      |                3 | -8.90%         | 53.74%                   | -3.29% | 16.69%         | -19.98%       | 38.24%                        | -1.48%                          | -38.81%        |                    4.28431 |                   12.8529  | 30.75%                    | 2026-02                        | -14.58%                  | 2026-08                     | 8.57%                 |         146 |
| E           | Benchmark-aware Top3          | weekly      |                3 | -14.97%        | 53.74%                   | -5.65% | 16.69%         | -22.34%       | 35.29%                        | -1.70%                          | -40.42%        |                    4.26471 |                   12.7941  | 28.59%                    | 2026-02                        | -11.73%                  | 2026-08                     | 8.57%                 |         146 |
| F           | Leadership Rotation Overlay   | weekly      |                3 | -16.27%        | 53.74%                   | -6.17% | 16.69%         | -22.86%       | 38.24%                        | -1.68%                          | -42.16%        |                    4.20588 |                   12.6176  | 27.76%                    | 2026-02                        | -11.73%                  | 2026-08                     | 8.44%                 |         146 |

## Decision

- Did weekly rebalance improve excess return? No. Historical excess CAGR delta vs baseline: -25.70%; recent excess delta: -1.45%.
- Did relative strength improve excess return? Recent yes, historical no, so rejected. Historical excess CAGR delta vs baseline: -23.33%; recent excess delta: 0.96%.
- Did benchmark-aware selection improve excess return? Recent yes, historical no, so rejected. Historical excess CAGR delta vs baseline: -25.69%; recent excess delta: 0.54%.
- Did any policy beat BIST100 robustly? No under the current acceptance filter.
- Next paper-trading candidate: none. No policy passed both historical and recent acceptance criteria.
- Current one-month fixed hold should be kept for tracking, while weekly/relative-strength variants remain research-only.

## Acceptance Rule

A policy is only eligible if it improves both historical walk-forward excess return and the recent 2026-06 counterfactual excess return. Policies that only fix June 2026 are rejected.
