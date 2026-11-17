# XMID-MQTT Methodology Map

Owner: Nastassja Monreal (documentation coordination)  
Related issues: #29, #30, #37, #38

## Reproduction scope

The team is reproducing this experiment chain:

**XMID-MQTT paper → MQTT-IoT-IDS2020 dataset → Bi-flow representation → preprocessing → 80/20 split → Random Forest → evaluation → paper comparison → SHAP/LIME**

UNSW-NB15 is not the selected dataset. Packet and Uni-flow are not the selected feature representations.

## Paper-to-repository map

| Stage | Paper target | Team implementation | Evidence/status | Difference or caution |
| --- | --- | --- | --- | --- |
| Study | XMID-MQTT | Approved reproduction paper | Proposal and README | Do not confuse the paper name with the dataset name |
| Dataset | MQTT-IoT-IDS2020 | Five verified scenario CSVs | [dataset-and-access.md](dataset-and-access.md) | A Kaggle host is a mirror, not a different dataset |
| Representation | Bi-flow | `biflow_*.csv` files only | Dataset inventory | Packet and Uni-flow are out of scope |
| Prediction task | Five traffic classes | normal, scan_A, scan_sU, sparta, mqtt_bruteforce | Preprocessing output | `is_attack` is only used for row selection, then removed |
| Preprocessing | Paper Section 4.2 | Leakage-aware 27-feature baseline | [preprocessing-decisions.md](preprocessing-decisions.md), PR #46 | Baseline removes IP fields and does not apply Min-Max scaling |
| Split | 80/20 | Stratified 80/20, seed 42 | 95,120 train; 23,781 test | Stratification and seed 42 are team choices |
| Model | Random Forest | 100-tree Random Forest, seed 42 | PR #45 | Do not call hyperparameters paper-specified without a direct citation |
| Evaluation | Accuracy and classification metrics | Accuracy, classification report, confusion matrix | PR #45 | Keep paper and team numbers separate |
| SHAP | Explain model behavior | Global feature importance and SHAP outputs | PR #45 | Verify plots use the Random Forest inputs |
| LIME | Explain individual predictions | Local explanation outputs | PR #45 | Record the selected sample/class |

## Result mapping

| Number | Meaning | Use in the project |
| ---: | --- | --- |
| 99.99% | Random Forest, Bi-flow, XMID-MQTT Table 2 | Paper comparison target |
| 99.16% | Linear SVM, Bi-flow, XMID-MQTT Table 3 | Context only; not the Random Forest target |
| 99.9411% | Team Random Forest reproduction currently under review in PR #45 | Team result; do not round or relabel as the paper result |

## Interpretation limits

The current result is based on a random stratified split of the prepared records. It demonstrates performance on that split, not guaranteed generalization to a new network, capture session, organization, or device population. Duplicate removal and training-only feature selection reduce leakage risk, but endpoint identity and capture structure still require careful discussion.

## Final verification checklist

- [ ] PR #46 is reviewed and the final data counts match this document.
- [ ] PR #45 is reviewed and its model inputs match the final preprocessing output.
- [ ] Reported paper values cite the correct table and model.
- [ ] Team values are labeled as reproduced results.
- [ ] SHAP and LIME artifacts come from the Random Forest Bi-flow run.
- [ ] README, Wiki, proposal, final report, and presentation use the same scope.
- [ ] Any deliberate deviation is written as a team choice with a reason.

Issues #29, #30, #37, and #38 should remain open until the implementation PRs are resolved and the final repository and Wiki audit is complete.
