# Detailed Edge Cases: AI-Powered Restaurant Recommendation System

This document lists practical edge cases for each architecture phase, along with likely impact and expected handling behavior.

## Cross-Cutting Edge Cases (Apply to All Phases)

### 1) Empty or Highly Restricted Result Path
- **Scenario:** User applies strict filters (high rating + low budget + rare cuisine) and no restaurants match.
- **Impact:** Broken user journey if system returns a blank state.
- **Expected Handling:**
  - Return a graceful fallback response.
  - Suggest nearest alternatives (expand radius, lower rating threshold, similar cuisines).
  - Provide one-click "relax filters" actions.

### 2) Contradictory Preferences
- **Scenario:** Preferences conflict (e.g., "luxury fine dining" + "low budget").
- **Impact:** Irrelevant recommendations or LLM confusion.
- **Expected Handling:**
  - Detect contradictions in validation layer.
  - Ask user to prioritize constraints.
  - Continue with explicit priority order (must-have vs nice-to-have).

### 3) Non-Deterministic Output Between Identical Requests
- **Scenario:** Same input produces different ranking across runs.
- **Impact:** Inconsistent UX and lower trust.
- **Expected Handling:**
  - Keep deterministic pre-ranking.
  - Use fixed prompt templates and stable temperature settings.
  - Optionally cache responses for repeated identical queries.

### 4) Sudden Traffic Spike
- **Scenario:** High concurrent requests during peak hours.
- **Impact:** Latency spikes, timeout errors, failed LLM calls.
- **Expected Handling:**
  - Introduce queueing/rate limiting.
  - Fallback to deterministic ranking when LLM is unavailable.
  - Monitor and alert on p95 latency and error rate.

## Phase 1: Data Layer Setup (Ingestion, Cleaning, Storage)

### 1) Schema Drift in Source Dataset
- **Scenario:** Dataset columns are renamed or removed.
- **Impact:** Ingestion pipeline fails or maps wrong fields.
- **Expected Handling:**
  - Add schema validation before processing.
  - Fail fast with actionable error logs.
  - Maintain versioned field-mapping rules.

### 2) Missing Critical Fields
- **Scenario:** Missing location, rating, or cost values.
- **Impact:** Filtering and ranking degrade.
- **Expected Handling:**
  - Define per-field fallback rules (impute, default bucket, or exclude).
  - Track data completeness metrics.
  - Mark low-confidence records in metadata.

### 3) Inconsistent Categorical Values
- **Scenario:** Same cuisine appears as "North Indian", "north-indian", "N. Indian".
- **Impact:** Incorrect filtering and low recall.
- **Expected Handling:**
  - Normalize with canonical dictionaries.
  - Use fuzzy standardization with manual review thresholds.
  - Store raw and normalized values.

### 4) Duplicate Restaurants
- **Scenario:** Same restaurant appears multiple times with slight name/address differences.
- **Impact:** Duplicate recommendations.
- **Expected Handling:**
  - Deduplicate using composite keys (name + area + phone if available).
  - Keep best/latest record per entity.
  - Retain mapping for auditability.

### 5) Outlier or Invalid Numeric Values
- **Scenario:** Rating > 5, negative cost, impossible values.
- **Impact:** Distorted sorting and invalid user output.
- **Expected Handling:**
  - Apply hard range checks.
  - Quarantine anomalous rows.
  - Emit data-quality alerts.

### 6) Dataset Fetch Failure
- **Scenario:** Hugging Face endpoint unreachable or throttled.
- **Impact:** Startup/job failure.
- **Expected Handling:**
  - Retry with exponential backoff.
  - Use last successful local snapshot.
  - Surface health status to ops dashboard.

## Phase 2: User Interaction Layer (Input + Validation)

### 1) Ambiguous Location Input
- **Scenario:** User enters "MG Road" (exists in multiple cities).
- **Impact:** Wrong geography filtering.
- **Expected Handling:**
  - Prompt for city disambiguation.
  - Prefer user geolocation (if available and consented).
  - Confirm interpreted location before query.

### 2) Free-Text Slang or Misspellings
- **Scenario:** "chinees", "italan", "cheap but good".
- **Impact:** Low match rate.
- **Expected Handling:**
  - Add typo correction and synonym mapping.
  - Convert qualitative budget terms to standard ranges.
  - Return interpreted query summary to user.

### 3) Unsupported Cuisine or Novel Preference
- **Scenario:** User asks for a cuisine not present in dataset.
- **Impact:** Zero results, confusion.
- **Expected Handling:**
  - Inform user clearly that category is unavailable.
  - Suggest nearest cuisine clusters.
  - Allow mixed-cuisine fallback.

### 4) Invalid Numeric Input
- **Scenario:** Rating = 8, budget = text in numeric field.
- **Impact:** Validation errors and crashes if unchecked.
- **Expected Handling:**
  - Strict schema validation with friendly error messages.
  - Client-side and server-side checks.
  - Prevent API calls until corrected.

### 5) Empty Submission
- **Scenario:** User submits no meaningful preferences.
- **Impact:** Overbroad query.
- **Expected Handling:**
  - Ask for at least one required signal (location recommended).
  - Provide default discovery mode (popular nearby).

## Phase 3: Candidate Retrieval Layer (Filtering + Pre-Ranking)

### 1) Over-Filtering to Zero
- **Scenario:** Rule engine removes all candidates.
- **Impact:** No recommendations.
- **Expected Handling:**
  - Progressive relaxation (rating, budget, distance).
  - Explain which constraint caused elimination.

### 2) Under-Filtering (Huge Candidate Set)
- **Scenario:** Broad preferences return thousands of rows.
- **Impact:** Slow prompt creation and high LLM cost.
- **Expected Handling:**
  - Enforce Top-N cap before LLM.
  - Use deterministic pre-score to choose best N.
  - Paginate or chunk large candidate pools.

### 3) Bias Toward Popular Chains
- **Scenario:** Ranking consistently favors high-volume chains.
- **Impact:** Poor diversity and personalization.
- **Expected Handling:**
  - Add diversity constraints in pre-ranking.
  - Balance quality score with novelty/locality.

### 4) Cost Scale Mismatch
- **Scenario:** Dataset cost unit differs by city or record (for two vs per person).
- **Impact:** Wrong budget filtering.
- **Expected Handling:**
  - Standardize cost semantics in preprocessing.
  - Normalize budget buckets by city context.

### 5) Stale Candidate Metadata
- **Scenario:** Closed restaurants still appear.
- **Impact:** User dissatisfaction.
- **Expected Handling:**
  - Add freshness timestamp and stale-data flag.
  - Penalize low-freshness records in ranking.

## Phase 4: LLM Reasoning Layer (Prompting + Generation)

### 1) Hallucinated Facts
- **Scenario:** LLM invents amenities or prices not in data.
- **Impact:** Misinformation and trust loss.
- **Expected Handling:**
  - Restrict prompt to provided structured fields only.
  - Post-validate generated facts against source metadata.
  - Remove unsupported claims before display.

### 2) Prompt Injection via User Input
- **Scenario:** User enters malicious prompt text ("ignore instructions...").
- **Impact:** Policy bypass or unsafe output.
- **Expected Handling:**
  - Sanitize/escape user text in prompt template.
  - Use clear system constraints and output schema.
  - Block unsafe content patterns.

### 3) Token Limit Exceeded
- **Scenario:** Candidate list or prompt context too large.
- **Impact:** Truncation, API failure, or partial output.
- **Expected Handling:**
  - Strict token budgeting.
  - Summarize/compact candidate context.
  - Multi-pass ranking if needed.

### 4) LLM Timeout or API Failure
- **Scenario:** Provider outage or slow response.
- **Impact:** Broken recommendation request.
- **Expected Handling:**
  - Timeouts + retries with circuit breaker.
  - Fallback to rule-based recommendation response.
  - Return partial results if available.

### 5) Output Format Drift
- **Scenario:** LLM returns malformed JSON or missing required fields.
- **Impact:** Parser failures and UI breakage.
- **Expected Handling:**
  - Enforce schema with structured output parser.
  - Retry once with corrective prompt.
  - Gracefully degrade to plain-text rendering.

### 6) Overly Generic Explanations
- **Scenario:** Explanations are repetitive and not user-specific.
- **Impact:** Low perceived intelligence.
- **Expected Handling:**
  - Include explicit user-preference references in prompt rubric.
  - Penalize generic templates in evaluation.

## Phase 5: Response and Experience Layer (Rendering + UX)

### 1) Missing Display Fields
- **Scenario:** Candidate lacks cuisine or cost values.
- **Impact:** Incomplete recommendation cards.
- **Expected Handling:**
  - Show "Not available" placeholders.
  - Keep ranking explanation transparent about missing data.

### 2) Mismatch Between Rank and Explanation
- **Scenario:** Card ranked #1 but explanation mentions weaker fit.
- **Impact:** User confusion.
- **Expected Handling:**
  - Validate coherence between rank score and explanation text.
  - Display key match tags (budget, cuisine, rating) per card.

### 3) Very Long Explanations
- **Scenario:** LLM returns verbose paragraphs.
- **Impact:** Poor readability on mobile.
- **Expected Handling:**
  - Enforce response length limits.
  - Use expandable "read more" interaction.

### 4) Noisy Re-query Loop
- **Scenario:** Every slight filter change triggers full LLM call.
- **Impact:** High cost and sluggish UX.
- **Expected Handling:**
  - Debounce input changes.
  - Reuse cached candidate retrieval and only rerank when needed.

### 5) Localization/Language Mismatch
- **Scenario:** User prefers Hindi but output is English only.
- **Impact:** Reduced usability.
- **Expected Handling:**
  - Support preferred response language setting.
  - Keep entity fields (names/cuisines) untranslated where necessary.

## Phase 6: Feedback and Improvement Layer (Learning + Monitoring)

### 1) Feedback Sparsity
- **Scenario:** Few users provide explicit likes/dislikes.
- **Impact:** Weak learning signal.
- **Expected Handling:**
  - Use implicit signals (clicks, dwell time, re-query rate).
  - Aggregate trends before tuning logic.

### 2) Feedback Bias
- **Scenario:** Most feedback comes from one city/user segment.
- **Impact:** Model drifts toward skewed preferences.
- **Expected Handling:**
  - Stratify evaluation by city and segment.
  - Use weighted updates to reduce overfitting.

### 3) Metric Gaming
- **Scenario:** CTR improves but satisfaction drops (clickbait recommendations).
- **Impact:** Long-term trust decline.
- **Expected Handling:**
  - Track multi-metric health: CTR + repeat usage + satisfaction.
  - Block promotions that degrade long-term quality metrics.

### 4) Silent Failure in Observability
- **Scenario:** Logs missing for failed calls.
- **Impact:** Issues cannot be diagnosed.
- **Expected Handling:**
  - Instrument every phase with correlation IDs.
  - Monitor missing-log anomalies.

### 5) Privacy and Data Retention Risks
- **Scenario:** User preferences or behavior logs retained indefinitely.
- **Impact:** Compliance and trust risk.
- **Expected Handling:**
  - Apply data minimization and retention policies.
  - Pseudonymize user identifiers.
  - Provide deletion/export workflows where required.

## High-Priority Test Scenarios (Recommended First)

1. Zero-result query with graceful fallback and filter relaxation.
2. Contradictory preferences and prioritization prompt.
3. Schema drift and ingestion failure recovery from cached snapshot.
4. LLM timeout with deterministic fallback response.
5. Hallucination prevention by validating generated facts against source data.
6. Malformed LLM output recovery via parser + retry path.
7. Large candidate set capped with Top-N pre-ranking under token budget.
8. Duplicate restaurant suppression in final output.
9. Ambiguous location disambiguation flow.
10. Monitoring check for end-to-end latency and failure visibility.

