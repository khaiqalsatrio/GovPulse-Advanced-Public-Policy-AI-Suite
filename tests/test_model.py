import pytest
from src.features.build_features import ml_service

def test_sentiment_prediction():
    text = "Kebijakan ini sangat membantu rakyat kecil"
    prediction = ml_service.predict_sentiment(text)
    assert prediction in ["Positif/Setuju", "Negatif/Tidak Setuju", "Netral"]

def test_impact_prediction():
    data = {
        "budget_edu_pct": 20.0,
        "budget_health_pct": 15.0,
        "infrastructure_score": 7.5,
        "digital_access_pct": 60.0,
        "unemployment_rate": 5.0
    }
    prediction = ml_service.predict_impact(data)
    assert isinstance(prediction, float)
    assert 0 <= prediction <= 1.0
