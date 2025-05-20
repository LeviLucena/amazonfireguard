import os

MODEL_PATH = "app/ml/fire_risk_model.pkl"

def model_exists():
    return os.path.isfile(MODEL_PATH)
