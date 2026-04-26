#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path

from src.config import RetrievalConfig
from src.models import UserPreferences
from src.pipeline import run_candidate_retrieval


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run Phase 3 candidate retrieval.")
    parser.add_argument("--preferences-json", type=Path, required=True)
    parser.add_argument("--data-path", type=Path, default=None)
    parser.add_argument("--top-n", type=int, default=None)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    cfg = RetrievalConfig()

    with args.preferences_json.open("r", encoding="utf-8") as f:
        payload = json.load(f)

    prefs = UserPreferences(**payload)
    data_path = args.data_path or cfg.default_data_path
    top_n = args.top_n or max(prefs.max_results, cfg.default_top_n)

    ranked = run_candidate_retrieval(data_path=data_path, prefs=prefs, top_n=top_n)
    print(ranked[["rank", "restaurant_name", "location", "cuisine", "rating", "average_cost", "pre_score"]].head(prefs.max_results).to_string(index=False))
    print(f"\nTotal candidates after filter: {len(ranked)}")


if __name__ == "__main__":
    main()

