# BIST100 Relative Strength Survival Backtest

- Period: 2023-09-23 to 2026-09-23
- Configured BIST100 symbols: 100
- Loaded symbols: 97
- Missing/no valid data symbols: 3
- Production tracking_state.json was not modified.

## Policy Summary

| policy_id       | policy_name                              |   months | total_return   | bist100_total_return   | cagr   | bist100_cagr   | excess_cagr   | max_drawdown   | bist100_max_drawdown   |   sharpe_proxy | monthly_win_rate_vs_bist100   | average_monthly_excess_return   | worst_month   | worst_month_excess   | best_month   | best_month_excess   | average_turnover   |   average_trades_per_month |   cash_months |   average_holdings | transaction_cost_impact   |
|:----------------|:-----------------------------------------|---------:|:---------------|:-----------------------|:-------|:---------------|:--------------|:---------------|:-----------------------|---------------:|:------------------------------|:--------------------------------|:--------------|:---------------------|:-------------|:--------------------|:-------------------|---------------------------:|--------------:|-------------------:|:--------------------------|
| BENCHMARK       | BIST100 benchmark                        |       37 | 59.57%         | 59.57%                 | 16.88% | 16.88%         | 0.00%         | -17.72%        | -17.72%                |       0.7671   | 0.00%                         | 0.00%                           | 2023-09       | 0.00%                | 2023-09      | 0.00%               | 0.00%              |                    0       |             0 |            0       | 0.00%                     |
| OLD_TOP3        | Old absolute-score Top3                  |       37 | 48.92%         | 59.57%                 | 14.22% | 16.88%         | -2.67%        | -31.62%        | -17.72%                |       0.55431  | 45.95%                        | 0.04%                           | 2024-03       | -14.56%              | 2026-05      | 22.66%              | 127.03%            |                    3.81081 |             8 |            2.35135 | 9.40%                     |
| RS_TOP10        | BIST100 relative-strength survival Top10 |       37 | 56.59%         | 59.57%                 | 16.15% | 16.88%         | -0.73%        | -27.51%        | -17.72%                |       0.631927 | 54.05%                        | 0.09%                           | 2026-07       | -12.00%              | 2026-05      | 20.05%              | 106.49%            |                   10.6486  |             8 |            7.83784 | 7.88%                     |
| RS_TOP3         | BIST100 relative-strength survival Top3  |       37 | 82.97%         | 59.57%                 | 22.35% | 16.88%         | 5.46%         | -33.30%        | -17.72%                |       0.623916 | 51.35%                        | 1.10%                           | 2023-12       | -15.95%              | 2023-11      | 38.81%              | 128.83%            |                    3.86486 |             8 |            2.35135 | 9.53%                     |
| RS_TOP5         | BIST100 relative-strength survival Top5  |       37 | 3.83%          | 59.57%                 | 1.26%  | 16.88%         | -15.62%       | -39.52%        | -17.72%                |       0.236532 | 48.65%                        | -0.66%                          | 2026-09       | -21.30%              | 2023-11      | 23.75%              | 119.46%            |                    5.97297 |             8 |            3.91892 | 8.84%                     |
| RS_TOP5_NO_CASH | Survival Top5 without MA200 cash filter  |       37 | 64.22%         | 59.57%                 | 18.01% | 16.88%         | 1.13%         | -39.52%        | -17.72%                |       0.589784 | 56.76%                        | 0.65%                           | 2026-09       | -21.30%              | 2023-11      | 23.75%              | 145.41%            |                    7.27027 |             0 |            5       | 10.76%                    |

## Decision

Selected winner: Survival Top5 without MA200 cash filter (excess CAGR 1.13%, max drawdown -39.52%).

No strict drawdown-safe candidate passed both excess-return and drawdown tests.

Raw-return winner: BIST100 relative-strength survival Top3 (excess CAGR 5.46%, max drawdown -33.30%).

This selected winner is the aggressive research champion: it removes the MA200 cash filter and accepts slightly worse drawdown than BIST100 in exchange for the strongest historical excess CAGR in this run.

## Latest Survival Selections

| policy_id       | date                | symbol   |   rank |   score |   relative_strength_1m |   relative_strength_3m |   relative_strength_6m |   trend_score |   volatility |
|:----------------|:--------------------|:---------|-------:|--------:|-----------------------:|-----------------------:|-----------------------:|--------------:|-------------:|
| OLD_TOP3        | 2026-09-01 00:00:00 | TKFEN.IS |      1 |  0.8948 |                 0.2457 |                 0.4051 |                 1.9714 |        1.0000 |       0.0384 |
| OLD_TOP3        | 2026-09-01 00:00:00 | TUPRS.IS |      2 |  0.8660 |                 0.3254 |                 0.6741 |                 0.7989 |        1.0000 |       0.0271 |
| OLD_TOP3        | 2026-09-01 00:00:00 | KCHOL.IS |      3 |  0.8655 |                 0.0305 |                 0.1195 |                 0.0737 |        1.0000 |       0.0191 |
| RS_TOP10        | 2026-09-01 00:00:00 | TUPRS.IS |      1 |  0.8450 |                 0.3254 |                 0.6741 |                 0.7989 |        1.0000 |       0.0271 |
| RS_TOP10        | 2026-09-01 00:00:00 | TKFEN.IS |      2 |  0.8067 |                 0.2457 |                 0.4051 |                 1.9714 |        1.0000 |       0.0384 |
| RS_TOP10        | 2026-09-01 00:00:00 | KTLEV.IS |      3 |  0.7883 |                 0.3042 |                 0.2634 |                 2.5615 |        1.0000 |       0.0431 |
| RS_TOP10        | 2026-09-01 00:00:00 | PASEU.IS |      4 |  0.7733 |                 0.2236 |                 0.9913 |                 0.6875 |        1.0000 |       0.0588 |
| RS_TOP10        | 2026-09-01 00:00:00 | BRSAN.IS |      5 |  0.7617 |                 0.2679 |                 0.2204 |                 0.1455 |        1.0000 |       0.0342 |
| RS_TOP10        | 2026-09-01 00:00:00 | AHGAZ.IS |      6 |  0.7000 |                 0.1359 |                 0.1970 |                 0.5275 |        1.0000 |       0.0270 |
| RS_TOP10        | 2026-09-01 00:00:00 | KCHOL.IS |      7 |  0.6650 |                 0.0305 |                 0.1195 |                 0.0737 |        1.0000 |       0.0191 |
| RS_TOP10        | 2026-09-01 00:00:00 | KRDMD.IS |      8 |  0.6033 |                 0.0429 |                 0.0780 |                 0.3034 |        1.0000 |       0.0281 |
| RS_TOP10        | 2026-09-01 00:00:00 | ENERY.IS |      9 |  0.5917 |                 0.0929 |                 0.1390 |                -0.0135 |        1.0000 |       0.0322 |
| RS_TOP10        | 2026-09-01 00:00:00 | AYDEM.IS |     10 |  0.5733 |                 0.0805 |                -0.0104 |                -0.0099 |        1.0000 |       0.0268 |
| RS_TOP3         | 2026-09-01 00:00:00 | TUPRS.IS |      1 |  0.8450 |                 0.3254 |                 0.6741 |                 0.7989 |        1.0000 |       0.0271 |
| RS_TOP3         | 2026-09-01 00:00:00 | TKFEN.IS |      2 |  0.8067 |                 0.2457 |                 0.4051 |                 1.9714 |        1.0000 |       0.0384 |
| RS_TOP3         | 2026-09-01 00:00:00 | KTLEV.IS |      3 |  0.7883 |                 0.3042 |                 0.2634 |                 2.5615 |        1.0000 |       0.0431 |
| RS_TOP5         | 2026-09-01 00:00:00 | TUPRS.IS |      1 |  0.8450 |                 0.3254 |                 0.6741 |                 0.7989 |        1.0000 |       0.0271 |
| RS_TOP5         | 2026-09-01 00:00:00 | TKFEN.IS |      2 |  0.8067 |                 0.2457 |                 0.4051 |                 1.9714 |        1.0000 |       0.0384 |
| RS_TOP5         | 2026-09-01 00:00:00 | KTLEV.IS |      3 |  0.7883 |                 0.3042 |                 0.2634 |                 2.5615 |        1.0000 |       0.0431 |
| RS_TOP5         | 2026-09-01 00:00:00 | PASEU.IS |      4 |  0.7733 |                 0.2236 |                 0.9913 |                 0.6875 |        1.0000 |       0.0588 |
| RS_TOP5         | 2026-09-01 00:00:00 | BRSAN.IS |      5 |  0.7617 |                 0.2679 |                 0.2204 |                 0.1455 |        1.0000 |       0.0342 |
| RS_TOP5_NO_CASH | 2026-09-01 00:00:00 | TUPRS.IS |      1 |  0.8450 |                 0.3254 |                 0.6741 |                 0.7989 |        1.0000 |       0.0271 |
| RS_TOP5_NO_CASH | 2026-09-01 00:00:00 | TKFEN.IS |      2 |  0.8067 |                 0.2457 |                 0.4051 |                 1.9714 |        1.0000 |       0.0384 |
| RS_TOP5_NO_CASH | 2026-09-01 00:00:00 | KTLEV.IS |      3 |  0.7883 |                 0.3042 |                 0.2634 |                 2.5615 |        1.0000 |       0.0431 |
| RS_TOP5_NO_CASH | 2026-09-01 00:00:00 | PASEU.IS |      4 |  0.7733 |                 0.2236 |                 0.9913 |                 0.6875 |        1.0000 |       0.0588 |
| RS_TOP5_NO_CASH | 2026-09-01 00:00:00 | BRSAN.IS |      5 |  0.7617 |                 0.2679 |                 0.2204 |                 0.1455 |        1.0000 |       0.0342 |

## Notes

- Strategy uses only data available at each rebalance date.
- Hard filters: stock above MA50, 20-day relative strength above BIST100, liquidity floor, volatility cap.
- Regime cash filter: no stock exposure when BIST100 is below MA200.
- Missing tickers are excluded and never substituted.
