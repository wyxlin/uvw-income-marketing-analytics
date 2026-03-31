from __future__ import annotations

from pathlib import Path
import pandas as pd

from src.config import ADULT_COLUMNS


def load_adult_data(path: str | Path) -> pd.DataFrame:
    """Load the UCI Adult dataset from a local file path."""
    path = Path(path)

    if not path.exists():
        raise FileNotFoundError(f"Data file not found at {path}")

    df = pd.read_csv(
        path,
        names=ADULT_COLUMNS,
        na_values=["?", " ?"],
        skipinitialspace=True,
    )
    return df
