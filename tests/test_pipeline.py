# tests/test_pipeline.py
from src.data_validation import validate_dataframe
import pandas as pd


def test_validation_passes():
    df = pd.DataFrame(
        {
            "feature1": [1, 2],
            "feature2": [3, 4],
            "target": [0, 1],
        }
    )
    assert validate_dataframe(df) is True
