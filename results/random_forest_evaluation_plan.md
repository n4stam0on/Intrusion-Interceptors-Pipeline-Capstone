# Random Forest Evaluation Plan

## Objective

Establish a consistent and reproducible evaluation procedure for the Random Forest Intrusion Detection System (IDS) before comparing final experimental results against the reference paper.

## Primary Comparison Metric

The primary metric used for comparison with the research paper will be:

- Accuracy (%)

The published Bi\-flow Random Forest target reported in Table 2 is:

- Target Accuracy: 99.99%

All final model results will be compared against this benchmark.

## Additional Evaluation Metrics

The following metrics will also be calculated:

- Precision
- Recall
- F1\-Score
- Accuracy

Metric formulas:

Precision = TP / (TP \+ FP)

Recall = TP / (TP \+ FN)

F1\-Score = 2 × (Precision × Recall) / (Precision \+ Recall)

Multiclass accuracy = number of correct predictions / total predictions.

For each class, TP/FP/FN/TN refer to that class versus all other classes.
Recall is sensitivity; specificity = TN / (TN + FP). State how a zero
denominator is handled. Macro/weighted averages must retain all five classes.

## Multiclass Averaging Method

Metrics will be reported using:

- Macro Average
- Weighted Average

Macro averaging ensures equal contribution from every class.

Weighted averaging accounts for differences in class frequencies.

## Expected Class Order

The expected class order for all evaluations, reports, and confusion matrices is:

| Label ID | Class |
|---:|---|
| 0 | normal |
| 1 | scan_A |
| 2 | scan_sU |
| 3 | sparta |
| 4 | mqtt_bruteforce |

This class order must remain consistent across all experiments.

Read `class_names` from the prepared NPZ and preserve its ID mapping. Pass
`labels=[0, 1, 2, 3, 4]` explicitly to metric/matrix functions. If display order
changes, reorder both matrix axes and labels together; never relabel unchanged
matrix values. This mapping agrees with preprocessing, #45's LIME configuration
and #46's recorded handoff matrix. Corrected November 17, 2026.

## Confusion Matrix Format

The confusion matrix will use:

- Rows = Actual Classes
- Columns = Predicted Classes

Labels will be displayed using the defined class order.

A confusion matrix image will be saved for every baseline evaluation.

## Result Verification

Metric values will be verified through:

1. Scikit\-learn metric functions
2. Manual cross\-checking of confusion matrix totals
3. Validation that confusion matrix totals equal the evaluation dataset size
4. Reproducible execution using a fixed random seed

## Planned Result Files

The following files will be generated:

- confusion\_matrix.png
- classification\_report.csv
- evaluation\_metrics.csv
- random\_forest\_results.md

## Reproducibility Settings

- Random Seed: 42
- Stratified data splitting
- Fixed preprocessing pipeline
- Documented Random Forest parameters

## Reference Target
Source Paper: Table 2

Model: Random Forest (Bi-flow)

Reported Accuracy: 99.99%

This value will be used as the benchmark for reproduction comparison.

## Evidence status and reference baseline

The canonical class mapping is defined once in the table above. PR #46's
independent verification and the final integrated-model evaluation remain pending.

A separate training-majority reference classifier is added retrospectively on
November 17, after the RF score was known. It selects the most frequent label
from training only and predicts it for every test record; it does not tune on
test performance. See [reference-baseline evidence](reference_baseline/README.md).
This improves comparison context but does not claim that the baseline was run
before the paper method.

The current experiment uses a stratified 80/20 holdout, not five-fold validation.
The recorded RF does not use `class_weight='balanced'`. ROC-AUC and alternative
weighting/cross-validation configurations are not measured by this PR.


## Plan Summary

This evaluation plan establishes the standard procedure that will be used for all Random Forest baseline experiments and final comparisons against the published Table 2 accuracy target of 99.99%.

