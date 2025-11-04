# src/train.py
import joblib
import pandas as pd
import os
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

    # Determine next model version
    os.makedirs("models", exist_ok=True)
    existing = [f for f in os.listdir("models") if f.startswith("model_v")]
    next_version = len(existing) + 1
    model_path = f"models/model_v{next_version}.joblib"

    joblib.dump(model, model_path)
    return model, (X_val, y_val), model_path


if __name__ == "__main__":
    import pandas as pd

    # Sample dummy data for demonstration
    df = pd.DataFrame(
        {
            "feature1": [1, 2, 3, 4],
            "feature2": [10, 20, 30, 40],
            "target": [0, 1, 0, 1],
        }
    )

    model, (X_val, y_val), model_path = train_model(df)

    print("✅ Model trained successfully.")
    print(f"📁 Saved model at: {model_path}")
