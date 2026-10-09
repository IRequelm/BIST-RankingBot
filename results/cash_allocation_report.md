# Cash Allocation Report

## Experiment

- Baseline model: trend_following Top3
- Baseline behavior: force all portfolio slots into stocks.
- Cash behavior: each stock must meet the threshold; failed slots remain in CASH.
- Thresholds tested: 2%, 5%, 8%, 10%, 12%
- Selected threshold: 5%
- Decision: accepted
- Reason: Accepted because the selected threshold improved out-of-sample risk-adjusted selection score or drawdown versus the full-invested baseline.

## Comparison

| threshold              | period        |   months |   avg_cash_weight |   avg_qualified_count |   selection_score |   strategy_total_return |   bist100_total_return |   excess_return_over_benchmark |   strategy_max_drawdown |   bist100_max_drawdown |   win_rate |
|:-----------------------|:--------------|---------:|------------------:|----------------------:|------------------:|------------------------:|-----------------------:|-------------------------------:|------------------------:|-----------------------:|-----------:|
| baseline_full_invested | out_of_sample |       33 |            0.0000 |                3.0000 |            0.0093 |                  0.5123 |                 0.4375 |                         0.0748 |                 -0.1767 |                -0.1728 |     0.5758 |
| baseline_full_invested | validation    |       24 |            0.0000 |                3.0000 |            2.2100 |                  5.3727 |                 3.2416 |                         2.1312 |                 -0.1168 |                -0.1618 |     0.6250 |
| 0.02                   | out_of_sample |       33 |            0.2727 |                2.1818 |           -0.2014 |                  0.2940 |                 0.4375 |                        -0.1435 |                 -0.1502 |                -0.1728 |     0.4848 |
| 0.02                   | train         |       43 |            0.5349 |                1.3953 |           -1.0247 |                  0.3400 |                 1.0754 |                        -0.7355 |                 -0.2493 |                -0.2476 |     0.4186 |
| 0.02                   | validation    |       24 |            0.4861 |                1.5417 |           -2.2842 |                  0.8614 |                 3.2416 |                        -2.3801 |                 -0.0770 |                -0.1618 |     0.5000 |
| 0.05                   | out_of_sample |       33 |            0.7172 |                0.8485 |           -0.2134 |                  0.1701 |                 0.4375 |                        -0.2673 |                 -0.0639 |                -0.1728 |     0.3636 |
| 0.05                   | train         |       43 |            0.8837 |                0.3488 |           -1.2373 |                 -0.0123 |                 1.0754 |                        -1.0877 |                 -0.1155 |                -0.2476 |     0.1628 |
| 0.05                   | validation    |       24 |            0.8194 |                0.5417 |           -2.9739 |                  0.2281 |                 3.2416 |                        -3.0135 |                 -0.0323 |                -0.1618 |     0.2083 |
| 0.08                   | out_of_sample |       33 |            0.8687 |                0.3939 |           -0.6301 |                 -0.0770 |                 0.4375 |                        -0.5145 |                 -0.0881 |                -0.1728 |     0.1212 |
| 0.08                   | train         |       43 |            0.9767 |                0.0698 |           -1.1625 |                 -0.0288 |                 1.0754 |                        -1.1042 |                 -0.0408 |                -0.2476 |     0.0465 |
| 0.08                   | validation    |       24 |            0.8889 |                0.3333 |           -3.0144 |                  0.2165 |                 3.2416 |                        -3.0250 |                 -0.0259 |                -0.1618 |     0.1250 |
| 0.1                    | out_of_sample |       33 |            0.9596 |                0.1212 |           -0.5158 |                 -0.0312 |                 0.4375 |                        -0.4686 |                 -0.0312 |                -0.1728 |     0.0303 |
| 0.1                    | train         |       43 |            0.9922 |                0.0233 |           -1.0540 |                  0.0098 |                 1.0754 |                        -1.0656 |                  0.0000 |                -0.2476 |     0.0233 |
| 0.1                    | validation    |       24 |            0.9444 |                0.1667 |           -3.0661 |                  0.1235 |                 3.2416 |                        -3.1181 |                 -0.0053 |                -0.1618 |     0.1250 |
| 0.12                   | out_of_sample |       33 |            0.9697 |                0.0909 |           -0.4767 |                 -0.0090 |                 0.4375 |                        -0.4465 |                 -0.0227 |                -0.1728 |     0.0303 |
| 0.12                   | train         |       43 |            0.9922 |                0.0233 |           -1.0540 |                  0.0098 |                 1.0754 |                        -1.0656 |                  0.0000 |                -0.2476 |     0.0233 |
| 0.12                   | validation    |       24 |            0.9722 |                0.0833 |           -3.0753 |                  0.1246 |                 3.2416 |                        -3.1169 |                  0.0000 |                -0.1618 |     0.0833 |
