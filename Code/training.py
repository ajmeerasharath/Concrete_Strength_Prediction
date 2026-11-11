from pathlib import Path

import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression


def train_linear_regression(
    X_train, X_test, y_train, y_test, feature_names, output_dir
):
    """Train multiple linear regression and save actual-vs-predicted plot."""
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    model = LinearRegression()
    model.fit(X_train, y_train)

    train_predictions = model.predict(X_train)
    test_predictions = model.predict(X_test)

    print("\nModel Intercept:", model.intercept_)
    print("\nFeature Coefficients:")
    for feature, coefficient in zip(feature_names, model.coef_):
        print(feature, ":", coefficient)

    plt.figure(figsize=(8, 6))
    plt.scatter(y_test, test_predictions, alpha=0.6)
    lower = min(float(y_test.min()), float(test_predictions.min()))
    upper = max(float(y_test.max()), float(test_predictions.max()))
    plt.plot([lower, upper], [lower, upper], linestyle="--")
    plt.xlabel("Actual Compressive Strength (MPa)")
    plt.ylabel("Predicted Compressive Strength (MPa)")
    plt.title("Actual vs Predicted Values")
    plt.grid(alpha=0.25)
    plt.tight_layout()
    plt.savefig(output_dir / "actual_vs_predicted.png", dpi=300)
    plt.show()
    plt.close()

    return model, train_predictions, test_predictions
