# BIST100 Relative Strength Survival Backtest

- Period: 2023-11-12 to 2026-11-12
- Configured BIST100 symbols: 100
- Loaded symbols: 97
- Missing/no valid data symbols: 3
- Production tracking_state.json was not modified.

## Policy Summary

| policy_id       | policy_name                              |   months | total_return   | bist100_total_return   | cagr   | bist100_cagr   | excess_cagr   | max_drawdown   | bist100_max_drawdown   |   sharpe_proxy | monthly_win_rate_vs_bist100   | average_monthly_excess_return   | worst_month   | worst_month_excess   | best_month   | best_month_excess   | average_turnover   |   average_trades_per_month |   cash_months |   average_holdings | transaction_cost_impact   |
|:----------------|:-----------------------------------------|---------:|:---------------|:-----------------------|:-------|:---------------|:--------------|:---------------|:-----------------------|---------------:|:------------------------------|:--------------------------------|:--------------|:---------------------|:-------------|:--------------------|:-------------------|---------------------------:|--------------:|-------------------:|:--------------------------|
| BENCHMARK       | BIST100 benchmark                        |       37 | 56.06%         | 56.06%                 | 16.01% | 16.01%         | 0.00%         | -23.72%        | -23.72%                |       0.710518 | 0.00%                         | 0.00%                           | 2023-11       | 0.00%                | 2023-11      | 0.00%               | 0.00%              |                    0       |             0 |            0       | 0.00%                     |
| OLD_TOP3        | Old absolute-score Top3                  |       37 | 24.36%         | 56.06%                 | 7.54%  | 16.01%         | -8.46%        | -31.62%        | -23.72%                |       0.379504 | 45.95%                        | -0.45%                          | 2024-03       | -14.56%              | 2026-05      | 22.66%              | 126.13%            |                    3.78378 |            10 |            2.18919 | 9.33%                     |
| RS_TOP10        | BIST100 relative-strength survival Top10 |       37 | 47.42%         | 56.06%                 | 13.82% | 16.01%         | -2.18%        | -26.80%        | -23.72%                |       0.589143 | 56.76%                        | -0.09%                          | 2025-06       | -11.89%              | 2026-05      | 13.30%              | 104.32%            |                   10.4324  |            10 |            7.2973  | 7.72%                     |
| RS_TOP3         | BIST100 relative-strength survival Top3  |       37 | 18.13%         | 56.06%                 | 5.72%  | 16.01%         | -10.29%       | -38.25%        | -23.72%                |       0.352596 | 51.35%                        | -0.05%                          | 2026-07       | -28.85%              | 2026-01      | 19.97%              | 124.32%            |                    3.72973 |            10 |            2.18919 | 9.20%                     |
| RS_TOP5         | BIST100 relative-strength survival Top5  |       37 | -11.03%        | 56.06%                 | -3.82% | 16.01%         | -19.83%       | -42.64%        | -23.72%                |       0.106202 | 48.65%                        | -1.10%                          | 2026-09       | -17.81%              | 2026-05      | 15.65%              | 118.92%            |                    5.94595 |            10 |            3.64865 | 8.80%                     |
| RS_TOP5_NO_CASH | Survival Top5 without MA200 cash filter  |       37 | 29.96%         | 56.06%                 | 9.13%  | 16.01%         | -6.87%        | -47.41%        | -23.72%                |       0.420981 | 56.76%                        | 0.01%                           | 2026-09       | -17.81%              | 2026-05      | 15.65%              | 148.65%            |                    7.35135 |             0 |            4.91892 | 11.00%                    |

## Decision

Selected winner: Survival Top5 without MA200 cash filter (excess CAGR -6.87%, max drawdown -47.41%).

No strict drawdown-safe candidate passed both excess-return and drawdown tests.

Raw-return winner: BIST100 relative-strength survival Top10 (excess CAGR -2.18%, max drawdown -26.80%).

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
| RS_TOP5_NO_CASH | 2026-11-02 00:00:00 | AHGAZ.IS |      1 |  0.7625 |                 0.1481 |                 0.6437 |                 0.9373 |        1.0000 |       0.0264 |
| RS_TOP5_NO_CASH | 2026-11-02 00:00:00 | ENERY.IS |      2 |  0.7375 |                 0.1140 |                 0.7621 |                 0.7828 |        1.0000 |       0.0337 |

## Notes

- Strategy uses only data available at each rebalance date.
- Hard filters: stock above MA50, 20-day relative strength above BIST100, liquidity floor, volatility cap.
- Regime cash filter: no stock exposure when BIST100 is below MA200.
- Missing tickers are excluded and never substituted.
