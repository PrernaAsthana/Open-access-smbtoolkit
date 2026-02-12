"""Fraud feature computation (synthetic/demo).
Implements rolling-window velocity, entropy, and deviation scores.
"""
from __future__ import annotations
import numpy as np
import pandas as pd

def compute_velocity_features(df: pd.DataFrame, time_col: str = "timestamp", group_col: str = "user_hash") -> pd.DataFrame:
    """Compute basic velocity features over multiple rolling windows per user_hash.
    Assumes df is sorted by timestamp within each group.
    """
    out = df.copy()
    out[time_col] = pd.to_datetime(out[time_col], utc=True)
    out = out.sort_values([group_col, time_col])
    for window in ["60s", "5min", "60min"]:
        out[f"events_last_{window}"] = (
            out.groupby(group_col)[time_col]
               .transform(lambda s: s.rolling(window, on=s).count())
        )
    return out

def entropy_from_counts(counts: np.ndarray) -> float:
    total = counts.sum()
    if total <= 0:
        return 0.0
    p = counts / total
    p = p[p > 0]
    return float(-(p * np.log2(p)).sum())
