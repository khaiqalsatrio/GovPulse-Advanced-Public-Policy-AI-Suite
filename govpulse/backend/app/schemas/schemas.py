from pydantic import BaseModel
from typing import List, Optional

class SentimentRequest(BaseModel):
    text: str

class SentimentResponse(BaseModel):
    label: str
    confidence: float

class ImpactRequest(BaseModel):
    budget_edu_pct: float
    budget_health_pct: float
    infrastructure_score: float
    digital_access_pct: float
    unemployment_rate: float

class ImpactResponse(BaseModel):
    estimated_happiness_index: float
    feature_importance: Optional[dict] = None
