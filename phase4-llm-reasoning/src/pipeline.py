from typing import List, Dict
from .models import UserPreferences, CandidateRestaurant, RecommendationResponse
from .llm_integration import LLMReasoningEngine

def run_phase4(preferences_dict: dict, candidates_list: List[dict]) -> dict:
    preferences = UserPreferences(**preferences_dict)
    candidates = [CandidateRestaurant(**c) for c in candidates_list]
    
    engine = LLMReasoningEngine()
    response = engine.generate_recommendations(preferences, candidates)
    
    return response.model_dump()
