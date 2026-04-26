# Problem Statement: AI-Powered Restaurant Recommendation System (Zomato-Inspired)

## Overview
Build an AI-powered restaurant recommendation service inspired by Zomato. The system should combine structured restaurant data with a Large Language Model (LLM) to deliver personalized, context-aware recommendations.

## Objective
Design and implement an application that:
- accepts user preferences (location, budget, cuisine, and rating),
- uses a real-world restaurant dataset,
- applies an LLM to generate ranked recommendations with clear reasoning, and
- presents the results in a clean, user-friendly format.

## Scope and Workflow

### 1) Data Ingestion and Preparation
- Load the Zomato dataset from Hugging Face:  
  <https://huggingface.co/datasets/ManikaSaini/zomato-restaurant-recommendation>
- Preprocess and standardize key fields such as:
  - restaurant name,
  - location,
  - cuisines,
  - average cost, and
  - user rating.
- Handle missing values and inconsistent formatting to ensure reliable filtering.

### 2) User Preference Collection
Capture user inputs through a basic web UI form, including:
- **Location** (e.g., Delhi, Bangalore),
- **Budget** (low, medium, high),
- **Cuisine** (e.g., Italian, Chinese),
- **Minimum rating**, and
- **Optional preferences** (e.g., family-friendly, quick service).

### 3) Integration Layer
- Filter the dataset using user constraints.
- Convert filtered records into structured context for prompting.
- Construct a prompt that enables the LLM to evaluate, compare, and rank options effectively.

### 4) Recommendation Engine (LLM)
Use the LLM to:
- rank the most relevant restaurants,
- explain why each option matches the user’s preferences, and
- optionally provide a short summary or comparison of top choices.

### 5) Output and Presentation
Display top recommendations with:
- Restaurant name,
- Cuisine,
- Rating,
- Estimated cost, and
- AI-generated explanation.

## Phase-Wise Architecture

### Phase 1: Data Layer Setup
**Goal:** Build a reliable and query-ready restaurant data foundation.

**Components:**
- Dataset loader (Hugging Face ingestion)
- Data cleaning and normalization module
- Storage layer (CSV/SQLite/PostgreSQL)

**Input:** Raw Zomato dataset  
**Output:** Cleaned and indexed restaurant dataset

---

### Phase 2: User Interaction Layer
**Goal:** Capture user preferences in a structured format.

**Components:**
- Basic web UI form (primary input source)
- Input validation service
- Preference schema mapper

**Input:** User criteria (location, budget, cuisine, rating, optional needs)  
**Output:** Validated preference object (JSON)

---

### Phase 3: Candidate Retrieval Layer
**Goal:** Reduce search space to relevant candidates before LLM reasoning.

**Components:**
- Rule-based filter engine
- Ranking pre-processor (basic scoring by match quality)
- Optional geospatial and cost-range filters

**Input:** Validated preferences + cleaned dataset  
**Output:** Top-N candidate restaurants with structured metadata

---

### Phase 4: LLM Reasoning Layer
**Goal:** Generate personalized recommendations and explanations.

**Components:**
- Prompt builder (context + user preferences + candidate list)
- LLM API integration
- Output parser and guardrails (format checks, hallucination control)

**Input:** Candidate list and user profile  
**Output:** Ranked recommendations with natural-language rationale

---

### Phase 5: Response and Experience Layer
**Goal:** Present results clearly and help users make decisions quickly.

**Components:**
- Recommendation response formatter
- UI cards/list view for top restaurants
- Optional re-query controls (refine budget/cuisine/location)

**Input:** LLM output + restaurant metadata  
**Output:** User-facing recommendation list with explanations

---

### Phase 6: Feedback and Improvement Layer
**Goal:** Continuously improve relevance and quality.

**Components:**
- Feedback capture (likes, skips, selected restaurant)
- Monitoring and logging (latency, token usage, failures)
- Evaluation pipeline (precision@k, user satisfaction, CTR)

**Input:** User behavior and system performance data  
**Output:** Insights for prompt tuning, ranking logic updates, and model improvements

## End-to-End Flow (High Level)
1. Ingest and clean restaurant data.
2. Collect and validate user preferences.
3. Retrieve top candidate restaurants using deterministic filters.
4. Ask the LLM to rank and explain best-fit options.
5. Show recommendations in a clear UI.
6. Capture feedback to improve future recommendations.

## Expected Outcome
The final system should help users discover restaurants faster by combining factual filtering with natural-language recommendations that are personalized, transparent, and easy to understand.

