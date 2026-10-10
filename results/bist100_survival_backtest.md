# BIST100 Relative Strength Survival Backtest

- Period: 2023-10-09 to 2026-10-09
- Configured BIST100 symbols: 100
- Loaded symbols: 97
- Missing/no valid data symbols: 3
- Production tracking_state.json was not modified.

## Policy Summary

| policy_id       | policy_name                              |   months | total_return   | bist100_total_return   | cagr   | bist100_cagr   | excess_cagr   | max_drawdown   | bist100_max_drawdown   |   sharpe_proxy | monthly_win_rate_vs_bist100   | average_monthly_excess_return   | worst_month   | worst_month_excess   | best_month   | best_month_excess   | average_turnover   |   average_trades_per_month |   cash_months |   average_holdings | transaction_cost_impact   |
|:----------------|:-----------------------------------------|---------:|:---------------|:-----------------------|:-------|:---------------|:--------------|:---------------|:-----------------------|---------------:|:------------------------------|:--------------------------------|:--------------|:---------------------|:-------------|:--------------------|:-------------------|---------------------------:|--------------:|-------------------:|:--------------------------|
| BENCHMARK       | BIST100 benchmark                        |       37 | 49.71%         | 49.71%                 | 14.39% | 14.39%         | 0.00%         | -17.72%        | -17.72%                |       0.66465  | 0.00%                         | 0.00%                           | 2023-10       | 0.00%                | 2023-10      | 0.00%               | 0.00%              |                    0       |             0 |            0       | 0.00%                     |
| OLD_TOP3        | Old absolute-score Top3                  |       37 | 66.44%         | 49.71%                 | 18.51% | 14.39%         | 4.11%         | -31.62%        | -17.72%                |       0.664219 | 48.65%                        | 0.51%                           | 2024-03       | -14.56%              | 2026-05      | 22.66%              | 127.93%            |                    3.83784 |             9 |            2.27027 | 9.47%                     |
| RS_TOP10        | BIST100 relative-strength survival Top10 |       37 | 51.23%         | 49.71%                 | 14.78% | 14.39%         | 0.39%         | -26.80%        | -17.72%                |       0.604207 | 56.76%                        | 0.13%                           | 2025-06       | -11.89%              | 2026-05      | 13.30%              | 107.03%            |                   10.7027  |             9 |            7.56757 | 7.92%                     |
| RS_TOP3         | BIST100 relative-strength survival Top3  |       37 | 38.67%         | 49.71%                 | 11.51% | 14.39%         | -2.88%        | -38.25%        | -17.72%                |       0.454176 | 51.35%                        | 0.66%                           | 2026-07       | -28.85%              | 2023-11      | 38.81%              | 127.93%            |                    3.83784 |             9 |            2.27027 | 9.47%                     |
| RS_TOP5         | BIST100 relative-strength survival Top5  |       37 | 8.40%          | 49.71%                 | 2.72%  | 14.39%         | -11.67%       | -42.64%        | -17.72%                |       0.275672 | 48.65%                        | -0.35%                          | 2026-09       | -17.81%              | 2023-11      | 23.83%              | 118.92%            |                    5.94595 |             9 |            3.78378 | 8.80%                     |
| RS_TOP5_NO_CASH | Survival Top5 without MA200 cash filter  |       37 | 75.93%         | 49.71%                 | 20.72% | 14.39%         | 6.32%         | -42.52%        | -17.72%                |       0.643396 | 59.46%                        | 1.03%                           | 2026-09       | -17.81%              | 2023-11      | 23.83%              | 145.41%            |                    7.27027 |             0 |            5       | 10.76%                    |

## Decision

Selected winner: Survival Top5 without MA200 cash filter (excess CAGR 6.32%, max drawdown -42.52%).

No strict drawdown-safe candidate passed both excess-return and drawdown tests.

Raw-return winner: Survival Top5 without MA200 cash filter (excess CAGR 6.32%, max drawdown -42.52%).

This selected winner is the aggressive research champion: it removes the MA200 cash filter and accepts slightly worse drawdown than BIST100 in exchange for the strongest historical excess CAGR in this run.

## Latest Survival Selections

| policy_id       | date                | symbol   |   rank |   score |   relative_strength_1m |   relative_strength_3m |   relative_strength_6m |   trend_score |   volatility |
|:----------------|:--------------------|:---------|-------:|--------:|-----------------------:|-----------------------:|-----------------------:|--------------:|-------------:|
| OLD_TOP3        | 2026-09-01 00:00:00 | TKFEN.IS |      1 |  0.8943 |                 0.2457 |                 0.4051 |                 1.7546 |        1.0000 |       0.0384 |
| OLD_TOP3        | 2026-09-01 00:00:00 | TUPRS.IS |      2 |  0.8670 |                 0.3254 |                 0.6741 |                 0.8955 |        1.0000 |       0.0271 |
| OLD_TOP3        | 2026-09-01 00:00:00 | KCHOL.IS |      3 |  0.8649 |                 0.0305 |                 0.1195 |                 0.0583 |        1.0000 |       0.0191 |
| RS_TOP10        | 2026-09-01 00:00:00 | TUPRS.IS |      1 |  0.8425 |                 0.3254 |                 0.6741 |                 0.8955 |        1.0000 |       0.0271 |
| RS_TOP10        | 2026-09-01 00:00:00 | TKFEN.IS |      2 |  0.8042 |                 0.2457 |                 0.4051 |                 1.7546 |        1.0000 |       0.0384 |
| RS_TOP10        | 2026-09-01 00:00:00 | KTLEV.IS |      3 |  0.7792 |                 0.3042 |                 0.3992 |                 3.9477 |        1.0000 |       0.0448 |
| RS_TOP10        | 2026-09-01 00:00:00 | PASEU.IS |      4 |  0.7742 |                 0.2236 |                 0.9913 |                 0.7261 |        1.0000 |       0.0588 |
| RS_TOP10        | 2026-09-01 00:00:00 | BRSAN.IS |      5 |  0.7242 |                 0.2679 |                 0.2204 |                 0.0010 |        1.0000 |       0.0342 |
| RS_TOP10        | 2026-09-01 00:00:00 | AHGAZ.IS |      6 |  0.6975 |                 0.1359 |                 0.1970 |                 0.5753 |        1.0000 |       0.0270 |
| RS_TOP10        | 2026-09-01 00:00:00 | KCHOL.IS |      7 |  0.6625 |                 0.0305 |                 0.1195 |                 0.0583 |        1.0000 |       0.0191 |
| RS_TOP10        | 2026-09-01 00:00:00 | KRDMD.IS |      8 |  0.6008 |                 0.0429 |                 0.0780 |                 0.3900 |        1.0000 |       0.0281 |
| RS_TOP10        | 2026-09-01 00:00:00 | ENERY.IS |      9 |  0.5992 |                 0.0929 |                 0.1390 |                 0.0355 |        1.0000 |       0.0322 |
| RS_TOP10        | 2026-09-01 00:00:00 | SOKM.IS  |     10 |  0.5658 |                 0.0655 |                 0.1338 |                -0.2108 |        1.0000 |       0.0232 |
| RS_TOP3         | 2026-09-01 00:00:00 | TUPRS.IS |      1 |  0.8425 |                 0.3254 |                 0.6741 |                 0.8955 |        1.0000 |       0.0271 |
| RS_TOP3         | 2026-09-01 00:00:00 | TKFEN.IS |      2 |  0.8042 |                 0.2457 |                 0.4051 |                 1.7546 |        1.0000 |       0.0384 |
| RS_TOP3         | 2026-09-01 00:00:00 | KTLEV.IS |      3 |  0.7792 |                 0.3042 |                 0.3992 |                 3.9477 |        1.0000 |       0.0448 |
| RS_TOP5         | 2026-09-01 00:00:00 | TUPRS.IS |      1 |  0.8425 |                 0.3254 |                 0.6741 |                 0.8955 |        1.0000 |       0.0271 |
| RS_TOP5         | 2026-09-01 00:00:00 | TKFEN.IS |      2 |  0.8042 |                 0.2457 |                 0.4051 |                 1.7546 |        1.0000 |       0.0384 |
| RS_TOP5         | 2026-09-01 00:00:00 | KTLEV.IS |      3 |  0.7792 |                 0.3042 |                 0.3992 |                 3.9477 |        1.0000 |       0.0448 |
| RS_TOP5         | 2026-09-01 00:00:00 | PASEU.IS |      4 |  0.7742 |                 0.2236 |                 0.9913 |                 0.7261 |        1.0000 |       0.0588 |
| RS_TOP5         | 2026-09-01 00:00:00 | BRSAN.IS |      5 |  0.7242 |                 0.2679 |                 0.2204 |                 0.0010 |        1.0000 |       0.0342 |
| RS_TOP5_NO_CASH | 2026-10-01 00:00:00 | ENERY.IS |      1 |  0.8025 |                 0.4168 |                 0.5654 |                 0.6098 |        1.0000 |       0.0298 |
| RS_TOP5_NO_CASH | 2026-10-01 00:00:00 | TKFEN.IS |      2 |  0.7975 |                 0.3322 |                 0.9440 |                 1.6467 |        1.0000 |       0.0421 |
| RS_TOP5_NO_CASH | 2026-10-01 00:00:00 | AHGAZ.IS |      3 |  0.7625 |                 0.2807 |                 0.3998 |                 1.1176 |        1.0000 |       0.0254 |
| RS_TOP5_NO_CASH | 2026-10-01 00:00:00 | TUPRS.IS |      4 |  0.6775 |                 0.1325 |                 0.7376 |                 0.6248 |        1.0000 |       0.0274 |
| RS_TOP5_NO_CASH | 2026-10-01 00:00:00 | BIMAS.IS |      5 |  0.5375 |                 0.1386 |                 0.3002 |                 0.2488 |        1.0000 |       0.0194 |

## Notes

- Strategy uses only data available at each rebalance date.
- Hard filters: stock above MA50, 20-day relative strength above BIST100, liquidity floor, volatility cap.
- Regime cash filter: no stock exposure when BIST100 is below MA200.
- Missing tickers are excluded and never substituted.
