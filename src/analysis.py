from __future__ import annotations

from src.config import FIGURES_DIR, RAW_DIR
from src.data_loader import load_adult_data
from src.preprocess import clean_adult_dataframe, build_segment_table
from src.visualize import save_age_income_plot, save_education_income_plot


def main() -> None:
    input_path = RAW_DIR / "adult.data"
    if not input_path.exists():
        raise FileNotFoundError(
            f"Expected dataset at {input_path}. Download adult.data and place it in data/raw/."
        )

    FIGURES_DIR.mkdir(parents=True, exist_ok=True)

    df = load_adult_data(input_path)
    df = clean_adult_dataframe(df)

    print("=" * 60)
    print("Dataset shape")
    print(df.shape)

    print("\n" + "=" * 60)
    print("Top missing values by column")
    print(df.isna().sum().sort_values(ascending=False).head(10))

    print("\n" + "=" * 60)
    print("Income distribution")
    print(df["income"].value_counts(dropna=False, normalize=True).round(3))

    print("\n" + "=" * 60)
    print("Top segment preview")
    segment_table = build_segment_table(df)
    print(segment_table.head(10))

    save_age_income_plot(df, FIGURES_DIR / "age_income.png")
    save_education_income_plot(df, FIGURES_DIR / "education_income.png")

    print("\n" + "=" * 60)
    print("Saved charts to figures/.")


if __name__ == "__main__":
    main()
