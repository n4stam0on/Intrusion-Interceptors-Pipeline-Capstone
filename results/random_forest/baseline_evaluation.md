### Random Forest Baseline Evaluation
Objective
Evaluate the baseline Random Forest classifier using the approved MQTT-IoT-IDS2020 Bi-flow test set and establish reproducible baseline metrics for later comparison with the XMID-MQTT paper.

## Experiment Configuration
Parameter             	Value
Dataset	                MQTT-IoT-IDS2020 Bi-flow
Classification Type    	Multiclass (5 Classes)
Classes               	normal, scan_A, scan_sU, sparta, mqtt_bruteforce
Model	                  RandomForestClassifier
Trees (n_estimators)	  100
Random State          	42
Train/Test Split	      80/20 Stratified
Training Records      	95,120
Testing Records	        23,781
Features	              27


## Test Set Class Distribution
Class	                   Test Samples
normal	                 17,202
scan_A                  	400
scan_sU	                 447
sparta	                 2,823
mqtt_bruteforce	         2,909
Total                 	23,781

## Overall Performance Metrics
Metric	                  Value
Accuracy          	      99.9411%
Macro Precision	          0.999551
Macro Recall             	0.999323
Macro F1 Score	          0.999437
Weighted Precision	      0.999411
Weighted Recall	          0.999411
Weighted F1 Score        	0.999411
Total incorrect predictions: 14

## Per-Class Performance
Class  	Precision	 Recall	  F1-Score	Support
normal	0.999477	0.999709	0.999593	17,202
scan_A	1.000000	1.000000	1.000000	400
scan_sU	1.000000	1.000000	1.000000	447
sparta	1.000000	1.000000	1.000000	2,823
mqtt_bruteforce	0.998279	0.996906	0.997592	2,909

## Reproducibility Verification
A full retraining verification was performed using the same processed dataset and model configuration.

Verification Check	  Result
Original Accuracy   	0.9994112947310878
Retrained Accuracy	  0.9994112947310878
Accuracy Match	      True
Saved Metrics Match	  True
The retraining test confirmed that the Random Forest baseline reproduces identical evaluation metrics when trained on the same prepared dataset with the documented configuration and random seed.

## Comparison Target
XMID-MQTT Reference Result
Source	    Metric	  Value
XMID-MQTT   Random Forest Bi-flow 
Table 2	    Accuracy	99.99%

## Reproduction Baseline
Metric                	Value
Reproduced Accuracy   	99.9411%

Difference from reported target:
99.9900% − 99.9411% = 0.0489 percentage points
This value establishes the baseline for future paper-comparison analysis and should not yet be interpreted as reproduction success or failure.

## Confusion Matrix Status
Per-class precision, recall, F1-score, and support statistics were preserved in the baseline evaluation outputs. However, a labeled confusion matrix artifact was not found among the saved Random Forest result files.

The confusion matrix should be regenerated from the original prediction outputs and stored as one of the following:

results/random_forest/confusion_matrix.png
