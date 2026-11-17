# Retrospective training-majority reference

Executed November 17, 2026, as Kien/Codex author-side work. This was added **after**
the Random Forest score was known; it does not satisfy a claim that a reference
was evaluated before the paper method. Independent #46 acceptance remains pending.

`DummyClassifier(strategy="most_frequent")` selects normal from training labels
only (68,806/95,120). It predicts normal for every held-out record and achieves
**17,202/23,781 = 72.335057% accuracy**, macro F1 **0.167894**, weighted F1
**0.607231**, and **zero recall for every attack class**. This shows why accuracy
alone is inadequate. The recorded RF score is 99.941129%; neither result proves
independent-network generalization.

The script checks all six logical array/name hashes against the #46 report before
scoring. Saved JSON records versions, source report checksum, preparation commit,
script checksum, class counts, metrics and matrix. CSVs use the canonical class
order: normal, scan_A, scan_sU, sparta, mqtt_bruteforce.

## Reproduce

Obtain the prepared NPZ and `results/data-verification.json` from the #46
verification workflow. These paths are supplied explicitly; no raw or processed
dataset is committed here. In an environment with NumPy and scikit-learn:

```powershell
python src/evaluate_reference_baseline.py --data PATH_TO_VERIFIED_SPLIT.npz --verification-report PATH_TO_DATA_VERIFICATION.json
```

Outputs: [metrics.json](metrics.json), [confusion_matrix.csv](confusion_matrix.csv),
[classification_report.csv](classification_report.csv). Recompute against final
integrated arrays if their hashes change; preserve this historical record.

Validation: the actual-array command completed successfully; hand checks confirmed
17,202 correct, 23,781 total, macro recall 0.2 and zero attack recall. Deliberately
swapped class names and a mismatched source hash were rejected before output
creation. This does not rerun the six #46 tests or replace a teammate's review.
