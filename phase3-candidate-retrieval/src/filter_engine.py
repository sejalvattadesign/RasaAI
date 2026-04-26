from __future__ import annotations

import re
from typing import Dict

import pandas as pd

from src.models import UserPreferences


_BUDGET_COST_RANGES: Dict[str, tuple[float, float]] = {
    "low": (0, 600),
    "medium": (601, 1500),
    "high": (1501, 100000),
}


def _contains_cuisine(cell: str, wanted: list[str]) -> bool:
    tokens = [x.strip().lower() for x in re.split(r"[,/|]", str(cell)) if x.strip()]
    wanted_set = {c.lower().strip() for c in wanted}
    return any(t in wanted_set for t in tokens) or any(w in str(cell).lower() for w in wanted_set)


def apply_filters(df: pd.DataFrame, prefs: UserPreferences) -> pd.DataFrame:
    filtered = df.copy()

    filtered = filtered[filtered["location"].str.lower() == prefs.location.lower()]
    filtered = filtered[filtered["rating"].fillna(0) >= prefs.min_rating]

    if prefs.cuisines:
        filtered = filtered[filtered["cuisine"].apply(lambda x: _contains_cuisine(x, prefs.cuisines))]

    budget_key = prefs.budget.lower().strip()
    if budget_key in _BUDGET_COST_RANGES:
        low, high = _BUDGET_COST_RANGES[budget_key]
        filtered = filtered[filtered["average_cost"].fillna(-1).between(low, high)]

    if prefs.cost_min is not None:
        filtered = filtered[filtered["average_cost"].fillna(-1) >= prefs.cost_min]
    if prefs.cost_max is not None:
        filtered = filtered[filtered["average_cost"].fillna(1000000) <= prefs.cost_max]

    return filtered.reset_index(drop=True)

