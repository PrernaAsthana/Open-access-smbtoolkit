"""Deterministic assignment utilities."""
from __future__ import annotations
import hashlib

def deterministic_bucket(user_hash: str, experiment_id: str, buckets: int = 100) -> int:
    h = hashlib.sha256((user_hash + '|' + experiment_id).encode('utf-8')).hexdigest()
    return int(h[:8], 16) % buckets

def assign_arm(bucket: int, treatment_pct: int = 50) -> str:
    return "treatment" if bucket < treatment_pct else "control"
