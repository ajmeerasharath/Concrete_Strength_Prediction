import re
import pandas as pd
import matplotlib.pyplot as plt

TARGET_NAME = "Concrete compressive strength (MPa)"


def normalise_label(label):
    return re.sub(r"[^a-z0-9]", "", str(label).lower())


def load_dataset(csv_path="concrete_data.csv"):
    df = pd.read_csv(csv_path)
    df.columns = [str(column).strip() for column in df.columns]

    target_column = None

    for column in df.columns:
        if "concretecompressivestrength" in normalise_label(column):
            target_column = column
            break

    if target_column is None:
        raise ValueError("Target column not found.")

    if target_column != TARGET_NAME:
        df.rename(columns={target_column: TARGET_NAME}, inplace=True)

    for column in df.columns:
        df[column] = pd.to_numeric(df[column], errors="coerce")

    print("Dataset loaded successfully!")
    return df


def perform_initial_analysis(df):

    print("\n========== DATASET OVERVIEW ==========")
    print("Rows:", df.shape[0])
    print("Columns:", df.shape[1])
    print("\nFirst five rows:")
    print(df.head())
    print("\nData types:")
    print(df.dtypes)
    print("\nMissing values:")
    print(df.isnull().sum())
    print("\nDuplicate rows:", df.duplicated().sum())

    statistics = pd.DataFrame({
        "Mean": df.mean(numeric_only=True),
        "Median": df.median(numeric_only=True),
        "Standard Deviation": df.std(numeric_only=True),
    })

    print("\n========== DESCRIPTIVE STATISTICS ==========")
    print(statistics.round(3))
    statistics.to_csv("descriptive_statistics.csv")

    covariance = df.cov(numeric_only=True)
    print("\n========== COVARIANCE MATRIX ==========")
    print(covariance.round(3))
    covariance.to_csv("covariance_matrix.csv")

    correlation = df.corr(numeric_only=True)
    print("\n========== CORRELATION MATRIX ==========")
    print(correlation.round(3))
    correlation.to_csv("correlation_matrix.csv")

    plt.figure(figsize=(11, 8))
    plt.imshow(correlation, cmap="coolwarm", vmin=-1, vmax=1)
    plt.xticks(
        range(len(correlation.columns)),
        correlation.columns,
        rotation=75,
        ha="right"
    )
    plt.yticks(range(len(correlation.columns)), correlation.columns)
    plt.title("Correlation Heatmap — Concrete Dataset")
    plt.colorbar(label="Pearson correlation")
    plt.tight_layout()
