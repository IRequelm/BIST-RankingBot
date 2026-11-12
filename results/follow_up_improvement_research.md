# Follow-Up Improvement Research

This is research-only. Production follow-up tracking remains fixed and still reads reports/tracking_state.json.

## Policy Summary

| policy_id   | policy_name                   | frequency   |   portfolio_size | total_return   | benchmark_total_return   | cagr   | bist100_cagr   | excess_cagr   | monthly_win_rate_vs_bist100   | average_monthly_excess_return   | max_drawdown   |   average_monthly_turnover |   average_trades_per_month | transaction_cost_impact   | worst_underperformance_month   | worst_underperformance   | best_outperformance_month   | best_outperformance   |   intervals |
|:------------|:------------------------------|:------------|-----------------:|:---------------|:-------------------------|:-------|:---------------|:--------------|:------------------------------|:--------------------------------|:---------------|---------------------------:|---------------------------:|:--------------------------|:-------------------------------|:-------------------------|:----------------------------|:----------------------|------------:|
| A           | Current baseline monthly Top3 | monthly     |                3 | 55.54%         | 53.02%                   | 16.71% | 16.05%         | 0.67%         | 44.12%                        | 0.12%                           | -19.32%        |                    1.2451  |                    3.73529 | 13.56%                    | 2024-04                        | -10.59%                  | 2025-04                     | 15.27%                |          35 |
| B           | Weekly rebalance Top3         | weekly      |                3 | -21.51%        | 53.02%                   | -8.13% | 16.05%         | -24.17%       | 40.00%                        | -1.80%                          | -42.13%        |                    3.07619 |                    9.22857 | 18.98%                    | 2024-03                        | -12.42%                  | 2025-03                     | 12.41%                |         150 |
| C           | Weekly rebalance Top5         | weekly      |                5 | 4.18%          | 53.02%                   | 1.44%  | 16.05%         | -14.60%       | 42.86%                        | -1.05%                          | -36.45%        |                    2.68    |                   13.4     | 21.54%                    | 2024-08                        | -9.16%                   | 2026-09                     | 6.85%                 |         150 |
| D           | Relative Strength Top3        | weekly      |                3 | -1.89%         | 53.02%                   | -0.67% | 16.05%         | -16.71%       | 40.00%                        | -1.21%                          | -39.97%        |                    4.25714 |                   12.7714  | 33.99%                    | 2026-02                        | -14.58%                  | 2026-08                     | 8.57%                 |         150 |
| E           | Benchmark-aware Top3          | weekly      |                3 | -13.09%        | 53.02%                   | -4.79% | 16.05%         | -20.84%       | 37.14%                        | -1.58%                          | -40.89%        |                    4.25714 |                   12.7714  | 30.15%                    | 2026-02                        | -11.73%                  | 2026-08                     | 8.57%                 |         150 |
| F           | Leadership Rotation Overlay   | weekly      |                3 | -15.39%        | 53.02%                   | -5.68% | 16.05%         | -21.73%       | 40.00%                        | -1.59%                          | -42.16%        |                    4.2     |                   12.6     | 28.94%                    | 2026-02                        | -11.73%                  | 2026-08                     | 8.44%                 |         150 |

## Decision

- Did weekly rebalance improve excess return? No. Historical excess CAGR delta vs baseline: -24.84%; recent excess delta: -0.06%.
- Did relative strength improve excess return? Recent yes, historical no, so rejected. Historical excess CAGR delta vs baseline: -17.38%; recent excess delta: 16.80%.
- Did benchmark-aware selection improve excess return? Recent yes, historical no, so rejected. Historical excess CAGR delta vs baseline: -21.50%; recent excess delta: 11.16%.
- Did any policy beat BIST100 robustly? No under the current acceptance filter.
- Next paper-trading candidate: none. No policy passed both historical and recent acceptance criteria.
- Current one-month fixed hold should be kept for tracking, while weekly/relative-strength variants remain research-only.

## Acceptance Rule

A policy is only eligible if it improves both historical walk-forward excess return and the recent 2026-06 counterfactual excess return. Policies that only fix June 2026 are rejected.
