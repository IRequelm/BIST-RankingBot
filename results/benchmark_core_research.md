# Benchmark-Core Portfolio Research

Research-only. Production tracking_state.json and live follow-up behavior are unchanged.

## Policy Results

| policy_id   | policy_name                   |   months | total_return   | bist100_total_return   | cagr   | bist100_cagr   | excess_cagr   | max_drawdown   | bist100_max_drawdown   |   sharpe_proxy | monthly_win_rate_vs_bist100   | average_monthly_excess_return   | worst_month   | worst_month_return   | best_month   | best_month_return   | average_turnover   |   total_turnover | active_allocation_average   |   active_overlay_months | transaction_cost_impact   |
|:------------|:------------------------------|---------:|:---------------|:-----------------------|:-------|:---------------|:--------------|:---------------|:-----------------------|---------------:|:------------------------------|:--------------------------------|:--------------|:---------------------|:-------------|:--------------------|:-------------------|-----------------:|:----------------------------|------------------------:|:--------------------------|
| A           | BIST100 only                  |       33 | 56.70%         | 56.70%                 | 17.79% | 17.79%         | 0.00%         | -17.72%        | -17.72%                |       0.785071 | 0.00%                         | 0.00%                           | 2026-09       | -16.04%              | 2026-01      | 18.46%              | 0.00%              |          0       | 0.00%                       |                       0 | 0.00%                     |
| B           | Current active Top3 only      |       33 | 77.27%         | 56.70%                 | 23.21% | 17.79%         | 5.42%         | -19.32%        | -17.72%                |       0.918583 | 48.48%                        | 0.41%                           | 2024-08       | -10.88%              | 2026-01      | 16.86%              | 118.18%            |         39       | 100.00%                     |                      33 | 7.80%                     |
| C           | 80/20 benchmark-core          |       33 | 61.93%         | 56.70%                 | 19.21% | 17.79%         | 1.42%         | -18.00%        | -17.72%                |       0.854364 | 48.48%                        | 0.08%                           | 2026-09       | -13.68%              | 2026-01      | 18.14%              | 23.64%             |          7.8     | 20.00%                      |                      33 | 1.56%                     |
| D           | 70/30 benchmark-core          |       33 | 64.35%         | 56.70%                 | 19.85% | 17.79%         | 2.06%         | -18.15%        | -17.72%                |       0.882382 | 48.48%                        | 0.12%                           | 2026-09       | -12.50%              | 2026-01      | 17.98%              | 35.45%             |         11.7     | 30.00%                      |                      33 | 2.34%                     |
| E           | 50/50 benchmark-core          |       33 | 68.79%         | 56.70%                 | 21.02% | 17.79%         | 3.23%         | -18.46%        | -17.72%                |       0.921248 | 48.48%                        | 0.21%                           | 2026-09       | -10.15%              | 2026-01      | 17.66%              | 59.09%             |         19.5     | 50.00%                      |                      33 | 3.90%                     |
| F           | Conditional active overlay    |       33 | 60.03%         | 56.70%                 | 18.70% | 17.79%         | 0.91%         | -18.54%        | -17.72%                |       0.827166 | 21.21%                        | 0.05%                           | 2026-09       | -13.68%              | 2026-01      | 18.14%              | 12.32%             |          4.06667 | 7.88%                       |                      13 | 0.81%                     |
| G           | Drawdown-aware active overlay |       33 | 63.99%         | 56.70%                 | 19.76% | 17.79%         | 1.97%         | -18.00%        | -17.72%                |       0.872282 | 36.36%                        | 0.12%                           | 2026-09       | -13.68%              | 2026-01      | 18.46%              | 17.58%             |          5.8     | 13.94%                      |                      23 | 1.16%                     |

## Decision

- Is pure active Top3 still worth paper trading? Only as a monitored sleeve. It delivered 5.42% excess CAGR versus BIST100 in this walk-forward.
- Does benchmark-core improve robustness? No. Core policies reduce active drawdown and tracking error mechanically, but must be checked against BIST100 drag.
- Best balance of CAGR, drawdown, and excess return: Policy E — 50/50 benchmark-core (CAGR 21.02%, max drawdown -18.46%, excess CAGR 3.23%).
- Best fixed benchmark-core allocation if an active sleeve must be retained: Policy E — 50/50 benchmark-core (active allocation 50.00%, excess CAGR 3.23%).
- Best dynamic benchmark-core/satellite variant: Policy E — 50/50 benchmark-core (active allocation average 50.00%, excess CAGR 3.23%).
- Next paper-trading candidate: Policy E — 50/50 benchmark-core.
- Active stock-picking should be demoted from main strategy to satellite only unless it regains persistent benchmark-relative edge.

## Acceptance Criteria

A new candidate must improve robustness versus pure active Top3 and avoid material historical underperformance versus BIST100. June 2026 improvement alone is not sufficient.
