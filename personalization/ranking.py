"""Simple personalization baselines (demo)."""
from __future__ import annotations
import pandas as pd
from sklearn.ensemble import GradientBoostingClassifier

def train_gbdt_ranker(X: pd.DataFrame, y: pd.Series) -> GradientBoostingClassifier:
    model = GradientBoostingClassifier(
        learning_rate=0.01,
        max_depth=4,
        n_estimators=200,
        random_state=42
    )
    model.fit(X, y)
    return model

def rank_candidates(model: GradientBoostingClassifier, X_candidates: pd.DataFrame, item_ids: pd.Series) -> pd.DataFrame:
    scores = model.predict_proba(X_candidates)[:, 1]
    out = pd.DataFrame({"item_id": item_ids.values, "score": scores})
    return out.sort_values("score", ascending=False).reset_index(drop=True)
