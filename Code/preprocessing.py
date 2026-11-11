from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline

from analysis import TARGET_NAME

preprocessing_pipeline = Pipeline([
    ("imputer", SimpleImputer(strategy="median"))
])


def preprocess_data(df):
    """Split features/target and fit median imputation on training features only."""
    df = df.copy()
    df.columns = df.columns.str.strip()

    if TARGET_NAME not in df.columns:
        raise ValueError(f"Expected target column '{TARGET_NAME}' was not found.")

    print("Available columns:", df.columns.tolist())
    target_name = TARGET_NAME
    print("Target column:", target_name)

    X = df.drop(columns=[target_name])
    y = df[target_name]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    pipeline = Pipeline([
        ("imputer", SimpleImputer(strategy="median"))
    ])
    X_train_processed = pipeline.fit_transform(X_train)
    X_test_processed = pipeline.transform(X_test)

    feature_names = X.columns.tolist()

    print("Training features:", X_train_processed.shape)
    print("Testing features:", X_test_processed.shape)
    print("Training targets:", y_train.shape)
    print("Testing targets:", y_test.shape)

    return (
        X_train_processed,
        X_test_processed,
        y_train,
        y_test,
        pipeline,
        feature_names,
    )
