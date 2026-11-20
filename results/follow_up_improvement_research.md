# Follow-Up Improvement Research

This is research-only. Production follow-up tracking remains fixed and still reads reports/tracking_state.json.

## Policy Summary

| policy_id   | policy_name                   | frequency   |   portfolio_size | total_return   | benchmark_total_return   | cagr   | bist100_cagr   | excess_cagr   | monthly_win_rate_vs_bist100   | average_monthly_excess_return   | max_drawdown   |   average_monthly_turnover |   average_trades_per_month | transaction_cost_impact   | worst_underperformance_month   | worst_underperformance   | best_outperformance_month   | best_outperformance   |   intervals |
|:------------|:------------------------------|:------------|-----------------:|:---------------|:-------------------------|:-------|:---------------|:--------------|:------------------------------|:--------------------------------|:---------------|---------------------------:|---------------------------:|:--------------------------|:-------------------------------|:-------------------------|:----------------------------|:----------------------|------------:|
| A           | Current baseline monthly Top3 | monthly     |                3 | 51.66%         | 49.52%                   | 15.56% | 14.99%         | 0.57%         | 44.12%                        | 0.11%                           | -19.32%        |                    1.2451  |                    3.73529 | 13.23%                    | 2024-04                        | -10.59%                  | 2025-04                     | 15.27%                |          35 |
| B           | Weekly rebalance Top3         | weekly      |                3 | -23.82%        | 49.52%                   | -9.01% | 14.99%         | -24.00%       | 40.00%                        | -1.81%                          | -42.13%        |                    3.07619 |                    9.22857 | 18.42%                    | 2024-03                        | -12.42%                  | 2025-03                     | 12.41%                |         151 |
| C           | Weekly rebalance Top5         | weekly      |                5 | 2.52%          | 49.52%                   | 0.87%  | 14.99%         | -14.12%       | 42.86%                        | -1.03%                          | -36.45%        |                    2.69143 |                   13.4571  | 21.29%                    | 2024-08                        | -9.16%                   | 2026-09                     | 6.85%                 |         151 |
| D           | Relative Strength Top3        | weekly      |                3 | -1.90%         | 49.52%                   | -0.66% | 14.99%         | -15.65%       | 40.00%                        | -1.14%                          | -39.97%        |                    4.25714 |                   12.7714  | 33.98%                    | 2026-02                        | -14.58%                  | 2026-08                     | 8.57%                 |         151 |
| E           | Benchmark-aware Top3          | weekly      |                3 | -13.53%        | 49.52%                   | -4.92% | 14.99%         | -19.91%       | 37.14%                        | -1.53%                          | -40.89%        |                    4.27619 |                   12.8286  | 30.15%                    | 2026-02                        | -11.73%                  | 2026-08                     | 8.57%                 |         151 |
| F           | Leadership Rotation Overlay   | weekly      |                3 | -15.82%        | 49.52%                   | -5.80% | 14.99%         | -20.79%       | 40.00%                        | -1.54%                          | -42.16%        |                    4.21905 |                   12.6571  | 28.95%                    | 2026-02                        | -11.73%                  | 2026-08                     | 8.44%                 |         151 |

## Decision

- Did weekly rebalance improve excess return? No. Historical excess CAGR delta vs baseline: -24.57%; recent excess delta: -1.54%.
- Did relative strength improve excess return? Recent yes, historical no, so rejected. Historical excess CAGR delta vs baseline: -16.22%; recent excess delta: 17.84%.
- Did benchmark-aware selection improve excess return? Recent yes, historical no, so rejected. Historical excess CAGR delta vs baseline: -20.48%; recent excess delta: 11.71%.
- Did any policy beat BIST100 robustly? No under the current acceptance filter.
- Next paper-trading candidate: none. No policy passed both historical and recent acceptance criteria.
- Current one-month fixed hold should be kept for tracking, while weekly/relative-strength variants remain research-only.

## Acceptance Rule

A policy is only eligible if it improves both historical walk-forward excess return and the recent 2026-06 counterfactual excess return. Policies that only fix June 2026 are rejected.
