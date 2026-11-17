# Preprocessing Decision Record

Owner: Nastassja Monreal (documentation coordination)  
Related issues: #20, #22, #23, #29

## Purpose

This record prevents team choices from being presented as instructions or results from XMID-MQTT. The approved reproduction target is MQTT-IoT-IDS2020 Bi-flow, an 80/20 split, Random Forest evaluation, and SHAP/LIME explanation.

## Decision matrix

| Item | Source | Current decision | Status |
| --- | --- | --- | --- |
| MQTT-IoT-IDS2020 | Paper | Use the paper's dataset | Aligned |
| Bi-flow representation | Paper | Use only the five Bi-flow scenario files | Aligned |
| Five-class task | Paper and dataset scenarios | normal, scan_A, scan_sU, sparta, mqtt_bruteforce | Aligned |
| 80/20 train-test split | Paper | Use an 80/20 split | Aligned |
| IP label encoding | Paper Section 4.2 | Not used in the current baseline because IP fields are removed | Documented deviation |
| Min-Max scaling | Paper Section 4.2 | Not used for the Random Forest baseline | Documented deviation |
| Scenario row selection | Dataset companion workflow and team implementation | Select normal rows from the normal file and attack rows from each attack file | Team implementation |
| Remove `ip_src` and `ip_dst` | Team baseline | Prevent memorizing endpoint identities | Team choice |
| Remove `proto` | Companion/baseline choice | Excluded from the current feature set | Team choice |
| Remove `is_attack` after selection | Team baseline | Prevent direct target leakage | Team choice |
| Deduplicate before splitting | Team baseline | Reduce duplicate leakage between train and test | Team choice |
| Fit constant-feature removal on training data only | Team baseline in PR #46 | Avoid test-set information leakage | Team choice |
| Stratify the split | Team baseline | Preserve class proportions | Team choice |
| Random seed 42 | Team baseline | Make the split and model reproducible | Team choice |
| Random Forest with 100 trees | Current model implementation in PR #45 | Reproduction baseline | Team implementation; verify against the paper before calling it paper-specified |

## Accepted baseline

The current leakage-aware pipeline:

1. loads the five MQTT-IoT-IDS2020 Bi-flow files;
2. keeps the intended normal or attack rows for each scenario;
3. creates the five-class `class` label;
4. removes identifiers and the binary selection label;
5. removes duplicates;
6. performs a stratified 80/20 split with seed 42;
7. identifies constant features using training data only;
8. outputs 95,120 training rows, 23,781 testing rows, and 27 features.

This is a defensible Random Forest baseline, but it is not an exact reproduction of every preprocessing step described in Section 4.2 because IP label encoding and Min-Max scaling are not applied. Reports must state that difference.

## Why no scaling in the baseline?

Random Forest decisions are based on feature thresholds and do not require features to share a numeric scale. Omitting scaling is a team simplification, not evidence that the paper omitted it. A strict paper-aligned comparison can be added as a separate experiment without overwriting the baseline.

## Evidence and dependencies

- Current preprocessing description: [preprocessing.md](preprocessing.md)
- Dataset verification: [dataset-verification.md](dataset-verification.md)
- Data preparation implementation: PR #16
- Final leakage-safe verification under review: PR #46
- Random Forest and explainability under review: PR #45

## Required reporting language

Use wording such as: “The paper specifies X; our baseline uses Y because Z.” Never write that the paper specified seed 42, IP removal, no scaling, or 100 trees unless the cited paper text directly supports that statement.

Issue #20 should remain open until PRs #45 and #46 are resolved and the final merged pipeline is checked against this record.
