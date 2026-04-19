import joblib
import os
import numpy as np
from src.utils.helper import IMPACT_MODEL_PATH
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import StandardScaler

class ImpactEngine:
    def __init__(self):
        self.model = Pipeline([
            ('scaler', StandardScaler()),
            ('regressor', RandomForestRegressor(n_estimators=10))
        ])
        
        # Load from disk if available, otherwise bootstrap
        if os.path.exists(IMPACT_MODEL_PATH):
            try:
                self.model = joblib.load(IMPACT_MODEL_PATH)
                print(f"Loaded impact model from {IMPACT_MODEL_PATH}")
            except Exception as e:
                print(f"Error loading model: {e}, bootstrapping instead.")
                self._bootstrap()
        else:
            self._bootstrap()

    def _bootstrap(self):
        print("Bootstrapping impact model with initial data...")
        # 5 features: edu, health, infra, digital, unemployment
        X = np.random.rand(50, 5)
        y = np.random.rand(50)
        self.model.fit(X, y)
        self.save()

    def save(self):
        joblib.dump(self.model, IMPACT_MODEL_PATH)
        print(f"Model saved to {IMPACT_MODEL_PATH}")

    def predict(self, features: list) -> float:
        X_test = np.array([features])
        return float(self.model.predict(X_test)[0])
