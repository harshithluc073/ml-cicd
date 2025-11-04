# src/evaluate.py
from sklearn.metrics import accuracy_score
import json
import os


def evaluate_model(model, X_val, y_val):
    preds = model.predict(X_val)
    accuracy = accuracy_score(y_val, preds)

    # Save metrics report
    os.makedirs("reports", exist_ok=True)
    report = {"accuracy": accuracy}
    with open("reports/performance_report.json", "w") as f:
        json.dump(report, f, indent=4)

    return report
