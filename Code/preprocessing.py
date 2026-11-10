
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline

from analysis import TARGET_NAME

preprocessing_pipeline = Pipeline([
    ("imputer", SimpleImputer(strategy="median"))
])
def preprocess_data(df):

    df.columns = df.columns.str.strip()
    print("Available columns:", df.columns.tolist())
    target_name = df.columns[-1]
    print("Target column:", target_name)
    X = df.drop(columns=[target_name])
    y = df[target_name]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    X_train_processed = preprocessing_pipeline.fit_transform(X_train)
    X_test_processed = preprocessing_pipeline.transform(X_test)

    feature_names = X.columns

    print("Training features:", X_train_processed.shape)
    print("Testing features:", X_test_processed.shape)
    print("Training targets:", y_train.shape)
    print("Testing targets:", y_test.shape)

    return (
        X_train_processed,
        X_test_processed,
        y_train,
        y_test,
        preprocessing_pipeline,
        feature_names
    )
