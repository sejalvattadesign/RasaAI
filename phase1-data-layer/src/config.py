from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class PipelineConfig:
    dataset_id: str = "ManikaSaini/zomato-restaurant-recommendation"
    split: str = "train"
    raw_output_csv: Path = Path("data/raw/zomato_raw.csv")
    processed_output_csv: Path = Path("data/processed/zomato_cleaned.csv")
    sqlite_path: Path = Path("data/processed/zomato.db")
    sqlite_table: str = "restaurants"

