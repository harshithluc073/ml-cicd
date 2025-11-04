# src/dashboard.py
import json
import os
from datetime import datetime


def update_dashboard():
    os.makedirs("dashboard", exist_ok=True)
    report_path = "reports/previous_performance.json"

    with open(report_path, "r", encoding="utf-8") as file:
        metrics = json.load(file)

    accuracy = metrics.get("accuracy", 0.0)

    # Break long string clearly below 79 characters
    timestamp = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")

    dashboard_path = "dashboard/performance.md"

    # Add header if file is new or very small
    if not os.path.exists(dashboard_path) or os.path.getsize(dashboard_path) < 50:
        with open(dashboard_path, "w", encoding="utf-8") as dash:
            dash.write("| Timestamp | Accuracy | Version |\n")
            dash.write("|------------|-----------|----------|\n")

    # Append new line for this release
    version_count = len(os.listdir("models"))
    with open(dashboard_path, "a", encoding="utf-8") as dash:
        dash.write(f"| {timestamp} | {accuracy:.4f} | v{version_count} |\n")


if __name__ == "__main__":
    update_dashboard()
