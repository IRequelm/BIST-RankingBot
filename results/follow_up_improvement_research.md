# Follow-Up Improvement Research

This is research-only. Production follow-up tracking remains fixed and still reads reports/tracking_state.json.

## Policy Summary

| policy_id   | policy_name                   | frequency   |   portfolio_size | total_return   | benchmark_total_return   | cagr   | bist100_cagr   | excess_cagr   | monthly_win_rate_vs_bist100   | average_monthly_excess_return   | max_drawdown   |   average_monthly_turnover |   average_trades_per_month | transaction_cost_impact   | worst_underperformance_month   | worst_underperformance   | best_outperformance_month   | best_outperformance   |   intervals |
|:------------|:------------------------------|:------------|-----------------:|:---------------|:-------------------------|:-------|:---------------|:--------------|:------------------------------|:--------------------------------|:---------------|---------------------------:|---------------------------:|:--------------------------|:-------------------------------|:-------------------------|:----------------------------|:----------------------|------------:|
| A           | Current baseline monthly Top3 | monthly     |                3 | 54.12%         | 41.12%                   | 16.54% | 12.97%         | 3.58%         | 45.45%                        | 0.28%                           | -19.32%        |                    1.24242 |                    3.72727 | 13.00%                    | 2024-04                        | -10.59%                  | 2025-04                     | 15.27%                |          34 |
| B           | Weekly rebalance Top3         | weekly      |                3 | -22.44%        | 41.12%                   | -8.60% | 12.97%         | -21.57%       | 41.18%                        | -1.65%                          | -42.13%        |                    3.10784 |                    9.32353 | 18.37%                    | 2024-03                        | -12.42%                  | 2025-03                     | 12.41%                |         148 |
| C           | Weekly rebalance Top5         | weekly      |                5 | -1.49%         | 41.12%                   | -0.53% | 12.97%         | -13.49%       | 44.12%                        | -1.01%                          | -36.45%        |                    2.71176 |                   13.5588  | 20.00%                    | 2024-08                        | -9.16%                   | 2026-09                     | 6.85%                 |         148 |
| D           | Relative Strength Top3        | weekly      |                3 | -14.10%        | 41.12%                   | -5.24% | 12.97%         | -18.20%       | 38.24%                        | -1.42%                          | -40.16%        |                    4.32353 |                   12.9706  | 29.32%                    | 2026-02                        | -14.58%                  | 2026-08                     | 8.57%                 |         148 |
| E           | Benchmark-aware Top3          | weekly      |                3 | -19.82%        | 41.12%                   | -7.52% | 12.97%         | -20.49%       | 35.29%                        | -1.63%                          | -41.08%        |                    4.30392 |                   12.9118  | 27.26%                    | 2026-02                        | -11.73%                  | 2026-08                     | 8.57%                 |         148 |
| F           | Leadership Rotation Overlay   | weekly      |                3 | -21.94%        | 41.12%                   | -8.40% | 12.97%         | -21.36%       | 38.24%                        | -1.65%                          | -42.16%        |                    4.2451  |                   12.7353  | 26.17%                    | 2026-02                        | -11.73%                  | 2026-08                     | 8.44%                 |         148 |

## Decision

- Did weekly rebalance improve excess return? Recent yes, historical no, so rejected. Historical excess CAGR delta vs baseline: -25.15%; recent excess delta: 1.32%.
- Did relative strength improve excess return? Recent yes, historical no, so rejected. Historical excess CAGR delta vs baseline: -21.78%; recent excess delta: 6.44%.
- Did benchmark-aware selection improve excess return? Recent yes, historical no, so rejected. Historical excess CAGR delta vs baseline: -24.06%; recent excess delta: 6.04%.
- Did any policy beat BIST100 robustly? No under the current acceptance filter.
- Next paper-trading candidate: none. No policy passed both historical and recent acceptance criteria.
- Current one-month fixed hold should be kept for tracking, while weekly/relative-strength variants remain research-only.

## Acceptance Rule

A policy is only eligible if it improves both historical walk-forward excess return and the recent 2026-06 counterfactual excess return. Policies that only fix June 2026 are rejected.
