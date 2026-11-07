# Follow-Up Improvement Research

This is research-only. Production follow-up tracking remains fixed and still reads reports/tracking_state.json.

## Policy Summary

| policy_id   | policy_name                   | frequency   |   portfolio_size | total_return   | benchmark_total_return   | cagr   | bist100_cagr   | excess_cagr   | monthly_win_rate_vs_bist100   | average_monthly_excess_return   | max_drawdown   |   average_monthly_turnover |   average_trades_per_month | transaction_cost_impact   | worst_underperformance_month   | worst_underperformance   | best_outperformance_month   | best_outperformance   |   intervals |
|:------------|:------------------------------|:------------|-----------------:|:---------------|:-------------------------|:-------|:---------------|:--------------|:------------------------------|:--------------------------------|:---------------|---------------------------:|---------------------------:|:--------------------------|:-------------------------------|:-------------------------|:----------------------------|:----------------------|------------:|
| A           | Current baseline monthly Top3 | monthly     |                3 | 51.86%         | 50.61%                   | 15.82% | 15.48%         | 0.34%         | 44.12%                        | 0.09%                           | -19.32%        |                    1.2451  |                    3.73529 | 13.25%                    | 2024-04                        | -10.59%                  | 2025-04                     | 15.27%                |          35 |
| B           | Weekly rebalance Top3         | weekly      |                3 | -22.24%        | 50.61%                   | -8.46% | 15.48%         | -23.94%       | 40.00%                        | -1.78%                          | -42.13%        |                    3.0381  |                    9.11429 | 18.54%                    | 2024-03                        | -12.42%                  | 2025-03                     | 12.41%                |         149 |
| C           | Weekly rebalance Top5         | weekly      |                5 | 0.83%          | 50.61%                   | 0.29%  | 15.48%         | -15.19%       | 42.86%                        | -1.10%                          | -36.45%        |                    2.65714 |                   13.2857  | 20.66%                    | 2024-08                        | -9.16%                   | 2026-09                     | 6.85%                 |         149 |
| D           | Relative Strength Top3        | weekly      |                3 | -9.69%         | 50.61%                   | -3.52% | 15.48%         | -19.00%       | 37.14%                        | -1.41%                          | -39.97%        |                    4.21905 |                   12.6571  | 30.98%                    | 2026-02                        | -14.58%                  | 2026-08                     | 8.57%                 |         149 |
| E           | Benchmark-aware Top3          | weekly      |                3 | -16.53%        | 50.61%                   | -6.16% | 15.48%         | -21.64%       | 34.29%                        | -1.65%                          | -40.89%        |                    4.21905 |                   12.6571  | 28.67%                    | 2026-02                        | -11.73%                  | 2026-08                     | 8.57%                 |         149 |
| F           | Leadership Rotation Overlay   | weekly      |                3 | -18.74%        | 50.61%                   | -7.04% | 15.48%         | -22.52%       | 37.14%                        | -1.67%                          | -42.16%        |                    4.1619  |                   12.4857  | 27.52%                    | 2026-02                        | -11.73%                  | 2026-08                     | 8.44%                 |         149 |

## Decision

- Did weekly rebalance improve excess return? Recent yes, historical no, so rejected. Historical excess CAGR delta vs baseline: -24.28%; recent excess delta: 0.38%.
- Did relative strength improve excess return? Recent yes, historical no, so rejected. Historical excess CAGR delta vs baseline: -19.34%; recent excess delta: 9.88%.
- Did benchmark-aware selection improve excess return? Recent yes, historical no, so rejected. Historical excess CAGR delta vs baseline: -21.98%; recent excess delta: 8.54%.
- Did any policy beat BIST100 robustly? No under the current acceptance filter.
- Next paper-trading candidate: none. No policy passed both historical and recent acceptance criteria.
- Current one-month fixed hold should be kept for tracking, while weekly/relative-strength variants remain research-only.

## Acceptance Rule

A policy is only eligible if it improves both historical walk-forward excess return and the recent 2026-06 counterfactual excess return. Policies that only fix June 2026 are rejected.
