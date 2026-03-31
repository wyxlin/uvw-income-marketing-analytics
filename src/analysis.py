from __future__ import annotations

from pathlib import Path
import pandas as pd

from .config import FIGURES_DIR, RAW_DIR
from .data_loader import load_adult_data
from .preprocess import clean_adult_dataframe, build_segment_table
from .visualize import save_age_income_plot, save_education_income_plot


def main() -> None:
    input_path = RAW_DIR / "adult.data"
    if not input_path.exists():
        raise FileNotFoundError(
            f"Expected dataset at {input_path}. Download adult.data and place it in data/raw/."
        )

    FIGURES_DIR.mkdir(parents=True, exist_ok=True)

    df = load_adult_data(input_path)
    df = clean_adult_dataframe(df)

    print("Rows, columns:", df.shape)
    print("\nMissing values by column:")
    print(df.isna().sum().sort_values(ascending=False).head(10))

    print("\nIncome distribution:")
    print(df["income"].value_counts(dropna=False, normalize=True).round(3))

    print("\nTop segment preview:")
    segment_table = build_segment_table(df)
    print(segment_table.head(10))

    save_age_income_plot(df, FIGURES_DIR / "age_income.png")
    save_education_income_plot(df, FIGURES_DIR / "education_income.png")

    print("\nSaved charts to figures/.")


if __name__ == "__main__":
    main()
