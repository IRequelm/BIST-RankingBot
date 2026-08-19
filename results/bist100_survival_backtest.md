# BIST100 Relative Strength Survival Backtest

- Period: 2023-08-18 to 2026-08-18
- Configured BIST100 symbols: 100
- Loaded symbols: 97
- Missing/no valid data symbols: 3
- Production tracking_state.json was not modified.

## Policy Summary

| policy_id       | policy_name                              |   months | total_return   | bist100_total_return   | cagr   | bist100_cagr   | excess_cagr   | max_drawdown   | bist100_max_drawdown   |   sharpe_proxy | monthly_win_rate_vs_bist100   | average_monthly_excess_return   | worst_month   | worst_month_excess   | best_month   | best_month_excess   | average_turnover   |   average_trades_per_month |   cash_months |   average_holdings | transaction_cost_impact   |
|:----------------|:-----------------------------------------|---------:|:---------------|:-----------------------|:-------|:---------------|:--------------|:---------------|:-----------------------|---------------:|:------------------------------|:--------------------------------|:--------------|:---------------------|:-------------|:--------------------|:-------------------|---------------------------:|--------------:|-------------------:|:--------------------------|
| BENCHMARK       | BIST100 benchmark                        |       37 | 88.04%         | 88.04%                 | 23.42% | 23.42%         | 0.00%         | -17.72%        | -17.72%                |       1.00906  | 0.00%                         | 0.00%                           | 2023-08       | 0.00%                | 2023-08      | 0.00%               | 0.00%              |                    0       |             0 |            0       | 0.00%                     |
| OLD_TOP3        | Old absolute-score Top3                  |       37 | 109.84%        | 88.04%                 | 28.02% | 23.42%         | 4.60%         | -31.62%        | -17.72%                |       0.831721 | 48.65%                        | 0.64%                           | 2024-03       | -14.56%              | 2023-09      | 24.29%              | 130.63%            |                    3.91892 |             8 |            2.35135 | 9.67%                     |
| RS_TOP10        | BIST100 relative-strength survival Top10 |       37 | 161.28%        | 88.04%                 | 37.72% | 23.42%         | 14.30%        | -20.97%        | -17.72%                |       1.12358  | 59.46%                        | 1.11%                           | 2026-07       | -12.00%              | 2026-05      | 20.05%              | 105.95%            |                   10.5946  |             8 |            7.83784 | 7.84%                     |
| RS_TOP3         | BIST100 relative-strength survival Top3  |       37 | 134.83%        | 88.04%                 | 32.91% | 23.42%         | 9.49%         | -33.30%        | -17.72%                |       0.810184 | 54.05%                        | 1.23%                           | 2023-12       | -15.95%              | 2023-11      | 38.81%              | 132.43%            |                    3.97297 |             8 |            2.35135 | 9.80%                     |
| RS_TOP5         | BIST100 relative-strength survival Top5  |       37 | 119.11%        | 88.04%                 | 29.88% | 23.42%         | 6.45%         | -27.45%        | -17.72%                |       0.830215 | 54.05%                        | 0.86%                           | 2026-07       | -17.70%              | 2023-11      | 23.75%              | 121.62%            |                    6.08108 |             8 |            3.91892 | 9.00%                     |
| RS_TOP5_NO_CASH | Survival Top5 without MA200 cash filter  |       37 | 246.56%        | 88.04%                 | 51.32% | 23.42%         | 27.89%        | -27.45%        | -17.72%                |       1.18678  | 62.16%                        | 2.18%                           | 2026-07       | -17.70%              | 2023-11      | 23.75%              | 147.57%            |                    7.37838 |             0 |            5       | 10.92%                    |

## Decision

Selected winner: Survival Top5 without MA200 cash filter (excess CAGR 27.89%, max drawdown -27.45%).

No strict drawdown-safe candidate passed both excess-return and drawdown tests.

Raw-return winner: Survival Top5 without MA200 cash filter (excess CAGR 27.89%, max drawdown -27.45%).

This selected winner is the aggressive research champion: it removes the MA200 cash filter and accepts slightly worse drawdown than BIST100 in exchange for the strongest historical excess CAGR in this run.

## Latest Survival Selections

| policy_id       | date                | symbol   |   rank |   score |   relative_strength_1m |   relative_strength_3m |   relative_strength_6m |   trend_score |   volatility |
|:----------------|:--------------------|:---------|-------:|--------:|-----------------------:|-----------------------:|-----------------------:|--------------:|-------------:|
| OLD_TOP3        | 2026-08-03 00:00:00 | AKSEN.IS |      1 |  0.8722 |                 0.1916 |                 0.1255 |                 0.2656 |        1.0000 |       0.0343 |
| OLD_TOP3        | 2026-08-03 00:00:00 | TUPRS.IS |      2 |  0.8428 |                 0.3273 |                 0.1174 |                 0.2484 |        1.0000 |       0.0244 |
| OLD_TOP3        | 2026-08-03 00:00:00 | AKFYE.IS |      3 |  0.8294 |                 0.1021 |                 0.1396 |                 0.2880 |        0.5000 |       0.0398 |
| RS_TOP10        | 2026-08-03 00:00:00 | EUPWR.IS |      1 |  0.7024 |                 0.1598 |                 0.6916 |                 1.2020 |        1.0000 |       0.0519 |
| RS_TOP10        | 2026-08-03 00:00:00 | TKFEN.IS |      2 |  0.6810 |                 0.2670 |                 0.2733 |                 1.1255 |        1.0000 |       0.0372 |
| RS_TOP10        | 2026-08-03 00:00:00 | PASEU.IS |      3 |  0.6762 |                 1.0443 |                 0.3186 |                 0.1690 |        1.0000 |       0.0573 |
| RS_TOP10        | 2026-08-03 00:00:00 | TUPRS.IS |      4 |  0.6714 |                 0.3273 |                 0.1174 |                 0.2484 |        1.0000 |       0.0244 |
| RS_TOP10        | 2026-08-03 00:00:00 | ISGYO.IS |      5 |  0.6619 |                 0.1038 |                 0.3482 |                 0.1163 |        1.0000 |       0.0302 |
| RS_TOP10        | 2026-08-03 00:00:00 | AKSEN.IS |      6 |  0.6548 |                 0.1916 |                 0.1255 |                 0.2656 |        1.0000 |       0.0343 |
| RS_TOP10        | 2026-08-03 00:00:00 | AEFES.IS |      7 |  0.6357 |                 0.0998 |                 0.2593 |                 0.1987 |        1.0000 |       0.0232 |
| RS_TOP10        | 2026-08-03 00:00:00 | EREGL.IS |      8 |  0.5690 |                 0.0558 |                 0.2863 |                 0.4784 |        1.0000 |       0.0279 |
| RS_TOP10        | 2026-08-03 00:00:00 | CCOLA.IS |      9 |  0.5667 |                 0.0979 |                 0.2477 |                 0.2047 |        1.0000 |       0.0251 |
| RS_TOP10        | 2026-08-03 00:00:00 | AKSA.IS  |     10 |  0.5595 |                 0.0834 |                 0.2860 |                 0.2473 |        1.0000 |       0.0277 |
| RS_TOP3         | 2026-08-03 00:00:00 | EUPWR.IS |      1 |  0.7024 |                 0.1598 |                 0.6916 |                 1.2020 |        1.0000 |       0.0519 |
| RS_TOP3         | 2026-08-03 00:00:00 | TKFEN.IS |      2 |  0.6810 |                 0.2670 |                 0.2733 |                 1.1255 |        1.0000 |       0.0372 |
| RS_TOP3         | 2026-08-03 00:00:00 | PASEU.IS |      3 |  0.6762 |                 1.0443 |                 0.3186 |                 0.1690 |        1.0000 |       0.0573 |
| RS_TOP5         | 2026-08-03 00:00:00 | EUPWR.IS |      1 |  0.7024 |                 0.1598 |                 0.6916 |                 1.2020 |        1.0000 |       0.0519 |
| RS_TOP5         | 2026-08-03 00:00:00 | TKFEN.IS |      2 |  0.6810 |                 0.2670 |                 0.2733 |                 1.1255 |        1.0000 |       0.0372 |
| RS_TOP5         | 2026-08-03 00:00:00 | PASEU.IS |      3 |  0.6762 |                 1.0443 |                 0.3186 |                 0.1690 |        1.0000 |       0.0573 |
| RS_TOP5         | 2026-08-03 00:00:00 | TUPRS.IS |      4 |  0.6714 |                 0.3273 |                 0.1174 |                 0.2484 |        1.0000 |       0.0244 |
| RS_TOP5         | 2026-08-03 00:00:00 | ISGYO.IS |      5 |  0.6619 |                 0.1038 |                 0.3482 |                 0.1163 |        1.0000 |       0.0302 |
| RS_TOP5_NO_CASH | 2026-08-03 00:00:00 | EUPWR.IS |      1 |  0.7024 |                 0.1598 |                 0.6916 |                 1.2020 |        1.0000 |       0.0519 |
| RS_TOP5_NO_CASH | 2026-08-03 00:00:00 | TKFEN.IS |      2 |  0.6810 |                 0.2670 |                 0.2733 |                 1.1255 |        1.0000 |       0.0372 |
| RS_TOP5_NO_CASH | 2026-08-03 00:00:00 | PASEU.IS |      3 |  0.6762 |                 1.0443 |                 0.3186 |                 0.1690 |        1.0000 |       0.0573 |
| RS_TOP5_NO_CASH | 2026-08-03 00:00:00 | TUPRS.IS |      4 |  0.6714 |                 0.3273 |                 0.1174 |                 0.2484 |        1.0000 |       0.0244 |
| RS_TOP5_NO_CASH | 2026-08-03 00:00:00 | ISGYO.IS |      5 |  0.6619 |                 0.1038 |                 0.3482 |                 0.1163 |        1.0000 |       0.0302 |

## Notes

- Strategy uses only data available at each rebalance date.
- Hard filters: stock above MA50, 20-day relative strength above BIST100, liquidity floor, volatility cap.
- Regime cash filter: no stock exposure when BIST100 is below MA200.
- Missing tickers are excluded and never substituted.
