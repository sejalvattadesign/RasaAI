# Phase 1 Data Layer Implementation

This folder contains the standalone implementation for **Phase 1: Data Layer Setup** from `docs/phased-architecture.md`.

## What It Implements
- Dataset ingestion from Hugging Face (`ManikaSaini/zomato-restaurant-recommendation`) or local CSV.
- Column normalization and schema standardization.
- Data cleaning for key fields (`restaurant_name`, `location`, `cuisine`, `average_cost`, `rating`).
- Basic deduplication.
- Persistence to:
  - `data/raw/zomato_raw.csv`
  - `data/processed/zomato_cleaned.csv`
  - `data/processed/zomato.db` (SQLite table: `restaurants`)

## Setup
From this folder:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Run

### Option A: Ingest directly from Hugging Face
```bash
PYTHONPATH=. python scripts/run_phase1.py
```

### Option B: Use local CSV
```bash
PYTHONPATH=. python scripts/run_phase1.py --source-csv /path/to/zomato.csv
```

## Outputs
- Raw and cleaned CSV files in `data/`.
- SQLite DB with cleaned restaurant records for fast downstream retrieval.

