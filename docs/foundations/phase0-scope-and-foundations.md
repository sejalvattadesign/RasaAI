# Phase 0 Implementation: Scope and Foundations

This document is the executable baseline for Phase 0.

## 1) MVP Scope (Must-Have)
- Ingest and clean the Zomato dataset.
- Accept user preferences: location, budget, cuisine, minimum rating, optional notes.
- Retrieve candidate restaurants using deterministic filters.
- Use an LLM to rank candidates and provide short explanations.
- Use a basic web UI as the source of user input.
- Show results in a minimal web UI (single input form + simple recommendation list).
- Add basic logging, error handling, and fallback when LLM is unavailable.

## 2) Deferred Scope (Not in MVP)
- Maps, map pins, route views, and distance visuals.
- Rich dashboards and advanced personalization panels.
- Real-time recommendations or live restaurant availability.
- Multi-provider model orchestration and A/B experimentation UI.
- Native mobile apps.

## 3) Minimal UI Definition
- One screen/page with:
  - web form-based user preference input controls,
  - submit action,
  - recommendation cards/list.
- The web form is the only input channel in MVP (no chat interface).
- No advanced client state management required for MVP.
- Prioritize clarity and response speed over UI polish.

## 4) System Boundaries
- **In scope:** preference-to-recommendation flow, data quality checks, explainable ranking, service observability.
- **Out of scope:** restaurant booking/payment, delivery tracking, social features (reviews/comments), identity and auth complexity.

## 5) Delivery Gates for Exiting Phase 0
- Requirements baseline approved.
- Contracts approved (`specs/contracts/*.schema.json`).
- LLM policy approved (`docs/foundations/llm-policy.md`).
- Non-functional baseline approved (`docs/foundations/non-functional-baseline.md`).
- Backlog created with Phase 1 tasks.

## 6) Execution Plan (Next Phases)
1. Phase 1: Build data ingestion and normalization pipeline.
2. Phase 2: Build input collection and validation flow.
3. Phase 3: Implement deterministic candidate retrieval and pre-ranking.
4. Phase 4: Integrate LLM ranking and guardrails.
5. Phase 5: Render responses in minimal UI and add retry/refine loop.
6. Phase 6: Collect feedback and track quality metrics.

