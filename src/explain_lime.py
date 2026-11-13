from pathlib import Path
import json

import joblib
import numpy as np
import pandas as pd
from lime.lime_tabular import LimeTabularExplainer

data_path = Path("data/processed/mqtt_iot_ids2020_biflow_split.npz")
features_path = Path("data/processed/X_train.csv.gz")
model_path = Path("results/random_forest/random_forest_model.joblib")
output_dir = Path("results/lime")
output_dir.mkdir(parents=True, exist_ok=True)

# Load the trained model and processed data
model = joblib.load(model_path)
with np.load(data_path) as data:
    X_train = data["X_train"]
    X_test = data["X_test"]
    y_test = data["y_test"]

feature_names = pd.read_csv(features_path, nrows=0).columns.tolist()

if len(feature_names) != X_train.shape[1]:
    raise ValueError("Feature names do not match training columns.")

# Class IDs follow the team's preprocessing metadata
class_names = [
    "normal",
    "scan_A",
    "scan_sU",
    "sparta",
    "mqtt_bruteforce",
]

if not np.array_equal(model.classes_, np.arange(5)):
    raise ValueError("Unexpected class order. Check preprocessing metadata.")

print("Creating LIME explainer...")

explainer = LimeTabularExplainer(
    training_data=X_train,
    feature_names=feature_names,
    class_names=class_names,
    mode="classification",
    discretize_continuous=True,
    random_state=42,
)

predictions = model.predict(X_test)

# Select one correctly predicted record per class
selected = []
for class_id in range(5):
    candidates = np.where(
        (y_test == class_id) & (predictions == class_id)
    )[0]
    if len(candidates):
        selected.append(int(candidates[0]))

# Also explain one incorrect prediction if available
errors = np.where(predictions != y_test)[0]
if len(errors):
    selected.append(int(errors[0]))

summary = []

for index in selected:
    actual = int(y_test[index])
    predicted = int(predictions[index])

    print(f"Explaining record {index}: "
          f"actual={class_names[actual]}, "
          f"predicted={class_names[predicted]}")

    explanation = explainer.explain_instance(
        data_row=X_test[index],
        predict_fn=model.predict_proba,
        labels=[predicted],
        num_features=10,
        num_samples=1000,
    )

    name = f"record_{index}_pred_{class_names[predicted]}"
    explanation.save_to_file(str(output_dir / f"{name}.html"))

    for feature, weight in explanation.as_list(label=predicted):
        summary.append({
            "record_index": index,
            "actual_class": class_names[actual],
            "predicted_class": class_names[predicted],
            "feature_condition": feature,
            "lime_weight": weight,
        })

pd.DataFrame(summary).to_csv(
    output_dir / "lime_explanations.csv",
    index=False
)

with open(output_dir / "run_config.json", "w") as file:
    json.dump({
        "random_state": 42,
        "num_samples": 1000,
        "num_features": 10,
        "selected_test_indices": selected,
        "class_names": class_names,
    }, file, indent=2)

print("LIME completed!")
print(f"Explained {len(selected)} test records.")
print(f"Results saved in {output_dir}")
