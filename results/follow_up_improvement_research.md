# Follow-Up Improvement Research

This is research-only. Production follow-up tracking remains fixed and still reads reports/tracking_state.json.

## Policy Summary

| policy_id   | policy_name                   | frequency   |   portfolio_size | total_return   | benchmark_total_return   | cagr   | bist100_cagr   | excess_cagr   | monthly_win_rate_vs_bist100   | average_monthly_excess_return   | max_drawdown   |   average_monthly_turnover |   average_trades_per_month | transaction_cost_impact   | worst_underperformance_month   | worst_underperformance   | best_outperformance_month   | best_outperformance   |   intervals |
|:------------|:------------------------------|:------------|-----------------:|:---------------|:-------------------------|:-------|:---------------|:--------------|:------------------------------|:--------------------------------|:---------------|---------------------------:|---------------------------:|:--------------------------|:-------------------------------|:-------------------------|:----------------------------|:----------------------|------------:|
| A           | Current baseline monthly Top3 | monthly     |                3 | 90.92%         | 82.21%                   | 27.04% | 24.86%         | 2.18%         | 46.88%                        | 0.25%                           | -19.32%        |                    1.21875 |                    3.65625 | 15.18%                    | 2024-04                        | -10.59%                  | 2025-04                     | 15.27%                |          33 |
| B           | Weekly rebalance Top3         | weekly      |                3 | 0.41%          | 82.21%                   | 0.15%  | 24.86%         | -24.71%       | 39.39%                        | -1.67%                          | -42.13%        |                    3.10101 |                    9.30303 | 22.89%                    | 2024-03                        | -12.42%                  | 2025-03                     | 12.41%                |         142 |
| C           | Weekly rebalance Top5         | weekly      |                5 | 17.50%         | 82.21%                   | 6.15%  | 24.86%         | -18.71%       | 42.42%                        | -1.25%                          | -36.45%        |                    2.73333 |                   13.6667  | 23.25%                    | 2024-08                        | -9.16%                   | 2026-03                     | 6.68%                 |         142 |
| D           | Relative Strength Top3        | weekly      |                3 | 5.52%          | 82.21%                   | 2.01%  | 24.86%         | -22.85%       | 36.36%                        | -1.57%                          | -38.81%        |                    4.21212 |                   12.6364  | 33.72%                    | 2026-02                        | -14.58%                  | 2026-08                     | 8.57%                 |         142 |
| E           | Benchmark-aware Top3          | weekly      |                3 | -1.42%         | 82.21%                   | -0.53% | 24.86%         | -25.39%       | 33.33%                        | -1.79%                          | -39.49%        |                    4.25253 |                   12.7576  | 31.89%                    | 2026-02                        | -11.73%                  | 2026-08                     | 8.57%                 |         142 |
| F           | Leadership Rotation Overlay   | weekly      |                3 | -3.05%         | 82.21%                   | -1.14% | 24.86%         | -26.00%       | 39.39%                        | -1.78%                          | -42.16%        |                    4.09091 |                   12.2727  | 30.05%                    | 2026-02                        | -11.73%                  | 2026-08                     | 8.44%                 |         142 |

## Decision

- Did weekly rebalance improve excess return? Recent yes, historical no, so rejected. Historical excess CAGR delta vs baseline: -26.89%; recent excess delta: 7.03%.
- Did relative strength improve excess return? Recent yes, historical no, so rejected. Historical excess CAGR delta vs baseline: -25.03%; recent excess delta: 7.70%.
- Did benchmark-aware selection improve excess return? Recent yes, historical no, so rejected. Historical excess CAGR delta vs baseline: -27.57%; recent excess delta: 7.31%.
- Did any policy beat BIST100 robustly? No under the current acceptance filter.
- Next paper-trading candidate: none. No policy passed both historical and recent acceptance criteria.
- Current one-month fixed hold should be kept for tracking, while weekly/relative-strength variants remain research-only.

## Acceptance Rule

A policy is only eligible if it improves both historical walk-forward excess return and the recent 2026-06 counterfactual excess return. Policies that only fix June 2026 are rejected.
