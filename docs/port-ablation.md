# Random Forest Port-Feature Sensitivity Test

## Objective
Investigate whether the Random Forest classifier depends
heavily on source and destination port numbers.

## Configuration
- Dataset: MQTT-IoT-IDS2020 Bi-flow
- Training records: 95,120
- Testing records: 23,781
- Classifier: RandomForestClassifier
- Trees: 100
- Random state: 42

## Results

| Metric | Original | Without Ports |
|---|---:|---:|
| Features | 27 | 25 |
| Accuracy | 99.941129% | 99.945335% |
| Macro F1 | 0.999437 | 0.999477 |
| Incorrect predictions | 14 | 13 |

## Interpretation
Removing source and destination ports did not meaningfully
reduce classification accuracy on the existing test split.

This suggests the model does not depend entirely on
port-number features for this dataset.

## Limitations
Both experiments used the same existing holdout test set.
This analysis is exploratory and must not be used to select
a final model based on test-set performance.

The experiment does not establish generalization to
independent network sessions, devices, or capture periods.

## Decision
Retain the original 27-feature Random Forest baseline.
Investigate independent-traffic validation separately.
