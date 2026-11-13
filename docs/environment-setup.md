# Python Environment and Project Setup

Owner: Nastassja Monreal (documentation coordination)  
Related issues: #6, #19, #27, #32

## Supported baseline

Use Python 3.11 for the combined preprocessing, Random Forest, SHAP, and LIME workflow. The model branch was clean-environment tested with Python 3.11.9; the data-verification branch was also tested with Python 3.12. Record any additional version that the team verifies.

At the time of this guide, final data verification is under review in PR #46 and the model/explainability work is under review in PR #45. Commands for files introduced by those PRs require the relevant branch or merged changes.

## 1. Clone and enter the repository

```powershell
git clone https://github.com/n4stam0on/Intrusion-Interceptors-Pipeline-Capstone.git
cd Intrusion-Interceptors-Pipeline-Capstone
```

## 2. Create an isolated environment

Windows PowerShell:

```powershell
py -3.11 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
```

macOS or Linux:

```bash
python3.11 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
```

## 3. Install dependencies

For the current main branch:

```powershell
python -m pip install -r Requirements.txt
python -m pip check
```

After PR #45 is available, prefer the fully pinned environment:

```powershell
python -m pip install -r requirements-lock.txt
python -m pip check
```

Do not commit `.venv/` or credentials.

## 4. Add the Bi-flow data locally

Download MQTT-IoT-IDS2020 from the verified source described in [dataset-and-access.md](dataset-and-access.md). Place only these five files under `data/raw/kaggle-replication/`:

- `biflow_normal.csv`
- `biflow_scan_A.csv`
- `biflow_scan_sU.csv`
- `biflow_sparta.csv`
- `biflow_mqtt_bruteforce.csv`

Raw and processed datasets are intentionally ignored by Git.

## 5. Inspect and preprocess

```powershell
python src/inspect_dataset.py data/raw/kaggle-replication/biflow_normal.csv --label is_attack --full
python src/preprocess_dataset.py --input-dir data/raw/kaggle-replication
```

Repeat inspection for all five files. The current baseline should produce 95,120 training rows, 23,781 testing rows, and 27 features.

After PR #46 is available, run its verifier and tests as documented in that PR. Save generated evidence under the documented results directory; do not commit raw CSVs.

## 6. Train and explain the model

After PR #45 is available, run the Random Forest, SHAP, and LIME entry points documented by that PR. Confirm that inputs are the generated Bi-flow train/test files and that the reported model is Random Forest, not Linear SVM.

The paper comparison is 99.99% for Random Forest Bi-flow in Table 2. The current team reproduction under review reports 99.9411%; do not relabel that number as the paper's result.

## 7. Run tests

```powershellpython -m unittest discover -s tests -v
```

If a command is unavailable, first confirm that the branch or PR containing it is checked out. If imports fail, confirm the virtual environment is active and rerun dependency installation.

## Clean-checkout evidence for issue #19

A teammate other than the author should record:

- operating system and Python version;
- dependency file used and `pip check` result;
- preprocessing row/feature counts;
- test result;
- model command and output, when PR #45 is available;
- any deviation or troubleshooting step.

Issue #19 should remain open until this independent clean-checkout test is attached or linked.
