import os
from dotenv import load_dotenv

# Load from docs/.env where the key is located
load_dotenv("../docs/.env")

from src.pipeline import run_phase4

preferences = {
    "location": "Bellandur",
    "budget": "high",  # We interpret 2000 as high
    "cuisines": ["North Indian", "Chinese", "Continental", "Italian"],
    "min_rating": 4.0,
    "additional_preferences": ["Budget around 2000 INR", "Good ambiance"]
}

# Provide some mock candidates since Phase 4 expects a candidate list
candidates = [
    {
        "id": "1",
        "name": "The Irish House",
        "location": "Bellandur, Bangalore",
        "cuisine": "European, American",
        "rating": 4.3,
        "cost": "1700",
        "metadata": {"votes": 1200, "ambiance": "Great"}
    },
    {
        "id": "2",
        "name": "Flechazo",
        "location": "Bellandur, Bangalore",
        "cuisine": "Asian, Mediterranean, North Indian",
        "rating": 4.6,
        "cost": "1400",
        "metadata": {"votes": 4000, "ambiance": "Buffet, Lively"}
    },
    {
        "id": "3",
        "name": "Mocha",
        "location": "Bellandur, Bangalore",
        "cuisine": "Cafe, Continental, Italian",
        "rating": 4.1,
        "cost": "1500",
        "metadata": {"votes": 500, "ambiance": "Cozy, Cafe"}
    },
    {
        "id": "4",
        "name": "Punjab Grill",
        "location": "Bellandur, Bangalore",
        "cuisine": "North Indian",
        "rating": 4.5,
        "cost": "2000",
        "metadata": {"votes": 800, "ambiance": "Fine Dining, Elegant"}
    },
    {
        "id": "5",
        "name": "Chili's American Grill & Bar",
        "location": "Bellandur, Bangalore",
        "cuisine": "American, Mexican, Tex-Mex",
        "rating": 4.4,
        "cost": "1800",
        "metadata": {"votes": 2000, "ambiance": "Casual, Sports Bar"}
    },
    {
        "id": "6",
        "name": "Nasi and Mee",
        "location": "Bellandur, Bangalore",
        "cuisine": "Asian, Chinese, Thai",
        "rating": 4.2,
        "cost": "1500",
        "metadata": {"votes": 900, "ambiance": "Modern Asian"}
    },
    {
        "id": "7",
        "name": "Under The Stars",
        "location": "Bellandur, Bangalore",
        "cuisine": "North Indian, Continental",
        "rating": 3.9,  # This one should be ranked lower or excluded ideally based on reasoning
        "cost": "1600",
        "metadata": {"votes": 300, "ambiance": "Rooftop"}
    }
]

response = run_phase4(preferences, candidates)

import json
print(json.dumps(response, indent=2))
