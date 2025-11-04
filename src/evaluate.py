# src/evaluate.py
from sklearn.metrics import accuracy_score
import json
import os


def evaluate_model(model, X_val, y_val):
    preds = model.predict(X_val)
    accuracy = accuracy_score(y_val, preds)

    os.makedirs("reports", exist_ok=True)
    report = {"accuracy": accuracy}

    # Save current performance report
    with open("reports/performance_report.json", "w") as f:
        json.dump(report, f, indent=4)

    return report


def compare_with_previous():
    """Compare new model accuracy with previous report, if exists."""
    current_report_path = "reports/performance_report.json"
    previous_report_path = "reports/previous_performance.json"

    if not os.path.exists(previous_report_path):
        print("No previous performance found, treating current as best.")
        os.replace(current_report_path, previous_report_path)
        return True  # Accept new model as baseline

    with open(previous_report_path) as prev, open(current_report_path) as curr:
        prev_acc = json.load(prev)["accuracy"]
        curr_acc = json.load(curr)["accuracy"]

    print(f"Previous accuracy: {prev_acc}, Current accuracy: {curr_acc}")
    if curr_acc > prev_acc:
        print("New model performs better, promoting it.")
        os.replace(current_report_path, previous_report_path)
        return True
    else:
        print("New model performs worse or equal, rolling back.")
        return False
