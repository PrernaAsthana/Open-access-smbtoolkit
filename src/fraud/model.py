"""Fraud anomaly model (Isolation Forest baseline)."""
from __future__ import annotations
import pandas as pd
from sklearn.ensemble import IsolationForest

def train_isolation_forest(X: pd.DataFrame, contamination: float = 0.02, random_state: int = 42) -> IsolationForest:
    model = IsolationForest(
        n_estimators=100,
        max_samples=256,
        contamination=contamination,
        random_state=random_state,
        n_jobs=-1,
    )
    model.fit(X)
    return model

def score(model: IsolationForest, X: pd.DataFrame) -> pd.Series:
    # decision_function: higher is more normal; we invert to produce anomaly_score
    return pd.Series(-model.decision_function(X), index=X.index, name="anomaly_score")
