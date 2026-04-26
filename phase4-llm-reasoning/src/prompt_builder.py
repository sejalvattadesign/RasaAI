from typing import List
from .models import UserPreferences, CandidateRestaurant

def build_prompt(preferences: UserPreferences, candidates: List[CandidateRestaurant]) -> str:
    prompt = f"""
You are an expert restaurant recommendation assistant.
Based on the user's preferences, select and rank the best options from the provided candidate list.
Provide a clear explanation for why each restaurant is recommended.

User Preferences:
- Location: {preferences.location}
- Budget: {preferences.budget}
- Cuisines: {', '.join(preferences.cuisines)}
- Minimum Rating: {preferences.min_rating}
- Additional Preferences: {', '.join(preferences.additional_preferences) if preferences.additional_preferences else 'None'}
- Max Results: {preferences.max_results}

Candidate Restaurants:
"""
    for i, candidate in enumerate(candidates):
        prompt += f"""
{i+1}. Name: {candidate.name}
   Location: {candidate.location}
   Cuisine: {candidate.cuisine}
   Rating: {candidate.rating}
   Cost: {candidate.cost}
   Additional Info: {candidate.metadata}
"""

    prompt += """
Respond strictly in JSON format matching the following schema. Do not include markdown formatting or extra text outside the JSON.
{
  "query_summary": "Summary of the user's request",
  "recommendations": [
    {
      "rank": 1,
      "restaurant_name": "...",
      "location": "...",
      "cuisine": "...",
      "rating": 4.5,
      "estimated_cost": "...",
      "explanation": "...",
      "match_tags": ["tag1", "tag2"]
    }
  ],
  "fallback_used": false,
  "warnings": []
}
"""
    return prompt
