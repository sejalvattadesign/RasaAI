# Phase 2 User Interaction Implementation

This folder implements Phase 2 from `docs/phased-architecture.md` in a standalone module.

## Included Components
- **Basic web UI form** (primary input source for MVP)
- **Input validation service** using `jsonschema`
- **Preference schema mapper** from web form input to canonical JSON contract

## Contract Alignment
Validation is enforced against:
- `specs/contracts/user-preferences.schema.json`

## Run Locally
From this folder:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
PYTHONPATH=. python app/main.py
```

Open:
- <http://127.0.0.1:8080>

Submit the form to receive validated JSON payload output.

## Run Tests

```bash
source .venv/bin/activate
PYTHONPATH=. pytest -q
```

