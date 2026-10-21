# Work Log: Bi-flow Class Balance and Data Quality Analysis

## Objective
Produce a verified summary of class balance and dataset quality prior to Random Forest baseline training.

## Executive Summary & Data Quality Assessment
- **Total Records Analyzed:** 259,379 bidirectional flow samples across 5 CSV files.
- **Missing Values:** 0 null values across all 32 features.
- **Duplicate Records:** 0 duplicate rows detected.
- **Data Cleanliness:** 100% verified. No imputation or filtering required.

## Class Distribution Breakdown

| Dataset File | Normal Traffic (0) | Attack Traffic (1) | Total Records | Attack % | Status |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `biflow_normal.csv` | 86,008 | 0 | 86,008 | 0.00% | Verified |
| `biflow_sparta.csv` | 77,202 | 14,116 | 91,318 | 15.46% | Verified |
| `biflow_scan_sU.csv` | 17,230 | 22,434 | 39,664 | 56.56% | Verified |
| `biflow_scan_A.csv` | 5,786 | 19,907 | 25,693 | 77.48% | Verified |
| `biflow_mqtt_bruteforce.csv` | 2,152 | 14,544 | 16,696 | 87.11% | Verified |
| **Combined Total** | **188,378** | **71,001** | **259,379** | **27.37%** | **Clean** |

## Key Observations & Recommendations
1. **Class Ratio:** Aggregate distribution is 72.63% Normal vs 27.37% Attack (~3:1 ratio).
2. **Imbalance Variance:** File-level attack rates vary significantly from 0.00% to 87.11%.
3. **Splitting Strategy:** Must use `StratifiedKFold` cross-validation to maintain class proportions.
4. **Primary Evaluation Metrics:** Precision, Recall, Macro F1-score, and ROC-AUC. Avoid raw accuracy as a single baseline performance metric.
