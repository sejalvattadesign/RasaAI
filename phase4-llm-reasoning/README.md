# Phase 4: LLM Reasoning Layer

This phase integrates with the Groq API to provide personalized restaurant recommendations based on the user's preferences and a candidate list generated from Phase 3.

## Setup

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Set the `GROQ_API_KEY` environment variable:
   ```bash
   export GROQ_API_KEY="your-groq-api-key"
   ```

## Usage

```python
from src.pipeline import run_phase4

preferences = {
    "location": "New York",
    "budget": "medium",
    "cuisines": ["Italian", "Pizza"],
    "min_rating": 4.0
}

candidates = [
    {
        "id": "1",
        "name": "Joe's Pizza",
        "location": "New York",
        "cuisine": "Pizza",
        "rating": 4.5,
        "cost": "$$"
    }
]

response = run_phase4(preferences, candidates)
print(response)
```
