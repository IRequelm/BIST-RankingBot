# Follow-Up Improvement Research

This is research-only. Production follow-up tracking remains fixed and still reads reports/tracking_state.json.

## Policy Summary

| policy_id   | policy_name                   | frequency   |   portfolio_size | total_return   | benchmark_total_return   | cagr   | bist100_cagr   | excess_cagr   | monthly_win_rate_vs_bist100   | average_monthly_excess_return   | max_drawdown   |   average_monthly_turnover |   average_trades_per_month | transaction_cost_impact   | worst_underperformance_month   | worst_underperformance   | best_outperformance_month   | best_outperformance   |   intervals |
|:------------|:------------------------------|:------------|-----------------:|:---------------|:-------------------------|:-------|:---------------|:--------------|:------------------------------|:--------------------------------|:---------------|---------------------------:|---------------------------:|:--------------------------|:-------------------------------|:-------------------------|:----------------------------|:----------------------|------------:|
| A           | Current baseline monthly Top3 | monthly     |                3 | 69.75%         | 83.38%                   | 23.18% | 26.99%         | -3.80%        | 43.33%                        | -0.18%                          | -19.32%        |                    1.23333 |                    3.7     | 12.79%                    | 2024-04                        | -10.59%                  | 2025-04                     | 15.27%                |          31 |
| B           | Weekly rebalance Top3         | weekly      |                3 | -11.95%        | 83.38%                   | -4.89% | 26.99%         | -31.88%       | 35.48%                        | -2.24%                          | -42.13%        |                    3.19355 |                    9.58065 | 19.37%                    | 2024-03                        | -12.42%                  | 2025-03                     | 12.41%                |         133 |
| C           | Weekly rebalance Top5         | weekly      |                5 | 10.76%         | 83.38%                   | 4.11%  | 26.99%         | -22.88%       | 38.71%                        | -1.55%                          | -36.45%        |                    2.74194 |                   13.7097  | 20.56%                    | 2024-08                        | -9.16%                   | 2026-03                     | 6.68%                 |         133 |
| D           | Relative Strength Top3        | weekly      |                3 | -5.58%         | 83.38%                   | -2.24% | 26.99%         | -29.22%       | 32.26%                        | -2.08%                          | -36.49%        |                    4.33333 |                   13       | 29.03%                    | 2026-02                        | -14.58%                  | 2025-03                     | 6.67%                 |         133 |
| E           | Benchmark-aware Top3          | weekly      |                3 | -11.48%        | 83.38%                   | -4.69% | 26.99%         | -31.68%       | 29.03%                        | -2.30%                          | -38.70%        |                    4.35484 |                   13.0645  | 27.40%                    | 2026-02                        | -11.73%                  | 2025-03                     | 6.25%                 |         133 |
| F           | Leadership Rotation Overlay   | weekly      |                3 | -16.08%        | 83.38%                   | -6.67% | 26.99%         | -33.66%       | 35.48%                        | -2.40%                          | -42.16%        |                    4.22581 |                   12.6774  | 25.16%                    | 2026-02                        | -11.73%                  | 2024-04                     | 7.40%                 |         133 |

## Decision

- Did weekly rebalance improve excess return? No. Historical excess CAGR delta vs baseline: -28.08%; recent excess delta: -8.88%.
- Did relative strength improve excess return? No. Historical excess CAGR delta vs baseline: -25.42%; recent excess delta: -6.31%.
- Did benchmark-aware selection improve excess return? No. Historical excess CAGR delta vs baseline: -27.87%; recent excess delta: -6.31%.
- Did any policy beat BIST100 robustly? No under the current acceptance filter.
- Next paper-trading candidate: none. No policy passed both historical and recent acceptance criteria.
- Current one-month fixed hold should be kept for tracking, while weekly/relative-strength variants remain research-only.

## Acceptance Rule

A policy is only eligible if it improves both historical walk-forward excess return and the recent 2026-06 counterfactual excess return. Policies that only fix June 2026 are rejected.
