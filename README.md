# Zomato Restaurant Recommender

## Phase-Wise Code Layout

### Source
- `src/phase1/`: Data layer (ingestion, preprocessing, storage, pipeline runner)
- `src/phase2/`: User interaction layer (web form app, mapper, validator, schema loader)

### Tests
- `tests/phase1/`: Phase 1 unit tests
- `tests/phase2/`: Phase 2 unit tests

## Run Phase 1
```bash
PYTHONPATH=. python src/phase1/run.py
```

## Run Phase 2 Web UI
```bash
PYTHONPATH=. python src/phase2/web_app.py
```

## Run Tests
```bash
PYTHONPATH=. pytest -q tests
```

