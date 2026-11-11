from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score


def calculate_metrics(actual, predicted):
    mse = mean_squared_error(actual, predicted)
    return {
        "R2": r2_score(actual, predicted),
        "MAE": mean_absolute_error(actual, predicted),
        "MSE": mse,
        "RMSE": np.sqrt(mse),
    }


def evaluate_model(y_train, y_test, train_predictions, test_predictions, output_dir):
    """Calculate metrics, save the metrics table and residual plot."""
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    train_metrics = calculate_metrics(y_train, train_predictions)
    test_metrics = calculate_metrics(y_test, test_predictions)

    metrics = pd.DataFrame(
        [train_metrics, test_metrics], index=["Training", "Testing"]
    )
    print("\n========== MODEL EVALUATION ==========")
    print(metrics.round(4))
    metrics.to_csv(output_dir / "evaluation_metrics.csv")

    residuals = np.asarray(y_test) - np.asarray(test_predictions)
    plt.figure(figsize=(8, 6))
    plt.scatter(test_predictions, residuals, alpha=0.65)
    plt.axhline(y=0, linestyle="--")
    plt.xlabel("Predicted compressive strength (MPa)")
    plt.ylabel("Residual (Actual - Predicted)")
    plt.title("Residual Plot — Testing Set")
    plt.grid(alpha=0.25)
    plt.tight_layout()
    plt.savefig(output_dir / "residual_plot.png", dpi=300)
    plt.show()
    plt.close()

    print("\n========== FINAL ANALYSIS ==========")
    print("Testing R2:", round(test_metrics["R2"], 4))
    print("Testing MAE:", round(test_metrics["MAE"], 4), "MPa")
    print("Testing RMSE:", round(test_metrics["RMSE"], 4), "MPa")

    if test_metrics["R2"] > 0:
        print(
            "The model explains a positive proportion of the variation "
            "in unseen test-set concrete strength values."
        )
    else:
        print("The model performs poorly on this test split according to R2.")

    r2_gap = train_metrics["R2"] - test_metrics["R2"]
    if r2_gap > 0.15:
        print(
            "Training R2 is noticeably higher than testing R2. "
            "This may indicate overfitting or sensitivity to the data split."
        )
    else:
        print(
            "The training/testing R2 gap is not especially large for this "
            "split. Performance should still be checked on other data."
        )

    print(
        "\nA coefficient estimates the change in predicted strength for a "
        "one-unit increase in a feature, holding other features constant. "
        "It does not establish causation."
    )
    return metrics
