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

Accuracy = (TP \+ TN) / (TP \+ TN \+ FP \+ FN)

## Multiclass Averaging Method

Metrics will be reported using:

- Macro Average
- Weighted Average

Macro averaging ensures equal contribution from every class.

Weighted averaging accounts for differences in class frequencies.

## Expected Class Order

The expected class order for all evaluations, reports, and confusion matrices is:

1. normal
2. sparta
3. scan\_sU
4. scan\_A
5. mqtt\_bruteforce

This class order must remain consistent across all experiments.

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

## Class Order
1. normal
2. sparta
3. scan_sU
4. scan_A
5. mqtt_bruteforce


## Approval Summary

This evaluation plan establishes the standard procedure that will be used for all Random Forest baseline experiments and final comparisons against the published Table 2 accuracy target of 99.99%.

