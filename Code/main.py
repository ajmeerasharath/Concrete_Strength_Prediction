
from analysis import load_dataset, perform_initial_analysis
from preprocessing import preprocess_data
from training import train_linear_regression
from evaluation import evaluate_model
import inspect

project_folder = inspect.getfile(inspect.currentframe())
project_folder = project_folder.replace("main.py", "")

print("\n========== LOADING DATASET ==========")

dataset = load_dataset(project_folder + "Concrete_Data.csv")

print("Dataset loaded successfully!")
print("Dataset shape:", dataset.shape)

print("\n========== INITIAL DATA ANALYSIS ==========")

perform_initial_analysis(dataset)


print("\n========== DATA PREPROCESSING ==========")

X_train, X_test, y_train, y_test, preprocessing_pipeline, feature_names = preprocess_data(dataset)

print("Preprocessing completed successfully!")
print("Training samples:", len(X_train))
print("Testing samples:", len(X_test))
print("Number of features:", len(feature_names))


print("\n========== MODEL TRAINING ==========")
print("\nChecking data dimensions:")
print("X_train:", X_train.shape)
print("X_test:", X_test.shape)
print("y_train:", y_train.shape)
print("y_test:", y_test.shape)
model, train_predictions, test_predictions = train_linear_regression(
    X_train,
    X_test,
    y_train,
    y_test,
    feature_names
)

print("Linear Regression model trained successfully!")

print("\n========== MODEL EVALUATION ==========")

evaluate_model(
    y_train,
    y_test,
    train_predictions,
    test_predictions
)


print("\n========== PROJECT COMPLETED SUCCESSFULLY  ==========")
print("Project: Concrete Compressive Strength Prediction")
print("Algorithm: Multiple Linear Regression")
print("Status: Successfully Completed!")
