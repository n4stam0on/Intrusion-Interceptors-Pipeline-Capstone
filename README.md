# Intrusion Interceptors

CIS 3370 Intrusion Detection Systems Capstone Project

## Project Goal

Our team will reproduce the Random Forest intrusion-detection experiment from the XMID-MQTT research paper using the MQTT-IoT-IDS2020 Bi-flow dataset. We will evaluate the reproduced Random Forest model and compare its performance with the 99.99% Bi-flow accuracy reported in Table 2 of the paper. We will also use SHAP and LIME to examine and explain the model's predictions.

## Experiment Scope

- **Research paper:** XMID-MQTT
- **Dataset:** MQTT-IoT-IDS2020
- **Feature representation:** Bi-flow
- **Model:** Random Forest
- **Paper comparison:** Table 2
- **Reported Random Forest Bi-flow accuracy:** 99.99%
- **Explainability methods:** SHAP and LIME

The 99.16% Bi-flow result in Table 3 belongs to Linear SVM and is not the primary reproduction target.

## Current Status

- M1 — Proposal and research selection completed
- Dataset loading and baseline preprocessing are on `main`
- Final leakage-safe data verification is under review in PR #46
- Random Forest, evaluation, SHAP, and LIME are under review in PR #45
- The current reproduced Random Forest accuracy under review is 99.9411%; this is the team result, not the paper's 99.99% result
- Documentation for dataset access, environment setup, preprocessing choices, and methodology mapping is being proposed from `n4stam0on/documentation-tasks`

## Documentation

- [Dataset and access](docs/dataset-and-access.md)
- [Dataset verification](docs/dataset-verification.md)
- [Environment setup](docs/environment-setup.md)
- [Preprocessing implementation](docs/preprocessing.md)
- [Preprocessing decisions and deviations](docs/preprocessing-decisions.md)
- [Paper-to-repository methodology map](docs/methodology-map.md)

## Reproduction Reminder

Keep this chain consistent across code, issues, Wiki pages, reports, and slides:

**XMID-MQTT → MQTT-IoT-IDS2020 → Bi-flow → preprocessing → 80/20 split → Random Forest → evaluation → compare with paper → SHAP/LIME**

When the paper does not specify a choice, document it as a team decision instead of attributing it to the paper.
