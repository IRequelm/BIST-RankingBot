from datetime import date


# Yahoo Finance uses the ".IS" suffix for Borsa Istanbul symbols.
# Keep this list small for the MVP. Extend it later or load it from a file.
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

START_DATE = "2018-01-01"
END_DATE = date.today().isoformat()

DATA_DIR = "data"
RESULTS_DIR = "results"

PORTFOLIO_SIZES = [3, 5, 10, 15]
TRANSACTION_COST = 0.002  # 0.20% estimated round-trip monthly cost
TRANSACTION_COSTS = [0.001, 0.002, 0.005, 0.01]

# Split dates are month-end ranking dates. The best model is selected only
# from the validation period, then checked on the out-of-sample period.
TRAIN_START = "2018-01-01"
TRAIN_END = "2021-12-31"
VALIDATION_START = "2022-01-01"
VALIDATION_END = "2023-12-31"
OUT_OF_SAMPLE_START = "2024-01-01"
OUT_OF_SAMPLE_END = END_DATE

BEST_MODEL_PORTFOLIO_SIZE = 5

FACTOR_MODELS = {
    "momentum_heavy": {
        "momentum_1m": 0.25,
        "momentum_3m": 0.30,
        "momentum_6m": 0.30,
        "volume_increase": 0.05,
        "above_ma": 0.05,
        "volatility_penalty": 0.05,
    },
    "volume_heavy": {
        "momentum_1m": 0.15,
        "momentum_3m": 0.20,
        "momentum_6m": 0.15,
        "volume_increase": 0.35,
        "above_ma": 0.10,
        "volatility_penalty": 0.05,
    },
    "low_volatility": {
        "momentum_1m": 0.10,
        "momentum_3m": 0.15,
        "momentum_6m": 0.15,
        "volume_increase": 0.05,
        "above_ma": 0.15,
        "volatility_penalty": 0.40,
    },
    "trend_following": {
        "momentum_1m": 0.15,
        "momentum_3m": 0.25,
        "momentum_6m": 0.20,
        "volume_increase": 0.05,
        "above_ma": 0.30,
        "volatility_penalty": 0.05,
    },
    "mixed_model": {
        "momentum_1m": 0.20,
        "momentum_3m": 0.25,
        "momentum_6m": 0.25,
        "volume_increase": 0.10,
        "above_ma": 0.10,
        "volatility_penalty": 0.10,
    },
}
