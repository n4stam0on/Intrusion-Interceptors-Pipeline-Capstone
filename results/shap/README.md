
# Random Forest SHAP Analysis

## Purpose
We used SHAP to understand which network traffic features influence our Random Forest intrusion detection model.

## Why TreeExplainer?
We selected SHAP TreeExplainer because our model is a Random Forest, which is made of decision trees. TreeExplainer is designed to explain tree-based models.

## Dataset and Sampling
We used the MQTT-IoT-IDS2020 Bi-flow dataset.

The model uses 27 network features and predicts 5 classes.

For this analysis, we randomly selected 10 test records from each class, giving us 50 records total.

We used random seed 42 so the same records can be selected again.

## Method
We calculated SHAP values for the 50 selected records.

We then calculated the mean absolute SHAP value for each feature, averaging across all selected records and all 5 classes.

A larger value means the feature had more influence on the model's predictions in this sample.

## Results
The three most influential features were:

1. bwd_num_bytes — 0.055184
2. fwd_num_bytes — 0.036965
3. bwd_max_pkt_len — 0.032152

These features describe the amount of network traffic and packet sizes.

## Output Files
- feature_importance.csv — rankings for all 27 features
- feature_importance.png — chart showing the top 15 features
- ../../src/explain_shap.py — Python script used to generate the results

## How to Reproduce
First, run the dataset preprocessing script:

    python src/preprocess_dataset.py

Next, train the Random Forest:

    python src/train_random_forest.py

Finally, generate the SHAP results:

    python src/explain_shap.py

## Limitations
This explanation uses only 50 test records, so the results may not represent the entire dataset.

We intentionally selected the same number of records from each class. This means the results represent a balanced sample rather than the actual class distribution.

SHAP describes how features influence model predictions. It does not prove that those features cause attacks.

The model's very high test accuracy also needs further validation before making claims about real-world performance.
