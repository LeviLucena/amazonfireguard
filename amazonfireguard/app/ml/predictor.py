import pandas as pd
import joblib

def predict(df):
    model = joblib.load("app/ml/fire_risk_model.pkl")
    predictions = model.predict(df)
    return predictions
