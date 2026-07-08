import pandas as pd
import joblib
import os

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split


df = pd.read_csv("D:\shyla\college-recommendation\dataset\synthetic_college_training_data.csv")

X = df[
    [
        "cutoff",
        "college_tier",
        "nirf_rank",
        "annual_fees",
        
    ]
]

y = df["user_selected"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

model = RandomForestClassifier(
    n_estimators=200,
    random_state=42
)

model.fit(X_train, y_train)

os.makedirs("models", exist_ok=True)

joblib.dump(
    model,
    "models/random_forest.pkl"
)

print("Model Saved")
