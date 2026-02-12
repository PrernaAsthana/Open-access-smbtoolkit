# Open Access-SMBToolkit (AI Infrastructure for SMBs)

**Open Access-SMBToolkit** is an open, privacy-first, CPU-friendly AI infrastructure toolkit that helps small and mid-sized organizations:
1) detect and mitigate automated abuse (Fraud Detection & Anomaly Monitoring),
2) run statistically valid experiments (Experimentation & Causal Inference), and
3) deliver responsible personalization (Personalization & Ranking).

This repository is designed as an implementation-oriented reference with runnable notebooks, demo code, and architecture artifacts.
It is intentionally modular so that organizations can adopt components incrementally.

## Repository Structure

- `docs/architecture/` — architecture diagrams and technical specification PDFs
- `docs/repo/` — repository documentation for evidentiary packaging (NIW/RFE exhibit)
- `notebooks/` — Jupyter notebooks demonstrating each module end-to-end
- `src/` — minimal, readable implementation code used by notebooks
- `data/` — synthetic datasets (no real user data)

## Modules

### 1) Fraud Detection & Real-Time Anomaly Monitoring
- Streaming-compatible feature extraction (velocity, entropy, deviation)
- Unsupervised baseline using Isolation Forest
- Dynamic thresholding, drift monitoring, and risk-tier routing

See: `notebooks/01_fraud_detection_demo.ipynb`

### 2) Experimentation & Causal Inference Toolkit
- Deterministic assignment and exposure logging
- SRM (sample ratio mismatch) detection
- Confidence intervals, power analysis, sequential testing controls
- Uplift / CATE estimation (T-learner baseline)

See: `notebooks/02_experimentation_toolkit_demo.ipynb`

### 3) Personalization & Responsible Ranking Engine
- Candidate generation + feature representation
- CPU-first ranking (GBDT baseline)
- Calibration concepts + uplift-aware and fairness-aware re-ranking

See: `notebooks/03_personalization_ranking_demo.ipynb`

### 4) Cross-Module Integration
- Using fraud signals as experiment guardrails
- Using uplift estimates for personalization re-ranking
- Unified governance/audit artifacts

See: `notebooks/04_end_to_end_integration.ipynb`

## Quickstart

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
jupyter lab
```

## Data & Privacy
All datasets in this repository are synthetic. No raw identifiers are stored. Identifiers shown are hashed placeholders.

## License
This project is released under the Apache 2.0 License. See `LICENSE`.

## Citation / Exhibit Note
For immigration evidentiary packaging, see:
`docs/repo/OpenAccess-SMBToolkit_Repository_Documentation_and_Technical_Assets.md`
