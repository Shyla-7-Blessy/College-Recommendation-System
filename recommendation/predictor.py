import joblib
import pandas as pd

from pathlib import Path
import joblib

BASE_DIR = Path(__file__).resolve().parent.parent

MODEL_PATH = BASE_DIR / "models" / "random_forest.pkl"

model = joblib.load(MODEL_PATH)

def rank_colleges(colleges):

    df = pd.DataFrame(colleges)
    
    print("Columns received:")
    print(df.columns.tolist())
    
    tier_mapping = {
    "Tier 1": 1,
    "Tier 2": 2,
    "Tier 3": 3
}
    df["cutoff"] = df["min_cutoff"]
    df["college_tier"] = df["college_tier"].map(tier_mapping)

    features = df[
        [
            "cutoff",
            "college_tier",
            "nirf_rank",
            "annual_fees"
        ]
    ]
    print(model.predict_proba(features))
    df["score"] = model.predict_proba(features)[:, 1]

    ranked = df.sort_values(
        by="score",
        ascending=False
    )

    return ranked.head(5)