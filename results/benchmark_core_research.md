# Benchmark-Core Portfolio Research

Research-only. Production tracking_state.json and live follow-up behavior are unchanged.

## Policy Results

| policy_id   | policy_name                   |   months | total_return   | bist100_total_return   | cagr   | bist100_cagr   | excess_cagr   | max_drawdown   | bist100_max_drawdown   |   sharpe_proxy | monthly_win_rate_vs_bist100   | average_monthly_excess_return   | worst_month   | worst_month_return   | best_month   | best_month_return   | average_turnover   |   total_turnover | active_allocation_average   |   active_overlay_months | transaction_cost_impact   |
|:------------|:------------------------------|---------:|:---------------|:-----------------------|:-------|:---------------|:--------------|:---------------|:-----------------------|---------------:|:------------------------------|:--------------------------------|:--------------|:---------------------|:-------------|:--------------------|:-------------------|-----------------:|:----------------------------|------------------------:|:--------------------------|
| A           | BIST100 only                  |       33 | 69.04%         | 69.04%                 | 21.23% | 21.23%         | 0.00%         | -17.72%        | -17.72%                |       0.939909 | 0.00%                         | 0.00%                           | 2026-09       | -9.42%               | 2026-01      | 18.46%              | 0.00%              |          0       | 0.00%                       |                       0 | 0.00%                     |
| B           | Current active Top3 only      |       33 | 86.38%         | 69.04%                 | 25.65% | 21.23%         | 4.42%         | -19.32%        | -17.72%                |       0.996494 | 48.48%                        | 0.36%                           | 2024-08       | -10.88%              | 2026-01      | 16.86%              | 118.18%            |         39       | 100.00%                     |                      33 | 7.80%                     |
| C           | 80/20 benchmark-core          |       33 | 73.70%         | 69.04%                 | 22.44% | 21.23%         | 1.21%         | -18.00%        | -17.72%                |       1.00302  | 48.48%                        | 0.07%                           | 2026-09       | -7.41%               | 2026-01      | 18.14%              | 23.64%             |          7.8     | 20.00%                      |                      33 | 1.56%                     |
| D           | 70/30 benchmark-core          |       33 | 75.82%         | 69.04%                 | 22.99% | 21.23%         | 1.76%         | -18.15%        | -17.72%                |       1.02509  | 48.48%                        | 0.11%                           | 2024-08       | -7.72%               | 2026-01      | 17.98%              | 35.45%             |         11.7     | 30.00%                      |                      33 | 2.34%                     |
| E           | 50/50 benchmark-core          |       33 | 79.62%         | 69.04%                 | 23.96% | 21.23%         | 2.73%         | -18.46%        | -17.72%                |       1.04747  | 48.48%                        | 0.18%                           | 2024-08       | -8.63%               | 2026-01      | 17.66%              | 59.09%             |         19.5     | 50.00%                      |                      33 | 3.90%                     |
| F           | Conditional active overlay    |       33 | 71.66%         | 69.04%                 | 21.92% | 21.23%         | 0.69%         | -18.54%        | -17.72%                |       0.971061 | 21.21%                        | 0.04%                           | 2024-09       | -7.55%               | 2026-01      | 18.14%              | 12.32%             |          4.06667 | 7.88%                       |                      13 | 0.81%                     |
| G           | Drawdown-aware active overlay |       33 | 75.92%         | 69.04%                 | 23.02% | 21.23%         | 1.79%         | -18.00%        | -17.72%                |       1.02154  | 36.36%                        | 0.11%                           | 2026-09       | -7.41%               | 2026-01      | 18.46%              | 17.58%             |          5.8     | 13.94%                      |                      23 | 1.16%                     |

## Decision

- Is pure active Top3 still worth paper trading? Only as a monitored sleeve. It delivered 4.42% excess CAGR versus BIST100 in this walk-forward.
- Does benchmark-core improve robustness? No. Core policies reduce active drawdown and tracking error mechanically, but must be checked against BIST100 drag.
- Best balance of CAGR, drawdown, and excess return: Policy E — 50/50 benchmark-core (CAGR 23.96%, max drawdown -18.46%, excess CAGR 2.73%).
- Best fixed benchmark-core allocation if an active sleeve must be retained: Policy E — 50/50 benchmark-core (active allocation 50.00%, excess CAGR 2.73%).
- Best dynamic benchmark-core/satellite variant: Policy E — 50/50 benchmark-core (active allocation average 50.00%, excess CAGR 2.73%).
- Next paper-trading candidate: Policy E — 50/50 benchmark-core.
- Active stock-picking should be demoted from main strategy to satellite only unless it regains persistent benchmark-relative edge.

## Acceptance Criteria

A new candidate must improve robustness versus pure active Top3 and avoid material historical underperformance versus BIST100. June 2026 improvement alone is not sufficient.
