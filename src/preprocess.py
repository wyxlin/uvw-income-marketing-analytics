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
        if cleaned[col].dtype == "object" or str(cleaned[col].dtype) == "string":
            cleaned[col] = cleaned[col].astype("string").str.strip()

    cleaned = cleaned.replace({"?": pd.NA, " ?": pd.NA})

    if TARGET_COLUMN in cleaned.columns:
        cleaned[TARGET_COLUMN] = cleaned[TARGET_COLUMN].str.replace(".", "", regex=False)
        cleaned[TARGET_COLUMN] = cleaned[TARGET_COLUMN].str.strip()

    return cleaned


def build_segment_table(df: pd.DataFrame) -> pd.DataFrame:
    """Return a business-facing education segment summary."""
    segment = (
        df.assign(is_high_income=df[TARGET_COLUMN] == ">50K")
        .groupby("education", dropna=False)
        .agg(
            total_count=(TARGET_COLUMN, "size"),
            high_income_count=("is_high_income", "sum"),
        )
        .reset_index()
    )

    segment["high_income_rate"] = (
        segment["high_income_count"] / segment["total_count"]
    ).round(3)

    segment = segment.sort_values(
        by=["high_income_rate", "total_count"], ascending=[False, False]
    )

    return segment
