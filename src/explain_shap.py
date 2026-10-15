
from pathlib import Path

import joblib
import numpy as np
import pandas as pd
import shap
import matplotlib.pyplot as plt

# 1. Find our saved files
model_path = Path("results/random_forest/random_forest_model.joblib")
data_path = Path("data/processed/mqtt_iot_ids2020_biflow_split.npz")
features_path = Path("data/processed/X_train.csv.gz")

# 2. Load the trained Random Forest
model = joblib.load(model_path)
print("Random Forest loaded!")

# 3. Load the prepared dataset
data = np.load(data_path)
X_test = data["X_test"]

# Get the real names of our 27 network features
feature_names = pd.read_csv(features_path, nrows=0).columns.tolist()

# 4. Select 50 test records to explain
# 4. Select 10 test records from each of the 5 classes
y_test = data["y_test"]

rng = np.random.default_rng(42)
selected_indices = []

for class_id in np.unique(y_test):
    class_indices = np.where(y_test == class_id)[0]
    chosen = rng.choice(class_indices, size=10, replace=False)
    selected_indices.extend(chosen)

sample = pd.DataFrame(X_test[selected_indices], columns=feature_names)

print("Selected 10 records from each class.")

# 5. Create the SHAP explainer
print("Calculating SHAP values...")
explainer = shap.TreeExplainer(model)
shap_values = explainer(sample)

# 6. Calculate overall feature importance
values = np.abs(shap_values.values).mean(axis=(0, 2))

importance = pd.DataFrame({
    "feature": feature_names,
    "importance": values
})

importance = importance.sort_values("importance", ascending=False)

# 7. Save the results
output_dir = Path("results/shap")
output_dir.mkdir(parents=True, exist_ok=True)

importance.to_csv(output_dir / "feature_importance.csv", index=False)

# 8. Create a chart of the 15 most important features
top_features = importance.head(15).sort_values("importance")

plt.figure(figsize=(10, 7))
plt.barh(top_features["feature"], top_features["importance"])
plt.xlabel("Mean absolute SHAP value")
plt.title("Random Forest - Top 15 Important Network Features")
plt.tight_layout()
plt.savefig(output_dir / "feature_importance.png")
plt.close()

print("SHAP completed!")
print(importance.head(15))
print("Results saved in results/shap/")
