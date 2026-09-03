# Dataset Verification

Owner: `mvpmvpmvpmvpmvp`

Status: **Blocked until the team confirms one dataset and one research paper.**

The repository currently names UNSW-NB15, while the team discussion names
MQTT-IoT-IDS2020. This page must describe the dataset used by the
instructor-approved paper.

## Decision Record

- Final dataset:
- Date approved by team:
- Approved research paper:
- Exact result to reproduce:
- Paper table or figure:

## Official Dataset Source

- Publisher/maintainer:
- Official URL:
- Licence or usage terms:
- Download date:
- Download size:
- File checksum (SHA-256):

Do not use a Kaggle mirror as the only source when an official source is
available.

## Selected Data Representation

- CSV filename(s):
- Feature level (packet, unidirectional flow, or bidirectional flow):
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
