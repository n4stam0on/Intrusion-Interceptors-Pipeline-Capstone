"""Prepare MQTT-IoT-IDS2020 Bi-flow data for multiclass modeling.

The script follows the class construction used by the dataset authors' companion
code while preventing target leakage and duplicate rows across the train/test
boundary. Raw files are read-only; all generated artifacts go to data/processed.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split


EXPECTED_COLUMNS = (
    "ip_src",
    "ip_dst",
    "prt_src",
    "prt_dst",
    "proto",
    "fwd_num_pkts",
    "bwd_num_pkts",
    "fwd_mean_iat",
    "bwd_mean_iat",
    "fwd_std_iat",
    "bwd_std_iat",
    "fwd_min_iat",
    "bwd_min_iat",
    "fwd_max_iat",
    "bwd_max_iat",
    "fwd_mean_pkt_len",
    "bwd_mean_pkt_len",
    "fwd_std_pkt_len",
    "bwd_std_pkt_len",
    "fwd_min_pkt_len",
    "bwd_min_pkt_len",
    "fwd_max_pkt_len",
    "bwd_max_pkt_len",
    "fwd_num_bytes",
    "bwd_num_bytes",
    "fwd_num_psh_flags",
    "bwd_num_psh_flags",
    "fwd_num_rst_flags",
    "bwd_num_rst_flags",
    "fwd_num_urg_flags",
    "bwd_num_urg_flags",
    "is_attack",
)

DROP_FOR_MODELING = ("ip_src", "ip_dst", "proto", "is_attack")

METRIC_DESCRIPTIONS = {
    "num_pkts": ("discrete count", "number of packets"),
    "mean_iat": ("continuous", "mean packet inter-arrival time"),
    "std_iat": ("continuous", "standard deviation of packet inter-arrival time"),
    "min_iat": ("continuous", "minimum packet inter-arrival time"),
    "max_iat": ("continuous", "maximum packet inter-arrival time"),
    "mean_pkt_len": ("continuous", "mean packet length"),
    "std_pkt_len": ("continuous", "standard deviation of packet length"),
    "min_pkt_len": ("continuous", "minimum packet length"),
    "max_pkt_len": ("continuous", "maximum packet length"),
    "num_bytes": ("discrete count", "number of bytes"),
    "num_psh_flags": ("discrete count", "number of TCP PSH flags"),
    "num_rst_flags": ("discrete count", "number of TCP RST flags"),
    "num_urg_flags": ("discrete count", "number of TCP URG flags"),
}


@dataclass(frozen=True)
class Scenario:
    class_id: int
    class_name: str
    filename: str
    selected_is_attack: int


SCENARIOS = (
    Scenario(0, "normal", "biflow_normal.csv", 0),
    Scenario(1, "scan_A", "biflow_scan_A.csv", 1),
    Scenario(2, "scan_sU", "biflow_scan_sU.csv", 1),
    Scenario(3, "sparta", "biflow_sparta.csv", 1),
    Scenario(4, "mqtt_bruteforce", "biflow_mqtt_bruteforce.csv", 1),
)


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _class_counts(values: pd.Series | np.ndarray) -> dict[str, int]:
    series = pd.Series(values)
    counts = series.value_counts().sort_index()
    return {
        scenario.class_name: int(counts.get(scenario.class_id, 0))
        for scenario in SCENARIOS
    }


def _validate_schema(frame: pd.DataFrame, path: Path) -> None:
    actual = tuple(frame.columns)
    missing = [column for column in EXPECTED_COLUMNS if column not in actual]
    unexpected = [column for column in actual if column not in EXPECTED_COLUMNS]
    if missing or unexpected:
        raise ValueError(
            f"Schema mismatch in {path.name}: missing={missing}, "
            f"unexpected={unexpected}"
        )


def describe_feature(name: str, dtype: str) -> dict[str, str]:
    if name == "prt_src":
        return {
            "name": name,
            "dtype": dtype,
            "semantic_type": "discrete identifier-like numeric",
            "meaning": "source transport-layer port",
        }
    if name == "prt_dst":
        return {
            "name": name,
            "dtype": dtype,
            "semantic_type": "discrete identifier-like numeric",
            "meaning": "destination transport-layer port",
        }

    direction, metric = name.split("_", maxsplit=1)
    semantic_type, meaning = METRIC_DESCRIPTIONS[metric]
    direction_name = "forward" if direction == "fwd" else "backward"
    return {
        "name": name,
        "dtype": dtype,
        "semantic_type": semantic_type,
        "meaning": f"{direction_name} flow {meaning}",
    }

    labels = set(frame["is_attack"].dropna().unique().tolist())
    if not labels.issubset({0, 1}):
        raise ValueError(
            f"{path.name} contains unexpected is_attack values: {sorted(labels)}"
        )


def prepare_dataset(
    input_dir: Path,
    *,
    test_size: float = 0.25,
    random_state: int = 42,
    drop_constant_features: bool = True,
) -> tuple[pd.DataFrame, pd.DataFrame, pd.Series, pd.Series, dict[str, Any]]:
    """Load, validate, clean, deduplicate, and stratify the five Bi-flow files."""
    if not 0 < test_size < 1:
        raise ValueError("test_size must be between 0 and 1")

    selected_frames: list[pd.DataFrame] = []
    input_records: list[dict[str, Any]] = []

    for scenario in SCENARIOS:
        path = input_dir / scenario.filename
        if not path.is_file():
            raise FileNotFoundError(f"Required dataset file not found: {path}")

        frame = pd.read_csv(path)
        _validate_schema(frame, path)
        selected = frame.loc[frame["is_attack"].eq(scenario.selected_is_attack)].copy()
        if selected.empty:
            raise ValueError(
                f"{path.name} has no rows where is_attack={scenario.selected_is_attack}"
            )

        selected["target"] = scenario.class_id
        selected_frames.append(selected)
        input_records.append(
            {
                "filename": scenario.filename,
                "sha256": sha256_file(path),
                "raw_rows": int(len(frame)),
                "selected_rows": int(len(selected)),
                "excluded_background_rows": int(len(frame) - len(selected)),
                "selected_is_attack": scenario.selected_is_attack,
                "assigned_class_id": scenario.class_id,
                "assigned_class_name": scenario.class_name,
            }
        )

    combined = pd.concat(selected_frames, ignore_index=True)
    candidate_features = combined.drop(columns=[*DROP_FOR_MODELING, "target"])
    non_numeric = candidate_features.select_dtypes(exclude=[np.number]).columns.tolist()
    if non_numeric:
        raise ValueError(f"Unexpected non-numeric model features: {non_numeric}")

    missing_cells = int(candidate_features.isna().sum().sum())
    infinite_cells = int(
        np.isinf(candidate_features.to_numpy(dtype=np.float64, copy=False)).sum()
    )
    if missing_cells or infinite_cells:
        raise ValueError(
            "Model features contain invalid values; no undocumented imputation is "
            f"performed (missing={missing_cells}, infinite={infinite_cells})."
        )

    feature_columns = candidate_features.columns.tolist()
    before_dedup_counts = _class_counts(combined["target"])
    deduplicated = pd.concat(
        [
            combined.loc[combined["target"].eq(scenario.class_id)].drop_duplicates(
                subset=feature_columns
            )
            for scenario in SCENARIOS
        ],
        ignore_index=True,
    )
    after_dedup_counts = _class_counts(deduplicated["target"])

    cross_class_collisions = deduplicated.duplicated(
        subset=feature_columns, keep=False
    )
    if cross_class_collisions.any():
        raise ValueError(
            "Identical feature vectors occur under different class labels; resolve "
            "the label conflict before modeling."
        )

    X = deduplicated.loc[:, feature_columns].copy()
    y = deduplicated["target"].astype("int64")
    constant_features = [
        column for column in X.columns if X[column].nunique(dropna=False) <= 1
    ]
    if drop_constant_features:
        X = X.drop(columns=constant_features)

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=test_size,
        random_state=random_state,
        stratify=y,
    )

    X_train = X_train.reset_index(drop=True)
    X_test = X_test.reset_index(drop=True)
    y_train = y_train.reset_index(drop=True)
    y_test = y_test.reset_index(drop=True)

    metadata: dict[str, Any] = {
        "dataset": "MQTT-IoT-IDS2020 Bi-flow",
        "task": "five-class multiclass intrusion classification",
        "class_mapping": {
            str(scenario.class_id): scenario.class_name for scenario in SCENARIOS
        },
        "input_files": input_records,
        "raw_rows_total": int(sum(record["raw_rows"] for record in input_records)),
        "selected_rows_total": int(len(combined)),
        "rows_before_deduplication_by_class": before_dedup_counts,
        "rows_after_deduplication_by_class": after_dedup_counts,
        "duplicates_removed_by_class": {
            name: before_dedup_counts[name] - after_dedup_counts[name]
            for name in before_dedup_counts
        },
        "prepared_rows_total": int(len(X)),
        "train_rows": int(len(X_train)),
        "test_rows": int(len(X_test)),
        "train_class_counts": _class_counts(y_train),
        "test_class_counts": _class_counts(y_test),
        "test_size": test_size,
        "random_state": random_state,
        "stratified_split": True,
        "dropped_identifier_or_leakage_columns": list(DROP_FOR_MODELING),
        "constant_features_detected": constant_features,
        "constant_features_dropped": constant_features if drop_constant_features else [],
        "feature_count": int(X.shape[1]),
        "feature_names": X.columns.tolist(),
        "feature_dtypes": {name: str(dtype) for name, dtype in X.dtypes.items()},
        "feature_schema": [
            describe_feature(name, str(X.dtypes[name])) for name in X.columns
        ],
        "missing_feature_cells": missing_cells,
        "infinite_feature_cells": infinite_cells,
        "cross_class_feature_collisions": 0,
        "categorical_encoding": "not required; all retained features are numeric",
        "scaling": "not applied; Random Forest is invariant to monotonic feature scaling",
    }
    return X_train, X_test, y_train, y_test, metadata


def write_outputs(
    output_dir: Path,
    X_train: pd.DataFrame,
    X_test: pd.DataFrame,
    y_train: pd.Series,
    y_test: pd.Series,
    metadata: dict[str, Any],
    *,
    write_csv: bool = True,
) -> list[Path]:
    """Write a compact NumPy bundle, metadata, and optionally four CSV files."""
    output_dir.mkdir(parents=True, exist_ok=True)
    created: list[Path] = []

    bundle_path = output_dir / "mqtt_iot_ids2020_biflow_split.npz"
    np.savez_compressed(
        bundle_path,
        X_train=X_train.to_numpy(dtype=np.float64),
        X_test=X_test.to_numpy(dtype=np.float64),
        y_train=y_train.to_numpy(dtype=np.int64),
        y_test=y_test.to_numpy(dtype=np.int64),
        feature_names=np.asarray(X_train.columns, dtype=str),
        class_names=np.asarray(
            [scenario.class_name for scenario in SCENARIOS], dtype=str
        ),
    )
    created.append(bundle_path)

    metadata_path = output_dir / "preprocessing_metadata.json"
    metadata_path.write_text(
        json.dumps(metadata, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    created.append(metadata_path)

    if write_csv:
        csv_outputs = (
            (output_dir / "X_train.csv.gz", X_train),
            (output_dir / "X_test.csv.gz", X_test),
            (output_dir / "y_train.csv.gz", y_train.rename("target").to_frame()),
            (output_dir / "y_test.csv.gz", y_test.rename("target").to_frame()),
        )
        for path, frame in csv_outputs:
            frame.to_csv(path, index=False, compression="gzip")
            created.append(path)

    return created


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--input-dir",
        type=Path,
        default=Path("data/raw/kaggle-replication"),
        help="Directory containing the five biflow_*.csv files",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=Path("data/processed"),
        help="Directory for ignored, generated model-ready files",
    )
    parser.add_argument("--test-size", type=float, default=0.25)
    parser.add_argument("--random-state", type=int, default=42)
    parser.add_argument(
        "--keep-constant-features",
        action="store_true",
        help="Retain zero-variance columns for strict 28-feature comparison",
    )
    parser.add_argument(
        "--no-csv",
        action="store_true",
        help="Write only the compact NPZ bundle and JSON metadata",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    X_train, X_test, y_train, y_test, metadata = prepare_dataset(
        args.input_dir,
        test_size=args.test_size,
        random_state=args.random_state,
        drop_constant_features=not args.keep_constant_features,
    )
    paths = write_outputs(
        args.output_dir,
        X_train,
        X_test,
        y_train,
        y_test,
        metadata,
        write_csv=not args.no_csv,
    )

    print("Prepared MQTT-IoT-IDS2020 Bi-flow dataset")
    print(f"  train: {len(X_train):,} rows x {X_train.shape[1]} features")
    print(f"  test:  {len(X_test):,} rows x {X_test.shape[1]} features")
    print(f"  train classes: {metadata['train_class_counts']}")
    print(f"  test classes:  {metadata['test_class_counts']}")
    print("  created:")
    for path in paths:
        print(f"    {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
