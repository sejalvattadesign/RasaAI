# Phase 3 Candidate Retrieval (Standalone)

Implements Phase 3 from `docs/phased-architecture.md`:
- Rule-based filter engine
- Deterministic pre-ranking by match quality
- Optional cost-range filtering

## Structure
- `src/data_loader.py`: loads cleaned restaurant dataset
- `src/filter_engine.py`: applies location/rating/cuisine/budget/cost filters
- `src/ranking.py`: computes deterministic pre-score and rank
- `src/pipeline.py`: orchestrates candidate retrieval
- `scripts/run_phase3.py`: CLI runner

## Setup
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Run
Create a JSON file (example):

```json
{
  "location": "Bangalore",
  "budget": "medium",
  "cuisines": ["Italian", "Chinese"],
  "min_rating": 3.8,
  "additional_preferences": [],
  "max_results": 5
}
```

Then execute:

```bash
PYTHONPATH=. python scripts/run_phase3.py --preferences-json ./preferences.json --data-path ../data/processed/zomato_cleaned.csv --top-n 20
```

## Test
```bash
PYTHONPATH=. pytest -q
```

