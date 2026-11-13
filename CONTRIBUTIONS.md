# Team Contribution Logs for Commits

This document tracks individual contributions made by each member of the Intrusion Interceptors team. Paper values, team results, and open-PR work must be labeled accurately.

## Nastassja Monreal
| Date | Time | Contribution | Related Issue/Commit |
|------|------|--------------|----------------------|
| 9/8/26 | 10:02 AM | Reviewed and resolved the outdated dataset mismatch. Confirmed MQTT-IoT-IDS2020 Bi-flow as the finalized dataset based on the submitted capstone proposal and updated project tracking accordingly. | [Issue #2](https://github.com/n4stam0on/Intrusion-Interceptors-Pipeline-Capstone/issues/2) |
| 9/8/26 | 10:48 AM | Reviewed the completed paper and numerical-claim task. A later paper-table audit corrected the reproduction comparison to 99.99% Random Forest Bi-flow in Table 2; 99.16% is Linear SVM Bi-flow in Table 3. | [Issue #3](https://github.com/n4stam0on/Intrusion-Interceptors-Pipeline-Capstone/issues/3) |
| 9/8/26 | 10:57 AM | Reviewed and closed the completed capstone proposal task. Confirmed the proposal was finalized, reviewed, signed by all team members, and submitted with the team's finalized project plan. | [Issue #4](https://github.com/n4stam0on/Intrusion-Interceptors-Pipeline-Capstone/issues/4) |
| 9/8/26 | 11:08 AM | Reviewed and closed the separate clean-checkout reproducibility task after identifying that its verification requirements are covered by the project environment setup task. | [Issue #11](https://github.com/n4stam0on/Intrusion-Interceptors-Pipeline-Capstone/issues/11) |
| 9/8/26 | 11:40 AM | Updated the main project README with the selected XMID-MQTT paper, MQTT-IoT-IDS2020 Bi-flow dataset, completed proposal, and then-current verification status. The numerical target was later corrected to 99.99% Random Forest Bi-flow, Table 2. | README update |
| 11/13/26 | Documentation session | Audited main and PRs #45–#46, added verified dataset/access, environment, preprocessing-decision, methodology, and README documentation in five commits, opened PR #47, and synchronized eight Wiki pages with the correct paper/team result mapping. | [PR #47](https://github.com/n4stam0on/Intrusion-Interceptors-Pipeline-Capstone/pull/47) / Issues #18, #19, #20, #29, #30, #37, #38 |

## Kien Nguyen
| Date | Time | Contribution | Related Issue/Commit |
|------|------|--------------|----------------------|
| 9/3/26 | 5:54–5:55 PM | Created the dataset inspection script, dataset-verification procedure, and pull-request checklist for Sprint 1. | [Issue #1](https://github.com/n4stam0on/Intrusion-Interceptors-Pipeline-Capstone/issues/1) / [PR #5](https://github.com/n4stam0on/Intrusion-Interceptors-Pipeline-Capstone/pull/5) |
| 9/8/26 | 10:39–10:43 AM | Aligned the repository documentation with the finalized MQTT-IoT-IDS2020 Bi-flow dataset and documented its official source, archive details, and research-paper result question. | [PR #5](https://github.com/n4stam0on/Intrusion-Interceptors-Pipeline-Capstone/pull/5) / [d90091e](https://github.com/n4stam0on/Intrusion-Interceptors-Pipeline-Capstone/commit/d90091ef3cd6d778b7a4619065fb720946ea12bc) / [6c7b1ff](https://github.com/n4stam0on/Intrusion-Interceptors-Pipeline-Capstone/commit/6c7b1ffa13183d2dcc77f1e539d510ca2a033535) |
| 9/8/26 | 10:46–10:54 AM | Downloaded the team-provided Kaggle replication, validated all five Bi-flow CSVs, and recorded schema, class, integrity, checksum, and reproducibility evidence. | [Issue #1](https://github.com/n4stam0on/Intrusion-Interceptors-Pipeline-Capstone/issues/1) / [PR #5](https://github.com/n4stam0on/Intrusion-Interceptors-Pipeline-Capstone/pull/5) / [0965f94](https://github.com/n4stam0on/Intrusion-Interceptors-Pipeline-Capstone/commit/0965f944769b94685f04b40e20d92f6bc6313020) |
| 9/8/26 | 4:48–5:03 PM | Built and tested the reproducible MQTT-IoT-IDS2020 Bi-flow preprocessing pipeline, including class construction, leakage controls, deduplication, feature documentation, class-balance reporting, and stratified train/test artifacts for the Random Forest handoff. | [Issue #14](https://github.com/n4stam0on/Intrusion-Interceptors-Pipeline-Capstone/issues/14) / [PR #16](https://github.com/n4stam0on/Intrusion-Interceptors-Pipeline-Capstone/pull/16) |
| 10/13/26 | 4:34 PM | Addressed PR #16 review: changed API/CLI defaults to 80/20, restored active binary-label validation, added regression tests, regenerated and verified X/y artifacts, and documented counts and remaining method decisions. | [PR #16](https://github.com/n4stam0on/Intrusion-Interceptors-Pipeline-Capstone/pull/16) / [Issue #23](https://github.com/n4stam0on/Intrusion-Interceptors-Pipeline-Capstone/issues/23) |
| 10/13/26 | 4:34 PM | Resolved PR #5 conflicts against current main, preserved the coordinator's updated dataset documentation, and recorded the confirmed Random Forest Bi-flow 99.99% Table 2 target. | [PR #5](https://github.com/n4stam0on/Intrusion-Interceptors-Pipeline-Capstone/pull/5) / [Issue #21](https://github.com/n4stam0on/Intrusion-Interceptors-Pipeline-Capstone/issues/21) |

## Mia Gonzalez
| Date | Time | Contribution | Related Issue/Commit |
|------|------|--------------|----------------------|
| Pending | Pending | No dated repository contribution has been recorded yet. Add evaluation and results work here with issue, commit, or PR evidence. | Evaluation and Results Lead |

## Yassin Khodir
| Date | Time | Contribution | Related Issue/Commit |
|------|------|--------------|----------------------|
| 11/13/26 | Model and evaluation branch | Implemented and evaluated the 100-tree Random Forest baseline, reproduced 99.9411% accuracy in a clean environment, generated SHAP/LIME outputs, tested port-feature sensitivity, and documented independent-traffic limitations. Work remains under review. | [PR #45](https://github.com/n4stam0on/Intrusion-Interceptors-Pipeline-Capstone/pull/45) / Issues #7, #17, #27, #28, #31 |
