# Benchmark-Core Portfolio Research

Research-only. Production tracking_state.json and live follow-up behavior are unchanged.

## Policy Results

| policy_id   | policy_name                   |   months | total_return   | bist100_total_return   | cagr   | bist100_cagr   | excess_cagr   | max_drawdown   | bist100_max_drawdown   |   sharpe_proxy | monthly_win_rate_vs_bist100   | average_monthly_excess_return   | worst_month   | worst_month_return   | best_month   | best_month_return   | average_turnover   |   total_turnover | active_allocation_average   |   active_overlay_months | transaction_cost_impact   |
|:------------|:------------------------------|---------:|:---------------|:-----------------------|:-------|:---------------|:--------------|:---------------|:-----------------------|---------------:|:------------------------------|:--------------------------------|:--------------|:---------------------|:-------------|:--------------------|:-------------------|-----------------:|:----------------------------|------------------------:|:--------------------------|
| A           | BIST100 only                  |       33 | 69.19%         | 69.19%                 | 21.24% | 21.24%         | 0.00%         | -17.72%        | -17.72%                |       0.941711 | 0.00%                         | 0.00%                           | 2026-09       | -9.34%               | 2026-01      | 18.46%              | 0.00%              |          0       | 0.00%                       |                       0 | 0.00%                     |
| B           | Current active Top3 only      |       33 | 82.96%         | 69.19%                 | 24.77% | 21.24%         | 3.53%         | -19.32%        | -17.72%                |       0.968457 | 48.48%                        | 0.30%                           | 2024-08       | -10.88%              | 2026-01      | 16.86%              | 118.18%            |         39       | 100.00%                     |                      33 | 7.80%                     |
| C           | 80/20 benchmark-core          |       33 | 73.12%         | 69.19%                 | 22.27% | 21.24%         | 1.03%         | -18.00%        | -17.72%                |       0.995927 | 48.48%                        | 0.06%                           | 2026-09       | -7.71%               | 2026-01      | 18.14%              | 23.64%             |          7.8     | 20.00%                      |                      33 | 1.56%                     |
| D           | 70/30 benchmark-core          |       33 | 74.88%         | 69.19%                 | 22.72% | 21.24%         | 1.48%         | -18.15%        | -17.72%                |       1.01378  | 48.48%                        | 0.09%                           | 2024-08       | -7.72%               | 2026-01      | 17.98%              | 35.45%             |         11.7     | 30.00%                      |                      33 | 2.34%                     |
| E           | 50/50 benchmark-core          |       33 | 77.96%         | 69.19%                 | 23.51% | 21.24%         | 2.26%         | -18.46%        | -17.72%                |       1.02891  | 48.48%                        | 0.15%                           | 2024-08       | -8.63%               | 2026-01      | 17.66%              | 59.09%             |         19.5     | 50.00%                      |                      33 | 3.90%                     |
| F           | Conditional active overlay    |       33 | 71.09%         | 69.19%                 | 21.74% | 21.24%         | 0.50%         | -18.54%        | -17.72%                |       0.964196 | 21.21%                        | 0.03%                           | 2026-09       | -7.71%               | 2026-01      | 18.14%              | 12.32%             |          4.06667 | 7.88%                       |                      13 | 0.81%                     |
| G           | Drawdown-aware active overlay |       33 | 75.33%         | 69.19%                 | 22.84% | 21.24%         | 1.59%         | -18.00%        | -17.72%                |       1.01443  | 36.36%                        | 0.10%                           | 2026-09       | -7.71%               | 2026-01      | 18.46%              | 17.58%             |          5.8     | 13.94%                      |                      23 | 1.16%                     |

## Decision

- Is pure active Top3 still worth paper trading? Only as a monitored sleeve. It delivered 3.53% excess CAGR versus BIST100 in this walk-forward.
- Does benchmark-core improve robustness? No. Core policies reduce active drawdown and tracking error mechanically, but must be checked against BIST100 drag.
- Best balance of CAGR, drawdown, and excess return: Policy E — 50/50 benchmark-core (CAGR 23.51%, max drawdown -18.46%, excess CAGR 2.26%).
- Best fixed benchmark-core allocation if an active sleeve must be retained: Policy E — 50/50 benchmark-core (active allocation 50.00%, excess CAGR 2.26%).
- Best dynamic benchmark-core/satellite variant: Policy E — 50/50 benchmark-core (active allocation average 50.00%, excess CAGR 2.26%).
- Next paper-trading candidate: Policy E — 50/50 benchmark-core.
- Active stock-picking should be demoted from main strategy to satellite only unless it regains persistent benchmark-relative edge.

## Acceptance Criteria

A new candidate must improve robustness versus pure active Top3 and avoid material historical underperformance versus BIST100. June 2026 improvement alone is not sufficient.
