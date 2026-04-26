import os
import json
from typing import List
from groq import Groq
from pydantic import ValidationError
from .models import UserPreferences, CandidateRestaurant, RecommendationResponse
from .prompt_builder import build_prompt

class LLMReasoningEngine:
    def __init__(self, api_key: str = None, model_name: str = "llama-3.1-8b-instant"):
        self.api_key = api_key or os.environ.get("GROQ_API_KEY")
        if not self.api_key:
            raise ValueError("GROQ_API_KEY is not set.")
        self.client = Groq(api_key=self.api_key)
        self.model_name = model_name

    def generate_recommendations(
        self, preferences: UserPreferences, candidates: List[CandidateRestaurant]
    ) -> RecommendationResponse:
        prompt = build_prompt(preferences, candidates)
        
        try:
            chat_completion = self.client.chat.completions.create(
                messages=[
                    {"role": "system", "content": "You are a helpful assistant that outputs only valid JSON. Do not include any markdown blocks."},
                    {"role": "user", "content": prompt}
                ],
                model=self.model_name,
                response_format={"type": "json_object"},
                temperature=0.3,
            )
            
            result_text = chat_completion.choices[0].message.content
            result_json = json.loads(result_text)
            
            return RecommendationResponse(**result_json)
            
        except Exception as e:
            # Let the caller handle the exception
            print(f"Error during generation: {e}")
            raise e
