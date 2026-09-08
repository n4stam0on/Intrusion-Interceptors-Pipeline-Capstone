# Dataset Verification

Owner: `mvpmvpmvpmvpmvp`

Status: **Dataset selected; real-data loading evidence is pending.**

The team selected the MQTT-IoT-IDS2020 Bi-flow representation and the
XMID-MQTT paper on September 8, 2026. Before the numerical target is frozen,
the team must resolve the model/metric discrepancy recorded below.

## Decision Record

- Final dataset: MQTT-IoT-IDS2020, bidirectional-flow (Bi-flow) representation
- Date confirmed by team: September 8, 2026
- Selected research paper: *XMID-MQTT: explaining machine learning-based intrusion detection system for MQTT protocol in IoT environment*
- Paper DOI: https://doi.org/10.1007/s10207-025-01036-w
- Numerical target: **Team confirmation required.** The team message names
  99.16% Random Forest accuracy, but the paper reports 99.99% Random Forest
  Bi-flow accuracy in Table 2 and 99.16% Linear SVM Bi-flow accuracy in Table 3.
- Paper table or figure: Table 2 (Random Forest) or Table 3 (Linear SVM), after
  the team confirms which result it intends to reproduce

## Official Dataset Source

- Publisher/maintainer: IEEE DataPort; dataset record maintained by the
  University of Strathclyde
- Official URL: https://pureportal.strath.ac.uk/en/datasets/mqtt-iot-ids2020-mqtt-internet-of-things-intrusion-detection-data/
- Dataset DOI: https://doi.org/10.21227/bhxy-ep04
- Licence or usage terms:
- Download date:
- Download size:
- File checksum (SHA-256):

Do not use a Kaggle mirror as the only source when an official source is
available.

## Selected Data Representation

- CSV filename(s):
- Feature level (packet, unidirectional flow, or bidirectional flow): Bidirectional flow
- Target/label column:
- Classification task (binary or multiclass):
- Reason this representation matches the paper:

## Loading Test

Place downloaded files under `data/raw/`. That directory is intentionally
excluded from Git.

Install dependencies:

```bash
python -m pip install -r Requirements.txt
```

Run a 100,000-row smoke test:

```bash
python src/inspect_dataset.py data/raw/FILE.csv --label LABEL_COLUMN
```

After the smoke test succeeds, audit the complete file if the computer has
enough memory:

```bash
python src/inspect_dataset.py data/raw/FILE.csv --label LABEL_COLUMN --full
```

## Verified Results

- Rows loaded:
- Number of columns:
- Class names and counts:
- Missing values:
- Duplicate rows:
- Notes about class imbalance:
- Hardware used:
- Approximate runtime:

Paste or link the saved command output here. Every number in the proposal and
final report should trace back to a reproducible command in the repository.

## Clean-Checkout Verification

- [ ] Clone the repository into a new directory.
- [ ] Install dependencies from `Requirements.txt`.
- [ ] Obtain the data using only the instructions above.
- [ ] Run the inspection command successfully.
- [ ] Confirm no complete dataset files are tracked by Git.
