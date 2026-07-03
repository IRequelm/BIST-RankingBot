# Real Return Report

This report evaluates performance in both TL and USD terms. USD performance is estimated with USDTRY.

## Cash Allocation

- Minimum BUY expected return: 0.00%
- BUY candidates meeting threshold: 5
- Active portfolio slot count: 10
- Implied CASH weight when using equal opportunity slots: 50.00%

## Paper Portfolio TL / USD

- Latest portfolio value TL: 2,229,243.86
- Portfolio TL return: -1.80%
- USDTRY return over paper period: 1.70%
- Portfolio USD return: -3.44%
- Benchmark TL return: 5.48%

## Best Model TL / USD

- Model: trend_following
- Portfolio size: 3
- Period in `best_model_results.csv`: all available rows for selected model/size

| metric             |      TL |     USD |   USDTRY |
|:-------------------|--------:|--------:|---------:|
| total_return       | 20.9159 |  1.0997 |   9.4374 |
| avg_monthly_return |  0.0371 |  0.0130 |   0.0263 |
| max_drawdown       | -0.3455 | -0.4140 |  -0.2322 |
| win_rate           |  0.6392 |  0.5052 |          |

Interpretation: USD return converts TL strategy returns by the monthly USDTRY change. When USDTRY rises faster than the TL portfolio, USD-based performance falls.

## Market Reference

- Latest BIST100 close: 14,455.00
