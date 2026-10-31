# Benchmark-Core Portfolio Research

Research-only. Production tracking_state.json and live follow-up behavior are unchanged.

## Policy Results

| policy_id   | policy_name                   |   months | total_return   | bist100_total_return   | cagr   | bist100_cagr   | excess_cagr   | max_drawdown   | bist100_max_drawdown   |   sharpe_proxy | monthly_win_rate_vs_bist100   | average_monthly_excess_return   | worst_month   | worst_month_return   | best_month   | best_month_return   | average_turnover   |   total_turnover | active_allocation_average   |   active_overlay_months | transaction_cost_impact   |
|:------------|:------------------------------|---------:|:---------------|:-----------------------|:-------|:---------------|:--------------|:---------------|:-----------------------|---------------:|:------------------------------|:--------------------------------|:--------------|:---------------------|:-------------|:--------------------|:-------------------|-----------------:|:----------------------------|------------------------:|:--------------------------|
| A           | BIST100 only                  |       34 | 41.12%         | 41.12%                 | 12.97% | 12.97%         | 0.00%         | -25.12%        | -25.12%                |       0.60652  | 0.00%                         | 0.00%                           | 2026-09       | -13.92%              | 2026-01      | 18.46%              | 0.00%              |          0       | 0.00%                       |                       0 | 0.00%                     |
| B           | Current active Top3 only      |       34 | 54.12%         | 41.12%                 | 16.54% | 12.97%         | 3.58%         | -19.32%        | -25.12%                |       0.691714 | 47.06%                        | 0.31%                           | 2024-08       | -10.88%              | 2026-01      | 16.86%              | 120.59%            |         41       | 100.00%                     |                      34 | 8.20%                     |
| C           | 80/20 benchmark-core          |       34 | 44.78%         | 41.12%                 | 13.99% | 12.97%         | 1.03%         | -22.40%        | -25.12%                |       0.653157 | 47.06%                        | 0.06%                           | 2026-09       | -11.99%              | 2026-01      | 18.14%              | 24.12%             |          8.2     | 20.00%                      |                      34 | 1.64%                     |
| D           | 70/30 benchmark-core          |       34 | 46.41%         | 41.12%                 | 14.45% | 12.97%         | 1.48%         | -21.03%        | -25.12%                |       0.671547 | 47.06%                        | 0.09%                           | 2026-09       | -11.02%              | 2026-01      | 17.98%              | 36.18%             |         12.3     | 30.00%                      |                      34 | 2.46%                     |
| E           | 50/50 benchmark-core          |       34 | 49.30%         | 41.12%                 | 15.24% | 12.97%         | 2.28%         | -18.46%        | -25.12%                |       0.696352 | 47.06%                        | 0.15%                           | 2026-10       | -10.09%              | 2026-01      | 17.66%              | 60.29%             |         20.5     | 50.00%                      |                      34 | 4.10%                     |
| F           | Conditional active overlay    |       34 | 43.26%         | 41.12%                 | 13.57% | 12.97%         | 0.60%         | -22.73%        | -25.12%                |       0.631847 | 20.59%                        | 0.04%                           | 2026-10       | -12.20%              | 2026-01      | 18.14%              | 12.55%             |          4.26667 | 7.65%                       |                      13 | 0.85%                     |
| G           | Drawdown-aware active overlay |       34 | 44.56%         | 41.12%                 | 13.93% | 12.97%         | 0.97%         | -23.49%        | -25.12%                |       0.651991 | 32.35%                        | 0.06%                           | 2026-09       | -11.98%              | 2026-01      | 18.46%              | 17.84%             |          6.06667 | 13.53%                      |                      23 | 1.21%                     |

## Decision

- Is pure active Top3 still worth paper trading? Only as a monitored sleeve. It delivered 3.58% excess CAGR versus BIST100 in this walk-forward.
- Does benchmark-core improve robustness? No. Core policies reduce active drawdown and tracking error mechanically, but must be checked against BIST100 drag.
- Best balance of CAGR, drawdown, and excess return: Policy E — 50/50 benchmark-core (CAGR 15.24%, max drawdown -18.46%, excess CAGR 2.28%).
- Best fixed benchmark-core allocation if an active sleeve must be retained: Policy E — 50/50 benchmark-core (active allocation 50.00%, excess CAGR 2.28%).
- Best dynamic benchmark-core/satellite variant: Policy E — 50/50 benchmark-core (active allocation average 50.00%, excess CAGR 2.28%).
- Next paper-trading candidate: Policy E — 50/50 benchmark-core.
- Active stock-picking should be demoted from main strategy to satellite only unless it regains persistent benchmark-relative edge.

## Acceptance Criteria

A new candidate must improve robustness versus pure active Top3 and avoid material historical underperformance versus BIST100. June 2026 improvement alone is not sufficient.
