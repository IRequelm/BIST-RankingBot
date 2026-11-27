# Follow-Up Improvement Research

This is research-only. Production follow-up tracking remains fixed and still reads reports/tracking_state.json.

## Policy Summary

| policy_id   | policy_name                   | frequency   |   portfolio_size | total_return   | benchmark_total_return   | cagr    | bist100_cagr   | excess_cagr   | monthly_win_rate_vs_bist100   | average_monthly_excess_return   | max_drawdown   |   average_monthly_turnover |   average_trades_per_month | transaction_cost_impact   | worst_underperformance_month   | worst_underperformance   | best_outperformance_month   | best_outperformance   |   intervals |
|:------------|:------------------------------|:------------|-----------------:|:---------------|:-------------------------|:--------|:---------------|:--------------|:------------------------------|:--------------------------------|:---------------|---------------------------:|---------------------------:|:--------------------------|:-------------------------------|:-------------------------|:----------------------------|:----------------------|------------:|
| A           | Current baseline monthly Top3 | monthly     |                3 | 41.77%         | 40.91%                   | 12.79%  | 12.56%         | 0.24%         | 44.12%                        | 0.10%                           | -19.32%        |                    1.2451  |                    3.73529 | 12.39%                    | 2024-04                        | -10.59%                  | 2025-04                     | 15.27%                |          35 |
| B           | Weekly rebalance Top3         | weekly      |                3 | -27.84%        | 40.91%                   | -10.64% | 12.56%         | -23.20%       | 40.00%                        | -1.79%                          | -42.13%        |                    3.09524 |                    9.28571 | 17.57%                    | 2024-03                        | -12.42%                  | 2025-03                     | 12.41%                |         152 |
| C           | Weekly rebalance Top5         | weekly      |                5 | -1.91%         | 40.91%                   | -0.66%  | 12.56%         | -13.22%       | 45.71%                        | -0.99%                          | -36.45%        |                    2.70286 |                   13.5143  | 20.47%                    | 2024-08                        | -9.16%                   | 2026-09                     | 6.85%                 |         152 |
| D           | Relative Strength Top3        | weekly      |                3 | -6.24%         | 40.91%                   | -2.20%  | 12.56%         | -14.75%       | 40.00%                        | -1.11%                          | -39.97%        |                    4.25714 |                   12.7714  | 32.48%                    | 2026-02                        | -14.58%                  | 2026-11                     | 9.38%                 |         152 |
| E           | Benchmark-aware Top3          | weekly      |                3 | -17.35%        | 40.91%                   | -6.36%  | 12.56%         | -18.92%       | 37.14%                        | -1.49%                          | -40.89%        |                    4.27619 |                   12.8286  | 28.82%                    | 2026-02                        | -11.73%                  | 2026-08                     | 8.57%                 |         152 |
| F           | Leadership Rotation Overlay   | weekly      |                3 | -19.54%        | 40.91%                   | -7.23%  | 12.56%         | -19.78%       | 40.00%                        | -1.51%                          | -42.16%        |                    4.21905 |                   12.6571  | 27.67%                    | 2026-02                        | -11.73%                  | 2026-08                     | 8.44%                 |         152 |

## Decision

- Did weekly rebalance improve excess return? No. Historical excess CAGR delta vs baseline: -23.44%; recent excess delta: -0.87%.
- Did relative strength improve excess return? Recent yes, historical no, so rejected. Historical excess CAGR delta vs baseline: -14.99%; recent excess delta: 18.37%.
- Did benchmark-aware selection improve excess return? Recent yes, historical no, so rejected. Historical excess CAGR delta vs baseline: -19.15%; recent excess delta: 12.51%.
- Did any policy beat BIST100 robustly? No under the current acceptance filter.
- Next paper-trading candidate: none. No policy passed both historical and recent acceptance criteria.
- Current one-month fixed hold should be kept for tracking, while weekly/relative-strength variants remain research-only.

## Acceptance Rule

A policy is only eligible if it improves both historical walk-forward excess return and the recent 2026-06 counterfactual excess return. Policies that only fix June 2026 are rejected.
