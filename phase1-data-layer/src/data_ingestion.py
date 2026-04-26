from pathlib import Path

import pandas as pd
from datasets import load_dataset


def ingest_from_huggingface(dataset_id: str, split: str = "train") -> pd.DataFrame:
    dataset = load_dataset(dataset_id, split=split)
    return dataset.to_pandas()


def ingest_from_csv(csv_path: Path) -> pd.DataFrame:
    return pd.read_csv(csv_path)

