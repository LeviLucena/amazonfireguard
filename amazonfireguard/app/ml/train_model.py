import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import joblib

def train_model():
    df = pd.read_csv("data/fire_data.csv")
    X = df[["temperature", "humidity", "wind_speed"]]
    y = df["fire_occurred"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

    model = RandomForestClassifier()
    model.fit(X_train, y_train)

    joblib.dump(model, "app/ml/fire_risk_model.pkl")
    print("Modelo treinado e salvo.")

if __name__ == "__main__":
    train_model()
