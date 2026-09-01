# BIST100 Relative Strength Survival Backtest

- Period: 2023-08-31 to 2026-08-31
- Configured BIST100 symbols: 100
- Loaded symbols: 97
- Missing/no valid data symbols: 3
- Production tracking_state.json was not modified.

## Policy Summary

| policy_id       | policy_name                              |   months | total_return   | bist100_total_return   | cagr   | bist100_cagr   | excess_cagr   | max_drawdown   | bist100_max_drawdown   |   sharpe_proxy | monthly_win_rate_vs_bist100   | average_monthly_excess_return   | worst_month   | worst_month_excess   | best_month   | best_month_excess   | average_turnover   |   average_trades_per_month |   cash_months |   average_holdings | transaction_cost_impact   |
|:----------------|:-----------------------------------------|---------:|:---------------|:-----------------------|:-------|:---------------|:--------------|:---------------|:-----------------------|---------------:|:------------------------------|:--------------------------------|:--------------|:---------------------|:-------------|:--------------------|:-------------------|---------------------------:|--------------:|-------------------:|:--------------------------|
| BENCHMARK       | BIST100 benchmark                        |       37 | 81.04%         | 81.04%                 | 21.87% | 21.87%         | 0.00%         | -17.72%        | -17.72%                |       0.95804  | 0.00%                         | 0.00%                           | 2023-08       | 0.00%                | 2023-08      | 0.00%               | 0.00%              |                    0       |             0 |            0       | 0.00%                     |
| OLD_TOP3        | Old absolute-score Top3                  |       37 | 94.38%         | 81.04%                 | 24.79% | 21.87%         | 2.92%         | -31.62%        | -17.72%                |       0.764844 | 48.65%                        | 0.53%                           | 2024-03       | -14.56%              | 2023-09      | 24.29%              | 130.63%            |                    3.91892 |             8 |            2.35135 | 9.67%                     |
| RS_TOP10        | BIST100 relative-strength survival Top10 |       37 | 134.27%        | 81.04%                 | 32.80% | 21.87%         | 10.93%        | -20.97%        | -17.72%                |       1.04683  | 62.16%                        | 0.88%                           | 2026-07       | -12.00%              | 2026-05      | 20.05%              | 104.86%            |                   10.4865  |             8 |            7.83784 | 7.76%                     |
| RS_TOP3         | BIST100 relative-strength survival Top3  |       37 | 151.20%        | 81.04%                 | 35.93% | 21.87%         | 14.06%        | -33.30%        | -17.72%                |       0.840894 | 54.05%                        | 1.58%                           | 2023-12       | -15.95%              | 2023-11      | 38.81%              | 130.63%            |                    3.91892 |             8 |            2.35135 | 9.67%                     |
| RS_TOP5         | BIST100 relative-strength survival Top5  |       37 | 90.31%         | 81.04%                 | 23.92% | 21.87%         | 2.05%         | -27.45%        | -17.72%                |       0.723577 | 51.35%                        | 0.55%                           | 2026-07       | -17.70%              | 2023-11      | 23.75%              | 120.54%            |                    6.02703 |             8 |            3.91892 | 8.92%                     |
| RS_TOP5_NO_CASH | Survival Top5 without MA200 cash filter  |       37 | 201.01%        | 81.04%                 | 44.37% | 21.87%         | 22.50%        | -27.45%        | -17.72%                |       1.08675  | 59.46%                        | 1.87%                           | 2026-07       | -17.70%              | 2023-11      | 23.75%              | 146.49%            |                    7.32432 |             0 |            5       | 10.84%                    |

## Decision

Selected winner: Survival Top5 without MA200 cash filter (excess CAGR 22.50%, max drawdown -27.45%).

No strict drawdown-safe candidate passed both excess-return and drawdown tests.

Raw-return winner: Survival Top5 without MA200 cash filter (excess CAGR 22.50%, max drawdown -27.45%).

This selected winner is the aggressive research champion: it removes the MA200 cash filter and accepts slightly worse drawdown than BIST100 in exchange for the strongest historical excess CAGR in this run.

## Latest Survival Selections

| policy_id       | date                | symbol   |   rank |   score |   relative_strength_1m |   relative_strength_3m |   relative_strength_6m |   trend_score |   volatility |
|:----------------|:--------------------|:---------|-------:|--------:|-----------------------:|-----------------------:|-----------------------:|--------------:|-------------:|
| OLD_TOP3        | 2026-08-03 00:00:00 | AKSEN.IS |      1 |  0.8799 |                 0.1916 |                 0.1255 |                 0.2656 |        1.0000 |       0.0343 |
| OLD_TOP3        | 2026-08-03 00:00:00 | TUPRS.IS |      2 |  0.8474 |                 0.2837 |                 0.1387 |                 0.2663 |        1.0000 |       0.0243 |
| OLD_TOP3        | 2026-08-03 00:00:00 | AKFYE.IS |      3 |  0.8113 |                 0.1046 |                 0.0849 |                 0.2929 |        0.5000 |       0.0407 |
| RS_TOP10        | 2026-08-03 00:00:00 | TUPRS.IS |      1 |  0.6974 |                 0.2837 |                 0.1387 |                 0.2663 |        1.0000 |       0.0243 |
| RS_TOP10        | 2026-08-03 00:00:00 | TKFEN.IS |      2 |  0.6974 |                 0.2437 |                 0.2432 |                 1.1677 |        1.0000 |       0.0362 |
| RS_TOP10        | 2026-08-03 00:00:00 | EUPWR.IS |      3 |  0.6895 |                 0.1598 |                 0.6916 |                 1.2020 |        1.0000 |       0.0519 |
| RS_TOP10        | 2026-08-03 00:00:00 | PASEU.IS |      4 |  0.6868 |                 1.0443 |                 0.3186 |                 0.1690 |        1.0000 |       0.0573 |
| RS_TOP10        | 2026-08-03 00:00:00 | AEFES.IS |      5 |  0.6579 |                 0.1493 |                 0.2361 |                 0.1899 |        1.0000 |       0.0225 |
| RS_TOP10        | 2026-08-03 00:00:00 | AKSEN.IS |      6 |  0.6105 |                 0.1916 |                 0.1255 |                 0.2656 |        1.0000 |       0.0343 |
| RS_TOP10        | 2026-08-03 00:00:00 | AKSA.IS  |      7 |  0.5868 |                 0.1307 |                 0.2839 |                 0.2199 |        1.0000 |       0.0287 |
| RS_TOP10        | 2026-08-03 00:00:00 | ISGYO.IS |      8 |  0.5842 |                 0.1197 |                 0.3720 |                 0.1159 |        1.0000 |       0.0301 |
| RS_TOP10        | 2026-08-03 00:00:00 | CCOLA.IS |      9 |  0.5658 |                 0.1249 |                 0.2176 |                 0.2610 |        1.0000 |       0.0247 |
| RS_TOP10        | 2026-08-03 00:00:00 | ANHYT.IS |     10 |  0.5632 |                 0.1952 |                 0.1103 |                 0.0272 |        1.0000 |       0.0223 |
| RS_TOP3         | 2026-08-03 00:00:00 | TUPRS.IS |      1 |  0.6974 |                 0.2837 |                 0.1387 |                 0.2663 |        1.0000 |       0.0243 |
| RS_TOP3         | 2026-08-03 00:00:00 | TKFEN.IS |      2 |  0.6974 |                 0.2437 |                 0.2432 |                 1.1677 |        1.0000 |       0.0362 |
| RS_TOP3         | 2026-08-03 00:00:00 | EUPWR.IS |      3 |  0.6895 |                 0.1598 |                 0.6916 |                 1.2020 |        1.0000 |       0.0519 |
| RS_TOP5         | 2026-08-03 00:00:00 | TUPRS.IS |      1 |  0.6974 |                 0.2837 |                 0.1387 |                 0.2663 |        1.0000 |       0.0243 |
| RS_TOP5         | 2026-08-03 00:00:00 | TKFEN.IS |      2 |  0.6974 |                 0.2437 |                 0.2432 |                 1.1677 |        1.0000 |       0.0362 |
| RS_TOP5         | 2026-08-03 00:00:00 | EUPWR.IS |      3 |  0.6895 |                 0.1598 |                 0.6916 |                 1.2020 |        1.0000 |       0.0519 |
| RS_TOP5         | 2026-08-03 00:00:00 | PASEU.IS |      4 |  0.6868 |                 1.0443 |                 0.3186 |                 0.1690 |        1.0000 |       0.0573 |
| RS_TOP5         | 2026-08-03 00:00:00 | AEFES.IS |      5 |  0.6579 |                 0.1493 |                 0.2361 |                 0.1899 |        1.0000 |       0.0225 |
| RS_TOP5_NO_CASH | 2026-08-03 00:00:00 | TUPRS.IS |      1 |  0.6974 |                 0.2837 |                 0.1387 |                 0.2663 |        1.0000 |       0.0243 |
| RS_TOP5_NO_CASH | 2026-08-03 00:00:00 | TKFEN.IS |      2 |  0.6974 |                 0.2437 |                 0.2432 |                 1.1677 |        1.0000 |       0.0362 |
| RS_TOP5_NO_CASH | 2026-08-03 00:00:00 | EUPWR.IS |      3 |  0.6895 |                 0.1598 |                 0.6916 |                 1.2020 |        1.0000 |       0.0519 |
| RS_TOP5_NO_CASH | 2026-08-03 00:00:00 | PASEU.IS |      4 |  0.6868 |                 1.0443 |                 0.3186 |                 0.1690 |        1.0000 |       0.0573 |
| RS_TOP5_NO_CASH | 2026-08-03 00:00:00 | AEFES.IS |      5 |  0.6579 |                 0.1493 |                 0.2361 |                 0.1899 |        1.0000 |       0.0225 |

## Notes

- Strategy uses only data available at each rebalance date.
- Hard filters: stock above MA50, 20-day relative strength above BIST100, liquidity floor, volatility cap.
- Regime cash filter: no stock exposure when BIST100 is below MA200.
- Missing tickers are excluded and never substituted.
