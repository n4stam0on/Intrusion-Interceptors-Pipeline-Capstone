# Presentation outline, speaking notes, and rehearsal plan

Prepared November 17, 2026 by Nastassja Monreal (documentation coordination). Supports #9, #12, #30, #37, #38. This is a working presentation script, not completed slides or rehearsal evidence. Proposed roles and timing require team agreement. The instructor’s required duration takes precedence over this suggested ten-minute plan.

## Slide-by-slide outline

| Slide | On-slide content | Proposed speaker | Budget | Evidence |
| --- | --- | --- | --- | --- |
| 1. Intrusion Interceptors | XMID-MQTT reproduction, MQTT-IoT-IDS2020 Bi-flow, Random Forest | Nastassja | 30 sec | README and methodology-map.md |
| 2. Reproduction question | Compare the RF Bi-flow experiment with Table 2’s 99.99% accuracy | Nastassja | 45 sec | methodology-map.md and paper Table 2 |
| 3. Dataset and classes | Five Bi-flow files, normal/scan_A/scan_sU/sparta/mqtt_bruteforce | Kien | 60 sec | dataset-and-access.md and dataset-verification.md |
| 4. Data preparation | 95,120 train, 23,781 test, 27 features, stratified 80/20, seed 42 | Kien | 75 sec | PR #46 verification reports and preprocessing code |
| 5. Random Forest | 100 trees, seed 42, training and prediction steps | Yassin | 60 sec | PR #45 code and reproducibility record |
| 6. Evaluation | 99.9411% team accuracy, 14 errors, per-class results, labeled confusion matrix when available | Mia | 75 sec | PR #48 baseline_evaluation.md and saved model evidence |
| 7. Paper comparison | Paper 99.99%, team 99.9411%, difference about 0.0489 percentage points | Mia | 45 sec | Table 2 and the recorded team metrics |
| 8. Explainability | One verified SHAP figure and one verified LIME example, labeled by class/sample | Yassin | 60 sec | PR #45 explainability artifacts |
| 9. Reproducibility demonstration | Show branch/commit, tests, verifier report and model output | Kien/Yassin | 90 sec | Actual successful run or explicitly labeled saved output |
| 10. Limitations and next steps | Preprocessing deviations, random-holdout limits, open verification gates | Nastassja | 60 sec | preprocessing-decisions.md, docs audit, PR discussions |

The suggested total is ten minutes. Keep questions outside this estimate unless the instructor includes them.

## Nastassja’s speaking notes

### Opening

“We are Intrusion Interceptors. Our project follows the XMID-MQTT paper using the MQTT-IoT-IDS2020 dataset. We focus on bidirectional flow features and a Random Forest classifier. We compare our recorded result with the Random Forest Bi-flow result in Table 2, and use SHAP and LIME to examine the model’s predictions.”

### Reproduction question

“The paper reports 99.99% accuracy for this Random Forest comparison. Our current run reports 99.9411%. We keep those numbers separate throughout our documentation. Our goal is to explain both the measured performance and the choices that affect how closely our experiment follows the paper.”

### Handoff to Kien

“Kien will explain the five dataset files, how we selected the traffic classes, and how we prepared the training and testing records.”

### Limitations and closing

“Our baseline removes IP fields and does not apply the paper’s IP encoding and Min-Max scaling steps. We document those as deliberate deviations. We also use a random stratified holdout, so the recorded accuracy alone does not show how the model performs on a new network or independent capture session. Our remaining checks include independent execution, final artifact review, and consistent documentation after integration.”

Before presenting, replace the remaining-check sentence with the actual current status. Do not claim all checks passed if evidence is missing.

### If asked about Mia’s test attempt

“Mia checked out the data-verification branch and attempted the tests, but Windows Application Control blocked pandas during import. The same error occurred with a direct pandas import before our project code ran. We recorded that attempt as blocked verification and still require a successful independent run.”

### If asked whether 99.9411% proves reproduction success

“The value is close to the paper’s reported accuracy, but the preprocessing differs and the split may differ. We report the result and those limitations rather than treating numerical closeness as proof of an exact reproduction.”

## Evidence to collect before slide assembly

- [ ] Mia supplies a readable metrics table and labeled confusion matrix. PR #48 currently identifies the saved matrix as missing.
- [ ] Yassin selects a SHAP plot and LIME example and records model/input provenance.
- [ ] Kien supplies successful verifier output, package versions, split dimensions, and hash comparison.
- [ ] Independent tester supplies the six-test output and real-data report.
- [ ] Each speaker reviews the proposed section and confirms the timing in #30.
- [ ] Nastassja adds the final deck link and reconciles slide claims with the Wiki.

## Demonstration run sheet

Use an approved environment, activate its virtual environment, and show the exact checked-out commit. PR #46 contains the verifier. Model commands require PR #45’s files or the reviewed integrated branch. Do not assume separate open branches contain one another’s files.

```bash
git rev-parse HEAD
python --version
python -m pip check
python -m unittest discover -s tests -v
python src/verify_prepared_data.py --input-dir data/raw/kaggle-replication --report results/independent-data-verification.json
```

Expected evidence is six passing tests followed by the separate verifier’s PASS with 95,120 train rows, 23,781 test rows, and 27 features. Unit tests use synthetic data and cannot establish those real-data dimensions by themselves. Keep the five raw CSVs outside Git.

The model lead must copy the exact tested model/SHAP/LIME commands from the final code and rehearse them before the demo. This plan does not assert those commands have been run.

### Backup procedure

1. Save a recording of the successful integrated run, with branch/commit and versions visible.
2. Keep copies of the verifier report, metrics, labeled confusion matrix, and selected explanations.
3. If live execution fails, state the error and show the dated saved evidence as backup output.
4. Do not disable security policies or silently substitute output from another model or dataset.

## Rehearsal checklist

- [ ] Confirm instructor duration and proposed speaking order.
- [ ] Each member practices their section and transitions.
- [ ] Time a complete run including demo loading.
- [ ] Check figure labels and readability at presentation size.
- [ ] Verify paper/team values and percentage-point wording.
- [ ] Test the live workflow and the backup recording on the presentation machine.
- [ ] Record actual rehearsal date, attendees, duration, failures, corrections, and evidence link in #30.

## Contribution confirmation request

Each member should review their entry in CONTRIBUTIONS.md and comment on #38 with: work authored, work reviewed, evidence links, corrections needed, and whether the entry is accurate. A blocked test attempt can count as review effort but must remain separate from a successful verification claim. No confirmations have been supplied by this document.

## Source references

- [Methodology mapping](methodology-map.md)
- [Preprocessing decisions](preprocessing-decisions.md)
- [Environment setup](environment-setup.md)
- [Final audit checklist](README.md)
- [Contribution log](../CONTRIBUTIONS.md)
- [PR #45](https://github.com/n4stam0on/Intrusion-Interceptors-Pipeline-Capstone/pull/45)
- [PR #46](https://github.com/n4stam0on/Intrusion-Interceptors-Pipeline-Capstone/pull/46)
- [PR #48](https://github.com/n4stam0on/Intrusion-Interceptors-Pipeline-Capstone/pull/48)
