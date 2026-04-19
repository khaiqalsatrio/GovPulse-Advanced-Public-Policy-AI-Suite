import os

# Base directory
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Model paths
MODELS_DIR = os.path.join(os.path.dirname(BASE_DIR), "models")

# Ensure directory exists
if not os.path.exists(MODELS_DIR):
    os.makedirs(MODELS_DIR)

SENTIMENT_MODEL_PATH = os.path.join(MODELS_DIR, "sentiment_model.joblib")
IMPACT_MODEL_PATH = os.path.join(MODELS_DIR, "impact_model.joblib")
