# Benchmark-Core Portfolio Research

Research-only. Production tracking_state.json and live follow-up behavior are unchanged.

## Policy Results

| policy_id   | policy_name                   |   months | total_return   | bist100_total_return   | cagr   | bist100_cagr   | excess_cagr   | max_drawdown   | bist100_max_drawdown   |   sharpe_proxy | monthly_win_rate_vs_bist100   | average_monthly_excess_return   | worst_month   | worst_month_return   | best_month   | best_month_return   | average_turnover   |   total_turnover | active_allocation_average   |   active_overlay_months | transaction_cost_impact   |
|:------------|:------------------------------|---------:|:---------------|:-----------------------|:-------|:---------------|:--------------|:---------------|:-----------------------|---------------:|:------------------------------|:--------------------------------|:--------------|:---------------------|:-------------|:--------------------|:-------------------|-----------------:|:----------------------------|------------------------:|:--------------------------|
| A           | BIST100 only                  |       33 | 90.25%         | 90.25%                 | 27.06% | 27.06%         | 0.00%         | -17.72%        | -17.72%                |        1.1733  | 0.00%                         | 0.00%                           | 2024-09       | -7.51%               | 2026-01      | 18.46%              | 0.00%              |          0       | 0.00%                       |                       0 | 0.00%                     |
| B           | Current active Top3 only      |       33 | 88.49%         | 90.25%                 | 26.62% | 27.06%         | -0.44%        | -19.32%        | -17.72%                |        1.01293 | 45.45%                        | 0.05%                           | 2024-08       | -10.88%              | 2026-01      | 16.86%              | 118.18%            |         39       | 100.00%                     |                      33 | 7.80%                     |
| C           | 80/20 benchmark-core          |       33 | 91.19%         | 90.25%                 | 27.29% | 27.06%         | 0.23%         | -18.00%        | -17.72%                |        1.19312 | 45.45%                        | 0.01%                           | 2024-08       | -7.27%               | 2026-01      | 18.14%              | 23.64%             |          7.8     | 20.00%                      |                      33 | 1.56%                     |
| D           | 70/30 benchmark-core          |       33 | 91.41%         | 90.25%                 | 27.34% | 27.06%         | 0.29%         | -18.15%        | -17.72%                |        1.19117 | 45.45%                        | 0.02%                           | 2024-08       | -7.72%               | 2026-01      | 17.98%              | 35.45%             |         11.7     | 30.00%                      |                      33 | 2.34%                     |
| E           | 50/50 benchmark-core          |       33 | 91.37%         | 90.25%                 | 27.33% | 27.06%         | 0.28%         | -18.46%        | -17.72%                |        1.16466 | 45.45%                        | 0.03%                           | 2024-08       | -8.63%               | 2026-01      | 17.66%              | 59.09%             |         19.5     | 50.00%                      |                      33 | 3.90%                     |
| F           | Conditional active overlay    |       33 | 88.94%         | 90.25%                 | 26.73% | 27.06%         | -0.33%        | -18.54%        | -17.72%                |        1.15592 | 18.18%                        | -0.02%                          | 2024-09       | -7.55%               | 2026-01      | 18.14%              | 12.32%             |          4.06667 | 7.88%                       |                      13 | 0.81%                     |
| G           | Drawdown-aware active overlay |       33 | 93.62%         | 90.25%                 | 27.89% | 27.06%         | 0.83%         | -18.00%        | -17.72%                |        1.21197 | 33.33%                        | 0.05%                           | 2024-08       | -7.27%               | 2026-01      | 18.46%              | 17.58%             |          5.8     | 13.94%                      |                      23 | 1.16%                     |

## Decision

- Is pure active Top3 still worth paper trading? No. It delivered -0.44% excess CAGR versus BIST100 in this walk-forward.
- Does benchmark-core improve robustness? No. Core policies reduce active drawdown and tracking error mechanically, but must be checked against BIST100 drag.
- Best balance of CAGR, drawdown, and excess return: Policy G — Drawdown-aware active overlay (CAGR 27.89%, max drawdown -18.00%, excess CAGR 0.83%).
- Best fixed benchmark-core allocation if an active sleeve must be retained: Policy D — 70/30 benchmark-core (active allocation 30.00%, excess CAGR 0.29%).
- Best dynamic benchmark-core/satellite variant: Policy G — Drawdown-aware active overlay (active allocation average 13.94%, excess CAGR 0.83%).
- Next paper-trading candidate: Policy G — Drawdown-aware active overlay.
- Active stock-picking should be demoted from main strategy to satellite only unless it regains persistent benchmark-relative edge.

## Acceptance Criteria

A new candidate must improve robustness versus pure active Top3 and avoid material historical underperformance versus BIST100. June 2026 improvement alone is not sufficient.
