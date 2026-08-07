# Benchmark-Core Portfolio Research

Research-only. Production tracking_state.json and live follow-up behavior are unchanged.

## Policy Results

| policy_id   | policy_name                   |   months | total_return   | bist100_total_return   | cagr   | bist100_cagr   | excess_cagr   | max_drawdown   | bist100_max_drawdown   |   sharpe_proxy | monthly_win_rate_vs_bist100   | average_monthly_excess_return   | worst_month   | worst_month_return   | best_month   | best_month_return   | average_turnover   |   total_turnover | active_allocation_average   |   active_overlay_months | transaction_cost_impact   |
|:------------|:------------------------------|---------:|:---------------|:-----------------------|:-------|:---------------|:--------------|:---------------|:-----------------------|---------------:|:------------------------------|:--------------------------------|:--------------|:---------------------|:-------------|:--------------------|:-------------------|-----------------:|:----------------------------|------------------------:|:--------------------------|
| A           | BIST100 only                  |       32 | 80.99%         | 80.99%                 | 25.71% | 25.71%         | 0.00%         | -17.72%        | -17.72%                |       1.1113   | 0.00%                         | 0.00%                           | 2024-09       | -7.51%               | 2026-01      | 18.46%              | 0.00%              |          0       | 0.00%                       |                       0 | 0.00%                     |
| B           | Current active Top3 only      |       32 | 65.08%         | 80.99%                 | 21.33% | 25.71%         | -4.38%        | -19.32%        | -17.72%                |       0.861495 | 43.75%                        | -0.23%                          | 2024-08       | -10.88%              | 2026-01      | 16.86%              | 117.71%            |         37.6667  | 100.00%                     |                      32 | 7.53%                     |
| C           | 80/20 benchmark-core          |       32 | 78.82%         | 80.99%                 | 25.13% | 25.71%         | -0.58%        | -18.00%        | -17.72%                |       1.10672  | 43.75%                        | -0.05%                          | 2024-08       | -7.27%               | 2026-01      | 18.14%              | 23.54%             |          7.53333 | 20.00%                      |                      32 | 1.51%                     |
| D           | 70/30 benchmark-core          |       32 | 77.53%         | 80.99%                 | 24.78% | 25.71%         | -0.93%        | -18.15%        | -17.72%                |       1.09381  | 43.75%                        | -0.07%                          | 2024-08       | -7.72%               | 2026-01      | 17.98%              | 35.31%             |         11.3     | 30.00%                      |                      32 | 2.26%                     |
| E           | 50/50 benchmark-core          |       32 | 74.57%         | 80.99%                 | 23.97% | 25.71%         | -1.74%        | -18.46%        | -17.72%                |       1.04804  | 43.75%                        | -0.11%                          | 2024-08       | -8.63%               | 2026-01      | 17.66%              | 58.85%             |         18.8333  | 50.00%                      |                      32 | 3.77%                     |
| F           | Conditional active overlay    |       32 | 76.72%         | 80.99%                 | 24.56% | 25.71%         | -1.15%        | -18.54%        | -17.72%                |       1.07023  | 15.62%                        | -0.08%                          | 2024-09       | -7.55%               | 2026-01      | 18.14%              | 11.88%             |          3.8     | 7.50%                       |                      12 | 0.76%                     |
| G           | Drawdown-aware active overlay |       32 | 81.10%         | 80.99%                 | 25.74% | 25.71%         | 0.03%         | -18.00%        | -17.72%                |       1.12616  | 31.25%                        | -0.00%                          | 2024-08       | -7.27%               | 2026-01      | 18.46%              | 17.29%             |          5.53333 | 13.75%                      |                      22 | 1.11%                     |

## Decision

- Is pure active Top3 still worth paper trading? No. It delivered -4.38% excess CAGR versus BIST100 in this walk-forward.
- Does benchmark-core improve robustness? Yes. Core policies reduce active drawdown and tracking error mechanically, but must be checked against BIST100 drag.
- Best balance of CAGR, drawdown, and excess return: Policy A — BIST100 only (CAGR 25.71%, max drawdown -17.72%, excess CAGR 0.00%).
- Best fixed benchmark-core allocation if an active sleeve must be retained: Policy C — 80/20 benchmark-core (active allocation 20.00%, excess CAGR -0.58%).
- Best dynamic benchmark-core/satellite variant: Policy G — Drawdown-aware active overlay (active allocation average 13.75%, excess CAGR 0.03%).
- Next paper-trading candidate: Policy A — BIST100 only.
- Active stock-picking should be demoted from main strategy to satellite only unless it regains persistent benchmark-relative edge.

## Acceptance Criteria

A new candidate must improve robustness versus pure active Top3 and avoid material historical underperformance versus BIST100. June 2026 improvement alone is not sufficient.
