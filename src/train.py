# src/train.py
import joblib
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split


def train_model(df: pd.DataFrame):
    X = df.drop(columns=["target"])
    y = df["target"]
    X_train, X_val, y_train, y_val = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    model = RandomForestClassifier(n_estimators=50, random_state=42)
    model.fit(X_train, y_train)
    joblib.dump(model, "models/model_v0.joblib")
    return model, (X_val, y_val)


if __name__ == "__main__":
    # Placeholder: replace with real data load
    df = pd.DataFrame(
        {
            "feature1": [1, 2, 3, 4],
            "feature2": [10, 20, 30, 40],
            "target": [0, 1, 0, 1],
        }
    )
    train_model(df)
