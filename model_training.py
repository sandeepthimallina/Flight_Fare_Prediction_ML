import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score


# Load dataset
df = pd.read_csv(
    "data/Freshly_cleaned.csv/Freshly_cleaned.csv"
)

print("Dataset loaded successfully!")
print("Rows:", len(df))


# Remove unnecessary column
df = df.drop(columns=["Unnamed: 0"])


# Features and target
features = [
    "airline",
    "from",
    "to",
    "class",
    "day",
    "month",
    "dep_hour",
    "arr_hour",
    "duration_in_min",
    "stops"
]

target = "price"

X = df[features]
y = df[target]


# Categorical features
categorical_features = [
    "airline",
    "from",
    "to"
]


# Numerical features
numerical_features = [
    "class",
    "day",
    "month",
    "dep_hour",
    "arr_hour",
    "duration_in_min",
    "stops"
]


# Preprocessing
preprocessor = ColumnTransformer(
    transformers=[
        (
            "categorical",
            OneHotEncoder(handle_unknown="ignore"),
            categorical_features
        )
    ],
    remainder="passthrough"
)


# Random Forest model
model = RandomForestRegressor(
    n_estimators=100,
    max_depth=20,
    random_state=42,
    n_jobs=-1
)


# Pipeline
pipeline = Pipeline(
    steps=[
        ("preprocessor", preprocessor),
        ("model", model)
    ]
)


# Train/test split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

print("\nTraining data:", len(X_train))
print("Testing data:", len(X_test))


# Train model
print("\nTraining model...")

pipeline.fit(X_train, y_train)

print("Model training completed!")


# Predictions
print("\nMaking predictions...")

y_pred = pipeline.predict(X_test)


# Evaluation
mae = mean_absolute_error(y_test, y_pred)
rmse = mean_squared_error(y_test, y_pred) ** 0.5
r2 = r2_score(y_test, y_pred)


print("\n==========================================")
print("MODEL PERFORMANCE")
print("==========================================")

print("MAE:", round(mae, 2))
print("RMSE:", round(rmse, 2))
print("R2 Score:", round(r2, 4))


# Save model
joblib.dump(
    pipeline,
    "models/flight_fare_model.pkl"
)

print("\nModel saved successfully!")
print("Location: models/flight_fare_model.pkl")