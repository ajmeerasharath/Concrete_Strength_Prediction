from pathlib import Path

from analysis import load_dataset, perform_initial_analysis
from preprocessing import preprocess_data
from training import train_linear_regression
from evaluation import evaluate_model


PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATASET_PATH = PROJECT_ROOT / "data" / "concrete_data.csv"
OUTPUT_DIR = PROJECT_ROOT / "outputs"


def main():
    print("\n========== LOADING DATASET ==========")
    dataset = load_dataset(DATASET_PATH)
    print("Dataset shape:", dataset.shape)

    print("\n========== INITIAL DATA ANALYSIS ==========")
    perform_initial_analysis(dataset, OUTPUT_DIR)

    print("\n========== DATA PREPROCESSING ==========")
    X_train, X_test, y_train, y_test, preprocessing_pipeline, feature_names = (
        preprocess_data(dataset)
    )
    print("Preprocessing completed successfully!")
    print("Training samples:", len(X_train))
    print("Testing samples:", len(X_test))
    print("Number of features:", len(feature_names))

    print("\n========== MODEL TRAINING ==========")
    print("X_train:", X_train.shape)
    print("X_test:", X_test.shape)
    print("y_train:", y_train.shape)
    print("y_test:", y_test.shape)

    model, train_predictions, test_predictions = train_linear_regression(
        X_train, X_test, y_train, y_test, feature_names, OUTPUT_DIR
    )
    print("Linear Regression model trained successfully!")

    print("\n========== MODEL EVALUATION ==========")
    evaluate_model(
        y_train, y_test, train_predictions, test_predictions, OUTPUT_DIR
    )

    print("\n========== PROJECT COMPLETED SUCCESSFULLY ==========")
    print("Project: Concrete Compressive Strength Prediction")
    print("Algorithm: Multiple Linear Regression")
    print("Status: Successfully Completed!")
    print(f"Generated files: {OUTPUT_DIR}")


if __name__ == "__main__":
    main()
