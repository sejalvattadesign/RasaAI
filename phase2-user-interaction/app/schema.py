from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict


def load_user_preference_schema() -> Dict[str, Any]:
    schema_path = (
        Path(__file__).resolve().parents[2]
        / "specs"
        / "contracts"
        / "user-preferences.schema.json"
    )
    with schema_path.open("r", encoding="utf-8") as f:
        return json.load(f)

