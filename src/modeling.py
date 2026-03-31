from __future__ import annotations

from pathlib import Path

from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, roc_auc_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder

from .config import RAW_DIR
from .data_loader import load_adult_data
from .preprocess import clean_adult_dataframe, CATEGORICAL_COLUMNS, NUMERIC_COLUMNS


def main() -> None:
    input_path = RAW_DIR / "adult.data"
    if not input_path.exists():
        raise FileNotFoundError(
            f"Expected dataset at {input_path}. Download adult.data and place it in data/raw/."
        )

    df = clean_adult_dataframe(load_adult_data(input_path))
    df = df.dropna(subset=["income"]).copy()

    X = df[CATEGORICAL_COLUMNS + NUMERIC_COLUMNS]
    y = (df["income"] == ">50K").astype(int)

    preprocessor = ColumnTransformer(
        transformers=[
            (
                "num",
                Pipeline([
                    ("imputer", SimpleImputer(strategy="median")),
                ]),
                NUMERIC_COLUMNS,
            ),
            (
                "cat",
                Pipeline([
                    ("imputer", SimpleImputer(strategy="most_frequent")),
                    ("onehot", OneHotEncoder(handle_unknown="ignore")),
                ]),
                CATEGORICAL_COLUMNS,
            ),
        ]
    )

    model = Pipeline(
        steps=[
            ("preprocessor", preprocessor),
            ("classifier", LogisticRegression(max_iter=1000)),
        ]
    )

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    model.fit(X_train, y_train)
    preds = model.predict(X_test)
    probs = model.predict_proba(X_test)[:, 1]

    print("Accuracy:", round(accuracy_score(y_test, preds), 4))
    print("ROC AUC:", round(roc_auc_score(y_test, probs), 4))
    print("\nClassification report:\n")
    print(classification_report(y_test, preds))


if __name__ == "__main__":
    main()
