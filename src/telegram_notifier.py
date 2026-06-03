import json
import os
import re
import urllib.parse
import urllib.request
from pathlib import Path


def _read_text(path: Path) -> str:
    if not path.exists():
        return ""
    return path.read_text(encoding="utf-8")


def _extract_bullet(text: str, label: str, default: str = "N/A") -> str:
    pattern = rf"^- {re.escape(label)}:\s*(.+)$"
    match = re.search(pattern, text, flags=re.MULTILINE)
    return match.group(1).strip() if match else default


def _extract_section_text(text: str, section: str, default: str = "None") -> str:
    pattern = rf"## {re.escape(section)}\n\n(.+?)(?:\n\n## |\Z)"
    match = re.search(pattern, text, flags=re.DOTALL)
    if not match:
        return default

    value = match.group(1).strip()
    if not value or value.startswith("|"):
        return default
    return " ".join(value.split())


def build_message(results_dir: str = "results") -> str:
    results_path = Path(results_dir)
    portfolio = _read_text(results_path / "current_month_portfolio.md")
    paper = _read_text(results_path / "paper_performance_report.md")

    regime_status = _extract_bullet(portfolio, "Regime status")
    confidence = _extract_bullet(portfolio, "Confidence score")
    buy_list = _extract_section_text(portfolio, "Buy List")
    sell_list = _extract_section_text(portfolio, "Sell List")
    hold_list = _extract_section_text(portfolio, "Hold List")

    portfolio_value = _extract_bullet(paper, "Portfolio value")
    total_return = _extract_bullet(paper, "Total return")
    benchmark_return = _extract_bullet(paper, "Benchmark return")
    unrealized_pnl = _extract_bullet(paper, "Unrealized PnL")

    return "\n".join(
        [
            "BIST-RankingBot nightly research",
            f"Regime: {regime_status}",
            f"Confidence: {confidence}",
            "",
            f"BUY: {buy_list}",
            f"SELL: {sell_list}",
            f"HOLD: {hold_list}",
            "",
            f"Portfolio value: {portfolio_value}",
            f"Total return: {total_return}",
            f"BIST100 return: {benchmark_return}",
            f"Unrealized PnL: {unrealized_pnl}",
            "",
            "Research-only update. No trades placed.",
        ]
    )


def send_telegram_message(message: str, token: str, chat_id: str) -> None:
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = urllib.parse.urlencode(
        {
            "chat_id": chat_id,
            "text": message,
            "disable_web_page_preview": "true",
        }
    ).encode("utf-8")

    request = urllib.request.Request(url, data=payload, method="POST")
    with urllib.request.urlopen(request, timeout=20) as response:
        body = json.loads(response.read().decode("utf-8"))
        if not body.get("ok"):
            raise RuntimeError(f"Telegram API error: {body}")


def main() -> None:
    token = os.environ.get("TELEGRAM_BOT_TOKEN")
    chat_id = os.environ.get("TELEGRAM_CHAT_ID")

    if not token or not chat_id:
        print("Telegram secrets not configured.")
        return

    message = build_message()
    send_telegram_message(message, token, chat_id)
    print("Telegram notification sent.")


if __name__ == "__main__":
    main()
