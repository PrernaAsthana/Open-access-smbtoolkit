# OpenAI-SMBToolkit  
## Privacy-First AI Infrastructure for Small and Mid-Sized Organizations

OpenAI-SMBToolkit is a modular, CPU-friendly, privacy-preserving AI infrastructure framework designed to help organizations:

1. Detect and mitigate automated abuse (Fraud Detection & Anomaly Monitoring)
2. Run statistically valid experiments (Experimentation & Causal Inference Toolkit)
3. Deliver responsible personalization (Personalization & Ranking Engine)

This repository demonstrates implementation-level architecture aligned with a national-scale AI infrastructure specification. All datasets are synthetic and no real user data is included.

---

## Repository Structure

docs/ → Architecture diagrams and specification artifacts
notebooks/ → Jupyter notebooks demonstrating each module
src/ → Source code implementations
data/ → Synthetic data documentation
requirements.txt → Python dependencies
LICENSE → Apache 2.0 License

---

## Module Overview

### 1. Fraud Detection & Real-Time Anomaly Monitoring
- Rolling-window feature engineering (velocity, entropy, deviation)
- Unsupervised anomaly detection (Isolation Forest baseline)
- Dynamic threshold calibration
- Drift detection and risk-tier routing

Notebook: `notebooks/01_fraud_detection_demo.ipynb`

---

### 2. Experimentation & Causal Inference Toolkit
- Deterministic assignment
- Sample Ratio Mismatch (SRM) detection
- Confidence interval estimation
- Power analysis
- Sequential testing safeguards (Bonferroni correction)
- Uplift / Conditional Average Treatment Effect (CATE) modeling

Notebook: `notebooks/02_experimentation_toolkit_demo.ipynb`

---

### 3. Personalization & Responsible Ranking Engine
- Candidate generation
- Gradient boosted ranking baseline
- NDCG@K evaluation
- Uplift-aware re-ranking
- Fairness monitoring metrics

Notebook: `notebooks/03_personalization_ranking_demo.ipynb`

---

### 4. Cross-Module Integration
- Fraud signals as experiment guardrails
- Uplift-informed ranking adjustments

Notebook: `notebooks/04_end_to_end_integration.ipynb`

---

## Design Principles

- Privacy-first isolation (no raw identifiers stored)
- CPU-first deployment compatibility
- Modular adoption pathway
- Reproducible experimentation standards
- Auditability and governance support

---

## License

This project is released under the Apache 2.0 License.

