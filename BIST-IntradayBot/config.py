from pathlib import Path


PROJECT_NAME = "BIST-IntradayBot"

# Research-only. The bot never places real broker orders.
RESEARCH_ONLY = True

BIST_SYMBOLS = [
    "AKBNK.IS",
    "ARCLK.IS",
    "ASELS.IS",
    "BIMAS.IS",
    "EREGL.IS",
    "FROTO.IS",
    "GARAN.IS",
    "KCHOL.IS",
    "KOZAL.IS",
    "PETKM.IS",
    "PGSUS.IS",
    "SAHOL.IS",
    "SISE.IS",
    "TCELL.IS",
    "THYAO.IS",
    "TOASO.IS",
    "TUPRS.IS",
    "YKBNK.IS",
]

BENCHMARK_SYMBOL = "XU100.IS"

PREFERRED_INTERVALS = ["15m", "30m", "60m"]
YAHOO_PERIOD_BY_INTERVAL = {
    "15m": "5d",
    "30m": "60d",
    "60m": "730d",
}

STARTING_CAPITAL = 100_000.0
MAX_ACTIVE_POSITIONS = 3
TRANSACTION_COST_RATE = 0.0010
SLIPPAGE_RATE = 0.0005

DATA_DIR = Path("data")
REPORTS_DIR = Path("reports")
ARCHIVE_DIR = REPORTS_DIR / "archive"

MIN_OPENING_STRENGTH = 0.004
MIN_VOLUME_RATIO = 1.05
MAX_INTRADAY_VOLATILITY = 0.08
MAX_SPIKE_RETURN = 0.05
MAX_CANDLE_RANGE = 0.04
