from pathlib import Path

import pandas as pd

from src.models import UserPreferences
from src.pipeline import run_candidate_retrieval


def test_candidate_retrieval_filters_and_ranks(tmp_path: Path):
    data = pd.DataFrame(
        [
            {
                "restaurant_name": "Pasta Point",
                "location": "Bangalore",
                "cuisine": "Italian, Continental",
                "average_cost": 900,
                "rating": 4.5,
            },
            {
                "restaurant_name": "Noodle Nest",
                "location": "Bangalore",
                "cuisine": "Chinese",
                "average_cost": 700,
                "rating": 4.2,
            },
            {
                "restaurant_name": "Royal Grill",
                "location": "Bangalore",
                "cuisine": "North Indian",
                "average_cost": 2400,
                "rating": 4.8,
            },
            {
                "restaurant_name": "Delhi Diner",
                "location": "Delhi",
                "cuisine": "Italian",
                "average_cost": 850,
                "rating": 4.7,
            },
        ]
    )
    csv_path = tmp_path / "restaurants.csv"
    data.to_csv(csv_path, index=False)

    prefs = UserPreferences(
        location="Bangalore",
        budget="medium",
        cuisines=["Italian", "Chinese"],
        min_rating=4.0,
        max_results=3,
    )

    out = run_candidate_retrieval(data_path=csv_path, prefs=prefs, top_n=10)

    assert len(out) == 2
    assert out.iloc[0]["rank"] == 1
    assert set(out["restaurant_name"]) == {"Pasta Point", "Noodle Nest"}

