import os
from dotenv import load_dotenv
env_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../..", ".venv-root", ".env"))
load_dotenv(env_path)

from fastapi import FastAPI, Depends, Request, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded

from .database import engine, Base, SessionLocal
from . import models, schemas
from .orchestrator import run_orchestration

# Create DB tables
Base.metadata.create_all(bind=engine)

# Setup Rate Limiting
limiter = Limiter(key_func=get_remote_address)
app = FastAPI(title="Zomato Recommendation API - Phase 5")
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

# CORS config
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def read_root():
    return {"message": "Welcome to the Phase 5 Zomato Recommendation Backend"}

@app.post("/api/recommend", response_model=schemas.APIResponse)
@limiter.limit("5/minute")
def get_recommendations(request: Request, prefs: schemas.PreferencesInput, db: Session = Depends(get_db)):
    user_id = request.client.host # Simple user tracking
    
    try:
        # 1. Orchestrate the pipeline
        result = run_orchestration(prefs.model_dump())
        
        # 2. Convert raw dictionary result to API output model (ensure ints are converted to str for cost)
        for rec in result.get("recommendations", []):
            rec["estimated_cost"] = str(rec.get("estimated_cost", ""))
            
        # 3. Save to History DB
        history_entry = models.RecommendationHistory(
            user_id=user_id,
            preferences=prefs.model_dump(),
            recommendations=result.get("recommendations", [])
        )
        db.add(history_entry)
        db.commit()
        db.refresh(history_entry)
        
        return schemas.APIResponse(
            query_summary=result.get("query_summary", "Summary"),
            recommendations=result.get("recommendations", []),
            history_id=history_entry.id
        )
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/history")
def get_history(request: Request, db: Session = Depends(get_db)):
    user_id = request.client.host
    history = db.query(models.RecommendationHistory).filter(models.RecommendationHistory.user_id == user_id).all()
    return {"history": history}
