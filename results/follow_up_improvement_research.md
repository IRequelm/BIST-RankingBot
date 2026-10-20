# Follow-Up Improvement Research

This is research-only. Production follow-up tracking remains fixed and still reads reports/tracking_state.json.

## Policy Summary

| policy_id   | policy_name                   | frequency   |   portfolio_size | total_return   | benchmark_total_return   | cagr   | bist100_cagr   | excess_cagr   | monthly_win_rate_vs_bist100   | average_monthly_excess_return   | max_drawdown   |   average_monthly_turnover |   average_trades_per_month | transaction_cost_impact   | worst_underperformance_month   | worst_underperformance   | best_outperformance_month   | best_outperformance   |   intervals |
|:------------|:------------------------------|:------------|-----------------:|:---------------|:-------------------------|:-------|:---------------|:--------------|:------------------------------|:--------------------------------|:---------------|---------------------------:|---------------------------:|:--------------------------|:-------------------------------|:-------------------------|:----------------------------|:----------------------|------------:|
| A           | Current baseline monthly Top3 | monthly     |                3 | 60.42%         | 49.92%                   | 18.42% | 15.59%         | 2.83%         | 45.45%                        | 0.24%                           | -19.32%        |                    1.24242 |                    3.72727 | 13.52%                    | 2024-04                        | -10.59%                  | 2025-04                     | 15.27%                |          34 |
| B           | Weekly rebalance Top3         | weekly      |                3 | -17.73%        | 49.92%                   | -6.74% | 15.59%         | -22.33%       | 41.18%                        | -1.65%                          | -42.13%        |                    3.06863 |                    9.20588 | 19.21%                    | 2024-03                        | -12.42%                  | 2025-03                     | 12.41%                |         146 |
| C           | Weekly rebalance Top5         | weekly      |                5 | 4.71%          | 49.92%                   | 1.66%  | 15.59%         | -13.93%       | 44.12%                        | -1.01%                          | -36.45%        |                    2.67647 |                   13.3824  | 20.94%                    | 2024-08                        | -9.16%                   | 2026-09                     | 6.85%                 |         146 |
| D           | Relative Strength Top3        | weekly      |                3 | -10.87%        | 49.92%                   | -4.03% | 15.59%         | -19.62%       | 38.24%                        | -1.47%                          | -38.81%        |                    4.28431 |                   12.8529  | 30.10%                    | 2026-02                        | -14.58%                  | 2026-08                     | 8.57%                 |         146 |
| E           | Benchmark-aware Top3          | weekly      |                3 | -16.81%        | 49.92%                   | -6.37% | 15.59%         | -21.96%       | 35.29%                        | -1.69%                          | -40.42%        |                    4.26471 |                   12.7941  | 27.98%                    | 2026-02                        | -11.73%                  | 2026-08                     | 8.57%                 |         146 |
| F           | Leadership Rotation Overlay   | weekly      |                3 | -18.08%        | 49.92%                   | -6.89% | 15.59%         | -22.47%       | 38.24%                        | -1.67%                          | -42.16%        |                    4.20588 |                   12.6176  | 27.17%                    | 2026-02                        | -11.73%                  | 2026-08                     | 8.44%                 |         146 |

## Decision

- Did weekly rebalance improve excess return? No. Historical excess CAGR delta vs baseline: -25.16%; recent excess delta: -0.84%.
- Did relative strength improve excess return? Recent yes, historical no, so rejected. Historical excess CAGR delta vs baseline: -22.46%; recent excess delta: 2.49%.
- Did benchmark-aware selection improve excess return? Recent yes, historical no, so rejected. Historical excess CAGR delta vs baseline: -24.79%; recent excess delta: 2.08%.
- Did any policy beat BIST100 robustly? No under the current acceptance filter.
- Next paper-trading candidate: none. No policy passed both historical and recent acceptance criteria.
- Current one-month fixed hold should be kept for tracking, while weekly/relative-strength variants remain research-only.

## Acceptance Rule

A policy is only eligible if it improves both historical walk-forward excess return and the recent 2026-06 counterfactual excess return. Policies that only fix June 2026 are rejected.
