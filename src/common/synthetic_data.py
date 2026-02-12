"""Synthetic data generators for demos (no real data)."""
from __future__ import annotations
import numpy as np
import pandas as pd

def generate_synthetic_fraud_events(n: int = 5000, seed: int = 7) -> pd.DataFrame:
    rng = np.random.default_rng(seed)
    ts = pd.date_range("2026-01-01", periods=n, freq="S", tz="UTC")
    user = rng.integers(1, 500, size=n)
    user_hash = pd.Series(user).astype(str).apply(lambda x: f"u_{hash(x)%10_000_000}")
    event_type = rng.choice(["login", "purchase_attempt", "message_send", "api_call"], size=n, p=[0.25,0.25,0.25,0.25])
    latency = rng.normal(120, 30, size=n).clip(10, 1000).astype(int)
    # inject bursts
    burst_idx = rng.choice(np.arange(n), size=n//50, replace=False)
    latency[burst_idx] = (latency[burst_idx] * 2).clip(10, 2000).astype(int)
    df = pd.DataFrame({
        "event_id": [f"e_{i}" for i in range(n)],
        "org_id": "org_demo",
        "user_hash": user_hash.values,
        "timestamp": ts,
        "event_type": event_type,
        "latency_ms": latency,
        "status_code": rng.choice([200, 401, 403, 429, 500], size=n, p=[0.85,0.03,0.03,0.05,0.04]),
    })
    return df

def generate_synthetic_experiment(n_users: int = 20000, seed: int = 11) -> pd.DataFrame:
    rng = np.random.default_rng(seed)
    user = rng.integers(1, n_users+1, size=n_users)
    user_hash = pd.Series(user).astype(str).apply(lambda x: f"u_{hash(x)%10_000_000}")
    baseline = rng.random(n_users)
    # treatment lifts for a subgroup
    subgroup = rng.choice([0,1], size=n_users, p=[0.8,0.2])
    y_control = (baseline < 0.12).astype(int)
    y_treat = (baseline < (0.12 + 0.03*subgroup)).astype(int)
    df = pd.DataFrame({
        "user_hash": user_hash.values,
        "subgroup": subgroup,
        "y_control": y_control,
        "y_treat": y_treat
    })
    return df

def generate_synthetic_interactions(n: int = 50000, n_users: int = 5000, n_items: int = 2000, seed: int = 21) -> pd.DataFrame:
    rng = np.random.default_rng(seed)
    user = rng.integers(1, n_users+1, size=n)
    item = rng.integers(1, n_items+1, size=n)
    user_hash = pd.Series(user).astype(str).apply(lambda x: f"u_{hash(x)%10_000_000}")
    item_id = pd.Series(item).astype(str).apply(lambda x: f"it_{x}")
    # implicit feedback probability
    p = rng.random(n)
    clicked = (p < 0.08).astype(int)
    df = pd.DataFrame({"org_id":"org_demo","user_hash":user_hash.values,"item_id":item_id.values,"clicked":clicked})
    return df
