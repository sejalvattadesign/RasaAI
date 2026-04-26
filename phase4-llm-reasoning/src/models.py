from typing import List, Optional, Any
from pydantic import BaseModel, Field

class UserPreferences(BaseModel):
    location: str = Field(..., min_length=2, max_length=100)
    budget: str = Field(..., description="low, medium, or high")
    cuisines: List[str] = Field(..., min_length=1, max_length=5)
    min_rating: float = Field(..., ge=0, le=5)
    additional_preferences: List[str] = Field(default_factory=list, max_length=10)
    max_results: int = Field(default=5, ge=1, le=20)

class CandidateRestaurant(BaseModel):
    id: str
    name: str
    location: str
    cuisine: str
    rating: float
    cost: str
    metadata: dict = Field(default_factory=dict)

class Recommendation(BaseModel):
    rank: int = Field(..., ge=1)
    restaurant_name: str = Field(..., min_length=1, max_length=200)
    location: str = Field(..., min_length=0, max_length=120)
    cuisine: str = Field(..., min_length=0, max_length=120)
    rating: float = Field(..., ge=0, le=5)
    estimated_cost: Any
    explanation: str = Field(..., min_length=0, max_length=500)
    match_tags: List[str] = Field(default_factory=list, max_length=6)

class RecommendationResponse(BaseModel):
    query_summary: str = Field(..., min_length=1, max_length=300)
    recommendations: List[Recommendation] = Field(default_factory=list, max_length=20)
    fallback_used: bool = False
    warnings: List[str] = Field(default_factory=list)
