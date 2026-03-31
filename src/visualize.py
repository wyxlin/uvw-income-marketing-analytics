from __future__ import annotations

from pathlib import Path
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

sns.set_theme(style="whitegrid")


def save_age_income_plot(df: pd.DataFrame, output_path: str | Path) -> None:
    output_path = Path(output_path)

    # 计算高收入比例
    grouped = df.assign(is_high_income=df["income"] == ">50K")
    plot_data = grouped.groupby("age")["is_high_income"].mean()

    plt.figure(figsize=(10, 6))
    plt.plot(plot_data.index, plot_data.values, marker="o", linewidth=1.5)

    plt.title("High Income Rate by Age")
    plt.xlabel("Age")
    plt.ylabel("High Income Rate")

    plt.tight_layout()
    plt.savefig(output_path, dpi=200)
    plt.close()


def save_education_income_plot(df: pd.DataFrame, output_path: str | Path) -> None:
    output_path = Path(output_path)

    grouped = df.assign(is_high_income=df["income"] == ">50K")

    plot_data = (
        grouped.groupby("education")["is_high_income"]
        .mean()
        .sort_values(ascending=False)
    )

    plt.figure(figsize=(12, 6))
    plot_data.plot(kind="bar")

    plt.title("High Income Rate by Education Level")
    plt.xlabel("Education")
    plt.ylabel("High Income Rate")

    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.savefig(output_path, dpi=200)
    plt.close()


def save_occupation_income_plot(df: pd.DataFrame, output_path: str | Path) -> None:
    output_path = Path(output_path)

    grouped = df.assign(is_high_income=df["income"] == ">50K")

    plot_data = (
        grouped.groupby("occupation")["is_high_income"]
        .mean()
        .sort_values(ascending=False)
        .head(15)
    )

    plt.figure(figsize=(12, 6))
    plot_data.plot(kind="bar")

    plt.title("Top Occupations by High Income Rate")
    plt.xlabel("Occupation")
    plt.ylabel("High Income Rate")

    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.savefig(output_path, dpi=200)
    plt.close()
