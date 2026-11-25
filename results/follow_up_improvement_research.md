# Follow-Up Improvement Research

This is research-only. Production follow-up tracking remains fixed and still reads reports/tracking_state.json.

## Policy Summary

| policy_id   | policy_name                   | frequency   |   portfolio_size | total_return   | benchmark_total_return   | cagr   | bist100_cagr   | excess_cagr   | monthly_win_rate_vs_bist100   | average_monthly_excess_return   | max_drawdown   |   average_monthly_turnover |   average_trades_per_month | transaction_cost_impact   | worst_underperformance_month   | worst_underperformance   | best_outperformance_month   | best_outperformance   |   intervals |
|:------------|:------------------------------|:------------|-----------------:|:---------------|:-------------------------|:-------|:---------------|:--------------|:------------------------------|:--------------------------------|:---------------|---------------------------:|---------------------------:|:--------------------------|:-------------------------------|:-------------------------|:----------------------------|:----------------------|------------:|
| A           | Current baseline monthly Top3 | monthly     |                3 | 45.31%         | 43.83%                   | 13.78% | 13.38%         | 0.40%         | 44.12%                        | 0.10%                           | -19.32%        |                    1.2451  |                    3.73529 | 12.69%                    | 2024-04                        | -10.59%                  | 2025-04                     | 15.27%                |          35 |
| B           | Weekly rebalance Top3         | weekly      |                3 | -25.92%        | 43.83%                   | -9.85% | 13.38%         | -23.23%       | 40.00%                        | -1.78%                          | -42.13%        |                    3.09524 |                    9.28571 | 18.03%                    | 2024-03                        | -12.42%                  | 2025-03                     | 12.41%                |         152 |
| C           | Weekly rebalance Top5         | weekly      |                5 | -0.19%         | 43.83%                   | -0.07% | 13.38%         | -13.45%       | 45.71%                        | -1.00%                          | -36.45%        |                    2.70286 |                   13.5143  | 20.83%                    | 2024-08                        | -9.16%                   | 2026-09                     | 6.85%                 |         152 |
| D           | Relative Strength Top3        | weekly      |                3 | -3.87%         | 43.83%                   | -1.35% | 13.38%         | -14.74%       | 40.00%                        | -1.10%                          | -39.97%        |                    4.25714 |                   12.7714  | 33.30%                    | 2026-02                        | -14.58%                  | 2026-11                     | 10.05%                |         152 |
| E           | Benchmark-aware Top3          | weekly      |                3 | -15.26%        | 43.83%                   | -5.56% | 13.38%         | -18.94%       | 37.14%                        | -1.47%                          | -40.89%        |                    4.27619 |                   12.8286  | 29.55%                    | 2026-02                        | -11.73%                  | 2026-08                     | 8.57%                 |         152 |
| F           | Leadership Rotation Overlay   | weekly      |                3 | -17.51%        | 43.83%                   | -6.43% | 13.38%         | -19.82%       | 40.00%                        | -1.49%                          | -42.16%        |                    4.21905 |                   12.6571  | 28.37%                    | 2026-02                        | -11.73%                  | 2026-08                     | 8.44%                 |         152 |

## Decision

- Did weekly rebalance improve excess return? Recent yes, historical no, so rejected. Historical excess CAGR delta vs baseline: -23.63%; recent excess delta: 0.34%.
- Did relative strength improve excess return? Recent yes, historical no, so rejected. Historical excess CAGR delta vs baseline: -15.14%; recent excess delta: 19.96%.
- Did benchmark-aware selection improve excess return? Recent yes, historical no, so rejected. Historical excess CAGR delta vs baseline: -19.35%; recent excess delta: 13.95%.
- Did any policy beat BIST100 robustly? No under the current acceptance filter.
- Next paper-trading candidate: none. No policy passed both historical and recent acceptance criteria.
- Current one-month fixed hold should be kept for tracking, while weekly/relative-strength variants remain research-only.

## Acceptance Rule

A policy is only eligible if it improves both historical walk-forward excess return and the recent 2026-06 counterfactual excess return. Policies that only fix June 2026 are rejected.
