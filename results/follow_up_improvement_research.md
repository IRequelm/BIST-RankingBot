# Follow-Up Improvement Research

This is research-only. Production follow-up tracking remains fixed and still reads reports/tracking_state.json.

## Policy Summary

| policy_id   | policy_name                   | frequency   |   portfolio_size | total_return   | benchmark_total_return   | cagr   | bist100_cagr   | excess_cagr   | monthly_win_rate_vs_bist100   | average_monthly_excess_return   | max_drawdown   |   average_monthly_turnover |   average_trades_per_month | transaction_cost_impact   | worst_underperformance_month   | worst_underperformance   | best_outperformance_month   | best_outperformance   |   intervals |
|:------------|:------------------------------|:------------|-----------------:|:---------------|:-------------------------|:-------|:---------------|:--------------|:------------------------------|:--------------------------------|:---------------|---------------------------:|---------------------------:|:--------------------------|:-------------------------------|:-------------------------|:----------------------------|:----------------------|------------:|
| A           | Current baseline monthly Top3 | monthly     |                3 | 57.42%         | 55.32%                   | 17.12% | 16.57%         | 0.55%         | 44.12%                        | 0.11%                           | -19.32%        |                    1.2451  |                    3.73529 | 13.71%                    | 2024-04                        | -10.59%                  | 2025-04                     | 15.27%                |          35 |
| B           | Weekly rebalance Top3         | weekly      |                3 | -20.96%        | 55.32%                   | -7.86% | 16.57%         | -24.43%       | 40.00%                        | -1.82%                          | -42.13%        |                    3.07619 |                    9.22857 | 19.11%                    | 2024-03                        | -12.42%                  | 2025-03                     | 12.41%                |         150 |
| C           | Weekly rebalance Top5         | weekly      |                5 | 4.69%          | 55.32%                   | 1.61%  | 16.57%         | -14.96%       | 42.86%                        | -1.08%                          | -36.45%        |                    2.68    |                   13.4     | 21.64%                    | 2024-08                        | -9.16%                   | 2026-09                     | 6.85%                 |         150 |
| D           | Relative Strength Top3        | weekly      |                3 | -1.38%         | 55.32%                   | -0.48% | 16.57%         | -17.05%       | 40.00%                        | -1.24%                          | -39.97%        |                    4.25714 |                   12.7714  | 34.16%                    | 2026-02                        | -14.58%                  | 2026-08                     | 8.57%                 |         150 |
| E           | Benchmark-aware Top3          | weekly      |                3 | -12.96%        | 55.32%                   | -4.72% | 16.57%         | -21.28%       | 34.29%                        | -1.62%                          | -40.89%        |                    4.25714 |                   12.7714  | 30.20%                    | 2026-02                        | -11.73%                  | 2026-08                     | 8.57%                 |         150 |
| F           | Leadership Rotation Overlay   | weekly      |                3 | -15.26%        | 55.32%                   | -5.60% | 16.57%         | -22.17%       | 37.14%                        | -1.63%                          | -42.16%        |                    4.2     |                   12.6     | 28.99%                    | 2026-02                        | -11.73%                  | 2026-08                     | 8.44%                 |         150 |

## Decision

- Did weekly rebalance improve excess return? No. Historical excess CAGR delta vs baseline: -24.98%; recent excess delta: -1.25%.
- Did relative strength improve excess return? Recent yes, historical no, so rejected. Historical excess CAGR delta vs baseline: -17.60%; recent excess delta: 15.54%.
- Did benchmark-aware selection improve excess return? Recent yes, historical no, so rejected. Historical excess CAGR delta vs baseline: -21.83%; recent excess delta: 9.51%.
- Did any policy beat BIST100 robustly? No under the current acceptance filter.
- Next paper-trading candidate: none. No policy passed both historical and recent acceptance criteria.
- Current one-month fixed hold should be kept for tracking, while weekly/relative-strength variants remain research-only.

## Acceptance Rule

A policy is only eligible if it improves both historical walk-forward excess return and the recent 2026-06 counterfactual excess return. Policies that only fix June 2026 are rejected.
