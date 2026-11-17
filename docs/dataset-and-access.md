# Dataset and Access

Owner: Nastassja Monreal (documentation coordination)  
Related issues: #1, #18, #21, #31, #37

## Approved dataset scope

- **Paper:** XMID-MQTT
- **Dataset:** MQTT-IoT-IDS2020
- **Representation:** Bi-flow (bidirectional flow)
- **Task:** five-class intrusion detection
- **Model:** Random Forest
- **Paper comparison:** 99.99% Random Forest Bi-flow accuracy in Table 2

The 99.16% Bi-flow value in Table 3 belongs to Linear SVM. UNSW-NB15, Packet, and Uni-flow data are outside the approved experiment.

## Official source and access record

- University of Strathclyde record: https://pureportal.strath.ac.uk/en/datasets/mqtt-iot-ids2020-mqtt-internet-of-things-intrusion-detection-data/
- IEEE DataPort DOI: https://doi.org/10.21227/bhxy-ep04
- Dataset authors' companion code: https://github.com/AbertayMachineLearningGroup/MQTT_ML
- License recorded by the official record: CC BY 4.0
- Team mirror used for the verified local replication: https://www.kaggle.com/datasets/ogunyemioluwapelumi/mqtt-iot-ids2020-private

The official source remains authoritative for provenance and licensing. A mirror must not be treated as a different dataset merely because it is hosted elsewhere, and its files must be checked against the documented inventory and hashes.

## Required Bi-flow files

Place these files in `data/raw/kaggle-replication/`:

| File | Selected traffic | Multiclass label |
|---|---|---|
| `biflow_normal.csv` | `is_attack == 0` | normal |
| `biflow_scan_A.csv` | `is_attack == 1` | scan_A |
| `biflow_scan_sU.csv` | `is_attack == 1` | scan_sU |
| `biflow_sparta.csv` | `is_attack == 1` | sparta |
| `biflow_mqtt_bruteforce.csv` | `is_attack == 1` | mqtt_bruteforce |

Background normal rows inside attack captures are excluded. The binary `is_attack` field is used to select rows and is then removed from model features to prevent target leakage.

## Verified inventory

All five files have 32 columns and contain 259,379 raw rows in total. Scenario selection produces 157,009 rows. After the documented identifier removal and within-class feature deduplication, 118,901 labeled records remain.

| File | Raw rows | Selected rows | SHA-256 |
|---|---:|---:|---|
| `biflow_normal.csv` | 86,008 | 86,008 | `901bd9f475d9dd817017091caaec4a865bf654250baf4f2f54877b32b647db44` |
| `biflow_scan_A.csv` | 25,693 | 19,907 | `62de3d0c8478dd0774d0ffd7bba2c441c13ccfb2a4f7b17a0daaf6bc6091e361` |
| `biflow_scan_sU.csv` | 39,664 | 22,434 | `91047fd6072ab980b418ee28fcedc03b3eb8fbcf17426c080760aba3503bcff7` |
| `biflow_sparta.csv` | 91,318 | 14,116 | `9e3037f79c87e922b9cdf62125b9ec4db81b670b6bff6706385bd312becac976` |
| `biflow_mqtt_bruteforce.csv` | 16,696 | 14,544 | `790087e79e9d22f741ef06f1db3aed346a7a4980633e5c0619ae2c8a15ca4256` |

These hashes identify the team-verified replication files. Equivalence to a newly downloaded official archive should be checked separately if that archive becomes available.

## Storage rules

- Raw CSVs stay under `data/raw/` and are ignored by Git.
- Generated split files stay under `data/processed/` and are ignored by Git.
- Do not commit the complete dataset.
- Do not place absolute, user-specific paths in instructions or evidence.

## Verification

From the repository root:

```powershell
python src/inspect_dataset.py data/raw/kaggle-replication/biflow_normal.csv --label is_attack --full
python src/preprocess_dataset.py --input-dir data/raw/kaggle-replication
```

Repeat the inspection command for all five files. The preprocessing run should produce 95,120 training rows, 23,781 testing rows, and 27 features using the current baseline configuration.

## Evidence

- Loading script: [src/inspect_dataset.py](../src/inspect_dataset.py)
- Preprocessing script: [src/preprocess_dataset.py](../src/preprocess_dataset.py)
- Detailed verification: [dataset-verification.md](dataset-verification.md)
- Preprocessing record: [preprocessing.md](preprocessing.md)
- Loading implementation: PR #5
- Data-preparation implementation: PR #16
- Final data verification under review: PR #46
