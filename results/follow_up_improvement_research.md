# Follow-Up Improvement Research

This is research-only. Production follow-up tracking remains fixed and still reads reports/tracking_state.json.

## Policy Summary

| policy_id   | policy_name                   | frequency   |   portfolio_size | total_return   | benchmark_total_return   | cagr   | bist100_cagr   | excess_cagr   | monthly_win_rate_vs_bist100   | average_monthly_excess_return   | max_drawdown   |   average_monthly_turnover |   average_trades_per_month | transaction_cost_impact   | worst_underperformance_month   | worst_underperformance   | best_outperformance_month   | best_outperformance   |   intervals |
|:------------|:------------------------------|:------------|-----------------:|:---------------|:-------------------------|:-------|:---------------|:--------------|:------------------------------|:--------------------------------|:---------------|---------------------------:|---------------------------:|:--------------------------|:-------------------------------|:-------------------------|:----------------------------|:----------------------|------------:|
| A           | Current baseline monthly Top3 | monthly     |                3 | 76.26%         | 77.19%                   | 23.29% | 23.53%         | -0.24%        | 46.88%                        | 0.06%                           | -19.32%        |                    1.21875 |                    3.65625 | 14.05%                    | 2024-04                        | -10.59%                  | 2025-04                     | 15.27%                |          33 |
| B           | Weekly rebalance Top3         | weekly      |                3 | -7.34%         | 77.19%                   | -2.78% | 23.53%         | -26.30%       | 39.39%                        | -1.83%                          | -42.13%        |                    3.10101 |                    9.30303 | 21.14%                    | 2024-03                        | -12.42%                  | 2025-03                     | 12.41%                |         142 |
| C           | Weekly rebalance Top5         | weekly      |                5 | 8.00%          | 77.19%                   | 2.88%  | 23.53%         | -20.64%       | 42.42%                        | -1.42%                          | -36.45%        |                    2.73333 |                   13.6667  | 21.39%                    | 2024-08                        | -9.16%                   | 2026-03                     | 6.68%                 |         142 |
| D           | Relative Strength Top3        | weekly      |                3 | -2.62%         | 77.19%                   | -0.98% | 23.53%         | -24.50%       | 36.36%                        | -1.74%                          | -38.81%        |                    4.21212 |                   12.6364  | 31.13%                    | 2026-02                        | -14.58%                  | 2026-08                     | 8.57%                 |         142 |
| E           | Benchmark-aware Top3          | weekly      |                3 | -9.03%         | 77.19%                   | -3.44% | 23.53%         | -26.96%       | 33.33%                        | -1.95%                          | -39.49%        |                    4.25253 |                   12.7576  | 29.44%                    | 2026-02                        | -11.73%                  | 2026-08                     | 8.57%                 |         142 |
| F           | Leadership Rotation Overlay   | weekly      |                3 | -10.53%        | 77.19%                   | -4.03% | 23.53%         | -27.55%       | 39.39%                        | -1.94%                          | -42.16%        |                    4.09091 |                   12.2727  | 27.75%                    | 2026-02                        | -11.73%                  | 2026-08                     | 8.44%                 |         142 |

## Decision

- Did weekly rebalance improve excess return? Recent yes, historical no, so rejected. Historical excess CAGR delta vs baseline: -26.06%; recent excess delta: 8.03%.
- Did relative strength improve excess return? Recent yes, historical no, so rejected. Historical excess CAGR delta vs baseline: -24.26%; recent excess delta: 8.64%.
- Did benchmark-aware selection improve excess return? Recent yes, historical no, so rejected. Historical excess CAGR delta vs baseline: -26.72%; recent excess delta: 8.29%.
- Did any policy beat BIST100 robustly? No under the current acceptance filter.
- Next paper-trading candidate: none. No policy passed both historical and recent acceptance criteria.
- Current one-month fixed hold should be kept for tracking, while weekly/relative-strength variants remain research-only.

## Acceptance Rule

A policy is only eligible if it improves both historical walk-forward excess return and the recent 2026-06 counterfactual excess return. Policies that only fix June 2026 are rejected.
