from __future__ import annotations

import pandas as pd

from src.models import UserPreferences


def _budget_target(budget: str) -> float:
    b = budget.lower().strip()
    if b == "low":
        return 400
    if b == "medium":
        return 1000
    return 2200


def _score_row(row: pd.Series, prefs: UserPreferences) -> float:
    rating = float(row.get("rating") or 0)
    cost = float(row.get("average_cost") or 0)
    cuisine_text = str(row.get("cuisine") or "").lower()

    cuisine_match = 1.0 if any(c.lower() in cuisine_text for c in prefs.cuisines) else 0.0
    rating_score = rating / 5.0

    target = _budget_target(prefs.budget)
    cost_distance = min(abs(cost - target) / max(target, 1), 1.0)
    cost_score = 1.0 - cost_distance

    return 0.5 * rating_score + 0.35 * cuisine_match + 0.15 * cost_score


def rank_candidates(df: pd.DataFrame, prefs: UserPreferences, top_n: int) -> pd.DataFrame:
    if df.empty:
        return df.copy()

    ranked = df.copy()
    ranked["pre_score"] = ranked.apply(lambda row: _score_row(row, prefs), axis=1)
    ranked = ranked.sort_values(by=["pre_score", "rating"], ascending=[False, False]).head(top_n)
    ranked["rank"] = range(1, len(ranked) + 1)
    return ranked.reset_index(drop=True)

