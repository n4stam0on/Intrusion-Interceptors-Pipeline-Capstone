# Dataset Information

This project uses the MQTT-IoT-IDS2020 Bi-flow CSV dataset.

## Data Storage

The complete dataset will not be uploaded to GitHub because of its size. Team members will store the complete CSV files locally inside a `data/raw` folder.

A small sample may be added to the repository after the team verifies the
dataset's license and usage terms. Generated train/test artifacts are written to
`data/processed/`; both raw and processed data are intentionally ignored by Git.

## Local layout

```text
data/
  raw/kaggle-replication/   # five biflow_*.csv source files
  processed/                # generated X/y train/test artifacts and metadata
```

Run `python src/preprocess_dataset.py` to build the processed files. The exact
workflow and target mapping are documented in `docs/preprocessing.md`.
