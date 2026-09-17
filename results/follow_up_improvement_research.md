# Follow-Up Improvement Research

This is research-only. Production follow-up tracking remains fixed and still reads reports/tracking_state.json.

## Policy Summary

| policy_id   | policy_name                   | frequency   |   portfolio_size | total_return   | benchmark_total_return   | cagr   | bist100_cagr   | excess_cagr   | monthly_win_rate_vs_bist100   | average_monthly_excess_return   | max_drawdown   |   average_monthly_turnover |   average_trades_per_month | transaction_cost_impact   | worst_underperformance_month   | worst_underperformance   | best_outperformance_month   | best_outperformance   |   intervals |
|:------------|:------------------------------|:------------|-----------------:|:---------------|:-------------------------|:-------|:---------------|:--------------|:------------------------------|:--------------------------------|:---------------|---------------------------:|---------------------------:|:--------------------------|:-------------------------------|:-------------------------|:----------------------------|:----------------------|------------:|
| A           | Current baseline monthly Top3 | monthly     |                3 | 85.42%         | 72.12%                   | 25.64% | 22.23%         | 3.41%         | 46.88%                        | 0.32%                           | -19.32%        |                    1.21875 |                    3.65625 | 14.76%                    | 2024-04                        | -10.59%                  | 2026-09                     | 16.00%                |          33 |
| B           | Weekly rebalance Top3         | weekly      |                3 | -2.24%         | 72.12%                   | -0.83% | 22.23%         | -23.06%       | 39.39%                        | -1.59%                          | -42.13%        |                    3.10101 |                    9.30303 | 22.29%                    | 2024-03                        | -12.42%                  | 2025-03                     | 12.41%                |         142 |
| C           | Weekly rebalance Top5         | weekly      |                5 | 14.27%         | 72.12%                   | 5.06%  | 22.23%         | -17.17%       | 42.42%                        | -1.17%                          | -36.45%        |                    2.73333 |                   13.6667  | 22.62%                    | 2024-08                        | -9.16%                   | 2026-09                     | 8.76%                 |         142 |
| D           | Relative Strength Top3        | weekly      |                3 | 2.74%          | 72.12%                   | 1.00%  | 22.23%         | -21.23%       | 36.36%                        | -1.49%                          | -38.81%        |                    4.21212 |                   12.6364  | 32.84%                    | 2026-02                        | -14.58%                  | 2026-09                     | 9.52%                 |         142 |
| E           | Benchmark-aware Top3          | weekly      |                3 | -4.02%         | 72.12%                   | -1.51% | 22.23%         | -23.74%       | 33.33%                        | -1.71%                          | -39.49%        |                    4.25253 |                   12.7576  | 31.05%                    | 2026-02                        | -11.73%                  | 2026-09                     | 9.17%                 |         142 |
| F           | Leadership Rotation Overlay   | weekly      |                3 | -5.61%         | 72.12%                   | -2.11% | 22.23%         | -24.34%       | 39.39%                        | -1.70%                          | -42.16%        |                    4.09091 |                   12.2727  | 29.27%                    | 2026-02                        | -11.73%                  | 2026-09                     | 9.30%                 |         142 |

## Decision

- Did weekly rebalance improve excess return? Recent yes, historical no, so rejected. Historical excess CAGR delta vs baseline: -26.48%; recent excess delta: 6.94%.
- Did relative strength improve excess return? Recent yes, historical no, so rejected. Historical excess CAGR delta vs baseline: -24.64%; recent excess delta: 7.59%.
- Did benchmark-aware selection improve excess return? Recent yes, historical no, so rejected. Historical excess CAGR delta vs baseline: -27.15%; recent excess delta: 7.22%.
- Did any policy beat BIST100 robustly? No under the current acceptance filter.
- Next paper-trading candidate: none. No policy passed both historical and recent acceptance criteria.
- Current one-month fixed hold should be kept for tracking, while weekly/relative-strength variants remain research-only.

## Acceptance Rule

A policy is only eligible if it improves both historical walk-forward excess return and the recent 2026-06 counterfactual excess return. Policies that only fix June 2026 are rejected.
