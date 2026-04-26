from src.phase2.mapper import map_web_form_to_preferences


def test_map_web_form_to_preferences():
    form_payload = {
        "location": "delhi",
        "budget": "cheap",
        "cuisines": "italian, chinese",
        "min_rating": "4.2",
        "additional_preferences": "family-friendly, quick service",
        "max_results": "7",
    }
    mapped = map_web_form_to_preferences(form_payload)
    assert mapped["location"] == "Delhi"
    assert mapped["budget"] == "low"
    assert mapped["cuisines"] == ["Italian", "Chinese"]
    assert mapped["min_rating"] == 4.2
    assert mapped["max_results"] == 7

