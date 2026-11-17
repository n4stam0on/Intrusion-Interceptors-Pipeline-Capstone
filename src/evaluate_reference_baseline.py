"""Score a retrospective train-majority reference on a hash-verified split."""

import argparse
import csv
import hashlib
import json
import platform
from importlib.metadata import version
from pathlib import Path

import numpy as np
from sklearn.dummy import DummyClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix


CLASS_NAMES = ["normal", "scan_A", "scan_sU", "sparta", "mqtt_bruteforce"]
ARRAY_NAMES = ("X_train", "X_test", "y_train", "y_test", "feature_names", "class_names")


def array_hash(array):
    """Use the same logical-array format as #46's real-data verifier."""
    value = np.ascontiguousarray(array)
    header = json.dumps({"shape": value.shape, "dtype": value.dtype.str}, sort_keys=True)
    return hashlib.sha256(header.encode() + b"\n" + value.tobytes()).hexdigest()


def evaluate(data_path, verification_path, output_dir):
    verification_bytes = verification_path.read_bytes()
    verification = json.loads(verification_bytes)
    if verification.get("result") != "PASS":
        raise ValueError("Source verification report is not PASS")
    with np.load(data_path, allow_pickle=False) as data:
        names = data["class_names"].tolist()
        if names != CLASS_NAMES:
            raise ValueError("Class-name order differs from canonical label IDs")
        hashes = {name: array_hash(data[name]) for name in ARRAY_NAMES}
        if hashes != verification["logical_array_sha256"]:
            raise ValueError("Prepared arrays differ from the verification report")
        X_train, X_test = data["X_train"], data["X_test"]
        y_train, y_test = data["y_train"], data["y_test"]
        if X_train.shape != (95120, 27) or X_test.shape != (23781, 27):
            raise ValueError("Unexpected verified split dimensions")
        if len(X_train) != len(y_train) or len(X_test) != len(y_test):
            raise ValueError("Feature and target lengths differ")
        labels = list(range(len(names)))
        if set(np.unique(y_train)) != set(labels) or set(np.unique(y_test)) != set(labels):
            raise ValueError("Unexpected/missing target classes")
        model = DummyClassifier(strategy="most_frequent")
        model.fit(X_train, y_train)
        predictions = model.predict(X_test)
        matrix = confusion_matrix(y_test, predictions, labels=labels)
        metrics = classification_report(
            y_test, predictions, labels=labels, target_names=names,
            zero_division=0, output_dict=True,
        )
        predicted_class = int(predictions[0])
        expected_class = int(np.bincount(y_train, minlength=len(names)).argmax())
        if predicted_class != expected_class or not np.all(predictions == expected_class):
            raise ValueError("Reference did not predict training-majority label")
        counts = {
            partition: {name: int(np.sum(values == i)) for i, name in enumerate(names)}
            for partition, values in (("train", y_train), ("test", y_test))
        }
        result = {
            "recorded_on": "2026-11-17",
            "status": "retrospective author-side reference, not independent acceptance",
            "chronology": "Added after the RF score was known; not a pre-method experiment",
            "strategy": "most_frequent; majority selected using training labels only",
            "predicted_class_id": predicted_class,
            "predicted_class_name": names[predicted_class],
            "accuracy": float(accuracy_score(y_test, predictions)),
            "correct_predictions": int(np.sum(y_test == predictions)),
            "train_rows": len(y_train), "test_rows": len(y_test),
            "feature_count": X_train.shape[1], "class_names": names,
            "class_counts": counts, "classification_report": metrics,
            "confusion_matrix_rows_true_columns_predicted": matrix.tolist(),
            "logical_array_sha256": hashes,
            "source_preparation_commit": verification["git_commit"],
            "source_verification_sha256": hashlib.sha256(verification_bytes).hexdigest(),
            "source_verification_url": "https://github.com/n4stam0on/Intrusion-Interceptors-Pipeline-Capstone/blob/6f1f40fb335182ef122ceca578c2d11e07a6e1e9/results/data-verification.json",
            "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            "environment": {"python": platform.python_version(), "platform": platform.system(),
                            "numpy": version("numpy"), "scikit-learn": version("scikit-learn")},
        }
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "metrics.json").write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    with (output_dir / "confusion_matrix.csv").open("w", newline="", encoding="utf-8") as handle:
        writer = csv.writer(handle)
        writer.writerow(["true_class / predicted_class", *names])
        writer.writerows([name, *row] for name, row in zip(names, matrix.tolist()))
    with (output_dir / "classification_report.csv").open("w", newline="", encoding="utf-8") as handle:
        writer = csv.writer(handle)
        writer.writerow(["class", "precision", "recall", "f1-score", "support"])
        for name in names + ["macro avg", "weighted avg"]:
            row = metrics[name]
            writer.writerow([name, *(row[key] for key in ("precision", "recall", "f1-score", "support"))])
    print(f"Training-majority reference: {result['correct_predictions']}/{result['test_rows']} "
          f"= {result['accuracy']:.6%}; predicts {result['predicted_class_name']}")
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--data", type=Path, required=True)
    parser.add_argument("--verification-report", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, default=Path("results/reference_baseline"))
    args = parser.parse_args()
    evaluate(args.data, args.verification_report, args.output_dir)


if __name__ == "__main__":
    main()
