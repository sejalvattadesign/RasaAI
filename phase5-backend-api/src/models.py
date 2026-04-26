from sqlalchemy import Column, Integer, String, JSON
from .database import Base

class RecommendationHistory(Base):
    __tablename__ = "recommendation_history"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(String, index=True)
    preferences = Column(JSON)
    recommendations = Column(JSON)
