# Phase-Wise Architecture: AI-Powered Restaurant Recommendation System

## Phase 0: Scope and Foundations
**Goal:** Establish project boundaries, delivery priorities, and baseline technical decisions before implementation starts.

**Scope Decisions:**
- Focus on core recommendation quality over feature breadth.
- Keep UI minimal and web-based (simple web form input + basic recommendations list).
- Prioritize backend reliability, data quality, and explainable recommendations.
- Defer advanced UI features (maps, rich personalization dashboards, animations) to later iterations.

**Foundation Components:**
- Requirement baseline (must-have vs nice-to-have features)
- Data contract definition (input and output schemas)
- LLM usage policy (prompt format, guardrails, fallback strategy)
- Non-functional baseline (latency target, error handling, logging, and basic monitoring)

**Input:** Problem statement, architecture goals, and constraints  
**Output:** Approved implementation baseline, MVP scope, and phase execution plan

**Implementation Artifacts:**
- `docs/foundations/phase0-scope-and-foundations.md`
- `docs/foundations/llm-policy.md`
- `docs/foundations/non-functional-baseline.md`
- `specs/contracts/user-preferences.schema.json`
- `specs/contracts/recommendation-response.schema.json`

## Phase 1: Data Layer Setup
**Goal:** Build a reliable and query-ready restaurant data foundation.

**Components:**
- Dataset loader (Hugging Face ingestion)
- Data cleaning and normalization module
- Storage layer (CSV/SQLite/PostgreSQL)

**Input:** Raw Zomato dataset  
**Output:** Cleaned and indexed restaurant dataset

## Phase 2: User Interaction Layer
**Goal:** Capture user preferences in a structured format.

**Components:**
- Basic web UI form (primary and only input channel for MVP)
- Input validation service
- Preference schema mapper

**Input:** User criteria (location, budget, cuisine, rating, optional needs)  
**Output:** Validated preference object (JSON)

## Phase 3: Candidate Retrieval Layer
**Goal:** Reduce search space to relevant candidates before LLM reasoning.

**Components:**
- Rule-based filter engine
- Ranking pre-processor (basic scoring by match quality)
- Optional geospatial and cost-range filters

**Input:** Validated preferences + cleaned dataset  
**Output:** Top-N candidate restaurants with structured metadata

## Phase 4: LLM Reasoning Layer
**Goal:** Generate personalized recommendations and explanations.

**Components:**
- Prompt builder (context + user preferences + candidate list)
- LLM API integration
- Output parser and guardrails (format checks, hallucination control)

**Input:** Candidate list and user profile  
**Output:** Ranked recommendations with natural-language rationale

## Phase 5: Backend API & Integration Layer
**Goal:** Create a robust, scalable backend to serve frontend requests, orchestrate previous phases, and persist user data.

**Components:**
- RESTful or GraphQL API (e.g., FastAPI)
- Pipeline orchestrator (chaining Phase 2 -> Phase 3 -> Phase 4)
- User profile & history database
- Authentication & Rate Limiting

**Input:** API requests from Frontend  
**Output:** Standardized JSON responses for recommendations and user state

## Phase 6: Frontend Experience Layer
**Goal:** Deliver a premium, highly responsive user interface with modern web technologies.

**Components:**
- Single Page Application (e.g., React, Next.js, or Vite)
- Rich aesthetics, animations, and responsive design (TailwindCSS/CSS Modules)
- Interactive recommendation cards and maps
- State management (e.g., Redux, Context API)

**Input:** User interactions  
**Output:** Engaging web-based recommendation experience

## Phase 7: Feedback, Monitoring & DevOps
**Goal:** Ensure system reliability, continuous improvement, and easy deployment.

**Components:**
- Feedback capture (likes, skips, saved restaurants)
- System monitoring, logging, and LLM telemetry (token usage, latency)
- Dockerization and CI/CD pipelines

**Input:** User behavior and backend metrics  
**Output:** Automated deployments and actionable insights for model improvements

## End-to-End Architecture Flow (Full Stack)
1. **Frontend:** User interacts with the UI to input preferences.
2. **Backend API:** Receives preferences and validates them (Phase 2).
3. **Data Layer & Retrieval:** Backend queries the local database/search index for candidates (Phase 1 & 3).
4. **LLM Engine:** Backend sends candidates and context to the LLM (Groq) for ranking and explanations (Phase 4).
5. **Frontend:** Receives the curated response and renders dynamic UI cards (Phase 6).
6. **Telemetry:** Feedback and performance logs are captured continuously (Phase 7).

