from __future__ import annotations

from pathlib import Path

import pandas as pd

from src.data_loader import load_restaurants
from src.filter_engine import apply_filters
from src.models import UserPreferences
from src.ranking import rank_candidates


def run_candidate_retrieval(
    data_path: Path,
    prefs: UserPreferences,
    top_n: int,
) -> pd.DataFrame:
    restaurants = load_restaurants(data_path)
    filtered = apply_filters(restaurants, prefs)
    ranked = rank_candidates(filtered, prefs, top_n)
    return ranked

