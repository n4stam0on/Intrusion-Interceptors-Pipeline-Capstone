# Dataset demonstration and verification

Owner: Kien Nguyen. Supports #21, #23, #31, #32, #39, and #40.

## Fresh checkout on Windows (PowerShell)

Use Python 3.12. The five CSV files must be obtained separately using the source
information in `data/README.md` and checked against `docs/dataset-verification.md`.
The current `Requirements.txt` is unpinned; the additional data constraints fix
the three packages that control parsing and splitting. Reports record the
versions actually tested. This command sequence is supplied for #19,
whose coordinator-owned setup guide is still pending.

```powershell
git clone https://github.com/n4stam0on/Intrusion-Interceptors-Pipeline-Capstone.git
Set-Location Intrusion-Interceptors-Pipeline-Capstone
# Until this verification PR is merged, fetch and check out its review branch:
git fetch origin mvpmvp/final-data-verification
git switch mvpmvp/final-data-verification
py -3.12 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r Requirements.txt -c requirements-data-verification.txt
.\.venv\Scripts\python.exe -m unittest discover -s tests -v
```

Place only the five `biflow_*.csv` files in `data/raw/kaggle-replication/`.
Use `--input-dir data/raw` instead if they are directly in `data/raw/`.

```powershell
$files = @('biflow_normal.csv','biflow_scan_A.csv','biflow_scan_sU.csv','biflow_sparta.csv','biflow_mqtt_bruteforce.csv')
foreach ($file in $files) {
  .\.venv\Scripts\python.exe src/inspect_dataset.py "data/raw/kaggle-replication/$file" --label is_attack --full
  if ($LASTEXITCODE -ne 0) { throw "Loading failed: $file" }
}
.\.venv\Scripts\python.exe src/verify_prepared_data.py --input-dir data/raw/kaggle-replication
```

The verifier rebuilds the approved baseline twice, checks input checksums,
feature/target separation, labels, finite values, exact array equality, CSV
round-trip, and absence of duplicate feature vectors within/across partitions.
It records hashes of logical arrays, which exclude ZIP/gzip timestamps.
Do not compare archive byte hashes as a substitute for comparing array contents.

Generated data is ignored under `data/processed/verification/run1` and `run2`.
`results/data-verification.json` is compact evidence, not a replacement for running
the pipeline. A teammate should run these commands and compare the report's
`logical_array_sha256` fields before independent verification is marked complete.

For the model's default input path, run:

```powershell
.\.venv\Scripts\python.exe src/preprocess_dataset.py --input-dir data/raw/kaggle-replication
```

## Two-minute speaking outline

1. Show the five Bi-flow filenames. Explain that packet and Uni-flow files are
   excluded. Raw inspection gives 259,379 rows and 32 columns per file.
2. Explain the five-class target: keep normal rows from the normal file and
   attack rows from each attack scenario, then assign the scenario class.
3. Explain the row reduction: 157,009 selected rows become 118,901 unique feature
   records. IP/protocol fields and the binary answer are excluded; one constant
   field is dropped. These are documented baseline decisions.
4. Run the preprocessing/verification command. Show 95,120 training rows and
   23,781 testing rows, 27 features, seed 42, and stratification.
5. Explain that removing `is_attack` prevents exposing the answer and deduplicating
   before splitting prevents identical feature rows crossing train/test. These
   checks do not establish generalization to new devices, capture sessions, or
   networks. Capture/time-based validation remains a separate experiment.
6. Show the report's PASS result and class counts; pass the demonstration to the
   model lead. If execution fails, use the checked-in report as backup evidence
   and clearly say it is saved output. A full clean-checkout video is still
   required for the final presentation.

## Method decisions still awaiting sign-off

The paper describes IP label encoding and Min-Max scaling. The approved merged
baseline excludes IP fields and uses numeric features without scaling. Seed 42,
stratification, duplicate removal, protocol removal, and constant-feature removal
are team decisions. The 80/20 ratio is specified in Section 4 of XMID-MQTT.
Record final acceptance or add a separate paper-aligned configuration under
#20/#22; do not describe this baseline as an exact reproduction of all methods.

## Wiki review (November 5, 2026)

Reviewed `Dataset-and-Access` and `Reproduction-Method` from Wiki commit
`09cf19fd82a15be38eff754f2cd0d1948fcf4ba0`. The first page still lists the
source, target, labels, and verification as pending although merged code and
dataset evidence exist. The second still incorrectly compares Random Forest
with 99.16%; correct it to 99.99% in Table 2, record the 80/20 split, seed 42,
27 features, class mapping, and the deviations above. Final documentation
approval remains pending these corrections. This review supports #39 without
claiming the Wiki is already accurate.

## Environment comparison

The first environment used NumPy 2.5.2, pandas 3.0.5, and scikit-learn 1.9.0.
A fresh unpinned install resolved to 2.5.4, 3.1.1, and 1.9.1. Labels, feature
names, and split assignments matched, but 514,047 training cells and 128,344 test
cells differed by at most 9.094947017729282e-13. That difference is numerically
tiny but invalidates a claim of bit-identical output hashes. The added constraints
provide an explicit baseline environment. The fresh constrained run matched all
six logical array hashes from the original environment exactly (41.374 seconds,
installation excluded); all six tests passed in that environment. See
`results/data-verification-pinned.json`. These are data-path constraints, not a complete
lockfile for SHAP/LIME and all transitive/model dependencies.
