# BIST100 Relative Strength Survival Backtest

- Period: 2023-06-25 to 2026-06-25
- Configured BIST100 symbols: 100
- Loaded symbols: 97
- Missing/no valid data symbols: 3
- Production tracking_state.json was not modified.

## Policy Summary

| policy_id       | policy_name                              |   months | total_return   | bist100_total_return   | cagr   | bist100_cagr   | excess_cagr   | max_drawdown   | bist100_max_drawdown   |   sharpe_proxy | monthly_win_rate_vs_bist100   | average_monthly_excess_return   | worst_month   | worst_month_excess   | best_month   | best_month_excess   | average_turnover   |   average_trades_per_month |   cash_months |   average_holdings | transaction_cost_impact   |
|:----------------|:-----------------------------------------|---------:|:---------------|:-----------------------|:-------|:---------------|:--------------|:---------------|:-----------------------|---------------:|:------------------------------|:--------------------------------|:--------------|:---------------------|:-------------|:--------------------|:-------------------|---------------------------:|--------------:|-------------------:|:--------------------------|
| BENCHMARK       | BIST100 benchmark                        |       37 | 148.74%        | 148.74%                | 35.52% | 35.52%         | 0.00%         | -17.72%        | -17.72%                |        1.31938 | 0.00%                         | 0.00%                           | 2023-06       | 0.00%                | 2023-06      | 0.00%               | 0.00%              |                    0       |             0 |            0       | 0.00%                     |
| OLD_TOP3        | Old absolute-score Top3                  |       37 | 173.27%        | 148.74%                | 39.84% | 35.52%         | 4.32%         | -31.62%        | -17.72%                |        1.02239 | 51.35%                        | 0.64%                           | 2024-03       | -14.56%              | 2023-09      | 24.16%              | 130.63%            |                    3.91892 |             8 |            2.35135 | 9.67%                     |
| RS_TOP10        | BIST100 relative-strength survival Top10 |       37 | 334.10%        | 148.74%                | 63.18% | 35.52%         | 27.66%        | -14.69%        | -17.72%                |        1.55583 | 64.86%                        | 1.75%                           | 2025-06       | -11.89%              | 2023-08      | 22.14%              | 104.32%            |                   10.4324  |             8 |            7.83784 | 7.72%                     |
| RS_TOP3         | BIST100 relative-strength survival Top3  |       37 | 274.67%        | 148.74%                | 55.36% | 35.52%         | 19.84%        | -33.30%        | -17.72%                |        1.13932 | 54.05%                        | 1.71%                           | 2023-12       | -15.95%              | 2023-11      | 38.81%              | 130.63%            |                    3.91892 |             8 |            2.35135 | 9.67%                     |
| RS_TOP5         | BIST100 relative-strength survival Top5  |       37 | 257.12%        | 148.74%                | 52.90% | 35.52%         | 17.38%        | -22.51%        | -17.72%                |        1.20871 | 54.05%                        | 1.39%                           | 2023-12       | -13.80%              | 2023-08      | 28.89%              | 120.54%            |                    6.02703 |             8 |            3.91892 | 8.92%                     |
| RS_TOP5_NO_CASH | Survival Top5 without MA200 cash filter  |       37 | 505.46%        | 148.74%                | 82.34% | 35.52%         | 46.82%        | -18.81%        | -17.72%                |        1.61225 | 62.16%                        | 2.92%                           | 2023-12       | -13.80%              | 2023-08      | 28.89%              | 145.41%            |                    7.27027 |             0 |            5       | 10.76%                    |

## Decision

Selected winner: Survival Top5 without MA200 cash filter (excess CAGR 46.82%, max drawdown -18.81%).

Strict drawdown-safe candidate remains BIST100 relative-strength survival Top10 (excess CAGR 27.66%, max drawdown -14.69%).

Raw-return winner: Survival Top5 without MA200 cash filter (excess CAGR 46.82%, max drawdown -18.81%).

This selected winner is the aggressive research champion: it removes the MA200 cash filter and accepts slightly worse drawdown than BIST100 in exchange for the strongest historical excess CAGR in this run.

## Latest Survival Selections

| policy_id       | date                | symbol   |   rank |   score |   relative_strength_1m |   relative_strength_3m |   relative_strength_6m |   trend_score |   volatility |
|:----------------|:--------------------|:---------|-------:|--------:|-----------------------:|-----------------------:|-----------------------:|--------------:|-------------:|
| OLD_TOP3        | 2026-06-01 00:00:00 | YEOTK.IS |      1 |  0.9129 |                 1.0057 |                 1.8527 |                 1.8465 |        1.0000 |       0.0455 |
| OLD_TOP3        | 2026-06-01 00:00:00 | EUPWR.IS |      2 |  0.8964 |                 0.5680 |                 1.1022 |                 1.4050 |        1.0000 |       0.0444 |
| OLD_TOP3        | 2026-06-01 00:00:00 | GESAN.IS |      3 |  0.8959 |                 0.5155 |                 0.5200 |                 0.3915 |        1.0000 |       0.0378 |
| RS_TOP10        | 2026-06-01 00:00:00 | YEOTK.IS |      1 |  0.8137 |                 1.0057 |                 1.8527 |                 1.8465 |        1.0000 |       0.0455 |
| RS_TOP10        | 2026-06-01 00:00:00 | EUPWR.IS |      2 |  0.7911 |                 0.5680 |                 1.1022 |                 1.4050 |        1.0000 |       0.0444 |
| RS_TOP10        | 2026-06-01 00:00:00 | GESAN.IS |      3 |  0.7601 |                 0.5155 |                 0.5200 |                 0.3915 |        1.0000 |       0.0378 |
| RS_TOP10        | 2026-06-01 00:00:00 | SMRTG.IS |      4 |  0.7458 |                 0.6712 |                 0.6369 |                 0.1850 |        1.0000 |       0.0417 |
| RS_TOP10        | 2026-06-01 00:00:00 | ASTOR.IS |      5 |  0.7315 |                 0.2943 |                 0.7991 |                 2.3905 |        1.0000 |       0.0423 |
| RS_TOP10        | 2026-06-01 00:00:00 | MIATK.IS |      6 |  0.7149 |                 0.4385 |                 0.4609 |                 0.3207 |        1.0000 |       0.0426 |
| RS_TOP10        | 2026-06-01 00:00:00 | KTLEV.IS |      7 |  0.6994 |                 0.2171 |                 2.2968 |                 6.7905 |        1.0000 |       0.0400 |
| RS_TOP10        | 2026-06-01 00:00:00 | EREGL.IS |      8 |  0.6458 |                 0.2287 |                 0.2665 |                 0.4190 |        1.0000 |       0.0307 |
| RS_TOP10        | 2026-06-01 00:00:00 | TKFEN.IS |      9 |  0.6339 |                 0.1421 |                 0.9167 |                 0.9441 |        1.0000 |       0.0415 |
| RS_TOP10        | 2026-06-01 00:00:00 | ALFAS.IS |     10 |  0.6280 |                 0.3174 |                 0.3136 |                -0.0456 |        1.0000 |       0.0349 |
| RS_TOP3         | 2026-06-01 00:00:00 | YEOTK.IS |      1 |  0.8137 |                 1.0057 |                 1.8527 |                 1.8465 |        1.0000 |       0.0455 |
| RS_TOP3         | 2026-06-01 00:00:00 | EUPWR.IS |      2 |  0.7911 |                 0.5680 |                 1.1022 |                 1.4050 |        1.0000 |       0.0444 |
| RS_TOP3         | 2026-06-01 00:00:00 | GESAN.IS |      3 |  0.7601 |                 0.5155 |                 0.5200 |                 0.3915 |        1.0000 |       0.0378 |
| RS_TOP5         | 2026-06-01 00:00:00 | YEOTK.IS |      1 |  0.8137 |                 1.0057 |                 1.8527 |                 1.8465 |        1.0000 |       0.0455 |
| RS_TOP5         | 2026-06-01 00:00:00 | EUPWR.IS |      2 |  0.7911 |                 0.5680 |                 1.1022 |                 1.4050 |        1.0000 |       0.0444 |
| RS_TOP5         | 2026-06-01 00:00:00 | GESAN.IS |      3 |  0.7601 |                 0.5155 |                 0.5200 |                 0.3915 |        1.0000 |       0.0378 |
| RS_TOP5         | 2026-06-01 00:00:00 | SMRTG.IS |      4 |  0.7458 |                 0.6712 |                 0.6369 |                 0.1850 |        1.0000 |       0.0417 |
| RS_TOP5         | 2026-06-01 00:00:00 | ASTOR.IS |      5 |  0.7315 |                 0.2943 |                 0.7991 |                 2.3905 |        1.0000 |       0.0423 |
| RS_TOP5_NO_CASH | 2026-06-01 00:00:00 | YEOTK.IS |      1 |  0.8137 |                 1.0057 |                 1.8527 |                 1.8465 |        1.0000 |       0.0455 |
| RS_TOP5_NO_CASH | 2026-06-01 00:00:00 | EUPWR.IS |      2 |  0.7911 |                 0.5680 |                 1.1022 |                 1.4050 |        1.0000 |       0.0444 |
| RS_TOP5_NO_CASH | 2026-06-01 00:00:00 | GESAN.IS |      3 |  0.7601 |                 0.5155 |                 0.5200 |                 0.3915 |        1.0000 |       0.0378 |
| RS_TOP5_NO_CASH | 2026-06-01 00:00:00 | SMRTG.IS |      4 |  0.7458 |                 0.6712 |                 0.6369 |                 0.1850 |        1.0000 |       0.0417 |
| RS_TOP5_NO_CASH | 2026-06-01 00:00:00 | ASTOR.IS |      5 |  0.7315 |                 0.2943 |                 0.7991 |                 2.3905 |        1.0000 |       0.0423 |

## Notes

- Strategy uses only data available at each rebalance date.
- Hard filters: stock above MA50, 20-day relative strength above BIST100, liquidity floor, volatility cap.
- Regime cash filter: no stock exposure when BIST100 is below MA200.
- Missing tickers are excluded and never substituted.
