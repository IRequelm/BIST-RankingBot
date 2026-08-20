# BIST100 Relative Strength Survival Backtest

- Period: 2023-08-19 to 2026-08-19
- Configured BIST100 symbols: 100
- Loaded symbols: 97
- Missing/no valid data symbols: 3
- Production tracking_state.json was not modified.

## Policy Summary

| policy_id       | policy_name                              |   months | total_return   | bist100_total_return   | cagr   | bist100_cagr   | excess_cagr   | max_drawdown   | bist100_max_drawdown   |   sharpe_proxy | monthly_win_rate_vs_bist100   | average_monthly_excess_return   | worst_month   | worst_month_excess   | best_month   | best_month_excess   | average_turnover   |   average_trades_per_month |   cash_months |   average_holdings | transaction_cost_impact   |
|:----------------|:-----------------------------------------|---------:|:---------------|:-----------------------|:-------|:---------------|:--------------|:---------------|:-----------------------|---------------:|:------------------------------|:--------------------------------|:--------------|:---------------------|:-------------|:--------------------|:-------------------|---------------------------:|--------------:|-------------------:|:--------------------------|
| BENCHMARK       | BIST100 benchmark                        |       37 | 85.45%         | 85.45%                 | 22.90% | 22.90%         | 0.00%         | -17.72%        | -17.72%                |       0.989837 | 0.00%                         | 0.00%                           | 2023-08       | 0.00%                | 2023-08      | 0.00%               | 0.00%              |                    0       |             0 |            0       | 0.00%                     |
| OLD_TOP3        | Old absolute-score Top3                  |       37 | 122.14%        | 85.45%                 | 30.54% | 22.90%         | 7.64%         | -31.62%        | -17.72%                |       0.873486 | 48.65%                        | 0.85%                           | 2024-03       | -14.56%              | 2023-09      | 24.16%              | 132.43%            |                    3.97297 |             8 |            2.35135 | 9.80%                     |
| RS_TOP10        | BIST100 relative-strength survival Top10 |       37 | 143.41%        | 85.45%                 | 34.58% | 22.90%         | 11.68%        | -20.97%        | -17.72%                |       1.07885  | 59.46%                        | 0.93%                           | 2026-07       | -12.00%              | 2026-05      | 20.05%              | 105.95%            |                   10.5946  |             8 |            7.83784 | 7.84%                     |
| RS_TOP3         | BIST100 relative-strength survival Top3  |       37 | 149.83%        | 85.45%                 | 35.76% | 22.90%         | 12.86%        | -33.30%        | -17.72%                |       0.849875 | 54.05%                        | 1.46%                           | 2023-12       | -15.95%              | 2023-11      | 38.81%              | 132.43%            |                    3.97297 |             8 |            2.35135 | 9.80%                     |
| RS_TOP5         | BIST100 relative-strength survival Top5  |       37 | 90.63%         | 85.45%                 | 24.04% | 22.90%         | 1.14%         | -27.45%        | -17.72%                |       0.740377 | 54.05%                        | 0.45%                           | 2026-07       | -17.70%              | 2023-11      | 23.75%              | 122.70%            |                    6.13514 |             8 |            3.91892 | 9.08%                     |
| RS_TOP5_NO_CASH | Survival Top5 without MA200 cash filter  |       37 | 201.51%        | 85.45%                 | 44.55% | 22.90%         | 21.65%        | -27.45%        | -17.72%                |       1.11399  | 62.16%                        | 1.77%                           | 2026-07       | -17.70%              | 2023-11      | 23.75%              | 148.65%            |                    7.43243 |             0 |            5       | 11.00%                    |

## Decision

Selected winner: Survival Top5 without MA200 cash filter (excess CAGR 21.65%, max drawdown -27.45%).

No strict drawdown-safe candidate passed both excess-return and drawdown tests.

Raw-return winner: Survival Top5 without MA200 cash filter (excess CAGR 21.65%, max drawdown -27.45%).

This selected winner is the aggressive research champion: it removes the MA200 cash filter and accepts slightly worse drawdown than BIST100 in exchange for the strongest historical excess CAGR in this run.

## Latest Survival Selections

| policy_id       | date                | symbol   |   rank |   score |   relative_strength_1m |   relative_strength_3m |   relative_strength_6m |   trend_score |   volatility |
|:----------------|:--------------------|:---------|-------:|--------:|-----------------------:|-----------------------:|-----------------------:|--------------:|-------------:|
| OLD_TOP3        | 2026-08-03 00:00:00 | AKSEN.IS |      1 |  0.8608 |                 0.1704 |                 0.1573 |                 0.2353 |        1.0000 |       0.0352 |
| OLD_TOP3        | 2026-08-03 00:00:00 | TUPRS.IS |      2 |  0.8320 |                 0.3273 |                 0.1174 |                 0.2484 |        1.0000 |       0.0244 |
| OLD_TOP3        | 2026-08-03 00:00:00 | AKFYE.IS |      3 |  0.8258 |                 0.1021 |                 0.1396 |                 0.2880 |        0.5000 |       0.0398 |
| RS_TOP10        | 2026-08-03 00:00:00 | TKFEN.IS |      1 |  0.6987 |                 0.2670 |                 0.2733 |                 1.1255 |        1.0000 |       0.0372 |
| RS_TOP10        | 2026-08-03 00:00:00 | TUPRS.IS |      2 |  0.6912 |                 0.3273 |                 0.1174 |                 0.2484 |        1.0000 |       0.0244 |
| RS_TOP10        | 2026-08-03 00:00:00 | AEFES.IS |      3 |  0.6812 |                 0.1493 |                 0.2361 |                 0.1899 |        1.0000 |       0.0225 |
| RS_TOP10        | 2026-08-03 00:00:00 | EUPWR.IS |      4 |  0.6763 |                 0.1249 |                 0.9055 |                 1.1941 |        1.0000 |       0.0561 |
| RS_TOP10        | 2026-08-03 00:00:00 | ISGYO.IS |      5 |  0.6562 |                 0.1038 |                 0.3482 |                 0.1163 |        1.0000 |       0.0302 |
| RS_TOP10        | 2026-08-03 00:00:00 | AKSEN.IS |      6 |  0.6512 |                 0.1704 |                 0.1573 |                 0.2353 |        1.0000 |       0.0352 |
| RS_TOP10        | 2026-08-03 00:00:00 | EREGL.IS |      7 |  0.5913 |                 0.0558 |                 0.2863 |                 0.4784 |        1.0000 |       0.0279 |
| RS_TOP10        | 2026-08-03 00:00:00 | CCOLA.IS |      8 |  0.5887 |                 0.0979 |                 0.2477 |                 0.2047 |        1.0000 |       0.0251 |
| RS_TOP10        | 2026-08-03 00:00:00 | AKSA.IS  |      9 |  0.5687 |                 0.0834 |                 0.2860 |                 0.2473 |        1.0000 |       0.0277 |
| RS_TOP10        | 2026-08-03 00:00:00 | ANHYT.IS |     10 |  0.5637 |                 0.1689 |                 0.1093 |                 0.0677 |        1.0000 |       0.0224 |
| RS_TOP3         | 2026-08-03 00:00:00 | TKFEN.IS |      1 |  0.6987 |                 0.2670 |                 0.2733 |                 1.1255 |        1.0000 |       0.0372 |
| RS_TOP3         | 2026-08-03 00:00:00 | TUPRS.IS |      2 |  0.6912 |                 0.3273 |                 0.1174 |                 0.2484 |        1.0000 |       0.0244 |
| RS_TOP3         | 2026-08-03 00:00:00 | AEFES.IS |      3 |  0.6812 |                 0.1493 |                 0.2361 |                 0.1899 |        1.0000 |       0.0225 |
| RS_TOP5         | 2026-08-03 00:00:00 | TKFEN.IS |      1 |  0.6987 |                 0.2670 |                 0.2733 |                 1.1255 |        1.0000 |       0.0372 |
| RS_TOP5         | 2026-08-03 00:00:00 | TUPRS.IS |      2 |  0.6912 |                 0.3273 |                 0.1174 |                 0.2484 |        1.0000 |       0.0244 |
| RS_TOP5         | 2026-08-03 00:00:00 | AEFES.IS |      3 |  0.6812 |                 0.1493 |                 0.2361 |                 0.1899 |        1.0000 |       0.0225 |
| RS_TOP5         | 2026-08-03 00:00:00 | EUPWR.IS |      4 |  0.6763 |                 0.1249 |                 0.9055 |                 1.1941 |        1.0000 |       0.0561 |
| RS_TOP5         | 2026-08-03 00:00:00 | ISGYO.IS |      5 |  0.6562 |                 0.1038 |                 0.3482 |                 0.1163 |        1.0000 |       0.0302 |
| RS_TOP5_NO_CASH | 2026-08-03 00:00:00 | TKFEN.IS |      1 |  0.6987 |                 0.2670 |                 0.2733 |                 1.1255 |        1.0000 |       0.0372 |
| RS_TOP5_NO_CASH | 2026-08-03 00:00:00 | TUPRS.IS |      2 |  0.6912 |                 0.3273 |                 0.1174 |                 0.2484 |        1.0000 |       0.0244 |
| RS_TOP5_NO_CASH | 2026-08-03 00:00:00 | AEFES.IS |      3 |  0.6812 |                 0.1493 |                 0.2361 |                 0.1899 |        1.0000 |       0.0225 |
| RS_TOP5_NO_CASH | 2026-08-03 00:00:00 | EUPWR.IS |      4 |  0.6763 |                 0.1249 |                 0.9055 |                 1.1941 |        1.0000 |       0.0561 |
| RS_TOP5_NO_CASH | 2026-08-03 00:00:00 | ISGYO.IS |      5 |  0.6562 |                 0.1038 |                 0.3482 |                 0.1163 |        1.0000 |       0.0302 |

## Notes

- Strategy uses only data available at each rebalance date.
- Hard filters: stock above MA50, 20-day relative strength above BIST100, liquidity floor, volatility cap.
- Regime cash filter: no stock exposure when BIST100 is below MA200.
- Missing tickers are excluded and never substituted.
