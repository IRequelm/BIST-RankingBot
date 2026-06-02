from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


def max_drawdown(equity: pd.Series) -> float:
    running_max = equity.cummax()
    drawdown = equity / running_max - 1
    return drawdown.min()


def summarize_returns(returns: pd.Series) -> dict[str, float]:
    returns = returns.dropna()
    if returns.empty:
        return {
            "total_return": 0.0,
            "avg_monthly_return": 0.0,
            "max_drawdown": 0.0,
            "win_rate": 0.0,
        }

    equity = (1 + returns).cumprod()
    return {
        "total_return": equity.iloc[-1] - 1,
        "avg_monthly_return": returns.mean(),
        "max_drawdown": max_drawdown(equity),
        "win_rate": (returns > 0).mean(),
    }


def selection_score(excess_return: float, max_dd: float, win_rate: float) -> float:
    return excess_return - abs(max_dd) * 2 + win_rate * 0.5


def _benchmark_for_dates(benchmark_monthly: pd.Series | None, dates: pd.Series) -> pd.Series:
    if benchmark_monthly is None or benchmark_monthly.empty:
        return pd.Series(dtype=float)

    idx = pd.to_datetime(dates)
    benchmark = benchmark_monthly.copy()
    benchmark.index = pd.to_datetime(benchmark.index)
    return benchmark.reindex(idx).dropna()


def _summarize_strategy(group: pd.DataFrame, benchmark_monthly: pd.Series | None) -> dict[str, object]:
    group = group.sort_values("date").copy()
    group["date"] = pd.to_datetime(group["date"])
    monthly_returns = group["net_return"]
    strategy_stats = summarize_returns(monthly_returns)

    benchmark_returns = _benchmark_for_dates(benchmark_monthly, group["date"])
    benchmark_stats = summarize_returns(benchmark_returns)

    best_month = group.loc[monthly_returns.idxmax()]
    worst_month = group.loc[monthly_returns.idxmin()]
    excess = strategy_stats["total_return"] - benchmark_stats["total_return"]

    return {
        "model": group["model"].iloc[0] if "model" in group.columns else "single_model",
        "period": group["period"].iloc[0] if "period" in group.columns else "full",
        "portfolio_size": int(group["portfolio_size"].iloc[0]),
        "transaction_cost": float(group["transaction_cost"].iloc[0]),
        "strategy": f"top_{int(group['portfolio_size'].iloc[0])}",
        "months": len(group),
        "strategy_total_return": strategy_stats["total_return"],
        "bist100_total_return": benchmark_stats["total_return"],
        "excess_return_over_benchmark": excess,
        "avg_monthly_return": strategy_stats["avg_monthly_return"],
        "strategy_max_drawdown": strategy_stats["max_drawdown"],
        "bist100_max_drawdown": benchmark_stats["max_drawdown"],
        "win_rate": strategy_stats["win_rate"],
        "selection_score": selection_score(excess, strategy_stats["max_drawdown"], strategy_stats["win_rate"]),
        "best_month": best_month["date"],
        "best_month_return": best_month["net_return"],
        "worst_month": worst_month["date"],
        "worst_month_return": worst_month["net_return"],
    }


def assign_periods(backtest_results: pd.DataFrame, periods: dict[str, tuple[str, str]]) -> pd.DataFrame:
    """Label each monthly result as train, validation, or out-of-sample."""
    if backtest_results.empty:
        return backtest_results

    labeled = backtest_results.copy()
    labeled["date"] = pd.to_datetime(labeled["date"])
    labeled["period"] = "unused"

    for period_name, (start, end) in periods.items():
        mask = (labeled["date"] >= pd.Timestamp(start)) & (labeled["date"] <= pd.Timestamp(end))
        labeled.loc[mask, "period"] = period_name

    return labeled[labeled["period"] != "unused"].copy()


def build_summary(backtest_results: pd.DataFrame, benchmark_monthly: pd.Series | None) -> pd.DataFrame:
    if backtest_results.empty:
        return pd.DataFrame()

    return pd.DataFrame(
        [
            _summarize_strategy(group, benchmark_monthly)
            for _, group in backtest_results.groupby(
                ["model", "period", "portfolio_size", "transaction_cost"],
                dropna=False,
            )
        ]
    )


def build_model_selection(summary: pd.DataFrame) -> pd.DataFrame:
    """Rank models using validation, out-of-sample stability, drawdown, and size consistency."""
    rows = []
    candidates = summary[summary["model"] != "benchmark"].copy()

    for model, model_df in candidates.groupby("model"):
        validation = model_df[model_df["period"] == "validation"]
        out_sample = model_df[model_df["period"] == "out_of_sample"]

        if validation.empty or out_sample.empty:
            continue

        validation_score = validation["selection_score"].mean()
        out_sample_score = out_sample["selection_score"].mean()
        out_sample_stability = -out_sample["selection_score"].std(ddof=0)
        drawdown_penalty = abs(out_sample["strategy_max_drawdown"].min())
        portfolio_consistency = -validation["selection_score"].std(ddof=0)

        robust_score = (
            validation_score * 0.35
            + out_sample_score * 0.35
            + out_sample_stability * 0.10
            + portfolio_consistency * 0.10
            - drawdown_penalty * 0.10
        )

        rows.append(
            {
                "model": model,
                "validation_score": validation_score,
                "out_of_sample_score": out_sample_score,
                "out_of_sample_stability": out_sample_stability,
                "drawdown_penalty": drawdown_penalty,
                "portfolio_consistency": portfolio_consistency,
                "robust_score": robust_score,
            }
        )

    if not rows:
        return pd.DataFrame()

    return pd.DataFrame(rows).sort_values("robust_score", ascending=False)


def save_summary_report(
    backtest_results: pd.DataFrame,
    benchmark_monthly: pd.Series | None,
    results_dir: str,
) -> pd.DataFrame:
    """Save benchmark-relative summary metrics as CSV and Markdown."""
    Path(results_dir).mkdir(exist_ok=True)
    summary = build_summary(backtest_results, benchmark_monthly)

    summary_path = Path(results_dir) / "summary_report.csv"
    summary.to_csv(summary_path, index=False)

    markdown_path = Path(results_dir) / "summary_report.md"
    with markdown_path.open("w", encoding="utf-8") as file:
        file.write("# BIST-RankingBot Summary Report\n\n")
        if summary.empty:
            file.write("No backtest results were generated.\n")
        else:
            file.write(summary.to_markdown(index=False, floatfmt=".4f"))
            file.write("\n")

    return summary


def build_final_report(summary: pd.DataFrame, model_selection: pd.DataFrame) -> tuple[pd.DataFrame, str]:
    if summary.empty:
        return pd.DataFrame(), "No results were generated.\n"

    validation_rows = summary[summary["period"] == "validation"].copy()
    out_sample_rows = summary[summary["period"] == "out_of_sample"].copy()

    best_validation = validation_rows.sort_values("selection_score", ascending=False).head(1)
    best_out_sample = out_sample_rows.sort_values("selection_score", ascending=False).head(1)
    most_robust = model_selection.head(1)

    rows = []
    if not best_validation.empty:
        source = best_validation.iloc[0]
        rows.append(
            {
                "category": "best_model_by_validation",
                "model": source["model"],
                "period": source["period"],
                "portfolio_size": source["portfolio_size"],
                "transaction_cost": source["transaction_cost"],
                "selection_score": source["selection_score"],
                "strategy_total_return": source["strategy_total_return"],
                "bist100_total_return": source["bist100_total_return"],
                "excess_return_over_benchmark": source["excess_return_over_benchmark"],
                "strategy_max_drawdown": source["strategy_max_drawdown"],
                "bist100_max_drawdown": source["bist100_max_drawdown"],
                "win_rate": source["win_rate"],
            }
        )
    if not best_out_sample.empty:
        source = best_out_sample.iloc[0]
        rows.append(
            {
                "category": "best_model_by_out_of_sample",
                "model": source["model"],
                "period": source["period"],
                "portfolio_size": source["portfolio_size"],
                "transaction_cost": source["transaction_cost"],
                "selection_score": source["selection_score"],
                "strategy_total_return": source["strategy_total_return"],
                "bist100_total_return": source["bist100_total_return"],
                "excess_return_over_benchmark": source["excess_return_over_benchmark"],
                "strategy_max_drawdown": source["strategy_max_drawdown"],
                "bist100_max_drawdown": source["bist100_max_drawdown"],
                "win_rate": source["win_rate"],
            }
        )
    if not most_robust.empty:
        source = most_robust.iloc[0]
        rows.append(
            {
                "category": "most_robust_model",
                "model": source["model"],
                "period": "all_splits",
                "portfolio_size": "all",
                "transaction_cost": "default",
                "selection_score": source["robust_score"],
                "strategy_total_return": "",
                "bist100_total_return": "",
                "excess_return_over_benchmark": "",
                "strategy_max_drawdown": -source["drawdown_penalty"],
                "bist100_max_drawdown": "",
                "win_rate": "",
                "validation_score": source["validation_score"],
                "out_of_sample_score": source["out_of_sample_score"],
                "out_of_sample_stability": source["out_of_sample_stability"],
                "portfolio_consistency": source["portfolio_consistency"],
                "robust_score": source["robust_score"],
            }
        )

    final = pd.DataFrame(rows)
    validation_model = best_validation["model"].iloc[0] if not best_validation.empty else None
    out_sample_model = best_out_sample["model"].iloc[0] if not best_out_sample.empty else None
    warning = ""
    if validation_model and out_sample_model and validation_model != out_sample_model:
        warning = (
            f"WARNING: validation winner ({validation_model}) differs from "
            f"out-of-sample winner ({out_sample_model})."
        )

    lines = ["# Final Model Report", ""]
    if warning:
        lines.extend([warning, ""])
    if not final.empty:
        lines.append(final.to_markdown(index=False, floatfmt=".4f"))
        lines.append("")

    return final, "\n".join(lines)


def save_charts(
    backtest_results: pd.DataFrame,
    benchmark_monthly: pd.Series | None,
    results_dir: str,
    filename_prefix: str = "",
) -> None:
    """Save equity curve and monthly return charts."""
    if backtest_results.empty:
        return

    Path(results_dir).mkdir(exist_ok=True)

    plt.figure(figsize=(11, 6))
    for (model, portfolio_size), group in backtest_results.groupby(["model", "portfolio_size"], dropna=False):
        group = group.sort_values("date")
        equity = (1 + group["net_return"]).cumprod()
        plt.plot(group["date"], equity, label=f"{model} Top {portfolio_size}")

    if benchmark_monthly is not None and not benchmark_monthly.empty:
        benchmark_equity = (1 + benchmark_monthly).cumprod()
        plt.plot(benchmark_equity.index, benchmark_equity.values, label="BIST100", linestyle="--")

    plt.title("Equity Curve")
    plt.xlabel("Date")
    plt.ylabel("Growth of 1 TRY")
    plt.legend(fontsize=8)
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(Path(results_dir) / f"{filename_prefix}equity_curve.png", dpi=150)
    plt.close()

    chart_df = backtest_results.copy()
    chart_df["strategy"] = chart_df["model"].astype(str) + "_top_" + chart_df["portfolio_size"].astype(str)
    pivot = chart_df.pivot(index="date", columns="strategy", values="net_return")
    pivot.index = pd.to_datetime(pivot.index).strftime("%Y-%m")
    pivot.plot(kind="bar", figsize=(12, 6))
    plt.title("Monthly Net Returns")
    plt.xlabel("Date")
    plt.ylabel("Return")
    plt.tight_layout()
    plt.savefig(Path(results_dir) / f"{filename_prefix}monthly_returns.png", dpi=150)
    plt.close()
