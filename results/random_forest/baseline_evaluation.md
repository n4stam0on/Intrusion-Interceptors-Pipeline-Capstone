Random Forest Baseline Evaluation
Objective
Evaluate the baseline Random Forest classifier using the approved MQTT-IoT-IDS2020 Bi-flow test set and record reproducible performance metrics for comparison with the XMID-MQTT paper.

Experiment Configuration
Parameter	Value
Dataset	MQTT-IoT-IDS2020 Bi-flow
Model	RandomForestClassifier
Trees (n_estimators)	100
Random State	42
Train/Test Split	80/20 Stratified
Training Records	95,120
Testing Records	23,781
Features	27
Overall Performance Metrics
Metric	Value
Accuracy	99.9411%
Macro Precision	0.999551
Macro Recall	0.999323
Macro F1 Score	0.999437
Weighted Precision	0.999411
Weighted Recall	0.999411
Weighted F1 Score	0.999411
Total incorrect predictions on the test set: 14

Per-Class Performance
Class	Precision	Recall	F1-Score	Support
normal	0.999477	0.999709	0.999593	17,202
scan_A	1.000000	1.000000	1.000000	400
scan_sU	1.000000	1.000000	1.000000	447
sparta	1.000000	1.000000	1.000000	2,823
mqtt_bruteforce	0.998279	0.996906	0.997592	2,909
Reproducibility Verification
A full retraining verification was performed using the same processed dataset and model configuration.

Verification Check	Result
Original Accuracy	0.9994112947310878
Retrained Accuracy	0.9994112947310878
Accuracy Match	True
Saved Metrics Match	True
The retraining test confirmed that the Random Forest baseline produces reproducible evaluation results when using the documented configuration and random seed.

Comparison Target
The reproduction target identified from XMID-MQTT Table 2 is:

Reported Random Forest Bi-flow Accuracy: 99.99%
Observed baseline accuracy:

Reproduced Accuracy: 99.9411%
Difference from reported target:

Approximately 0.0489 percentage points
Notes
Results were generated using the team's approved 80/20 stratified train-test split.
Random seed 42 was used for both preprocessing and model training.
Per-class metrics indicate near-perfect classification performance across all five classes.
The mqtt_bruteforce class produced the lowest performance metrics but still achieved Precision, Recall, and F1 values above 0.996.
A confusion matrix artifact should be generated and stored alongside these results if prediction outputs become available.
Related Files
results/random_forest/metrics.json
results/random_forest/port_ablation.json
REPRODUCIBILITY_TEST.md
Related Commits
c3efd26 — Update Random Forest results with new preprocessing
a6e54b3 — Document Random Forest port-feature sensitivity analysis
6df611e — Verify Random Forest retraining reproducibility
