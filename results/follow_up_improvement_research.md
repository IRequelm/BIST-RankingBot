# Follow-Up Improvement Research

This is research-only. Production follow-up tracking remains fixed and still reads reports/tracking_state.json.

## Policy Summary

| policy_id   | policy_name                   | frequency   |   portfolio_size | total_return   | benchmark_total_return   | cagr   | bist100_cagr   | excess_cagr   | monthly_win_rate_vs_bist100   | average_monthly_excess_return   | max_drawdown   |   average_monthly_turnover |   average_trades_per_month | transaction_cost_impact   | worst_underperformance_month   | worst_underperformance   | best_outperformance_month   | best_outperformance   |   intervals |
|:------------|:------------------------------|:------------|-----------------:|:---------------|:-------------------------|:-------|:---------------|:--------------|:------------------------------|:--------------------------------|:---------------|---------------------------:|---------------------------:|:--------------------------|:-------------------------------|:-------------------------|:----------------------------|:----------------------|------------:|
| A           | Current baseline monthly Top3 | monthly     |                3 | 64.65%         | 60.68%                   | 19.65% | 18.61%         | 1.05%         | 45.45%                        | 0.14%                           | -19.32%        |                    1.24242 |                    3.72727 | 13.87%                    | 2024-04                        | -10.59%                  | 2025-04                     | 15.27%                |          34 |
| B           | Weekly rebalance Top3         | weekly      |                3 | -15.00%        | 60.68%                   | -5.68% | 18.61%         | -24.29%       | 38.24%                        | -1.75%                          | -42.13%        |                    3.06863 |                    9.20588 | 19.84%                    | 2024-03                        | -12.42%                  | 2025-03                     | 12.41%                |         146 |
| C           | Weekly rebalance Top5         | weekly      |                5 | 7.29%          | 60.68%                   | 2.57%  | 18.61%         | -16.04%       | 44.12%                        | -1.13%                          | -36.45%        |                    2.67647 |                   13.3824  | 21.45%                    | 2024-08                        | -9.16%                   | 2026-09                     | 6.85%                 |         146 |
| D           | Relative Strength Top3        | weekly      |                3 | -10.20%        | 60.68%                   | -3.80% | 18.61%         | -22.40%       | 35.29%                        | -1.65%                          | -38.81%        |                    4.28431 |                   12.8529  | 30.32%                    | 2026-02                        | -14.58%                  | 2026-08                     | 8.57%                 |         146 |
| E           | Benchmark-aware Top3          | weekly      |                3 | -16.18%        | 60.68%                   | -6.15% | 18.61%         | -24.76%       | 32.35%                        | -1.86%                          | -40.42%        |                    4.26471 |                   12.7941  | 28.19%                    | 2026-02                        | -11.73%                  | 2026-08                     | 8.57%                 |         146 |
| F           | Leadership Rotation Overlay   | weekly      |                3 | -17.46%        | 60.68%                   | -6.67% | 18.61%         | -25.28%       | 35.29%                        | -1.84%                          | -42.16%        |                    4.20588 |                   12.6176  | 27.37%                    | 2026-02                        | -11.73%                  | 2026-08                     | 8.44%                 |         146 |

## Decision

- Did weekly rebalance improve excess return? No. Historical excess CAGR delta vs baseline: -25.34%; recent excess delta: -1.43%.
- Did relative strength improve excess return? No. Historical excess CAGR delta vs baseline: -23.45%; recent excess delta: -0.36%.
- Did benchmark-aware selection improve excess return? No. Historical excess CAGR delta vs baseline: -25.81%; recent excess delta: -0.77%.
- Did any policy beat BIST100 robustly? No under the current acceptance filter.
- Next paper-trading candidate: none. No policy passed both historical and recent acceptance criteria.
- Current one-month fixed hold should be kept for tracking, while weekly/relative-strength variants remain research-only.

## Acceptance Rule

A policy is only eligible if it improves both historical walk-forward excess return and the recent 2026-06 counterfactual excess return. Policies that only fix June 2026 are rejected.
