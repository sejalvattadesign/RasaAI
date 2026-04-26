from __future__ import annotations

import re
from typing import Dict

import pandas as pd


def _normalize_column_name(name: str) -> str:
    name = name.strip().lower()
    name = re.sub(r"[^a-z0-9]+", "_", name)
    return name.strip("_")


def normalize_columns(df: pd.DataFrame) -> pd.DataFrame:
    renamed = {_col: _normalize_column_name(_col) for _col in df.columns}
    return df.rename(columns=renamed)


def _canonical_map(columns: list[str]) -> Dict[str, str]:
    mapping: Dict[str, str] = {}
    aliases = {
        "restaurant_name": ["name", "restaurant_name", "restaurant", "res_name"],
        "location": ["location", "city", "locality", "address"],
        "cuisine": ["cuisine", "cuisines", "category", "food_type"],
        "average_cost": [
            "average_cost",
            "cost",
            "approx_cost_for_two_people",
            "average_cost_for_two",
        ],
        "rating": ["rating", "aggregate_rating", "user_rating", "stars"],
    }

    for target, keys in aliases.items():
        for key in keys:
            if key in columns:
                mapping[key] = target
                break
    return mapping


def standardize_schema(df: pd.DataFrame) -> pd.DataFrame:
    cols = list(df.columns)
    map_to_target = _canonical_map(cols)
    if map_to_target:
        df = df.rename(columns=map_to_target)

    required = ["restaurant_name", "location", "cuisine", "average_cost", "rating"]
    for col in required:
        if col not in df.columns:
            df[col] = pd.NA
    return df


def clean_values(df: pd.DataFrame) -> pd.DataFrame:
    cleaned = df.copy()

    for col in ["restaurant_name", "location", "cuisine"]:
        cleaned[col] = cleaned[col].astype("string").str.strip()

    cleaned["average_cost"] = pd.to_numeric(cleaned["average_cost"], errors="coerce")
    cleaned["rating"] = pd.to_numeric(cleaned["rating"], errors="coerce")

    cleaned.loc[cleaned["average_cost"] < 0, "average_cost"] = pd.NA
    cleaned.loc[(cleaned["rating"] < 0) | (cleaned["rating"] > 5), "rating"] = pd.NA

    cleaned["cuisine"] = (
        cleaned["cuisine"].fillna("Unknown").str.replace(r"\s+", " ", regex=True).str.title()
    )
    cleaned["location"] = (
        cleaned["location"]
        .fillna("Unknown")
        .str.replace(r"\s+", " ", regex=True)
        .str.title()
    )

    cleaned = cleaned.drop_duplicates(subset=["restaurant_name", "location"], keep="first")
    cleaned = cleaned.dropna(subset=["restaurant_name", "location"])

    return cleaned.reset_index(drop=True)

