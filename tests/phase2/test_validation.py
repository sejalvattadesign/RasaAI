from src.phase2.validation import PreferenceValidationError, validate_preferences


def test_validate_preferences_success():
    payload = {
        "location": "Bangalore",
        "budget": "medium",
        "cuisines": ["Italian", "Chinese"],
        "min_rating": 3.5,
        "additional_preferences": ["family-friendly"],
        "max_results": 5,
    }
    validated = validate_preferences(payload)
    assert validated["location"] == "Bangalore"


def test_validate_preferences_failure():
    payload = {
        "location": "",
        "budget": "ultra-premium",
        "cuisines": [],
        "min_rating": 8,
    }
    try:
        validate_preferences(payload)
        assert False, "Expected validation to fail"
    except PreferenceValidationError as err:
        assert len(err.errors) > 0

