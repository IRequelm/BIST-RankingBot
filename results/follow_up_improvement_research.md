# Follow-Up Improvement Research

This is research-only. Production follow-up tracking remains fixed and still reads reports/tracking_state.json.

## Policy Summary

| policy_id   | policy_name                   | frequency   |   portfolio_size | total_return   | benchmark_total_return   | cagr   | bist100_cagr   | excess_cagr   | monthly_win_rate_vs_bist100   | average_monthly_excess_return   | max_drawdown   |   average_monthly_turnover |   average_trades_per_month | transaction_cost_impact   | worst_underperformance_month   | worst_underperformance   | best_outperformance_month   | best_outperformance   |   intervals |
|:------------|:------------------------------|:------------|-----------------:|:---------------|:-------------------------|:-------|:---------------|:--------------|:------------------------------|:--------------------------------|:---------------|---------------------------:|---------------------------:|:--------------------------|:-------------------------------|:-------------------------|:----------------------------|:----------------------|------------:|
| A           | Current baseline monthly Top3 | monthly     |                3 | 68.30%         | 58.94%                   | 20.58% | 18.13%         | 2.45%         | 45.45%                        | 0.23%                           | -19.32%        |                    1.24242 |                    3.72727 | 14.17%                    | 2024-04                        | -10.59%                  | 2025-04                     | 15.27%                |          34 |
| B           | Weekly rebalance Top3         | weekly      |                3 | -13.13%        | 58.94%                   | -4.93% | 18.13%         | -23.06%       | 41.18%                        | -1.66%                          | -42.13%        |                    3.06863 |                    9.20588 | 20.27%                    | 2024-03                        | -12.42%                  | 2025-03                     | 12.41%                |         146 |
| C           | Weekly rebalance Top5         | weekly      |                5 | 9.20%          | 58.94%                   | 3.22%  | 18.13%         | -14.91%       | 44.12%                        | -1.05%                          | -36.45%        |                    2.67647 |                   13.3824  | 21.83%                    | 2024-08                        | -9.16%                   | 2026-09                     | 6.85%                 |         146 |
| D           | Relative Strength Top3        | weekly      |                3 | -9.51%         | 58.94%                   | -3.53% | 18.13%         | -21.66%       | 35.29%                        | -1.59%                          | -38.81%        |                    4.28431 |                   12.8529  | 30.55%                    | 2026-02                        | -14.58%                  | 2026-08                     | 8.57%                 |         146 |
| E           | Benchmark-aware Top3          | weekly      |                3 | -15.54%        | 58.94%                   | -5.89% | 18.13%         | -24.02%       | 32.35%                        | -1.81%                          | -40.42%        |                    4.26471 |                   12.7941  | 28.40%                    | 2026-02                        | -11.73%                  | 2026-08                     | 8.57%                 |         146 |
| F           | Leadership Rotation Overlay   | weekly      |                3 | -16.83%        | 58.94%                   | -6.41% | 18.13%         | -24.54%       | 38.24%                        | -1.79%                          | -42.16%        |                    4.20588 |                   12.6176  | 27.57%                    | 2026-02                        | -11.73%                  | 2026-08                     | 8.44%                 |         146 |

## Decision

- Did weekly rebalance improve excess return? No. Historical excess CAGR delta vs baseline: -25.52%; recent excess delta: -0.63%.
- Did relative strength improve excess return? No. Historical excess CAGR delta vs baseline: -24.11%; recent excess delta: -0.90%.
- Did benchmark-aware selection improve excess return? No. Historical excess CAGR delta vs baseline: -26.47%; recent excess delta: -1.31%.
- Did any policy beat BIST100 robustly? No under the current acceptance filter.
- Next paper-trading candidate: none. No policy passed both historical and recent acceptance criteria.
- Current one-month fixed hold should be kept for tracking, while weekly/relative-strength variants remain research-only.

## Acceptance Rule

A policy is only eligible if it improves both historical walk-forward excess return and the recent 2026-06 counterfactual excess return. Policies that only fix June 2026 are rejected.
