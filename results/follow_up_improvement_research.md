# Follow-Up Improvement Research

This is research-only. Production follow-up tracking remains fixed and still reads reports/tracking_state.json.

## Policy Summary

| policy_id   | policy_name                   | frequency   |   portfolio_size | total_return   | benchmark_total_return   | cagr   | bist100_cagr   | excess_cagr   | monthly_win_rate_vs_bist100   | average_monthly_excess_return   | max_drawdown   |   average_monthly_turnover |   average_trades_per_month | transaction_cost_impact   | worst_underperformance_month   | worst_underperformance   | best_outperformance_month   | best_outperformance   |   intervals |
|:------------|:------------------------------|:------------|-----------------:|:---------------|:-------------------------|:-------|:---------------|:--------------|:------------------------------|:--------------------------------|:---------------|---------------------------:|---------------------------:|:--------------------------|:-------------------------------|:-------------------------|:----------------------------|:----------------------|------------:|
| A           | Current baseline monthly Top3 | monthly     |                3 | 58.73%         | 76.52%                   | 19.64% | 24.68%         | -5.03%        | 43.33%                        | -0.27%                          | -19.32%        |                    1.23333 |                    3.7     | 11.99%                    | 2024-04                        | -10.59%                  | 2025-04                     | 15.27%                |          31 |
| B           | Weekly rebalance Top3         | weekly      |                3 | -14.60%        | 76.52%                   | -5.94% | 24.68%         | -30.62%       | 35.48%                        | -2.21%                          | -42.13%        |                    3.19355 |                    9.58065 | 18.79%                    | 2024-03                        | -12.42%                  | 2025-03                     | 12.41%                |         135 |
| C           | Weekly rebalance Top5         | weekly      |                5 | 4.40%          | 76.52%                   | 1.69%  | 24.68%         | -22.99%       | 38.71%                        | -1.60%                          | -36.45%        |                    2.76774 |                   13.8387  | 19.58%                    | 2024-08                        | -9.16%                   | 2026-03                     | 6.68%                 |         135 |
| D           | Relative Strength Top3        | weekly      |                3 | -10.92%        | 76.52%                   | -4.39% | 24.68%         | -29.07%       | 32.26%                        | -2.14%                          | -37.95%        |                    4.37634 |                   13.129   | 27.71%                    | 2026-02                        | -14.58%                  | 2025-03                     | 6.67%                 |         135 |
| E           | Benchmark-aware Top3          | weekly      |                3 | -16.49%        | 76.52%                   | -6.76% | 24.68%         | -31.44%       | 29.03%                        | -2.36%                          | -38.70%        |                    4.39785 |                   13.1935  | 26.15%                    | 2026-02                        | -11.73%                  | 2025-03                     | 6.25%                 |         135 |
| F           | Leadership Rotation Overlay   | weekly      |                3 | -17.77%        | 76.52%                   | -7.31% | 24.68%         | -31.99%       | 35.48%                        | -2.34%                          | -42.16%        |                    4.24731 |                   12.7419  | 24.80%                    | 2026-02                        | -11.73%                  | 2024-04                     | 7.40%                 |         135 |

## Decision

- Did weekly rebalance improve excess return? No. Historical excess CAGR delta vs baseline: -25.59%; recent excess delta: -6.52%.
- Did relative strength improve excess return? No. Historical excess CAGR delta vs baseline: -24.03%; recent excess delta: -6.65%.
- Did benchmark-aware selection improve excess return? No. Historical excess CAGR delta vs baseline: -26.40%; recent excess delta: -6.65%.
- Did any policy beat BIST100 robustly? No under the current acceptance filter.
- Next paper-trading candidate: none. No policy passed both historical and recent acceptance criteria.
- Current one-month fixed hold should be kept for tracking, while weekly/relative-strength variants remain research-only.

## Acceptance Rule

A policy is only eligible if it improves both historical walk-forward excess return and the recent 2026-06 counterfactual excess return. Policies that only fix June 2026 are rejected.
