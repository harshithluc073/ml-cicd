# src/data_validation.py
import pandas as pd


def validate_dataframe(df: pd.DataFrame) -> bool:
    # Basic checks: no missing target, expected columns present
    expected_cols = {"feature1", "feature2", "target"}
    if not expected_cols.issubset(set(df.columns)):
        return False
    if df["target"].isnull().any():
        return False
    return True
