# Dataset Verification

Owner: `mvpmvpmvpmvpmvp`

Status: **Real-data loading completed on the team-provided Kaggle replication;
official-archive equivalence and clean-checkout verification remain pending.**

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
- Licence or usage terms: CC BY 4.0
- Download date: September 8, 2026
- Download archive: `biflow_features.zip`
- Published download size: 14.56 MB
- Local test source: https://www.kaggle.com/datasets/ogunyemioluwapelumi/mqtt-iot-ids2020-private
- Replication note: Kaggle reports 71,971,636 total extracted bytes and an
  unknown licence. Use the official IEEE DataPort record for licensing and
  verify file equivalence before final experiments.
- Archive checksum (SHA-256): Pending official archive download

Do not use a Kaggle mirror as the only source when an official source is
available.

## Selected Data Representation

- Expected CSV filename(s): `biflow_normal.csv`, `biflow_scan_A.csv`,
  `biflow_scan_sU.csv`, `biflow_sparta.csv`, and
  `biflow_mqtt_bruteforce.csv`
- Feature level (packet, unidirectional flow, or bidirectional flow): Bidirectional flow
- Target/label definition: Every CSV contains the binary `is_attack` column.
  The dataset authors' companion code keeps `is_attack == 0` from the normal
  file, keeps `is_attack == 1` from each attack file, and assigns the multiclass
  label from the scenario filename. Drop `is_attack` from model features after
  filtering so the target cannot leak into training.
- Classification task (binary or multiclass): Multiclass: normal, aggressive
  scan, UDP scan, Sparta SSH brute force, and MQTT brute force
- Reason this representation matches the paper: XMID-MQTT reports separate
  results for the Bi-flow representation and the same five traffic classes.

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

If the Bi-flow CSV has no multiclass label column, omit `--label` for the first
schema inspection. Inspect all five scenario files and document the verified
file-to-class mapping before combining them for modeling.

After the smoke test succeeds, audit the complete file if the computer has
enough memory:

```bash
python src/inspect_dataset.py data/raw/FILE.csv --label LABEL_COLUMN --full
```

## Verified Results

All five replicated CSVs were loaded in full with `src/inspect_dataset.py` on
September 8, 2026.

| File | Bytes | Rows | `is_attack=0` | `is_attack=1` | Paper-selected rows |
|---|---:|---:|---:|---:|---:|
| `biflow_normal.csv` | 26,444,796 | 86,008 | 86,008 | 0 | 86,008 |
| `biflow_scan_A.csv` | 4,342,749 | 25,693 | 5,786 | 19,907 | 19,907 |
| `biflow_scan_sU.csv` | 8,207,177 | 39,664 | 17,230 | 22,434 | 22,434 |
| `biflow_sparta.csv` | 28,301,124 | 91,318 | 77,202 | 14,116 | 14,116 |
| `biflow_mqtt_bruteforce.csv` | 4,675,790 | 16,696 | 2,152 | 14,544 | 14,544 |
| **Total** | **71,971,636** | **259,379** | **188,378** | **71,001** | **157,009** |

- Columns: 32 in every file, with a consistent schema
- Missing cells: 0
- Exact duplicate raw rows: 0
- Paper-selected multiclass counts before feature deduplication: normal 86,008;
  aggressive scan 19,907; UDP scan 22,434; Sparta 14,116; MQTT brute force
  14,544
- Unique paper-selected rows after dropping `proto`, `ip_src`, and `ip_dst`, as
  done by the authors' companion code: normal 86,008; aggressive scan 2,001;
  UDP scan 2,232; Sparta 14,116; MQTT brute force 14,544
- Class-balance note: preprocessing and feature deduplication greatly reduce
  both scan classes. The split must be documented and stratified.
- Hardware: Windows 11 Home, AMD Ryzen 5 5500U, 5.9 GB usable RAM
- Full five-file inspection runtime: approximately 15 seconds

### Per-file SHA-256

- `biflow_normal.csv`: `901bd9f475d9dd817017091caaec4a865bf654250baf4f2f54877b32b647db44`
- `biflow_scan_A.csv`: `62de3d0c8478dd0774d0ffd7bba2c441c13ccfb2a4f7b17a0daaf6bc6091e361`
- `biflow_scan_sU.csv`: `91047fd6072ab980b418ee28fcedc03b3eb8fbcf17426c080760aba3503bcff7`
- `biflow_sparta.csv`: `9e3037f79c87e922b9cdf62125b9ec4db81b670b6bff6706385bd312becac976`
- `biflow_mqtt_bruteforce.csv`: `790087e79e9d22f741ef06f1db3aed346a7a4980633e5c0619ae2c8a15ca4256`

Every number in the proposal and final report should trace back to a
reproducible command in the repository.

## Clean-Checkout Verification

- [ ] Clone the repository into a new directory.
- [ ] Install dependencies from `Requirements.txt`.
- [ ] Obtain the data using only the instructions above.
- [x] Run the inspection command successfully.
- [x] Confirm no complete dataset files are tracked by Git.
