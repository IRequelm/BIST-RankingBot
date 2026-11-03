# Follow-Up Improvement Research

This is research-only. Production follow-up tracking remains fixed and still reads reports/tracking_state.json.

## Policy Summary

| policy_id   | policy_name                   | frequency   |   portfolio_size | total_return   | benchmark_total_return   | cagr   | bist100_cagr   | excess_cagr   | monthly_win_rate_vs_bist100   | average_monthly_excess_return   | max_drawdown   |   average_monthly_turnover |   average_trades_per_month | transaction_cost_impact   | worst_underperformance_month   | worst_underperformance   | best_outperformance_month   | best_outperformance   |   intervals |
|:------------|:------------------------------|:------------|-----------------:|:---------------|:-------------------------|:-------|:---------------|:--------------|:------------------------------|:--------------------------------|:---------------|---------------------------:|---------------------------:|:--------------------------|:-------------------------------|:-------------------------|:----------------------------|:----------------------|------------:|
| A           | Current baseline monthly Top3 | monthly     |                3 | 48.23%         | 43.77%                   | 14.90% | 13.67%         | 1.23%         | 44.12%                        | 0.16%                           | -19.32%        |                    1.20588 |                    3.61765 | 12.51%                    | 2024-04                        | -10.59%                  | 2025-04                     | 15.27%                |          34 |
| B           | Weekly rebalance Top3         | weekly      |                3 | -25.25%        | 43.77%                   | -9.76% | 13.67%         | -23.43%       | 40.00%                        | -1.75%                          | -42.13%        |                    3.01905 |                    9.05714 | 17.71%                    | 2024-03                        | -12.42%                  | 2025-03                     | 12.41%                |         148 |
| C           | Weekly rebalance Top5         | weekly      |                5 | -5.07%         | 43.77%                   | -1.82% | 13.67%         | -15.49%       | 42.86%                        | -1.13%                          | -37.06%        |                    2.63429 |                   13.1714  | 19.28%                    | 2024-08                        | -9.16%                   | 2026-09                     | 6.85%                 |         148 |
| D           | Relative Strength Top3        | weekly      |                3 | -16.28%        | 43.77%                   | -6.08% | 13.67%         | -19.75%       | 37.14%                        | -1.49%                          | -41.68%        |                    4.2     |                   12.6     | 28.58%                    | 2026-02                        | -14.58%                  | 2026-08                     | 8.57%                 |         148 |
| E           | Benchmark-aware Top3          | weekly      |                3 | -21.86%        | 43.77%                   | -8.34% | 13.67%         | -22.01%       | 34.29%                        | -1.70%                          | -42.58%        |                    4.18095 |                   12.5429  | 26.57%                    | 2026-02                        | -11.73%                  | 2026-08                     | 8.57%                 |         148 |
| F           | Leadership Rotation Overlay   | weekly      |                3 | -23.93%        | 43.77%                   | -9.20% | 13.67%         | -22.87%       | 37.14%                        | -1.72%                          | -42.30%        |                    4.12381 |                   12.3714  | 25.51%                    | 2026-02                        | -11.73%                  | 2026-08                     | 8.44%                 |         148 |

## Decision

- Did weekly rebalance improve excess return? Recent yes, historical no, so rejected. Historical excess CAGR delta vs baseline: -24.66%; recent excess delta: 2.47%.
- Did relative strength improve excess return? Recent yes, historical no, so rejected. Historical excess CAGR delta vs baseline: -20.98%; recent excess delta: 8.36%.
- Did benchmark-aware selection improve excess return? Recent yes, historical no, so rejected. Historical excess CAGR delta vs baseline: -23.24%; recent excess delta: 7.98%.
- Did any policy beat BIST100 robustly? No under the current acceptance filter.
- Next paper-trading candidate: none. No policy passed both historical and recent acceptance criteria.
- Current one-month fixed hold should be kept for tracking, while weekly/relative-strength variants remain research-only.

## Acceptance Rule

A policy is only eligible if it improves both historical walk-forward excess return and the recent 2026-06 counterfactual excess return. Policies that only fix June 2026 are rejected.
