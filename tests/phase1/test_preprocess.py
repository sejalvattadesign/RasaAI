import pandas as pd

from src.phase1.preprocess import clean_values, normalize_columns, standardize_schema


def test_phase1_preprocess_flow():
    raw = pd.DataFrame(
        {
            "Restaurant Name": ["alpha bistro", "alpha bistro", "spice hub"],
            "City": ["bangalore", "bangalore", "delhi"],
            "Cuisines": ["italian", "italian", "north indian"],
            "Cost": ["1200", "1200", "-50"],
            "Rating": ["4.1", "4.1", "7.0"],
        }
    )
    df = normalize_columns(raw)
    df = standardize_schema(df)
    cleaned = clean_values(df)

    assert list(cleaned.columns)[:5] == [
        "restaurant_name",
        "location",
        "cuisine",
        "average_cost",
        "rating",
    ]
    assert len(cleaned) == 2  # duplicate row removed
    assert cleaned.iloc[0]["location"] == "Bangalore"

