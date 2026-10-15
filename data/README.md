# Dataset Information

This project uses the **MQTT-IoT-IDS2020** intrusion-detection dataset associated with the XMID-MQTT research paper.

The dataset provides three different feature representations:

- Packet
- Uni-flow
- Bi-flow

This project focuses exclusively on the **Bi-flow representation**. Packet and Uni-flow files are not part of the selected Random Forest reproduction experiment.

## Official Dataset Source

The XMID-MQTT paper identifies the publicly available MQTT-IoT-IDS2020 dataset as its data source:

[MQTT-IoT-IDS2020 on IEEE DataPort](https://ieee-dataport.org/open-access/mqtt-iot-ids2020-mqtt-internet-things-intrusion-detection-dataset)

Any mirror used by the team must be checked against the official dataset structure before it is accepted.

## Expected Bi-flow Files

The selected Bi-flow data should contain traffic representing the following classes:

- Normal traffic
- MQTT brute-force attack
- Scan A attack
- Scan sU attack
- Sparta attack

The expected CSV filenames are:

```text
biflow_normal.csv
biflow_mqtt_bruteforce.csv
biflow_scan_A.csv
biflow_scan_sU.csv
biflow_sparta.csv
```

If the downloaded files use different names, the team must document how each file maps to the expected class before using it.

## Data Storage

The complete dataset will not be committed to GitHub because of its size and to avoid redistributing files before confirming the applicable license and usage terms.

Team members will store the required Bi-flow CSV files locally in:

```text
data/raw/
```

The expected structure is:

```text
data/
├── README.md
├── raw/
│   ├── biflow_normal.csv
│   ├── biflow_mqtt_bruteforce.csv
│   ├── biflow_scan_A.csv
│   ├── biflow_scan_sU.csv
│   └── biflow_sparta.csv
└── processed/
```

The `data/raw/` directory contains the original downloaded files. The `data/processed/` directory is reserved for reproducible outputs created by the project’s preprocessing code.

Dataset files should remain excluded from version control through `.gitignore`.

## Training and Testing Split

The downloaded Bi-flow files are organized by traffic or attack category rather than as the team’s final training and testing sets.

The project will create a reproducible **80/20 train-test split** during preprocessing.

The team must document:

- The random seed
- Whether stratification was used
- Training and testing dimensions
- Class counts in both sets
- How preprocessing was prevented from learning from the test set
- Whether duplicate records appear across the two sets

XMID-MQTT Section 4 (page 6) explicitly specifies the 80/20 split. The random
seed and stratification remain team implementation decisions.

## Dataset Verification Checklist

Before model training, the team must confirm:

- [ ] The files belong to MQTT-IoT-IDS2020.
- [ ] Only the Bi-flow representation is being used.
- [ ] All five expected traffic categories are available.
- [ ] Packet and Uni-flow files are excluded.
- [ ] The official dataset source or verified mirror is documented.
- [ ] The dataset license and usage terms have been reviewed.
- [ ] File sizes are recorded.
- [ ] Row and column counts are recorded.
- [ ] Column names and data types are recorded.
- [ ] The target column is identified.
- [ ] Label values and meanings are documented.
- [ ] Missing values are counted.
- [ ] Duplicate records are counted.
- [ ] Possible leakage or identifier columns are reviewed.
- [ ] Every removed column has a documented reason.
- [ ] The 80/20 split and random seed are documented.

## Reproduction Scope

The dataset connects to the project experiment as follows:

```text
XMID-MQTT paper
→ MQTT-IoT-IDS2020 dataset
→ Bi-flow representation
→ preprocessing
→ reproducible 80/20 split
→ Random Forest classifier
→ evaluation
→ comparison with Table 2’s 99.99% accuracy
→ SHAP and LIME explanations
```

The **99.16% Bi-flow result in Table 3 belongs to Linear SVM** and is not the primary Random Forest reproduction target.

## Recorded Loading Evidence

See [dataset verification](../docs/dataset-verification.md) for the official
record, replication source, file sizes, row counts, binary labels, missing-value
and duplicate summaries, SHA-256 checksums, and reproducible inspection commands.
Official-archive equivalence and teammate verification remain pending.
