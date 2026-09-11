# BIST100 Relative Strength Survival Backtest

- Period: 2023-09-10 to 2026-09-10
- Configured BIST100 symbols: 100
- Loaded symbols: 97
- Missing/no valid data symbols: 3
- Production tracking_state.json was not modified.

## Policy Summary

| policy_id       | policy_name                              |   months | total_return   | bist100_total_return   | cagr   | bist100_cagr   | excess_cagr   | max_drawdown   | bist100_max_drawdown   |   sharpe_proxy | monthly_win_rate_vs_bist100   | average_monthly_excess_return   | worst_month   | worst_month_excess   | best_month   | best_month_excess   | average_turnover   |   average_trades_per_month |   cash_months |   average_holdings | transaction_cost_impact   |
|:----------------|:-----------------------------------------|---------:|:---------------|:-----------------------|:-------|:---------------|:--------------|:---------------|:-----------------------|---------------:|:------------------------------|:--------------------------------|:--------------|:---------------------|:-------------|:--------------------|:-------------------|---------------------------:|--------------:|-------------------:|:--------------------------|
| BENCHMARK       | BIST100 benchmark                        |       37 | 76.69%         | 76.69%                 | 20.91% | 20.91%         | 0.00%         | -17.72%        | -17.72%                |       0.926095 | 0.00%                         | 0.00%                           | 2023-09       | 0.00%                | 2023-09      | 0.00%               | 0.00%              |                    0       |             0 |            0       | 0.00%                     |
| OLD_TOP3        | Old absolute-score Top3                  |       37 | 85.21%         | 76.69%                 | 22.82% | 20.91%         | 1.92%         | -31.62%        | -17.72%                |       0.740727 | 51.35%                        | 0.43%                           | 2024-03       | -14.56%              | 2026-05      | 22.66%              | 128.83%            |                    3.86486 |             8 |            2.35135 | 9.53%                     |
| RS_TOP10        | BIST100 relative-strength survival Top10 |       37 | 87.51%         | 76.69%                 | 23.33% | 20.91%         | 2.42%         | -23.74%        | -17.72%                |       0.831837 | 56.76%                        | 0.31%                           | 2026-07       | -12.00%              | 2026-05      | 20.05%              | 107.57%            |                   10.7568  |             8 |            7.83784 | 7.96%                     |
| RS_TOP3         | BIST100 relative-strength survival Top3  |       37 | 162.21%        | 76.69%                 | 37.93% | 20.91%         | 17.02%        | -33.30%        | -17.72%                |       0.868686 | 54.05%                        | 1.79%                           | 2023-12       | -15.95%              | 2023-11      | 38.81%              | 130.63%            |                    3.91892 |             8 |            2.35135 | 9.67%                     |
| RS_TOP5         | BIST100 relative-strength survival Top5  |       37 | 61.81%         | 76.69%                 | 17.41% | 20.91%         | -3.50%        | -28.99%        | -17.72%                |       0.58333  | 51.35%                        | 0.22%                           | 2026-07       | -17.70%              | 2023-11      | 23.75%              | 121.62%            |                    6.08108 |             8 |            3.91892 | 9.00%                     |
| RS_TOP5_NO_CASH | Survival Top5 without MA200 cash filter  |       37 | 155.93%        | 76.69%                 | 36.81% | 20.91%         | 15.91%        | -28.99%        | -17.72%                |       0.938505 | 59.46%                        | 1.53%                           | 2026-07       | -17.70%              | 2023-11      | 23.75%              | 147.57%            |                    7.37838 |             0 |            5       | 10.92%                    |

## Decision

Selected winner: Survival Top5 without MA200 cash filter (excess CAGR 15.91%, max drawdown -28.99%).

No strict drawdown-safe candidate passed both excess-return and drawdown tests.

Raw-return winner: BIST100 relative-strength survival Top3 (excess CAGR 17.02%, max drawdown -33.30%).

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
