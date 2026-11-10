"""Load and validate the concrete strength dataset."""

from pathlib import Path
import pandas as pd

FEATURES = [
    "cement",
    "blast_furnace_slag",
    "fly_ash",
    "water",
    "superplasticizer",
    "coarse_aggregate",
    "fine_aggregate",
    "age",
]
TARGET = "concrete_compressive_strength"


def load_dataset(csv_path: str | Path) -> tuple[pd.DataFrame, pd.Series]:
    """Load the CSV, normalize column names, and return all 8 features and target."""
    csv_path = Path(csv_path)
    if not csv_path.exists():
        raise FileNotFoundError(
            f"Dataset not found: {csv_path}\n"
            "Place concrete_data.csv inside the project's data/ folder."
        )


    data = pd.read_csv(csv_path)
    # Remove accidental leading/trailing spaces from column names.
    data.columns = data.columns.astype(str).str.strip()

    required_columns = FEATURES + [TARGET]
    missing_columns = [col for col in required_columns if col not in data.columns]
    if missing_columns:
        raise ValueError(
            "The dataset is missing required columns: "
            + ", ".join(missing_columns)
            + "\nColumns found: "
            + ", ".join(data.columns)
        )

    # Keep the eight specified predictors and the target.
    selected = data[required_columns].copy()

    # Convert all selected columns to numeric; invalid entries become missing.
    for column in required_columns:
        selected[column] = pd.to_numeric(selected[column], errors="coerce")

    # Remove rows where the target is unavailable; feature missing values are
    # imputed later inside the training pipeline to avoid data leakage.
    selected = selected.dropna(subset=[TARGET])

    if selected.empty:
        raise ValueError("No usable rows remain after checking the target column.")

    X = selected[FEATURES]
    y = selected[TARGET]
    return X, y
