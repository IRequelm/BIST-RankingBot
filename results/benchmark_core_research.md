# Benchmark-Core Portfolio Research

Research-only. Production tracking_state.json and live follow-up behavior are unchanged.

## Policy Results

| policy_id   | policy_name                   |   months | total_return   | bist100_total_return   | cagr   | bist100_cagr   | excess_cagr   | max_drawdown   | bist100_max_drawdown   |   sharpe_proxy | monthly_win_rate_vs_bist100   | average_monthly_excess_return   | worst_month   | worst_month_return   | best_month   | best_month_return   | average_turnover   |   total_turnover | active_allocation_average   |   active_overlay_months | transaction_cost_impact   |
|:------------|:------------------------------|---------:|:---------------|:-----------------------|:-------|:---------------|:--------------|:---------------|:-----------------------|---------------:|:------------------------------|:--------------------------------|:--------------|:---------------------|:-------------|:--------------------|:-------------------|-----------------:|:----------------------------|------------------------:|:--------------------------|
| A           | BIST100 only                  |       31 | 84.67%         | 84.67%                 | 27.44% | 27.44%         | 0.00%         | -17.72%        | -17.72%                |       1.18675  | 0.00%                         | 0.00%                           | 2024-09       | -7.51%               | 2026-01      | 18.46%              | 0.00%              |              0   | 0.00%                       |                       0 | 0.00%                     |
| B           | Current active Top3 only      |       31 | 67.58%         | 84.67%                 | 22.64% | 27.44%         | -4.80%        | -19.32%        | -17.72%                |       0.903918 | 41.94%                        | -0.25%                          | 2024-08       | -10.88%              | 2026-01      | 16.86%              | 119.35%            |             37   | 100.00%                     |                      31 | 7.40%                     |
| C           | 80/20 benchmark-core          |       31 | 82.27%         | 84.67%                 | 26.78% | 27.44%         | -0.66%        | -18.00%        | -17.72%                |       1.17909  | 41.94%                        | -0.05%                          | 2024-08       | -7.27%               | 2026-01      | 18.14%              | 23.87%             |              7.4 | 20.00%                      |                      31 | 1.48%                     |
| D           | 70/30 benchmark-core          |       31 | 80.87%         | 84.67%                 | 26.40% | 27.44%         | -1.05%        | -18.15%        | -17.72%                |       1.16347  | 41.94%                        | -0.07%                          | 2024-08       | -7.72%               | 2026-01      | 17.98%              | 35.81%             |             11.1 | 30.00%                      |                      31 | 2.22%                     |
| E           | 50/50 benchmark-core          |       31 | 77.66%         | 84.67%                 | 25.51% | 27.44%         | -1.94%        | -18.46%        | -17.72%                |       1.11057  | 41.94%                        | -0.12%                          | 2024-08       | -8.63%               | 2026-01      | 17.66%              | 59.68%             |             18.5 | 50.00%                      |                      31 | 3.70%                     |
| F           | Conditional active overlay    |       31 | 80.89%         | 84.67%                 | 26.40% | 27.44%         | -1.04%        | -18.54%        | -17.72%                |       1.14933  | 16.13%                        | -0.07%                          | 2024-09       | -7.55%               | 2026-01      | 18.14%              | 11.61%             |              3.6 | 7.10%                       |                      11 | 0.72%                     |
| G           | Drawdown-aware active overlay |       31 | 84.60%         | 84.67%                 | 27.42% | 27.44%         | -0.02%        | -18.00%        | -17.72%                |       1.19918  | 29.03%                        | -0.01%                          | 2024-08       | -7.27%               | 2026-01      | 18.46%              | 17.42%             |              5.4 | 13.55%                      |                      21 | 1.08%                     |

## Decision

- Is pure active Top3 still worth paper trading? No. It delivered -4.80% excess CAGR versus BIST100 in this walk-forward.
- Does benchmark-core improve robustness? Yes. Core policies reduce active drawdown and tracking error mechanically, but must be checked against BIST100 drag.
- Best balance of CAGR, drawdown, and excess return: Policy A — BIST100 only (CAGR 27.44%, max drawdown -17.72%, excess CAGR 0.00%).
- Best fixed benchmark-core allocation if an active sleeve must be retained: Policy C — 80/20 benchmark-core (active allocation 20.00%, excess CAGR -0.66%).
- Best dynamic benchmark-core/satellite variant: Policy G — Drawdown-aware active overlay (active allocation average 13.55%, excess CAGR -0.02%).
- Next paper-trading candidate: Policy A — BIST100 only.
- Active stock-picking should be demoted from main strategy to satellite only unless it regains persistent benchmark-relative edge.

## Acceptance Criteria

A new candidate must improve robustness versus pure active Top3 and avoid material historical underperformance versus BIST100. June 2026 improvement alone is not sufficient.
