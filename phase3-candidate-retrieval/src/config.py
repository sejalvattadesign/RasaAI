from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class RetrievalConfig:
    default_data_path: Path = Path("../data/processed/zomato_cleaned.csv")
    default_top_n: int = 20

