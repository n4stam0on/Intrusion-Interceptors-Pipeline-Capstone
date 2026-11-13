
from pathlib import Path
import json

import joblib
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix,
)

# 1. Find the prepared dataset
data_path = Path("data/processed/mqtt_iot_ids2020_biflow_split.npz")

if not data_path.exists():
    raise FileNotFoundError(
        "Prepared dataset not found. Run preprocessing first."
    )

# 2. Load the training and testing data
data = np.load(data_path)

X_train = data["X_train"]
X_test = data["X_test"]
y_train = data["y_train"]
y_test = data["y_test"]

# 3. Create the Random Forest model
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42,
    n_jobs=-1
)

# 4. Train the model
print("Training Random Forest...")
model.fit(X_train, y_train)

# 5. Test the model
predictions = model.predict(X_test)

accuracy = accuracy_score(y_test, predictions)

print(f"Accuracy: {accuracy:.4%}")
print(classification_report(y_test, predictions, zero_division=0))
print("Confusion matrix:")
print(confusion_matrix(y_test, predictions))

# 6. Save the model and results
output_dir = Path("results/random_forest")
output_dir.mkdir(parents=True, exist_ok=True)

joblib.dump(model, output_dir / "random_forest_model.joblib")

metrics = {
    "accuracy": float(accuracy),
    "n_estimators": 100,
    "random_state": 42,
    "train_rows": len(X_train),
    "test_rows": len(X_test),
}

with open(output_dir / "metrics.json", "w") as file:
    json.dump(metrics, file, indent=4)

print("Model and results saved!")
