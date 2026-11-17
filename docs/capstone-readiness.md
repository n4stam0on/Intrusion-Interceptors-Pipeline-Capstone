# Capstone readiness audit — November 17, 2026

This is an evidence-based status record, not instructor acceptance or permission
to skip independent review. The four-member team was already approved.

## Course requirements and current evidence

| Requirement | Verified progress | Remaining gate |
|---|---|---|
| Approved recent paper and precise claim | Proposal completed; XMID-MQTT (2025), Random Forest Bi-flow, Table 2, 99.99% | Preserve this exact mapping in final materials |
| Repository reproducible from a clean checkout | Loading/preprocessing merged in #5/#16; six tests, real-data verifier, hashes, versions in #46 | Independent teammate full-data run and integrated main after review |
| Rebuilt model with honest comparison | #45 records 99.941129%, 23,767/23,781 correct; #48 records evaluation tables | Merge #46 first, update #45, rerun final code, then reconcile #47/#48 |
| Baseline before the paper method | #48 now includes a hash-verified training-majority reference: 72.335057%, macro F1 0.167894, zero attack recall | Added retrospectively November 17 after RF; review/integrate it and disclose chronology rather than claiming a before-method run |
| Wiki reproduction report | Eight pages corrected November 13; dataset, method, comparison and limitations present | Final audit against merged code and selected explanation outputs |
| Project board with written/sized stories | Browser verified assigned issues/sub-issues; eight started parent stories moved to In Progress; numeric Story Points field added November 17 | Team agrees and fills estimates, confirms individual credit and evidence links; estimates remain blank |
| Required GitHub collaborators | gdparra-edu is listed | Owner must add/verify cyberknowledge; it is absent from current collaborator listing |
| Contribution table in README and on a slide | CONTRIBUTIONS.md and Wiki summary exist; #47 expands all four members' records | Add concise README table, use it on a slide, obtain individual confirmations |
| 10–15 minute final presentation plus Q&A | #47 includes a proposed outline and speaking notes | Finished deck in repo, all four speakers, timed rehearsal and assigned Canvas slot |
| Live reproduction of a comparison number | Data and model run commands exist on separate branches | Rehearse an integrated clean-checkout run producing a reported number |
| Recording in repo of clean-checkout pipeline | A recording plan exists | Actual recording/file in repository, dated to final tested commit; saved JSON is not the recording |
| Final comparison table and all unstated choices | Wiki and #48 compare 99.99% with 99.941129%, a -0.048871 percentage-point gap | Include same table in slides; cite encoding/scaling deviations, deduplication, seeds, split, RF settings, sampling uncertainty |
| What would settle the gap | Port ablation and generalization limitations documented | State the next unrun experiment and expected finding; independent capture evaluation is still unverified |
| Canvas submission | Not accessible in this audit | User/team confirms repo + Project links, final slot, and authoritative deadlines on Canvas |

The course hub distinguishes the capstone reproduction from the lecture practice
pipeline. Do not add live attacks, an alerting service, or a dashboard merely to
complete the lecture-stage list unless the approved reproduction or instructor
requires them. A failed reproduction with evidence is an acceptable result;
numerical closeness alone is not proof of exact reproduction.

## Kien's completed work

See [Kien's completion status](kien-completion-status.md) for individual issue
updates, the closed loading checkpoint, review dependencies and remaining human
presentation obligations.

- PR #5 approved/merged: dataset inventory, inspection, labels, checksums and
  259,379 raw rows with 32 columns per file.
- PR #16 approved/merged: documented baseline cleaning, five-class construction,
  deduplication and stratified 80/20 seed-42 data preparation.
- PR #46 awaiting independent review: training-only constant selection, six
  passing author-side tests, real-data repeat builds and logical hashes, package
  constraints, verified model handoff, demo guide and reviewer notebook.
- 95,120 training rows, 23,781 testing rows and 27 features have been produced
  and checked in author-side runs; those are not independent teammate claims.
- Wiki technical review rechecked after coordinator corrections; checkpoint
  issues carry evidence and intentional pending gates.

## Next actions in order

1. Mia, Yassin or Nastassja runs the [reviewer notebook](https://colab.research.google.com/github/n4stam0on/Intrusion-Interceptors-Pipeline-Capstone/blob/mvpmvp/final-data-verification/notebooks/verify_pr46_colab.ipynb)
   in an authorized environment, attaches logs/report, and confirms six tests and
   95,120/23,781/27. Mia's Windows App Control failure remains a blocked attempt.
2. Reviewer approves #46; coordinator merges it. Kien cannot self-attest this
   independent requirement. No automatic approval/merge is implied by this audit.
3. Yassin updates #45 from merged main, preserves training-only feature selection,
   reruns training, and confirms approximately 99.9411% with the final data hashes.
4. Review #47/#48 against the integrated implementation. Preserve authorship and
   contribution records while resolving overlaps. Closed #24/#25/#26 are recorded
   as closed on GitHub, but their deliverables remain unmerged in #48.
5. Save a labeled confusion matrix for the final model. #45 currently prints it;
   #48 acknowledges the saved artifact is missing. The labeled matrix inside
   #46's author-side handoff JSON is supplementary evidence, not the final
   integrated model artifact. Save per-class sensitivity/specificity as well.
6. Model/evaluation owners verify SHAP/LIME sample provenance, final metrics and
   limitations. LIME is already implemented in #45; it needs review/integration,
   not a claim that it has not been written.
   #48's class order is corrected in commit `5f480fd` to normal, scan_A, scan_sU,
   sparta, mqtt_bruteforce. Its dashboard now distinguishes raw inventory from
   the prepared split and no longer claims five-fold validation, balanced RF
   weights, or no duplicate filtering. These corrections remain under review.
7. Kien finishes official-source comparison or records a clearly accepted
   provenance limitation; confirms final array hashes with model/evaluation
   leads; rehearses the dataset section and prepares screenshots/video.
8. Complete final Wiki, README contribution table, deck, recording, board sizing,
   individual confirmations and Canvas submission. Shared parent issues close
   only after their checkpoint acceptance criteria and final reviews are met.

## Tracking and dates

The repository milestones list M2 October 21 and M3 October 27 (both past), and
M4 December 3. These are project-board dates, not verified Canvas deadlines.
Check Canvas for the actual presentation slot and final cutoff. The course hub
rejects late final deliverables and states a missed scheduled presentation costs
15% of the total team capstone grade. Every member must present their own stories.

No recording, complete deck, rehearsal, Canvas submission, or successful
independent teammate full-data check was found in the repository evidence audited.
No unseen submission or offline work is assumed absent; the team should link it.

The board's closed #11 was retired as redundant; its Done status is not evidence
that the integrated clean-checkout run succeeded. Independent verification remains
tracked under #39/#46. No issues were newly closed or created by this audit.

## Primary sources

- [Course hub: capstone requirements and grading](https://uiwcyber.github.io/cis3370-public/course-hub.html#capstone)
- [Course resource browser](https://uiwcyber.github.io/cis3370-public/)
- [Presentation rubric](https://uiwcyber.github.io/cis3370-public/capstone/capstone-presentation-rubric.html)
- [Live PRs and review evidence](https://github.com/n4stam0on/Intrusion-Interceptors-Pipeline-Capstone/pulls)
- [Wiki method and comparison](https://github.com/n4stam0on/Intrusion-Interceptors-Pipeline-Capstone/wiki)
