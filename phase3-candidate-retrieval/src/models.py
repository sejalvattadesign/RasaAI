from dataclasses import dataclass, field
from typing import List, Optional


@dataclass(frozen=True)
class UserPreferences:
    location: str
    budget: str
    cuisines: List[str]
    min_rating: float
    additional_preferences: List[str] = field(default_factory=list)
    max_results: int = 5
    cost_min: Optional[float] = None
    cost_max: Optional[float] = None

