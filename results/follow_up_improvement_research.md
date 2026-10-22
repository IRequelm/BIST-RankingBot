# Follow-Up Improvement Research

This is research-only. Production follow-up tracking remains fixed and still reads reports/tracking_state.json.

## Policy Summary

| policy_id   | policy_name                   | frequency   |   portfolio_size | total_return   | benchmark_total_return   | cagr   | bist100_cagr   | excess_cagr   | monthly_win_rate_vs_bist100   | average_monthly_excess_return   | max_drawdown   |   average_monthly_turnover |   average_trades_per_month | transaction_cost_impact   | worst_underperformance_month   | worst_underperformance   | best_outperformance_month   | best_outperformance   |   intervals |
|:------------|:------------------------------|:------------|-----------------:|:---------------|:-------------------------|:-------|:---------------|:--------------|:------------------------------|:--------------------------------|:---------------|---------------------------:|---------------------------:|:--------------------------|:-------------------------------|:-------------------------|:----------------------------|:----------------------|------------:|
| A           | Current baseline monthly Top3 | monthly     |                3 | 60.26%         | 51.85%                   | 18.34% | 16.08%         | 2.26%         | 45.45%                        | 0.21%                           | -19.32%        |                    1.24242 |                    3.72727 | 13.50%                    | 2024-04                        | -10.59%                  | 2025-04                     | 15.27%                |          34 |
| B           | Weekly rebalance Top3         | weekly      |                3 | -17.24%        | 51.85%                   | -6.53% | 16.08%         | -22.62%       | 41.18%                        | -1.67%                          | -42.13%        |                    3.08824 |                    9.26471 | 19.45%                    | 2024-03                        | -12.42%                  | 2025-03                     | 12.41%                |         147 |
| C           | Weekly rebalance Top5         | weekly      |                5 | 5.19%          | 51.85%                   | 1.82%  | 16.08%         | -14.26%       | 44.12%                        | -1.03%                          | -36.45%        |                    2.68824 |                   13.4412  | 21.14%                    | 2024-08                        | -9.16%                   | 2026-09                     | 6.85%                 |         147 |
| D           | Relative Strength Top3        | weekly      |                3 | -8.73%         | 51.85%                   | -3.21% | 16.08%         | -19.29%       | 38.24%                        | -1.44%                          | -38.81%        |                    4.30392 |                   12.9118  | 30.98%                    | 2026-02                        | -14.58%                  | 2026-08                     | 8.57%                 |         147 |
| E           | Benchmark-aware Top3          | weekly      |                3 | -14.82%        | 51.85%                   | -5.56% | 16.08%         | -21.65%       | 35.29%                        | -1.66%                          | -40.42%        |                    4.28431 |                   12.8529  | 28.80%                    | 2026-02                        | -11.73%                  | 2026-08                     | 8.57%                 |         147 |
| F           | Leadership Rotation Overlay   | weekly      |                3 | -16.54%        | 51.85%                   | -6.25% | 16.08%         | -22.33%       | 38.24%                        | -1.65%                          | -42.16%        |                    4.22549 |                   12.6765  | 27.82%                    | 2026-02                        | -11.73%                  | 2026-08                     | 8.44%                 |         147 |

## Decision

- Did weekly rebalance improve excess return? No. Historical excess CAGR delta vs baseline: -24.87%; recent excess delta: -1.54%.
- Did relative strength improve excess return? Recent yes, historical no, so rejected. Historical excess CAGR delta vs baseline: -21.55%; recent excess delta: 3.50%.
- Did benchmark-aware selection improve excess return? Recent yes, historical no, so rejected. Historical excess CAGR delta vs baseline: -23.90%; recent excess delta: 3.08%.
- Did any policy beat BIST100 robustly? No under the current acceptance filter.
- Next paper-trading candidate: none. No policy passed both historical and recent acceptance criteria.
- Current one-month fixed hold should be kept for tracking, while weekly/relative-strength variants remain research-only.

## Acceptance Rule

A policy is only eligible if it improves both historical walk-forward excess return and the recent 2026-06 counterfactual excess return. Policies that only fix June 2026 are rejected.
