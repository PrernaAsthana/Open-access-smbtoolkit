"""Core experimentation stats: SRM, CI, power."""
from __future__ import annotations
import math
from dataclasses import dataclass
from typing import Tuple
from scipy.stats import chi2

def srm_p_value(observed_t: int, observed_c: int, expected_t: float = 0.5) -> float:
    n = observed_t + observed_c
    exp_t = n * expected_t
    exp_c = n * (1 - expected_t)
    chi = (observed_t - exp_t)**2 / (exp_t + 1e-12) + (observed_c - exp_c)**2 / (exp_c + 1e-12)
    return float(1 - chi2.cdf(chi, df=1))

def diff_in_proportions_ci(x_t: int, n_t: int, x_c: int, n_c: int, z: float = 1.96) -> Tuple[float, float, float]:
    p_t = x_t / max(n_t, 1)
    p_c = x_c / max(n_c, 1)
    delta = p_t - p_c
    p_pool = (x_t + x_c) / max(n_t + n_c, 1)
    se = math.sqrt(p_pool * (1 - p_pool) * (1/max(n_t,1) + 1/max(n_c,1)))
    return float(delta), float(delta - z*se), float(delta + z*se)

def bonferroni_alpha(alpha: float, looks: int) -> float:
    return alpha / max(looks, 1)
