import sys
import os
import importlib
import pandas as pd

# Add the project root to sys.path so we can import from other phases
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../"))
if project_root not in sys.path:
    sys.path.append(project_root)

# Try importing the pipeline from phase 4
try:
    phase4_pipeline = importlib.import_module("phase4-llm-reasoning.src.pipeline")
    has_phase4 = True
except Exception as e:
    print(f"Error loading Phase 4: {e}")
    has_phase4 = False

def get_real_candidates(preferences_dict: dict) -> list:
    """Reads the processed CSV and filters candidates based on preferences."""
    csv_path = os.path.join(project_root, "data", "processed", "zomato_cleaned.csv")
    if not os.path.exists(csv_path):
        return []

    try:
        df = pd.read_csv(csv_path)
        
        # Parse rate "4.1/5" to float 4.1
        def parse_rate(val):
            try:
                return float(str(val).split('/')[0].strip())
            except:
                return 0.0
        df['parsed_rate'] = df['rate'].apply(parse_rate)

        # Initial filters
        location = preferences_dict.get("location", "").lower().strip()
        min_rating = preferences_dict.get("min_rating", 0.0)
        cuisines = preferences_dict.get("cuisines", [])
        
        # Helper to apply filters
        def apply_filters(df_in, loc, rating, cuises):
            temp_df = df_in.copy()
            if loc:
                temp_df = temp_df[temp_df['location'].str.lower().str.contains(loc, na=False)]
            if rating > 0:
                temp_df = temp_df[temp_df['parsed_rate'] >= rating]
            if cuises and "Any" not in cuises:
                cuisine_mask = pd.Series(False, index=temp_df.index)
                for c in cuises:
                    cuisine_mask |= temp_df['cuisine'].str.contains(c, case=False, na=False)
                temp_df = temp_df[cuisine_mask]
            return temp_df

        # Tier 1: Strict match
        df_filtered = apply_filters(df, location, min_rating, cuisines)
        
        # Tier 2: Drop cuisine filter if less than 5 candidates
        if len(df_filtered) < 5:
            df_filtered = apply_filters(df, location, min_rating, [])
            
        # Tier 3: Drop rating filter as well
        if len(df_filtered) < 5:
            df_filtered = apply_filters(df, location, 0.0, [])

        # 4. Sort by votes to get the most popular ones
        if 'votes' in df_filtered.columns:
            df_filtered['votes'] = pd.to_numeric(df_filtered['votes'], errors='coerce').fillna(0)
            df_filtered = df_filtered.sort_values(by='votes', ascending=False)

        top_candidates = df_filtered.head(10)
        
        candidates = []
        for _, row in top_candidates.iterrows():
            loc = str(row.get('location', 'Unknown'))
            if loc == 'nan' or not loc: loc = 'Unknown'
            
            name = str(row.get('restaurant_name', 'Unknown'))
            if name == 'nan' or not name: name = 'Unknown'
            
            cuisine = str(row.get('cuisine', 'Unknown'))
            if cuisine == 'nan' or not cuisine: cuisine = 'Unknown'
            
            candidates.append({
                "id": str(row.name),
                "name": name,
                "location": loc,
                "cuisine": cuisine,
                "rating": float(row.get('parsed_rate', 0.0)),
                "cost": str(row.get('average_cost', '0')),
                "metadata": {"votes": int(row.get('votes', 0)), "rest_type": str(row.get('rest_type', ''))}
            })
        return candidates

    except Exception as e:
        print(f"Error reading candidates: {e}")
        return []

def run_orchestration(preferences_dict: dict) -> dict:
    """
    Orchestrates the flow from preferences -> retrieval -> LLM.
    Reads candidates from CSV and calls Phase 4 LLM pipeline.
    """
    candidates = get_real_candidates(preferences_dict)
    
    if not candidates:
        return {
            "query_summary": f"Looking for restaurants in {preferences_dict.get('location', 'Unknown')}.",
            "recommendations": [],
            "fallback_used": False,
            "warnings": ["No matching restaurants found in this location, even after relaxing filters."]
        }

    if has_phase4:
        return phase4_pipeline.run_phase4(preferences_dict, candidates)
    else:
        # Mock LLM Response if Phase 4 is unreachable
        return {
            "query_summary": f"Looking for restaurants in {preferences_dict.get('location', 'Unknown')}.",
            "recommendations": [
                {
                    "rank": 1,
                    "restaurant_name": candidates[0]["name"],
                    "location": candidates[0]["location"],
                    "cuisine": candidates[0]["cuisine"],
                    "rating": candidates[0]["rating"],
                    "estimated_cost": str(candidates[0]["cost"]),
                    "explanation": "This is a great place generated by mock orchestrator.",
                    "match_tags": ["mock"]
                }
            ],
            "fallback_used": True,
            "warnings": ["Phase 4 not found. Using mock orchestration."]
        }
