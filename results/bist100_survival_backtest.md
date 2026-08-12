# BIST100 Relative Strength Survival Backtest

- Period: 2023-08-11 to 2026-08-11
- Configured BIST100 symbols: 100
- Loaded symbols: 97
- Missing/no valid data symbols: 3
- Production tracking_state.json was not modified.

## Policy Summary

| policy_id       | policy_name                              |   months | total_return   | bist100_total_return   | cagr   | bist100_cagr   | excess_cagr   | max_drawdown   | bist100_max_drawdown   |   sharpe_proxy | monthly_win_rate_vs_bist100   | average_monthly_excess_return   | worst_month   | worst_month_excess   | best_month   | best_month_excess   | average_turnover   |   average_trades_per_month |   cash_months |   average_holdings | transaction_cost_impact   |
|:----------------|:-----------------------------------------|---------:|:---------------|:-----------------------|:-------|:---------------|:--------------|:---------------|:-----------------------|---------------:|:------------------------------|:--------------------------------|:--------------|:---------------------|:-------------|:--------------------|:-------------------|---------------------------:|--------------:|-------------------:|:--------------------------|
| BENCHMARK       | BIST100 benchmark                        |       37 | 77.65%         | 77.65%                 | 21.11% | 21.11%         | 0.00%         | -17.72%        | -17.72%                |       0.935116 | 0.00%                         | 0.00%                           | 2023-08       | 0.00%                | 2023-08      | 0.00%               | 0.00%              |                    0       |             0 |            0       | 0.00%                     |
| OLD_TOP3        | Old absolute-score Top3                  |       37 | 112.17%        | 77.65%                 | 28.49% | 21.11%         | 7.38%         | -31.62%        | -17.72%                |       0.835168 | 48.65%                        | 0.84%                           | 2024-03       | -14.56%              | 2023-09      | 24.16%              | 132.43%            |                    3.97297 |             8 |            2.35135 | 9.80%                     |
| RS_TOP10        | BIST100 relative-strength survival Top10 |       37 | 158.46%        | 77.65%                 | 37.23% | 21.11%         | 16.12%        | -20.97%        | -17.72%                |       1.12833  | 62.16%                        | 1.23%                           | 2026-07       | -12.00%              | 2026-05      | 20.05%              | 107.03%            |                   10.7027  |             8 |            7.83784 | 7.92%                     |
| RS_TOP3         | BIST100 relative-strength survival Top3  |       37 | 141.99%        | 77.65%                 | 34.25% | 21.11%         | 13.14%        | -33.30%        | -17.72%                |       0.830689 | 54.05%                        | 1.48%                           | 2023-12       | -15.95%              | 2023-11      | 38.81%              | 132.43%            |                    3.97297 |             8 |            2.35135 | 9.80%                     |
| RS_TOP5         | BIST100 relative-strength survival Top5  |       37 | 89.12%         | 77.65%                 | 23.66% | 21.11%         | 2.55%         | -27.45%        | -17.72%                |       0.731692 | 54.05%                        | 0.56%                           | 2026-07       | -17.70%              | 2023-11      | 23.75%              | 123.78%            |                    6.18919 |             8 |            3.91892 | 9.16%                     |
| RS_TOP5_NO_CASH | Survival Top5 without MA200 cash filter  |       37 | 199.11%        | 77.65%                 | 44.07% | 21.11%         | 22.96%        | -27.45%        | -17.72%                |       1.1042   | 62.16%                        | 1.87%                           | 2026-07       | -17.70%              | 2023-11      | 23.75%              | 149.73%            |                    7.48649 |             0 |            5       | 11.08%                    |

## Decision

Selected winner: Survival Top5 without MA200 cash filter (excess CAGR 22.96%, max drawdown -27.45%).

No strict drawdown-safe candidate passed both excess-return and drawdown tests.

Raw-return winner: Survival Top5 without MA200 cash filter (excess CAGR 22.96%, max drawdown -27.45%).

This selected winner is the aggressive research champion: it removes the MA200 cash filter and accepts slightly worse drawdown than BIST100 in exchange for the strongest historical excess CAGR in this run.

## Latest Survival Selections

| policy_id       | date                | symbol   |   rank |   score |   relative_strength_1m |   relative_strength_3m |   relative_strength_6m |   trend_score |   volatility |
|:----------------|:--------------------|:---------|-------:|--------:|-----------------------:|-----------------------:|-----------------------:|--------------:|-------------:|
| OLD_TOP3        | 2026-08-03 00:00:00 | AKSEN.IS |      1 |  0.8670 |                 0.1916 |                 0.1255 |                 0.2656 |        1.0000 |       0.0343 |
| OLD_TOP3        | 2026-08-03 00:00:00 | TUPRS.IS |      2 |  0.8428 |                 0.3273 |                 0.1174 |                 0.2484 |        1.0000 |       0.0244 |
| OLD_TOP3        | 2026-08-03 00:00:00 | AKFYE.IS |      3 |  0.8258 |                 0.1021 |                 0.1396 |                 0.2880 |        0.5000 |       0.0398 |
| RS_TOP10        | 2026-08-03 00:00:00 | TKFEN.IS |      1 |  0.6816 |                 0.2437 |                 0.2432 |                 1.1677 |        1.0000 |       0.0362 |
| RS_TOP10        | 2026-08-03 00:00:00 | TUPRS.IS |      2 |  0.6711 |                 0.3273 |                 0.1174 |                 0.2484 |        1.0000 |       0.0244 |
| RS_TOP10        | 2026-08-03 00:00:00 | AKSEN.IS |      3 |  0.6658 |                 0.1916 |                 0.1255 |                 0.2656 |        1.0000 |       0.0343 |
| RS_TOP10        | 2026-08-03 00:00:00 | EUPWR.IS |      4 |  0.6526 |                 0.1249 |                 0.9055 |                 1.1941 |        1.0000 |       0.0561 |
| RS_TOP10        | 2026-08-03 00:00:00 | AKSA.IS  |      5 |  0.6474 |                 0.1307 |                 0.2839 |                 0.2199 |        1.0000 |       0.0287 |
| RS_TOP10        | 2026-08-03 00:00:00 | AEFES.IS |      6 |  0.6421 |                 0.0998 |                 0.2593 |                 0.1987 |        1.0000 |       0.0232 |
| RS_TOP10        | 2026-08-03 00:00:00 | ISGYO.IS |      7 |  0.6342 |                 0.1038 |                 0.3482 |                 0.1163 |        1.0000 |       0.0302 |
| RS_TOP10        | 2026-08-03 00:00:00 | AKCNS.IS |      8 |  0.6053 |                 0.1583 |                 0.1966 |                 0.2568 |        1.0000 |       0.0318 |
| RS_TOP10        | 2026-08-03 00:00:00 | BIMAS.IS |      9 |  0.5816 |                 0.1324 |                 0.1105 |                 0.1483 |        1.0000 |       0.0211 |
| RS_TOP10        | 2026-08-03 00:00:00 | CCOLA.IS |     10 |  0.5763 |                 0.0979 |                 0.2477 |                 0.2047 |        1.0000 |       0.0251 |
| RS_TOP3         | 2026-08-03 00:00:00 | TKFEN.IS |      1 |  0.6816 |                 0.2437 |                 0.2432 |                 1.1677 |        1.0000 |       0.0362 |
| RS_TOP3         | 2026-08-03 00:00:00 | TUPRS.IS |      2 |  0.6711 |                 0.3273 |                 0.1174 |                 0.2484 |        1.0000 |       0.0244 |
| RS_TOP3         | 2026-08-03 00:00:00 | AKSEN.IS |      3 |  0.6658 |                 0.1916 |                 0.1255 |                 0.2656 |        1.0000 |       0.0343 |
| RS_TOP5         | 2026-08-03 00:00:00 | TKFEN.IS |      1 |  0.6816 |                 0.2437 |                 0.2432 |                 1.1677 |        1.0000 |       0.0362 |
| RS_TOP5         | 2026-08-03 00:00:00 | TUPRS.IS |      2 |  0.6711 |                 0.3273 |                 0.1174 |                 0.2484 |        1.0000 |       0.0244 |
| RS_TOP5         | 2026-08-03 00:00:00 | AKSEN.IS |      3 |  0.6658 |                 0.1916 |                 0.1255 |                 0.2656 |        1.0000 |       0.0343 |
| RS_TOP5         | 2026-08-03 00:00:00 | EUPWR.IS |      4 |  0.6526 |                 0.1249 |                 0.9055 |                 1.1941 |        1.0000 |       0.0561 |
| RS_TOP5         | 2026-08-03 00:00:00 | AKSA.IS  |      5 |  0.6474 |                 0.1307 |                 0.2839 |                 0.2199 |        1.0000 |       0.0287 |
| RS_TOP5_NO_CASH | 2026-08-03 00:00:00 | TKFEN.IS |      1 |  0.6816 |                 0.2437 |                 0.2432 |                 1.1677 |        1.0000 |       0.0362 |
| RS_TOP5_NO_CASH | 2026-08-03 00:00:00 | TUPRS.IS |      2 |  0.6711 |                 0.3273 |                 0.1174 |                 0.2484 |        1.0000 |       0.0244 |
| RS_TOP5_NO_CASH | 2026-08-03 00:00:00 | AKSEN.IS |      3 |  0.6658 |                 0.1916 |                 0.1255 |                 0.2656 |        1.0000 |       0.0343 |
| RS_TOP5_NO_CASH | 2026-08-03 00:00:00 | EUPWR.IS |      4 |  0.6526 |                 0.1249 |                 0.9055 |                 1.1941 |        1.0000 |       0.0561 |
| RS_TOP5_NO_CASH | 2026-08-03 00:00:00 | AKSA.IS  |      5 |  0.6474 |                 0.1307 |                 0.2839 |                 0.2199 |        1.0000 |       0.0287 |

## Notes

- Strategy uses only data available at each rebalance date.
- Hard filters: stock above MA50, 20-day relative strength above BIST100, liquidity floor, volatility cap.
- Regime cash filter: no stock exposure when BIST100 is below MA200.
- Missing tickers are excluded and never substituted.
