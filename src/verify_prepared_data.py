"""Rebuild the approved baseline twice and verify the model handoff arrays."""

import argparse
import hashlib
import json
import platform
import subprocess
import sys
import time
from importlib.metadata import version
from pathlib import Path

import numpy as np
import pandas as pd

from preprocess_dataset import prepare_dataset, write_outputs

EXPECTED_SOURCE_SHA256 = {
    "biflow_normal.csv": "901bd9f475d9dd817017091caaec4a865bf654250baf4f2f54877b32b647db44",
    "biflow_scan_A.csv": "62de3d0c8478dd0774d0ffd7bba2c441c13ccfb2a4f7b17a0daaf6bc6091e361",
    "biflow_scan_sU.csv": "91047fd6072ab980b418ee28fcedc03b3eb8fbcf17426c080760aba3503bcff7",
    "biflow_sparta.csv": "9e3037f79c87e922b9cdf62125b9ec4db81b670b6bff6706385bd312becac976",
    "biflow_mqtt_bruteforce.csv": "790087e79e9d22f741ef06f1db3aed346a7a4980633e5c0619ae2c8a15ca4256",
}


def array_hash(array):
    """Hash logical array data, independent of ZIP/gzip header timestamps."""
    value = np.ascontiguousarray(array)
    header = json.dumps({"shape": value.shape, "dtype": value.dtype.str}, sort_keys=True)
    return hashlib.sha256(header.encode() + b"\n" + value.tobytes()).hexdigest()


def verify(first, second):
    hashes = {}
    for name in ("X_train", "X_test", "y_train", "y_test", "feature_names", "class_names"):
        np.testing.assert_array_equal(first[name], second[name])
        hashes[name] = array_hash(first[name])
    if first["X_train"].shape != (95120, 27) or first["X_test"].shape != (23781, 27):
        raise ValueError("Unexpected baseline shape")
    np.testing.assert_array_equal(first["class_names"],
                                  ["normal", "scan_A", "scan_sU", "sparta", "mqtt_bruteforce"])
    for partition in ("train", "test"):
        X, y = first[f"X_{partition}"], first[f"y_{partition}"]
        if len(X) != len(y) or X.shape[1] != len(first["feature_names"]):
            raise ValueError("Feature/target dimensions do not match")
        if not np.isfinite(X).all() or set(np.unique(y)) != set(range(5)):
            raise ValueError("Non-finite features or unexpected/missing target class")
    forbidden = {"target", "is_attack", "ip_src", "ip_dst", "proto"}
    if forbidden.intersection(first["feature_names"]):
        raise ValueError("Target or excluded identifier in feature list")
    train = pd.DataFrame(first["X_train"])
    test = pd.DataFrame(first["X_test"])
    if pd.concat([train, test], ignore_index=True).duplicated().any():
        raise ValueError("Duplicate feature vectors within or across partitions")
    return hashes


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input-dir", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, default=Path("data/processed/verification"))
    parser.add_argument("--report", type=Path, default=Path("results/data-verification.json"))
    args = parser.parse_args()
    start = time.perf_counter()
    runs = []
    for run in ("run1", "run2"):
        prepared = prepare_dataset(args.input_dir)
        directory = args.output_dir / run
        write_outputs(directory, *prepared)
        runs.append(directory)
    with np.load(runs[0] / "mqtt_iot_ids2020_biflow_split.npz", allow_pickle=False) as first, np.load(
        runs[1] / "mqtt_iot_ids2020_biflow_split.npz", allow_pickle=False
    ) as second:
        hashes = verify(first, second)
        for directory in runs:
            for name in ("X_train", "X_test", "y_train", "y_test"):
                saved = pd.read_csv(directory / f"{name}.csv.gz").to_numpy()
                expected = first[name]
                if name.startswith("y_"):
                    expected = expected.reshape(-1, 1)
                np.testing.assert_allclose(saved, expected, rtol=1e-12, atol=1e-12)
    metadata = json.loads((runs[0] / "preprocessing_metadata.json").read_text())
    other_metadata = json.loads((runs[1] / "preprocessing_metadata.json").read_text())
    if metadata != other_metadata:
        raise ValueError("Repeated metadata does not match")
    if {record["filename"]: record["sha256"] for record in metadata["input_files"]} != EXPECTED_SOURCE_SHA256:
        raise ValueError("Input hashes differ from the recorded local replication")
    report = {
        "result": "PASS",
        "git_commit": subprocess.check_output(["git", "rev-parse", "HEAD"], text=True).strip(),
        "preprocessing_script_sha256": hashlib.sha256(
            Path(__file__).with_name("preprocess_dataset.py").read_bytes()
        ).hexdigest(),
        "python": platform.python_version(),
        "platform": platform.system(),
        "packages": {name: version(name) for name in ("numpy", "pandas", "scikit-learn")},
        "elapsed_seconds": round(time.perf_counter() - start, 3),
        "logical_array_sha256": hashes,
        "checks": ["two independent rebuilds match", "saved CSV/NPZ round-trip", "finite features",
                   "five target classes", "no target/identifier columns", "no duplicate feature vectors"],
        "metadata": metadata,
        "limitations": ["Local Kaggle replication; official archive equivalence not established",
                        "Baseline excludes IP fields and does not perform paper-described encoding/scaling",
                        "Another teammate must confirm matching logical hashes on their machine"],
    }
    args.report.parent.mkdir(parents=True, exist_ok=True)
    args.report.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(f"PASS: {metadata['train_rows']:,} train, {metadata['test_rows']:,} test, {metadata['feature_count']} features")
    print(f"Report: {args.report}; elapsed: {report['elapsed_seconds']} seconds")
    return 0


if __name__ == "__main__":
    sys.exit(main())
