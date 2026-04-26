from __future__ import annotations

from pathlib import Path

import pandas as pd

from src.config import PipelineConfig
from src.data_ingestion import ingest_from_csv, ingest_from_huggingface
from src.preprocess import clean_values, normalize_columns, standardize_schema
from src.storage import persist_csv, persist_sqlite


def run_phase1_pipeline(config: PipelineConfig, source_csv: Path | None = None) -> pd.DataFrame:
    if source_csv is not None:
        raw_df = ingest_from_csv(source_csv)
    else:
        raw_df = ingest_from_huggingface(config.dataset_id, config.split)

    persist_csv(raw_df, config.raw_output_csv)

    cleaned_df = normalize_columns(raw_df)
    cleaned_df = standardize_schema(cleaned_df)
    cleaned_df = clean_values(cleaned_df)

    persist_csv(cleaned_df, config.processed_output_csv)
    persist_sqlite(cleaned_df, config.sqlite_path, config.sqlite_table)

    return cleaned_df

