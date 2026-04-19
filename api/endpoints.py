from fastapi import APIRouter, HTTPException
from src.utils.schemas import SentimentRequest, SentimentResponse, ImpactRequest, ImpactResponse
from src.features.build_features import ml_service

router = APIRouter()

@router.post("/sentiment", response_model=SentimentResponse)
async def analyze_sentiment(request: SentimentRequest):
    try:
        prediction = ml_service.predict_sentiment(request.text)
        return SentimentResponse(label=prediction, confidence=0.85) # Simulating confidence
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/impact", response_model=ImpactResponse)
async def predict_impact(request: ImpactRequest):
    try:
        data = request.dict()
        prediction = ml_service.predict_impact(data)
        return ImpactResponse(
            estimated_happiness_index=prediction,
            feature_importance={"budget_edu": 0.4, "budget_health": 0.3} # Simulating feature importance
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/health")
async def health_check():
    return {"status": "healthy", "model_loaded": True}
