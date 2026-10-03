# Benchmark-Core Portfolio Research

Research-only. Production tracking_state.json and live follow-up behavior are unchanged.

## Policy Results

| policy_id   | policy_name                   |   months | total_return   | bist100_total_return   | cagr   | bist100_cagr   | excess_cagr   | max_drawdown   | bist100_max_drawdown   |   sharpe_proxy | monthly_win_rate_vs_bist100   | average_monthly_excess_return   | worst_month   | worst_month_return   | best_month   | best_month_return   | average_turnover   |   total_turnover | active_allocation_average   |   active_overlay_months | transaction_cost_impact   |
|:------------|:------------------------------|---------:|:---------------|:-----------------------|:-------|:---------------|:--------------|:---------------|:-----------------------|---------------:|:------------------------------|:--------------------------------|:--------------|:---------------------|:-------------|:--------------------|:-------------------|-----------------:|:----------------------------|------------------------:|:--------------------------|
| A           | BIST100 only                  |       34 | 60.94%         | 60.94%                 | 18.90% | 18.90%         | 0.00%         | -17.72%        | -17.72%                |       0.824764 | 0.00%                         | 0.00%                           | 2026-09       | -13.92%              | 2026-01      | 18.46%              | 0.00%              |          0       | 0.00%                       |                       0 | 0.00%                     |
| B           | Current active Top3 only      |       34 | 77.00%         | 60.94%                 | 23.09% | 18.90%         | 4.19%         | -19.32%        | -17.72%                |       0.902192 | 47.06%                        | 0.33%                           | 2024-08       | -10.88%              | 2026-01      | 16.86%              | 116.67%            |         39.6667  | 100.00%                     |                      34 | 7.93%                     |
| C           | 80/20 benchmark-core          |       34 | 65.29%         | 60.94%                 | 20.06% | 18.90%         | 1.16%         | -18.00%        | -17.72%                |       0.883029 | 47.06%                        | 0.07%                           | 2026-09       | -11.99%              | 2026-01      | 18.14%              | 23.33%             |          7.93333 | 20.00%                      |                      34 | 1.59%                     |
| D           | 70/30 benchmark-core          |       34 | 67.27%         | 60.94%                 | 20.58% | 18.90%         | 1.68%         | -18.15%        | -17.72%                |       0.904792 | 47.06%                        | 0.10%                           | 2026-09       | -11.02%              | 2026-01      | 17.98%              | 35.00%             |         11.9     | 30.00%                      |                      34 | 2.38%                     |
| E           | 50/50 benchmark-core          |       34 | 70.79%         | 60.94%                 | 21.50% | 18.90%         | 2.60%         | -18.46%        | -17.72%                |       0.930725 | 47.06%                        | 0.17%                           | 2026-09       | -9.10%               | 2026-01      | 17.66%              | 58.33%             |         19.8333  | 50.00%                      |                      34 | 3.97%                     |
| F           | Conditional active overlay    |       34 | 63.38%         | 60.94%                 | 19.55% | 18.90%         | 0.65%         | -18.54%        | -17.72%                |       0.855326 | 20.59%                        | 0.04%                           | 2026-09       | -11.99%              | 2026-01      | 18.14%              | 12.55%             |          4.26667 | 7.65%                       |                      13 | 0.85%                     |
| G           | Drawdown-aware active overlay |       34 | 67.40%         | 60.94%                 | 20.61% | 18.90%         | 1.72%         | -18.00%        | -17.72%                |       0.900821 | 35.29%                        | 0.11%                           | 2026-09       | -11.99%              | 2026-01      | 18.46%              | 17.45%             |          5.93333 | 14.12%                      |                      24 | 1.19%                     |

## Decision

- Is pure active Top3 still worth paper trading? Only as a monitored sleeve. It delivered 4.19% excess CAGR versus BIST100 in this walk-forward.
- Does benchmark-core improve robustness? No. Core policies reduce active drawdown and tracking error mechanically, but must be checked against BIST100 drag.
- Best balance of CAGR, drawdown, and excess return: Policy E — 50/50 benchmark-core (CAGR 21.50%, max drawdown -18.46%, excess CAGR 2.60%).
- Best fixed benchmark-core allocation if an active sleeve must be retained: Policy E — 50/50 benchmark-core (active allocation 50.00%, excess CAGR 2.60%).
- Best dynamic benchmark-core/satellite variant: Policy E — 50/50 benchmark-core (active allocation average 50.00%, excess CAGR 2.60%).
- Next paper-trading candidate: Policy E — 50/50 benchmark-core.
- Active stock-picking should be demoted from main strategy to satellite only unless it regains persistent benchmark-relative edge.

## Acceptance Criteria

A new candidate must improve robustness versus pure active Top3 and avoid material historical underperformance versus BIST100. June 2026 improvement alone is not sufficient.
