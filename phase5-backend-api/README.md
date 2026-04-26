# Phase 5: Backend API & Integration Layer

This is the FastAPI backend application for the Zomato Restaurant Recommendation system. It orchestrates the flow by handling API requests, communicating with the LLM reasoning layer, and storing user interactions in a SQLite database.

## Setup

1. Navigate to this directory and create a virtual environment:
   ```bash
   cd phase5-backend-api
   python3 -m venv .venv
   source .venv/bin/activate
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Ensure the `GROQ_API_KEY` is set in your environment (it will be needed when it orchestrates Phase 4):
   ```bash
   export GROQ_API_KEY="your-api-key"
   ```

## Running the Server

Run the development server using `uvicorn`:
```bash
uvicorn src.main:app --reload --host 0.0.0.0 --port 8000
```

## API Endpoints

- `GET /`: Health check endpoint.
- `POST /api/recommend`: Accepts a JSON payload matching the `PreferencesInput` schema. It orchestrates the retrieval of candidates and calls the LLM, then stores the result in the database.
  - *Note: This endpoint is rate-limited to 5 requests per minute per IP.*
- `GET /api/history`: Returns your past recommendation history based on your IP.

You can also view the interactive Swagger documentation by visiting: `http://localhost:8000/docs`.
