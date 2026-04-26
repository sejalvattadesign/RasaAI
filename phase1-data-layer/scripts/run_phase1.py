#!/usr/bin/env python3
from __future__ import annotations

import argparse
from pathlib import Path

from src.config import PipelineConfig
from src.pipeline import run_phase1_pipeline


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run Phase 1 data layer pipeline.")
    parser.add_argument(
        "--source-csv",
        type=Path,
        default=None,
        help="Optional local CSV path. If omitted, loads dataset from Hugging Face.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    config = PipelineConfig()
    cleaned_df = run_phase1_pipeline(config, source_csv=args.source_csv)
    print("Phase 1 pipeline completed.")
    print(f"Rows after cleaning: {len(cleaned_df)}")
    print(f"Raw CSV: {config.raw_output_csv}")
    print(f"Processed CSV: {config.processed_output_csv}")
    print(f"SQLite DB: {config.sqlite_path} (table: {config.sqlite_table})")


if __name__ == "__main__":
    main()

