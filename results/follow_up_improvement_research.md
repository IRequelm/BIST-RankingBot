# Follow-Up Improvement Research

This is research-only. Production follow-up tracking remains fixed and still reads reports/tracking_state.json.

## Policy Summary

| policy_id   | policy_name                   | frequency   |   portfolio_size | total_return   | benchmark_total_return   | cagr   | bist100_cagr   | excess_cagr   | monthly_win_rate_vs_bist100   | average_monthly_excess_return   | max_drawdown   |   average_monthly_turnover |   average_trades_per_month | transaction_cost_impact   | worst_underperformance_month   | worst_underperformance   | best_outperformance_month   | best_outperformance   |   intervals |
|:------------|:------------------------------|:------------|-----------------:|:---------------|:-------------------------|:-------|:---------------|:--------------|:------------------------------|:--------------------------------|:---------------|---------------------------:|---------------------------:|:--------------------------|:-------------------------------|:-------------------------|:----------------------------|:----------------------|------------:|
| A           | Current baseline monthly Top3 | monthly     |                3 | 65.67%         | 85.45%                   | 21.88% | 27.38%         | -5.51%        | 43.33%                        | -0.30%                          | -19.32%        |                    1.23333 |                    3.7     | 12.49%                    | 2024-04                        | -10.59%                  | 2025-04                     | 15.27%                |          31 |
| B           | Weekly rebalance Top3         | weekly      |                3 | -10.89%        | 85.45%                   | -4.42% | 27.38%         | -31.80%       | 35.48%                        | -2.24%                          | -42.13%        |                    3.19355 |                    9.58065 | 19.60%                    | 2024-03                        | -12.42%                  | 2025-03                     | 12.41%                |         134 |
| C           | Weekly rebalance Top5         | weekly      |                5 | 11.73%         | 85.45%                   | 4.44%  | 27.38%         | -22.94%       | 38.71%                        | -1.56%                          | -36.45%        |                    2.74194 |                   13.7097  | 20.73%                    | 2024-08                        | -9.16%                   | 2026-03                     | 6.68%                 |         134 |
| D           | Relative Strength Top3        | weekly      |                3 | -5.50%         | 85.45%                   | -2.19% | 27.38%         | -29.57%       | 32.26%                        | -2.11%                          | -36.49%        |                    4.35484 |                   13.0645  | 29.22%                    | 2026-02                        | -14.58%                  | 2025-03                     | 6.67%                 |         134 |
| E           | Benchmark-aware Top3          | weekly      |                3 | -11.41%        | 85.45%                   | -4.64% | 27.38%         | -32.02%       | 29.03%                        | -2.34%                          | -38.70%        |                    4.37634 |                   13.129   | 27.58%                    | 2026-02                        | -11.73%                  | 2025-03                     | 6.25%                 |         134 |
| F           | Leadership Rotation Overlay   | weekly      |                3 | -15.12%        | 85.45%                   | -6.22% | 27.38%         | -33.61%       | 35.48%                        | -2.40%                          | -42.16%        |                    4.24731 |                   12.7419  | 25.60%                    | 2026-02                        | -11.73%                  | 2024-04                     | 7.40%                 |         134 |

## Decision

- Did weekly rebalance improve excess return? No. Historical excess CAGR delta vs baseline: -26.30%; recent excess delta: -4.63%.
- Did relative strength improve excess return? No. Historical excess CAGR delta vs baseline: -24.07%; recent excess delta: -3.14%.
- Did benchmark-aware selection improve excess return? No. Historical excess CAGR delta vs baseline: -26.51%; recent excess delta: -3.14%.
- Did any policy beat BIST100 robustly? No under the current acceptance filter.
- Next paper-trading candidate: none. No policy passed both historical and recent acceptance criteria.
- Current one-month fixed hold should be kept for tracking, while weekly/relative-strength variants remain research-only.

## Acceptance Rule

A policy is only eligible if it improves both historical walk-forward excess return and the recent 2026-06 counterfactual excess return. Policies that only fix June 2026 are rejected.
