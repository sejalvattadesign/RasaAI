# Non-Functional Baseline (Phase 0)

## Objective
Set measurable reliability and performance targets for the MVP.

## 1) Performance Targets
- **End-to-end response time (p95):** <= 4.0s
- **Candidate retrieval time (p95):** <= 500ms
- **LLM call time (p95):** <= 3.0s
- **Cold start (if applicable):** <= 8.0s

## 2) Availability and Reliability
- **Target uptime (MVP):** 99.0%
- **Request success rate:** >= 98.5%
- **LLM timeout/error fallback success:** >= 99% of failed LLM attempts

## 3) Error Handling Baseline
- Standardize error types:
  - validation_error,
  - retrieval_error,
  - llm_error,
  - response_format_error.
- Ensure user-facing messages are clear and actionable.
- Avoid exposing raw stack traces in user responses.

## 4) Observability Minimum
- Collect logs for:
  - request ID / correlation ID,
  - phase durations,
  - candidate count before/after filtering,
  - model name, token usage, and fallback flags.
- Track baseline metrics:
  - p50/p95 latency,
  - error rate by phase,
  - zero-result rate,
  - fallback frequency.

## 5) Cost Guardrails
- Cap candidate count sent to LLM (Top-N).
- Set request-level token budget.
- Monitor token usage per request and daily total.

## 6) Data Quality Baseline
- Enforce mandatory fields for ranking (name, location, cuisine, rating/cost where available).
- Track missing-field ratio.
- Reject or quarantine invalid numeric outliers.

## 7) Security and Privacy Baseline
- Do not log sensitive raw payloads unnecessarily.
- Pseudonymize user identifiers in telemetry.
- Define retention window for interaction logs (for example, 30-90 days).

## 8) Exit Criteria for Phase 0
- Targets are documented and accepted.
- Monitoring events and metric names are finalized.
- Error taxonomy is implemented in API contract and service design.

