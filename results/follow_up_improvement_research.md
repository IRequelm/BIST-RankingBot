# Follow-Up Improvement Research

This is research-only. Production follow-up tracking remains fixed and still reads reports/tracking_state.json.

## Policy Summary

| policy_id   | policy_name                   | frequency   |   portfolio_size | total_return   | benchmark_total_return   | cagr    | bist100_cagr   | excess_cagr   | monthly_win_rate_vs_bist100   | average_monthly_excess_return   | max_drawdown   |   average_monthly_turnover |   average_trades_per_month | transaction_cost_impact   | worst_underperformance_month   | worst_underperformance   | best_outperformance_month   | best_outperformance   |   intervals |
|:------------|:------------------------------|:------------|-----------------:|:---------------|:-------------------------|:--------|:---------------|:--------------|:------------------------------|:--------------------------------|:---------------|---------------------------:|---------------------------:|:--------------------------|:-------------------------------|:-------------------------|:----------------------------|:----------------------|------------:|
| A           | Current baseline monthly Top3 | monthly     |                3 | 45.08%         | 43.97%                   | 13.68%  | 13.38%         | 0.30%         | 44.12%                        | 0.10%                           | -19.32%        |                    1.2451  |                    3.73529 | 12.67%                    | 2024-04                        | -10.59%                  | 2025-04                     | 15.27%                |          35 |
| B           | Weekly rebalance Top3         | weekly      |                3 | -27.13%        | 43.97%                   | -10.33% | 13.38%         | -23.71%       | 40.00%                        | -1.82%                          | -42.13%        |                    3.09524 |                    9.28571 | 17.74%                    | 2024-03                        | -12.42%                  | 2025-03                     | 12.41%                |         152 |
| C           | Weekly rebalance Top5         | weekly      |                5 | -0.76%         | 43.97%                   | -0.26%  | 13.38%         | -13.64%       | 42.86%                        | -1.02%                          | -36.45%        |                    2.70286 |                   13.5143  | 20.71%                    | 2024-08                        | -9.16%                   | 2026-09                     | 6.85%                 |         152 |
| D           | Relative Strength Top3        | weekly      |                3 | -6.00%         | 43.97%                   | -2.11%  | 13.38%         | -15.49%       | 40.00%                        | -1.17%                          | -39.97%        |                    4.25714 |                   12.7714  | 32.56%                    | 2026-02                        | -14.58%                  | 2026-08                     | 8.57%                 |         152 |
| E           | Benchmark-aware Top3          | weekly      |                3 | -17.14%        | 43.97%                   | -6.27%  | 13.38%         | -19.66%       | 37.14%                        | -1.54%                          | -40.89%        |                    4.27619 |                   12.8286  | 28.90%                    | 2026-02                        | -11.73%                  | 2026-08                     | 8.57%                 |         152 |
| F           | Leadership Rotation Overlay   | weekly      |                3 | -19.34%        | 43.97%                   | -7.14%  | 13.38%         | -20.52%       | 40.00%                        | -1.56%                          | -42.16%        |                    4.21905 |                   12.6571  | 27.74%                    | 2026-02                        | -11.73%                  | 2026-08                     | 8.44%                 |         152 |

## Decision

- Did weekly rebalance improve excess return? No. Historical excess CAGR delta vs baseline: -24.01%; recent excess delta: -2.36%.
- Did relative strength improve excess return? Recent yes, historical no, so rejected. Historical excess CAGR delta vs baseline: -15.79%; recent excess delta: 16.35%.
- Did benchmark-aware selection improve excess return? Recent yes, historical no, so rejected. Historical excess CAGR delta vs baseline: -19.95%; recent excess delta: 10.47%.
- Did any policy beat BIST100 robustly? No under the current acceptance filter.
- Next paper-trading candidate: none. No policy passed both historical and recent acceptance criteria.
- Current one-month fixed hold should be kept for tracking, while weekly/relative-strength variants remain research-only.

## Acceptance Rule

A policy is only eligible if it improves both historical walk-forward excess return and the recent 2026-06 counterfactual excess return. Policies that only fix June 2026 are rejected.
