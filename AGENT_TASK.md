# AGENT_TASK.md

Permanent operating manual for improvement cycles in this project.

Future work must be executable from this instruction:

```text
Follow AGENT_TASK.md and run one improvement cycle.
```

## Mission

Improve the BIST-RankingBot one controlled change at a time. Every cycle must start from the latest generated evidence, make exactly one improvement, validate the full project, compare against the previous baseline, and log the decision.

This project is research-only. It produces ranking, backtesting, paper trading, reporting, and portfolio recommendation outputs. It must not place trades or call broker APIs.

## Required Inputs To Read First

At the start of every cycle, read the latest available outputs before proposing any code or configuration change:

1. Latest reports:
   - `results/final_report.md`
   - `results/summary_report.md`
   - `results/regime_filter_report.md`
   - `results/ranking_audit_report.md`
   - `results/selection_report.md`
2. Current portfolio recommendation:
   - `results/current_month_portfolio.md`
   - `results/current_month_portfolio.csv`
3. Paper trading performance:
   - `results/paper_performance_report.md`
   - `results/paper_portfolio_history.csv`
   - `results/paper_trade_log.csv`
   - `paper_trading/recommendation_snapshots.csv`
4. Baseline metric tables:
   - `results/final_report.csv`
   - `results/summary_report.csv`
   - `results/model_selection.csv`
   - `results/backtest_results.csv`
   - `results/best_model_results.csv`
   - `results/rolling_out_of_sample_tests.csv`
   - `results/random_start_month_tests.csv`
   - `results/transaction_cost_sensitivity.csv`
   - `results/regime_filter_results.csv`
   - `results/regime_filter_policy_summary.csv`
   - `results/portfolio_size_sensitivity.csv`

If a listed file is missing, record that fact in the experiment log and continue with the available evidence.

## Cycle Rules

Each improvement cycle must follow this order:

1. Read the latest reports.
2. Read the current portfolio recommendation.
3. Read paper trading performance.
4. Identify the biggest weakness supported by the evidence.
5. Propose one improvement only.
6. Implement only that one improvement.
7. Run full validation.
8. Compare against the previous baseline.
9. Accept or reject the change.
10. Log results in `experiments/experiment_log.md`.

Do not bundle multiple unrelated changes in one cycle. Examples of separate cycles:

- Adjust one factor model's weights.
- Add one diagnostic metric.
- Change one portfolio selection rule.
- Change one regime policy rule.
- Add one robustness check.

Formatting-only edits, broad refactors, dependency churn, and output cleanup are not valid improvement cycles unless the user explicitly asks for them.

## Baseline Capture

Before editing files, capture the current baseline from existing outputs. At minimum, record:

- Best validation model and portfolio size from `results/best_model.csv` or `results/final_report.csv`.
- Validation `selection_score`, `strategy_total_return`, `excess_return_over_benchmark`, `strategy_max_drawdown`, and `win_rate`.
- Out-of-sample values for the same selected model and portfolio size when available.
- Paper trading total return, benchmark return, active positions, and latest portfolio value when available.
- Any clear weakness visible in robustness, regime, transaction cost, or selection reports.

Use exact values from CSV files when possible. Markdown reports may be used for narrative context.

## Choosing The Biggest Weakness

Select the biggest weakness by evidence, not preference. Prioritize:

1. Out-of-sample underperformance versus BIST100.
2. Weak validation selection score or unstable validation/out-of-sample transfer.
3. Severe drawdown relative to benchmark.
4. Poor transaction cost sensitivity.
5. Concentration, repeated weak tickers, illiquidity, or speculative selections.
6. Paper trading deterioration or recommendation churn.
7. Missing or unclear reporting that blocks reliable decisions.

Write the weakness as a falsifiable statement, for example:

```text
Weakness: The selected validation model has positive validation excess return but negative out-of-sample excess return, suggesting weak regime transfer.
```

## Improvement Scope

Every cycle must have one hypothesis and one implementation.

Good hypothesis:

```text
Increasing the volatility penalty in the mixed model will reduce out-of-sample drawdown without materially reducing validation excess return.
```

Bad hypothesis:

```text
Improve ranking, reporting, and portfolio construction.
```

If the proposed improvement touches multiple files, the files must all support the same single change.

## Full Validation

Run the full project after the change:

```bash
python main.py
```

If the project virtual environment is required on Windows, use:

```bash
.venv\Scripts\python.exe main.py
```

Full validation must regenerate the standard outputs under `results/` and update paper trading outputs as designed by the project.

If validation fails, fix only issues directly caused by the attempted improvement, rerun validation, and record the failure and fix in the log. If validation cannot be completed, reject the change unless the user explicitly decides otherwise.

## Acceptance Criteria

Accept the change only when the evidence improves or preserves the system according to the cycle hypothesis.

Default acceptance preference:

- Validation selection score improves, and
- Out-of-sample excess return or drawdown does not materially worsen, and
- Robustness checks do not reveal a new obvious failure, and
- Paper trading report remains coherent, and
- The project completes `python main.py` successfully.

Reject the change when:

- Full validation fails.
- The main target metric worsens without a compelling offset.
- Out-of-sample performance materially deteriorates.
- Drawdown or transaction cost sensitivity becomes materially worse.
- The change makes recommendations less explainable.
- The cycle accidentally included more than one improvement.

When rejecting, revert only the files changed by the cycle. Never revert unrelated user changes or generated outputs that predated the cycle.

## Experiment Log

Append every cycle to:

```text
experiments/experiment_log.md
```

Each entry must include:

- timestamp
- hypothesis
- files changed
- metrics before
- metrics after
- accepted/rejected
- reasoning

Use this entry format:

```markdown
## YYYY-MM-DD HH:MM TZ - Short experiment name

- Timestamp: YYYY-MM-DD HH:MM TZ
- Hypothesis: ...
- Biggest weakness: ...
- Improvement implemented: ...
- Files changed:
  - `path/to/file.py`
- Metrics before:
  - Best validation model / size: ...
  - Validation selection_score: ...
  - Validation strategy_total_return: ...
  - Validation excess_return_over_benchmark: ...
  - Validation strategy_max_drawdown: ...
  - Validation win_rate: ...
  - Out-of-sample selection_score: ...
  - Out-of-sample strategy_total_return: ...
  - Out-of-sample excess_return_over_benchmark: ...
  - Out-of-sample strategy_max_drawdown: ...
  - Out-of-sample win_rate: ...
  - Paper trading total return: ...
  - Paper trading benchmark return: ...
- Validation command: `python main.py`
- Validation result: passed/failed
- Metrics after:
  - Best validation model / size: ...
  - Validation selection_score: ...
  - Validation strategy_total_return: ...
  - Validation excess_return_over_benchmark: ...
  - Validation strategy_max_drawdown: ...
  - Validation win_rate: ...
  - Out-of-sample selection_score: ...
  - Out-of-sample strategy_total_return: ...
  - Out-of-sample excess_return_over_benchmark: ...
  - Out-of-sample strategy_max_drawdown: ...
  - Out-of-sample win_rate: ...
  - Paper trading total return: ...
  - Paper trading benchmark return: ...
- Decision: accepted/rejected
- Reasoning: ...
```

## Git And Workspace Safety

Before editing, inspect the working tree:

```bash
git status --short
```

There may already be generated output changes in `results/`, `paper_trading/`, `data/`, `.venv/`, or `__pycache__/`. Do not revert or delete unrelated user changes. Keep manual source edits focused and clearly list generated output changes separately from source/config changes when logging.

## Completion Response

At the end of a cycle, report:

- The weakness identified.
- The one improvement implemented.
- The validation command and result.
- The before/after headline metrics.
- Whether the change was accepted or rejected.
- The log entry location.
