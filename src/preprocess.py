from __future__ import annotations

import pandas as pd

CATEGORICAL_COLUMNS = [
    "workclass",
    "education",
    "marital-status",
    "occupation",
    "relationship",
    "race",
    "sex",
    "native-country",
]

NUMERIC_COLUMNS = [
    "age",
    "fnlwgt",
    "education-num",
    "capital-gain",
    "capital-loss",
    "hours-per-week",
]

TARGET_COLUMN = "income"


def clean_adult_dataframe(df: pd.DataFrame) -> pd.DataFrame:
    """Standardize whitespace, missing values, and target labels."""
    cleaned = df.copy()

    for col in cleaned.columns:
        if cleaned[col].dtype == "object":
            cleaned[col] = cleaned[col].astype("string").str.strip()

    cleaned = cleaned.replace({"?": pd.NA, " ?": pd.NA})

    if TARGET_COLUMN in cleaned.columns:
        cleaned[TARGET_COLUMN] = cleaned[TARGET_COLUMN].str.replace(".", "", regex=False)

    return cleaned


def build_segment_table(df: pd.DataFrame) -> pd.DataFrame:
    """Return a simple business-facing segment summary."""
    segment = (
        df.groupby(["education", "income"], dropna=False)
        .size()
        .reset_index(name="count")
        .sort_values(["education", "count"], ascending=[True, False])
    )
    return segment
