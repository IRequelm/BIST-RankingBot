# Follow-Up Improvement Research

This is research-only. Production follow-up tracking remains fixed and still reads reports/tracking_state.json.

## Policy Summary

| policy_id   | policy_name                   | frequency   |   portfolio_size | total_return   | benchmark_total_return   | cagr   | bist100_cagr   | excess_cagr   | monthly_win_rate_vs_bist100   | average_monthly_excess_return   | max_drawdown   |   average_monthly_turnover |   average_trades_per_month | transaction_cost_impact   | worst_underperformance_month   | worst_underperformance   | best_outperformance_month   | best_outperformance   |   intervals |
|:------------|:------------------------------|:------------|-----------------:|:---------------|:-------------------------|:-------|:---------------|:--------------|:------------------------------|:--------------------------------|:---------------|---------------------------:|---------------------------:|:--------------------------|:-------------------------------|:-------------------------|:----------------------------|:----------------------|------------:|
| A           | Current baseline monthly Top3 | monthly     |                3 | 85.97%         | 88.01%                   | 26.25% | 26.77%         | -0.52%        | 45.16%                        | 0.04%                           | -19.32%        |                    1.21505 |                    3.64516 | 14.27%                    | 2024-04                        | -10.59%                  | 2025-04                     | 15.27%                |          32 |
| B           | Weekly rebalance Top3         | weekly      |                3 | -3.39%         | 88.01%                   | -1.29% | 26.77%         | -28.06%       | 37.50%                        | -1.94%                          | -42.13%        |                    3.15625 |                    9.46875 | 21.72%                    | 2024-03                        | -12.42%                  | 2025-03                     | 12.41%                |         139 |
| C           | Weekly rebalance Top5         | weekly      |                5 | 14.68%         | 88.01%                   | 5.28%  | 26.77%         | -21.49%       | 40.62%                        | -1.46%                          | -36.45%        |                    2.78125 |                   13.9062  | 22.36%                    | 2024-08                        | -9.16%                   | 2026-03                     | 6.68%                 |         139 |
| D           | Relative Strength Top3        | weekly      |                3 | 1.79%          | 88.01%                   | 0.67%  | 26.77%         | -26.10%       | 34.38%                        | -1.83%                          | -38.81%        |                    4.30208 |                   12.9062  | 32.18%                    | 2026-02                        | -14.58%                  | 2026-08                     | 8.72%                 |         139 |
| E           | Benchmark-aware Top3          | weekly      |                3 | -4.58%         | 88.01%                   | -1.74% | 26.77%         | -28.52%       | 31.25%                        | -2.05%                          | -39.49%        |                    4.32292 |                   12.9688  | 30.37%                    | 2026-02                        | -11.73%                  | 2026-08                     | 8.72%                 |         139 |
| F           | Leadership Rotation Overlay   | weekly      |                3 | -6.72%         | 88.01%                   | -2.58% | 26.77%         | -29.35%       | 37.50%                        | -2.05%                          | -42.16%        |                    4.17708 |                   12.5312  | 28.60%                    | 2026-02                        | -11.73%                  | 2026-08                     | 8.06%                 |         139 |

## Decision

- Did weekly rebalance improve excess return? Recent yes, historical no, so rejected. Historical excess CAGR delta vs baseline: -27.54%; recent excess delta: 6.39%.
- Did relative strength improve excess return? Recent yes, historical no, so rejected. Historical excess CAGR delta vs baseline: -25.59%; recent excess delta: 7.30%.
- Did benchmark-aware selection improve excess return? Recent yes, historical no, so rejected. Historical excess CAGR delta vs baseline: -28.00%; recent excess delta: 7.30%.
- Did any policy beat BIST100 robustly? No under the current acceptance filter.
- Next paper-trading candidate: none. No policy passed both historical and recent acceptance criteria.
- Current one-month fixed hold should be kept for tracking, while weekly/relative-strength variants remain research-only.

## Acceptance Rule

A policy is only eligible if it improves both historical walk-forward excess return and the recent 2026-06 counterfactual excess return. Policies that only fix June 2026 are rejected.
