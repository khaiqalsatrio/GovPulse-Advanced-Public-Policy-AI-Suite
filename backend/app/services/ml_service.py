from app.ml.sentiment.processor import clean_text
from app.ml.sentiment.classifier import SentimentClassifier
from app.ml.predictor.engine import ImpactEngine

class MLService:
    def __init__(self):
        # Initialize specialized ML components
        self.sentiment_model = SentimentClassifier()
        self.impact_model = ImpactEngine()

    def predict_sentiment(self, text: str):
        # 1. Preprocessing
        cleaned = clean_text(text)
        # 2. Prediction
        pred = self.sentiment_model.predict(cleaned)
        
        mapping = {1: "Positif/Setuju", 0: "Negatif/Tidak Setuju"}
        return mapping.get(pred, "Netral")

    def predict_impact(self, data: dict):
        features = [
            data['budget_edu_pct'], 
            data['budget_health_pct'], 
            data['infrastructure_score'], 
            data['digital_access_pct'], 
            data['unemployment_rate']
        ]
        prediction = self.impact_model.predict(features)
        return prediction

# Global Instance for the app
ml_service = MLService()
