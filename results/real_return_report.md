# Real Return Report

This report evaluates performance in both TL and USD terms. USD performance is estimated with USDTRY.

## Cash Allocation

- Minimum BUY expected return: 0.00%
- BUY candidates meeting threshold: 5
- Active portfolio slot count: 10
- Implied CASH weight when using equal opportunity slots: 50.00%

## Paper Portfolio TL / USD

- Latest portfolio value TL: 10,216,153.92
- Portfolio TL return: 350.05%
- USDTRY return over paper period: 3.60%
- Portfolio USD return: 334.41%
- Benchmark TL return: 0.69%

## Best Model TL / USD

- Model: trend_following
- Portfolio size: 3
- Period in `best_model_results.csv`: all available rows for selected model/size

| metric             |      TL |     USD |   USDTRY |
|:-------------------|--------:|--------:|---------:|
| total_return       | 20.2793 |  1.0018 |   9.6300 |
| avg_monthly_return |  0.0364 |  0.0124 |   0.0262 |
| max_drawdown       | -0.3455 | -0.4140 |  -0.2322 |
| win_rate           |  0.6327 |  0.5000 |          |

Interpretation: USD return converts TL strategy returns by the monthly USDTRY change. When USDTRY rises faster than the TL portfolio, USD-based performance falls.

## Market Reference

- Latest BIST100 close: 13,779.40
