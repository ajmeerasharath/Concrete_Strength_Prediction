import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression


def train_linear_regression(X_train, X_test, y_train, y_test, feature_names):

    # Create model
    model = LinearRegression()

    # Train model
    model.fit(X_train, y_train)

    # Generate predictions
    train_predictions = model.predict(X_train)
    test_predictions = model.predict(X_test)

    # Display coefficients
    print("\nModel Intercept:", model.intercept_)

    print("\nFeature Coefficients:")
    for feature, coefficient in zip(feature_names, model.coef_):
        print(feature, ":", coefficient)

    # Actual vs Predicted plot
    plt.figure(figsize=(8, 6))
    plt.scatter(y_test, test_predictions, alpha=0.6)
    plt.xlabel("Actual Compressive Strength")
    plt.ylabel("Predicted Compressive Strength")
    plt.title("Actual vs Predicted Values")
    plt.savefig("actual_vs_predicted.png", dpi=300)
    plt.show()

    return model, train_predictions, test_predictions
