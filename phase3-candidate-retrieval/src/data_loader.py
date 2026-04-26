from pathlib import Path

import pandas as pd


def load_restaurants(data_path: Path) -> pd.DataFrame:
    df = pd.read_csv(data_path)
    required = {"restaurant_name", "location", "cuisine", "average_cost", "rating"}
    missing = required.difference(df.columns)
    if missing:
        raise ValueError(f"Dataset missing required columns: {sorted(missing)}")
    return df

