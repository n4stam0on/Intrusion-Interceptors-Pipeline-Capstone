# Clean Environment Reproducibility Test

Date: 2026-11-13
Platform: Windows
Python: 3.11.9
Branch: yassin/random-forest-model

## Test Results

- Created a fresh virtual environment: PASS
- Installed packages from requirements-lock.txt: PASS
- pip check: No broken requirements found
- Imported sklearn, shap, lime, pandas, numpy, joblib: PASS

## Conclusion

The pinned Python dependencies were successfully installed and imported in a fresh Windows environment.

Full model retraining reproducibility has not yet been tested.

## Full Random Forest Retraining Test

Date: 2026-11-13
Environment: Fresh Python 3.11.9 virtual environment

Configuration:
- Algorithm: Random Forest
- Number of trees: 100
- Random seed: 42
- Dataset: MQTT-IoT-IDS2020 Bi-flow
- Training samples: 95120
- Testing samples: 23781

Results:
- Original accuracy: 0.9994112947310878
- Retrained accuracy: 0.9994112947310878
- Accuracy matches: True
- All saved metrics match: True

Conclusion:
Retraining with the same prepared dataset and fixed model settings
reproduced all recorded evaluation metrics.

This test does not establish byte-for-byte model identity.
