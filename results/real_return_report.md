# Real Return Report

This report evaluates performance in both TL and USD terms. USD performance is estimated with USDTRY.

## Cash Allocation

- Minimum BUY expected return: 0.00%
- BUY candidates meeting threshold: 5
- Active portfolio slot count: 10
- Implied CASH weight when using equal opportunity slots: 50.00%

## Paper Portfolio TL / USD

- Latest portfolio value TL: 9,849,048.87
- Portfolio TL return: 333.88%
- USDTRY return over paper period: 3.57%
- Portfolio USD return: 318.94%
- Benchmark TL return: -2.14%

## Best Model TL / USD

- Model: trend_following
- Portfolio size: 3
- Period in `best_model_results.csv`: all available rows for selected model/size

| metric             |      TL |     USD |   USDTRY |
|:-------------------|--------:|--------:|---------:|
| total_return       | 19.3443 |  0.9139 |   9.6300 |
| avg_monthly_return |  0.0360 |  0.0119 |   0.0262 |
| max_drawdown       | -0.3455 | -0.4140 |  -0.2322 |
| win_rate           |  0.6224 |  0.5000 |          |

Interpretation: USD return converts TL strategy returns by the monthly USDTRY change. When USDTRY rises faster than the TL portfolio, USD-based performance falls.

## Market Reference

- Latest BIST100 close: 13,687.90
