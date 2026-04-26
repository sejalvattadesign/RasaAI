from __future__ import annotations

from typing import Any, Dict, List


BUDGET_MAP = {
    "low": "low",
    "budget": "low",
    "cheap": "low",
    "medium": "medium",
    "mid": "medium",
    "moderate": "medium",
    "high": "high",
    "premium": "high",
    "expensive": "high",
}


def _split_csv_field(value: str) -> List[str]:
    return [item.strip() for item in value.split(",") if item.strip()]


def map_web_form_to_preferences(form_data: Dict[str, Any]) -> Dict[str, Any]:
    location = str(form_data.get("location", "")).strip()
    budget_raw = str(form_data.get("budget", "")).strip().lower()
    cuisines_raw = str(form_data.get("cuisines", "")).strip()
    min_rating_raw = str(form_data.get("min_rating", "")).strip()
    additional_raw = str(form_data.get("additional_preferences", "")).strip()
    max_results_raw = str(form_data.get("max_results", "")).strip()

    mapped = {
        "location": location.title(),
        "budget": BUDGET_MAP.get(budget_raw, budget_raw),
        "cuisines": [c.title() for c in _split_csv_field(cuisines_raw)],
        "min_rating": float(min_rating_raw) if min_rating_raw else 0.0,
        "additional_preferences": [p.strip() for p in _split_csv_field(additional_raw)],
        "max_results": int(max_results_raw) if max_results_raw else 5,
    }
    return mapped

