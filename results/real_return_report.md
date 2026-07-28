# Real Return Report

This report evaluates performance in both TL and USD terms. USD performance is estimated with USDTRY.

## Cash Allocation

- Minimum BUY expected return: 0.00%
- BUY candidates meeting threshold: 5
- Active portfolio slot count: 10
- Implied CASH weight when using equal opportunity slots: 50.00%

## Paper Portfolio TL / USD

- Latest portfolio value TL: 10,223,232.76
- Portfolio TL return: 350.36%
- USDTRY return over paper period: 3.09%
- Portfolio USD return: 336.86%
- Benchmark TL return: 2.73%

## Best Model TL / USD

- Model: trend_following
- Portfolio size: 3
- Period in `best_model_results.csv`: all available rows for selected model/size

| metric             |      TL |     USD |   USDTRY |
|:-------------------|--------:|--------:|---------:|
| total_return       | 20.2922 |  1.0400 |   9.4374 |
| avg_monthly_return |  0.0368 |  0.0127 |   0.0263 |
| max_drawdown       | -0.3455 | -0.4140 |  -0.2322 |
| win_rate           |  0.6289 |  0.5052 |          |

Interpretation: USD return converts TL strategy returns by the monthly USDTRY change. When USDTRY rises faster than the TL portfolio, USD-based performance falls.

## Market Reference

- Latest BIST100 close: 13,774.80
