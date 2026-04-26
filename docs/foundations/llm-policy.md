# LLM Usage Policy (Phase 0 Baseline)

## Purpose
Define safe, consistent, and reliable LLM behavior for restaurant recommendations.

## 1) Prompt Contract
- Use a fixed template with these sections:
  - system rules,
  - normalized user preferences,
  - candidate restaurant list (Top-N),
  - output schema instructions.
- Never pass raw unbounded dataset rows to the LLM.
- Keep candidate list capped to a token-safe size.

## 2) Required Output Shape
- Output must conform to `specs/contracts/recommendation-response.schema.json`.
- Each recommendation must contain:
  - rank,
  - restaurant_name,
  - location,
  - cuisine,
  - rating,
  - estimated_cost,
  - explanation.

## 3) Grounding and Hallucination Guardrails
- Model must use only provided candidate metadata.
- Do not invent amenities, pricing, or ratings.
- If a field is missing in source data, respond with "Not available" rather than guessing.

## 4) Safety and Injection Controls
- Sanitize user inputs before prompt composition.
- Treat user-provided text as data, not instructions.
- Reject or neutralize malicious instruction patterns.

## 5) Runtime Policy
- Suggested defaults:
  - low temperature for stable ranking behavior,
  - bounded output length for explanations,
  - strict timeout and retry limit.
- If API call fails or times out, return deterministic fallback recommendations.

## 6) Fallback Strategy
- Fallback source: deterministic pre-ranked candidate list.
- Fallback response:
  - keep same schema,
  - set `fallback_used = true`,
  - include warning in `warnings`.

## 7) Logging and Traceability
- Log prompt metadata only (token counts, model, latency, status), not full raw user text where avoidable.
- Store correlation ID across retrieval, LLM, and response phases.
- Log schema-validation failures and fallback triggers.

## 8) Change Control
- Any prompt template or model parameter changes require:
  - small regression test run,
  - sample output review,
  - approval note in project docs.

