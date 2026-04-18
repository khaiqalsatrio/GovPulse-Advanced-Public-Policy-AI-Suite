import joblib
import os
from app.core.config import SENTIMENT_MODEL_PATH
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import TfidfVectorizer

class SentimentClassifier:
    def __init__(self):
        # Setup pipeline
        self.model = Pipeline([
            ('tfidf', TfidfVectorizer()),
            ('clf', LogisticRegression())
        ])
        
        # Load from disk if available, otherwise bootstrap
        if os.path.exists(SENTIMENT_MODEL_PATH):
            try:
                self.model = joblib.load(SENTIMENT_MODEL_PATH)
                print(f"Loaded sentiment model from {SENTIMENT_MODEL_PATH}")
            except Exception as e:
                print(f"Error loading model: {e}, bootstrapping instead.")
                self._bootstrap()
        else:
            self._bootstrap()

    def _bootstrap(self):
        print("Bootstrapping sentiment model with initial data...")
        texts = ["bagus", "buruk", "mantap", "kecewa", "oke", "parah"]
        labels = [1, 0, 1, 0, 1, 0]
        self.model.fit(texts, labels)
        self.save()

    def save(self):
        joblib.dump(self.model, SENTIMENT_MODEL_PATH)
        print(f"Model saved to {SENTIMENT_MODEL_PATH}")

    def predict(self, text: str) -> int:
        return self.model.predict([text])[0]
