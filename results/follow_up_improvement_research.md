# Follow-Up Improvement Research

This is research-only. Production follow-up tracking remains fixed and still reads reports/tracking_state.json.

## Policy Summary

| policy_id   | policy_name                   | frequency   |   portfolio_size | total_return   | benchmark_total_return   | cagr   | bist100_cagr   | excess_cagr   | monthly_win_rate_vs_bist100   | average_monthly_excess_return   | max_drawdown   |   average_monthly_turnover |   average_trades_per_month | transaction_cost_impact   | worst_underperformance_month   | worst_underperformance   | best_outperformance_month   | best_outperformance   |   intervals |
|:------------|:------------------------------|:------------|-----------------:|:---------------|:-------------------------|:-------|:---------------|:--------------|:------------------------------|:--------------------------------|:---------------|---------------------------:|---------------------------:|:--------------------------|:-------------------------------|:-------------------------|:----------------------------|:----------------------|------------:|
| A           | Current baseline monthly Top3 | monthly     |                3 | 56.64%         | 55.33%                   | 16.97% | 16.62%         | 0.34%         | 44.12%                        | 0.09%                           | -19.32%        |                    1.2451  |                    3.73529 | 13.65%                    | 2024-04                        | -10.59%                  | 2025-04                     | 15.27%                |          35 |
| B           | Weekly rebalance Top3         | weekly      |                3 | -20.64%        | 55.33%                   | -7.75% | 16.62%         | -24.38%       | 40.00%                        | -1.81%                          | -42.13%        |                    3.07619 |                    9.22857 | 19.19%                    | 2024-03                        | -12.42%                  | 2025-03                     | 12.41%                |         150 |
| C           | Weekly rebalance Top5         | weekly      |                5 | 4.87%          | 55.33%                   | 1.67%  | 16.62%         | -14.95%       | 42.86%                        | -1.08%                          | -36.45%        |                    2.68    |                   13.4     | 21.68%                    | 2024-08                        | -9.16%                   | 2026-09                     | 6.85%                 |         150 |
| D           | Relative Strength Top3        | weekly      |                3 | -1.17%         | 55.33%                   | -0.41% | 16.62%         | -17.03%       | 40.00%                        | -1.23%                          | -39.97%        |                    4.25714 |                   12.7714  | 34.24%                    | 2026-02                        | -14.58%                  | 2026-08                     | 8.57%                 |         150 |
| E           | Benchmark-aware Top3          | weekly      |                3 | -12.53%        | 55.33%                   | -4.57% | 16.62%         | -21.19%       | 34.29%                        | -1.60%                          | -40.89%        |                    4.25714 |                   12.7714  | 30.34%                    | 2026-02                        | -11.73%                  | 2026-08                     | 8.57%                 |         150 |
| F           | Leadership Rotation Overlay   | weekly      |                3 | -14.85%        | 55.33%                   | -5.46% | 16.62%         | -22.08%       | 37.14%                        | -1.62%                          | -42.16%        |                    4.2     |                   12.6     | 29.13%                    | 2026-02                        | -11.73%                  | 2026-08                     | 8.44%                 |         150 |

## Decision

- Did weekly rebalance improve excess return? No. Historical excess CAGR delta vs baseline: -24.72%; recent excess delta: -1.05%.
- Did relative strength improve excess return? Recent yes, historical no, so rejected. Historical excess CAGR delta vs baseline: -17.38%; recent excess delta: 15.61%.
- Did benchmark-aware selection improve excess return? Recent yes, historical no, so rejected. Historical excess CAGR delta vs baseline: -21.53%; recent excess delta: 9.83%.
- Did any policy beat BIST100 robustly? No under the current acceptance filter.
- Next paper-trading candidate: none. No policy passed both historical and recent acceptance criteria.
- Current one-month fixed hold should be kept for tracking, while weekly/relative-strength variants remain research-only.

## Acceptance Rule

A policy is only eligible if it improves both historical walk-forward excess return and the recent 2026-06 counterfactual excess return. Policies that only fix June 2026 are rejected.
