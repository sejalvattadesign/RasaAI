from __future__ import annotations

from typing import Any, Dict, List

from jsonschema import Draft202012Validator

from app.schema import load_user_preference_schema


class PreferenceValidationError(Exception):
    def __init__(self, errors: List[str]):
        super().__init__("Preference validation failed")
        self.errors = errors


def validate_preferences(payload: Dict[str, Any]) -> Dict[str, Any]:
    schema = load_user_preference_schema()
    validator = Draft202012Validator(schema)
    errors = sorted(validator.iter_errors(payload), key=lambda e: e.path)
    if errors:
        messages = []
        for err in errors:
            field = ".".join(str(p) for p in err.path) or "payload"
            messages.append(f"{field}: {err.message}")
        raise PreferenceValidationError(messages)
    return payload

