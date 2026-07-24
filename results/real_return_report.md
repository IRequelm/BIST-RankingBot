# Real Return Report

This report evaluates performance in both TL and USD terms. USD performance is estimated with USDTRY.

## Cash Allocation

- Minimum BUY expected return: 0.00%
- BUY candidates meeting threshold: 4
- Active portfolio slot count: 10
- Implied CASH weight when using equal opportunity slots: 60.00%

## Paper Portfolio TL / USD

- Latest portfolio value TL: 10,457,582.42
- Portfolio TL return: 360.69%
- USDTRY return over paper period: 2.83%
- Portfolio USD return: 348.00%
- Benchmark TL return: 3.17%

## Best Model TL / USD

- Model: trend_following
- Portfolio size: 3
- Period in `best_model_results.csv`: all available rows for selected model/size

| metric             |      TL |     USD |   USDTRY |
|:-------------------|--------:|--------:|---------:|
| total_return       | 20.6951 |  1.0786 |   9.4374 |
| avg_monthly_return |  0.0370 |  0.0129 |   0.0263 |
| max_drawdown       | -0.3455 | -0.4140 |  -0.2322 |
| win_rate           |  0.6289 |  0.5052 |          |

Interpretation: USD return converts TL strategy returns by the monthly USDTRY change. When USDTRY rises faster than the TL portfolio, USD-based performance falls.

## Market Reference

- Latest BIST100 close: 14,077.70
