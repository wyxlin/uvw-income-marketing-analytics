from __future__ import annotations

from pathlib import Path
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

sns.set_theme(style="whitegrid")


def save_age_income_plot(df: pd.DataFrame, output_path: str | Path) -> None:
    plot_data = df.groupby(["age", "income"]).size().unstack(fill_value=0)
    plt.figure(figsize=(10, 6))
    for column in plot_data.columns:
        plt.plot(plot_data.index, plot_data[column], marker="o", linewidth=1.5, label=column)
    plt.title("Income Distribution Across Age")
    plt.xlabel("Age")
    plt.ylabel("Count")
    plt.legend(title="Income")
    plt.tight_layout()
    plt.savefig(output_path, dpi=200)
    plt.close()


def save_education_income_plot(df: pd.DataFrame, output_path: str | Path) -> None:
    plot_data = df.groupby(["education", "income"]).size().unstack(fill_value=0)
    plot_data = plot_data.div(plot_data.sum(axis=1), axis=0).sort_index()
    plot_data.plot(kind="bar", stacked=True, figsize=(12, 6))
    plt.title("Income Share by Education Level")
    plt.xlabel("Education")
    plt.ylabel("Share")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.savefig(output_path, dpi=200)
    plt.close()
