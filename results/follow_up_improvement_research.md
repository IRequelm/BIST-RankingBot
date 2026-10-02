# Follow-Up Improvement Research

This is research-only. Production follow-up tracking remains fixed and still reads reports/tracking_state.json.

## Policy Summary

| policy_id   | policy_name                   | frequency   |   portfolio_size | total_return   | benchmark_total_return   | cagr   | bist100_cagr   | excess_cagr   | monthly_win_rate_vs_bist100   | average_monthly_excess_return   | max_drawdown   |   average_monthly_turnover |   average_trades_per_month | transaction_cost_impact   | worst_underperformance_month   | worst_underperformance   | best_outperformance_month   | best_outperformance   |   intervals |
|:------------|:------------------------------|:------------|-----------------:|:---------------|:-------------------------|:-------|:---------------|:--------------|:------------------------------|:--------------------------------|:---------------|---------------------------:|---------------------------:|:--------------------------|:-------------------------------|:-------------------------|:----------------------------|:----------------------|------------:|
| A           | Current baseline monthly Top3 | monthly     |                3 | 74.27%         | 60.66%                   | 22.42% | 18.85%         | 3.57%         | 48.48%                        | 0.30%                           | -19.32%        |                    1.18182 |                    3.54545 | 13.90%                    | 2024-04                        | -10.59%                  | 2025-04                     | 15.27%                |          33 |
| B           | Weekly rebalance Top3         | weekly      |                3 | -9.30%         | 60.66%                   | -3.49% | 18.85%         | -22.34%       | 38.24%                        | -1.57%                          | -42.13%        |                    3.0098  |                    9.02941 | 20.70%                    | 2024-03                        | -12.42%                  | 2025-03                     | 12.41%                |         144 |
| C           | Weekly rebalance Top5         | weekly      |                5 | 4.01%          | 60.66%                   | 1.44%  | 18.85%         | -17.40%       | 41.18%                        | -1.22%                          | -36.45%        |                    2.7     |                   13.5     | 21.01%                    | 2024-08                        | -9.16%                   | 2026-09                     | 7.20%                 |         144 |
| D           | Relative Strength Top3        | weekly      |                3 | -6.81%         | 60.66%                   | -2.54% | 18.85%         | -21.38%       | 35.29%                        | -1.54%                          | -38.81%        |                    4.18627 |                   12.5588  | 30.63%                    | 2026-02                        | -14.58%                  | 2026-08                     | 8.57%                 |         144 |
| E           | Benchmark-aware Top3          | weekly      |                3 | -12.00%        | 60.66%                   | -4.55% | 18.85%         | -23.39%       | 32.35%                        | -1.72%                          | -39.49%        |                    4.18627 |                   12.5588  | 28.95%                    | 2026-02                        | -11.73%                  | 2026-08                     | 8.57%                 |         144 |
| F           | Leadership Rotation Overlay   | weekly      |                3 | -14.52%        | 60.66%                   | -5.55% | 18.85%         | -24.40%       | 38.24%                        | -1.74%                          | -42.16%        |                    4.06863 |                   12.2059  | 27.29%                    | 2026-02                        | -11.73%                  | 2026-08                     | 8.44%                 |         144 |

## Decision

- Did weekly rebalance improve excess return? Recent yes, historical no, so rejected. Historical excess CAGR delta vs baseline: -25.91%; recent excess delta: 4.87%.
- Did relative strength improve excess return? Recent yes, historical no, so rejected. Historical excess CAGR delta vs baseline: -24.95%; recent excess delta: 3.24%.
- Did benchmark-aware selection improve excess return? Recent yes, historical no, so rejected. Historical excess CAGR delta vs baseline: -26.96%; recent excess delta: 3.96%.
- Did any policy beat BIST100 robustly? No under the current acceptance filter.
- Next paper-trading candidate: none. No policy passed both historical and recent acceptance criteria.
- Current one-month fixed hold should be kept for tracking, while weekly/relative-strength variants remain research-only.

## Acceptance Rule

A policy is only eligible if it improves both historical walk-forward excess return and the recent 2026-06 counterfactual excess return. Policies that only fix June 2026 are rejected.
