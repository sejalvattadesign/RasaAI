from typing import List, Optional
from pydantic import BaseModel, Field

class PreferencesInput(BaseModel):
    location: str = Field(..., min_length=2, max_length=100)
    budget: str = Field(..., description="low, medium, or high")
    cuisines: List[str] = Field(..., min_length=1, max_length=5)
    min_rating: float = Field(..., ge=0, le=5)
    additional_preferences: List[str] = Field(default_factory=list, max_length=10)

class RecommendationOutput(BaseModel):
    rank: int
    restaurant_name: str
    location: str
    cuisine: str
    rating: float
    estimated_cost: str
    explanation: str
    match_tags: List[str]

class APIResponse(BaseModel):
    query_summary: str
    recommendations: List[RecommendationOutput]
    history_id: Optional[int] = None
