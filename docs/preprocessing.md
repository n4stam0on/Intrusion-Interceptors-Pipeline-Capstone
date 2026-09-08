# MQTT-IoT-IDS2020 Bi-flow preprocessing

This workflow turns the five raw Bi-flow CSV files into deterministic,
model-ready training and testing data for the Random Forest experiment in
Issue #14.

## Input files and target classes

Place these files in `data/raw/kaggle-replication/`:

| File | Rows selected | Multiclass target |
|---|---:|---:|
| `biflow_normal.csv` | `is_attack == 0` | `0` (`normal`) |
| `biflow_scan_A.csv` | `is_attack == 1` | `1` (`scan_A`) |
| `biflow_scan_sU.csv` | `is_attack == 1` | `2` (`scan_sU`) |
| `biflow_sparta.csv` | `is_attack == 1` | `3` (`sparta`) |
| `biflow_mqtt_bruteforce.csv` | `is_attack == 1` | `4` (`mqtt_bruteforce`) |

The class construction follows the MQTT-IoT-IDS2020 authors' companion code:
normal traffic comes from the normal capture and attack rows come from the four
attack captures. Background normal rows inside attack captures are excluded.

## Cleaning and leakage controls

The script performs the following checks and transformations in order:

1. Requires all five files and validates the expected 32-column schema.
2. Records each source file's SHA-256 hash and raw/selected row counts.
3. Rejects unexpected labels, non-numeric model features, missing values, and
   infinite values instead of silently inventing imputations.
4. Removes `ip_src` and `ip_dst`, which are capture-specific identifiers.
5. Removes `proto` to match the authors' Bi-flow feature selection.
6. Removes `is_attack`, because keeping the binary answer in the feature matrix
   would leak the target into the multiclass model.
7. Removes exact duplicate feature vectors within each class before splitting,
   preventing identical examples from appearing in both train and test data.
8. Rejects any identical feature vector that has conflicting class labels.
9. Drops zero-variance features by default. In the current replication,
   `bwd_num_urg_flags` is always zero. Use `--keep-constant-features` only when a
   strict 28-feature comparison is required.
10. Creates a reproducible 75/25 stratified split with random seed 42.

No category encoding is needed after identifiers are removed: all retained
features are numeric. No scaling is applied because Random Forest decisions are
unchanged by monotonic feature scaling. Ports and packet/flag counts remain
discrete numeric values; inter-arrival-time and packet-length statistics remain
continuous values.

Feature names use these definitions:

| Name or part | Meaning | Type |
|---|---|---|
| `prt_src`, `prt_dst` | Source and destination transport-layer ports | Discrete numeric |
| `fwd_`, `bwd_` | Forward (source-to-destination) and backward flow directions | Prefix |
| `num_pkts`, `num_bytes` | Packet and byte totals | Discrete count |
| `mean_iat`, `std_iat`, `min_iat`, `max_iat` | Inter-arrival-time statistics | Continuous |
| `mean_pkt_len`, `std_pkt_len`, `min_pkt_len`, `max_pkt_len` | Packet-length statistics | Continuous |
| `num_psh_flags`, `num_rst_flags`, `num_urg_flags` | TCP flag totals | Discrete count |

`preprocessing_metadata.json` expands these rules into a meaning and semantic
type for every retained column.

## Run the workflow

From the repository root in the configured virtual environment:

```powershell
python src/preprocess_dataset.py
```

Generated files are written to ignored `data/processed/` so the full dataset is
not committed:

- `mqtt_iot_ids2020_biflow_split.npz`: compact bundle containing `X_train`,
  `X_test`, `y_train`, `y_test`, `feature_names`, and `class_names`.
- `X_train.csv.gz`, `X_test.csv.gz`, `y_train.csv.gz`, and `y_test.csv.gz`:
  compressed CSV handoff files.
- `preprocessing_metadata.json`: exact inputs, hashes, row counts, cleaning
  decisions, feature schema, class balance, and split settings.

Yassin can load the compact bundle with:

```python
import numpy as np

data = np.load("data/processed/mqtt_iot_ids2020_biflow_split.npz")
X_train, y_train = data["X_train"], data["y_train"]
X_test, y_test = data["X_test"], data["y_test"]
```

## Current audited result

The five raw files contain 259,379 rows. Class filtering selects 157,009 rows.
Deduplication after identifier removal leaves 118,901 unique labeled records.
The dataset is imbalanced, with normal traffic much larger than either scan
class; downstream evaluation should therefore report per-class precision,
recall, F1, and a confusion matrix in addition to overall accuracy.

| Class | Prepared rows | Share |
|---|---:|---:|
| Normal | 86,008 | 72.34% |
| Aggressive scan (`scan_A`) | 2,001 | 1.68% |
| UDP scan (`scan_sU`) | 2,232 | 1.88% |
| Sparta SSH brute force | 14,116 | 11.87% |
| MQTT brute force | 14,544 | 12.23% |

The 75/25 split and seed 42 are documented reproduction assumptions. If the
paper or instructor specifies a different holdout protocol, rerun the script
with `--test-size` and `--random-state` rather than editing generated files.

## Sources

- [University of Strathclyde dataset record](https://pureportal.strath.ac.uk/en/datasets/mqtt-iot-ids2020-mqtt-internet-of-things-intrusion-detection-data/)
- [IEEE DataPort DOI 10.21227/bhxy-ep04](https://doi.org/10.21227/bhxy-ep04)
- [Dataset authors' companion code](https://github.com/AbertayMachineLearningGroup/MQTT_ML)
- [Team-provided Kaggle replication](https://www.kaggle.com/datasets/ogunyemioluwapelumi/mqtt-iot-ids2020-private)
