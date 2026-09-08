# Source Code

This folder contains reusable Python scripts for:

- Loading the dataset
- Cleaning and preprocessing data
- Training the selected model
- Calculating evaluation metrics
- Producing results and comparison tables

## Available workflow

Run `python src/preprocess_dataset.py` from the repository root to validate,
clean, deduplicate, and split the five MQTT-IoT-IDS2020 Bi-flow CSVs. See
`docs/preprocessing.md` for inputs, decisions, outputs, and the model handoff.
