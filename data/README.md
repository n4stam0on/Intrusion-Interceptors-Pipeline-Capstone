# Dataset Information

This project will use the bidirectional-flow (Bi-flow) CSV representation of
the MQTT-IoT-IDS2020 dataset.

The official dataset record is maintained by the University of Strathclyde and
points to the IEEE DataPort deposit:

- Dataset record: https://pureportal.strath.ac.uk/en/datasets/mqtt-iot-ids2020-mqtt-internet-of-things-intrusion-detection-data/
- Dataset DOI: https://doi.org/10.21227/bhxy-ep04
- Licence: Creative Commons Attribution 4.0 International (CC BY 4.0)
- Selected download: `biflow_features.zip` (14.56 MB)

The dataset authors' companion code expects these extracted files:

- `biflow_normal.csv`
- `biflow_scan_A.csv`
- `biflow_scan_sU.csv`
- `biflow_sparta.csv`
- `biflow_mqtt_bruteforce.csv`

Companion code: https://github.com/AbertayMachineLearningGroup/MQTT_ML

The team also provided this Kaggle replication for local testing:

- https://www.kaggle.com/datasets/ogunyemioluwapelumi/mqtt-iot-ids2020-private

Kaggle reports the replication's licence as unknown. Use the official IEEE
DataPort record for provenance and licensing, and verify the replication
against the official archive before final experiments.

## Data Storage

The complete dataset will not be uploaded to GitHub because of its size. Team members will store the complete CSV files locally inside a `data/raw` folder.

A small sample may be added to the repository after the team verifies the dataset's license and usage terms

## Information to Confirm

- SHA-256 checksum of the downloaded archive
- Extracted file sizes
- Number of Rows and Columns
- Whether the CSVs contain a multiclass target column or require labels to be
  assigned from their scenario filenames
