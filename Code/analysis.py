from pathlib import Path
import re

import matplotlib.pyplot as plt
import pandas as pd

TARGET_NAME = "Concrete compressive strength (MPa)"


def normalise_label(label):
    return re.sub(r"[^a-z0-9]", "", str(label).lower())


def load_dataset(csv_path):
    """Load the CSV and identify/standardise the concrete-strength target column."""
    csv_path = Path(csv_path)
    if not csv_path.exists():
        raise FileNotFoundError(f"Dataset not found: {csv_path}")

    df = pd.read_csv(csv_path)
    df.columns = [str(column).strip() for column in df.columns]

    target_column = next(
        (column for column in df.columns
         if "concretecompressivestrength" in normalise_label(column)),
        None,
    )
    if target_column is None:
        raise ValueError(
            "Target column not found. Expected a column named "
            "'concrete_compressive_strength' or equivalent."
        )

    if target_column != TARGET_NAME:
        df = df.rename(columns={target_column: TARGET_NAME})

    for column in df.columns:
        df[column] = pd.to_numeric(df[column], errors="coerce")

    print("Dataset loaded successfully!")
    return df


def perform_initial_analysis(df, output_dir):
    """Print dataset summaries and save analysis tables/heatmap."""
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    print("\n========== DATASET OVERVIEW ==========")
    print("Rows:", df.shape[0])
    print("Columns:", df.shape[1])
    print("\nFirst five rows:\n", df.head())
    print("\nData types:\n", df.dtypes)
    print("\nMissing values:\n", df.isnull().sum())
    print("\nDuplicate rows:", df.duplicated().sum())

    statistics = pd.DataFrame({
        "Mean": df.mean(numeric_only=True),
        "Median": df.median(numeric_only=True),
        "Standard Deviation": df.std(numeric_only=True),
    })
    print("\n========== DESCRIPTIVE STATISTICS ==========")
    print(statistics.round(3))
    statistics.to_csv(output_dir / "descriptive_statistics.csv")

    covariance = df.cov(numeric_only=True)
    print("\n========== COVARIANCE MATRIX ==========")
    print(covariance.round(3))
    covariance.to_csv(output_dir / "covariance_matrix.csv")

    correlation = df.corr(numeric_only=True)
    print("\n========== CORRELATION MATRIX ==========")
    print(correlation.round(3))
    correlation.to_csv(output_dir / "correlation_matrix.csv")

    plt.figure(figsize=(11, 8))
    plt.imshow(correlation, cmap="coolwarm", vmin=-1, vmax=1)
    plt.xticks(range(len(correlation.columns)), correlation.columns,
               rotation=75, ha="right")
    plt.yticks(range(len(correlation.columns)), correlation.columns)
    plt.title("Correlation Heatmap — Concrete Dataset")
    plt.colorbar(label="Pearson correlation")
    plt.tight_layout()
    plt.savefig(output_dir / "correlation_heatmap.png", dpi=300)
    plt.show()
    plt.close()
