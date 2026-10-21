# Real Return Report

This report evaluates performance in both TL and USD terms. USD performance is estimated with USDTRY.

## Cash Allocation

- Minimum BUY expected return: 0.00%
- BUY candidates meeting threshold: 2
- Active portfolio slot count: 5
- Implied CASH weight when using equal opportunity slots: 60.00%

## Paper Portfolio TL / USD

- Latest portfolio value TL: 28,810,856.80
- Portfolio TL return: 1169.20%
- USDTRY return over paper period: 7.90%
- Portfolio USD return: 1076.29%
- Benchmark TL return: -16.59%

## Best Model TL / USD

- Model: trend_following
- Portfolio size: 3
- Period in `best_model_results.csv`: all available rows for selected model/size

| metric             |      TL |     USD |   USDTRY |
|:-------------------|--------:|--------:|---------:|
| total_return       | 20.2880 |  0.9411 |   9.9672 |
| avg_monthly_return |  0.0358 |  0.0119 |   0.0260 |
| max_drawdown       | -0.3455 | -0.4140 |  -0.2322 |
| win_rate           |  0.6200 |  0.5000 |          |

Interpretation: USD return converts TL strategy returns by the monthly USDTRY change. When USDTRY rises faster than the TL portfolio, USD-based performance falls.

## Market Reference

- Latest BIST100 close: 11,797.70
