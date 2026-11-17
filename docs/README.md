# Project Documentation

Owner: Nastassja Monreal — Documentation Lead. Supports #6, #8, #10, #13, #19, #20, #29, #37, and #38.

## Source-of-truth index

| Document | Purpose | Status |
| --- | --- | --- |
| [Dataset and access](dataset-and-access.md) | Official source, five Bi-flow files, local locations, replication checksums | Documented; official archive equivalence remains pending |
| [Dataset verification](dataset-verification.md) | Inspection evidence and dataset inventory | Recorded baseline evidence |
| [Environment setup](environment-setup.md) | Python environments, installation, tests, real-data verification, troubleshooting | Documented; successful independent clean-checkout run pending |
| [Preprocessing](preprocessing.md) | Data preparation and split implementation | Reconcile with final PR #46 version |
| [Preprocessing decisions](preprocessing-decisions.md) | Paper requirements versus team choices | Documented; final team sign-off pending |
| [Methodology map](methodology-map.md) | Paper-to-code and paper-to-result mapping | Current branches mapped; final integrated audit pending |
| [Contribution log](../CONTRIBUTIONS.md) | Evidence for all four members, authorship and review separated | Interim audit; team confirmations pending |

## Documentation audit — November 17, 2026

The approved scope is XMID-MQTT / MQTT-IoT-IDS2020 / Bi-flow / Random Forest / Table 2 / SHAP and LIME. The paper comparison is **99.99%**; the team result under review is **99.9411%** (23,767 correct out of 23,781). These are separate results, differing by approximately **0.0489 percentage points**. The Linear SVM value is not the RF comparison.

The baseline uses 95,120 training records, 23,781 test records, 27 features, stratified 80/20 splitting, and seed 42. IP removal and omitted Min-Max scaling are documented deviations, not paper requirements. Random holdout performance does not establish independent-session or new-network generalization.

### Evidence by branch

- [PR #45](https://github.com/n4stam0on/Intrusion-Interceptors-Pipeline-Capstone/pull/45): Random Forest, SHAP/LIME, reproducibility and sensitivity evidence.
- [PR #46](https://github.com/n4stam0on/Intrusion-Interceptors-Pipeline-Capstone/pull/46): training-only constant selection, six synthetic-fixture tests, real-data rebuild/hash verifier.
- [PR #47](https://github.com/n4stam0on/Intrusion-Interceptors-Pipeline-Capstone/pull/47): coordinated documentation.
- [PR #48](https://github.com/n4stam0on/Intrusion-Interceptors-Pipeline-Capstone/pull/48): Mia’s class-balance dashboard, evaluation plan, and baseline evaluation document. These are open-PR deliverables, not final accepted results.

### Blocking and remaining checks

- [ ] Successful independent unit-test run and real-data verifier report; compare logical hashes with the recorded baseline. Mia’s App Control-blocked attempt is evidence of review effort only.
- [ ] Reconcile Python 3.11 model and Python 3.12 constrained-data instructions against the final tested environment. Do not bypass security policies.
- [ ] Review and integrate #46, then reconcile #45’s overlapping preprocessing and rerun the model. Recheck actual mergeability before integration.
- [ ] Review #48 numbers against saved model outputs, not just narrative descriptions.
- [ ] Save a labeled confusion-matrix CSV/figure. PR #48 explicitly reports this artifact missing; do not fabricate one from rounded metrics.
- [ ] Confirm final SHAP/LIME outputs originate from the final RF model and feature order.
- [ ] Resolve CONTRIBUTIONS.md overlap while preserving every member’s evidence.
- [ ] Verify official archive equivalence, or retain the explicit provenance limitation.
- [ ] Recheck every Wiki page, README, issue, final report, and slide after integration. Historical references must be labeled rather than silently interpreted as current instructions.
- [ ] Obtain team sign-off on documented preprocessing deviations.
- [ ] Link final slides, speaking contributions, demo recording/backup, and rehearsal evidence.
- [ ] Obtain each member’s contribution confirmation in #38.

## Completion rules

A checked documentation task means the written material exists; it does not mean the code was independently executed, merged, or approved. Keep #19 open for successful independent setup evidence, #20/#29 open for final implementation reconciliation, and #37/#38 open for the final repository/Wiki and contribution audits.

This is an interim repository-document review, not a claim that the final Wiki, proposal, presentation, or all code paths have been verified.
