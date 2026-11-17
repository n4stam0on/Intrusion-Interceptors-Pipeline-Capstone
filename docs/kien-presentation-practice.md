# Kien's dataset and preprocessing presentation

Prepared November 17, 2026. Five main slides plus two hidden backup slides.
Target: about **2 minutes 35 seconds to 3 minutes**, without the optional live run.
Timings are a practice target, not a recorded rehearsal. Keep the backup slides
hidden when merging into the team deck. The opening slide can become a section
divider if the team already has a cover.

## Slide 1: Dataset and preprocessing (about 20 seconds)

“My part is preparing the MQTT-IoT-IDS2020 Bi-flow data for our Random Forest
model. Bi-flow summarizes traffic in both directions. I verify the files,
construct the class labels, clean the features, and create a repeatable training
and testing split.”

Cue words: **my role, both directions, model-ready data**.

## Slide 2: Five files, one five-class dataset (about 35 seconds)

“We use five files covering normal traffic and four attack scenarios. They
contain 259,379 raw rows. Attack files also include background normal traffic,
so we select normal rows from the normal file and attack rows from each attack
file. After selection and duplicate removal, 118,901 unique records remain.
Our working copy is a checksum-verified Kaggle mirror. Equivalence to the
official archive remains unverified.”

Cue words: **five files, select correct rows, remove duplicates, source limit**.
Point to the chart once. The intermediate count is 157,009 and the number of
duplicate feature records removed is 38,108. You can read the chart instead of
saying every number aloud.

## Slide 3: Features and leakage prevention (about 40 seconds)

“The final model receives 27 numeric features, including packet counts, timing,
bytes and ports. We remove IP addresses, protocol and the binary is_attack
field. Keeping is_attack would reveal part of the answer. We also remove one
constant feature. PR 46 identifies constants using training data only, then
applies the same feature mask to test data. No text categories remain. Removing
IPs and omitting scaling differ from the paper, and we document those choices.”

Cue words: **27 features, remove answer, learn preprocessing on training only**.
Say “is attack” aloud. You do not need to pronounce every column name.

## Slide 4: A repeatable 80/20 split (about 30 seconds)

“I separate the feature inputs, X, from the scenario labels, y. A stratified
80/20 split produces 95,120 training records and 23,781 test records.
Stratification preserves similar class proportions, and seed 42 makes the split
repeatable. We check for duplicate feature vectors across the split. This
within-dataset evaluation does not establish performance on new networks.”

Cue words: **X and y, train/test counts, stratified, seed 42, generalization limit**.
Pause briefly after the two large numbers.

## Slide 5: Verification and model handoff (about 30 seconds)

“I record source checksums and rebuild the data twice. Saved reports check
labels, dimensions, duplicate separation and array hashes. Six tests pass in
the recorded author-side runs. Another teammate still needs to verify PR 46
independently before approval. My implementation and handoff evidence are
ready. Next, Yassin will explain how the Random Forest uses these prepared inputs.”

Cue words: **checksums, two builds, six tests, independent check pending, handoff**.
If another person presents after you, replace Yassin's name. Update the pending
statement only when a successful reviewer run is actually recorded.

## Optional demonstration (adds about 45–60 seconds)

Use backup slide 7 only if the coordinator includes a live dataset step in the
team's timing. Prepare the environment and raw CSVs beforehand. The verifier's
recorded author runtimes were roughly 36–41 seconds, excluding installation.
Measure your actual runtime before relying on this budget.

Run each command from the repository root in the documented environment:

```powershell
python -m unittest discover -s tests -v
python src/verify_prepared_data.py --input-dir data/raw/kaggle-replication --report data/processed/demo-verification.json
```

Say: “First I run the regression checks. Then the verifier rebuilds the real
data twice and records the actual counts and hashes.” Show the actual result.
Expected: six tests pass, 95,120 train, 23,781 test, 27 features.

If it fails: “The live run stopped with this error. Here is the dated saved
verification report from the recorded author-side run.” Show
`results/data-verification.json` and say its recorded status/date. Do not claim
that a backup proves today's live command succeeded. This presentation is not
the required recording of the final integrated pipeline.

## Short version if the group cuts your time (about 60 seconds)

“My role is preparing the MQTT-IoT-IDS2020 Bi-flow data for the model. We start
with five scenario files and 259,379 raw rows. We select the correct normal and
attack rows, remove duplicate feature records, and retain 118,901 unique records.
The model receives 27 numeric features. We remove identifiers and the binary
answer field, and identify constant features using training data only. A
stratified 80/20 split with seed 42 gives 95,120 training rows and 23,781 test
rows. Author-side checks include six passing tests, source checksums and
matching repeated builds. Independent verification of PR 46 is still pending.
Our IP removal and no-scaling choices differ from the paper. These prepared
arrays are the handoff to the model lead.”

## Likely questions and plain-language answers

**What is Bi-flow?** A bidirectional flow summarizes communication in both
directions between endpoints. We use those tabular summaries rather than packet
captures or the Uni-flow representation.

**Why do you filter rows in attack files?** Those files include background normal
traffic. We select attack rows from each attack scenario and normal rows from
the normal file, then assign the scenario class.

**What is the label?** It is a separate five-class target: 0 normal, 1 scan_A,
2 scan_sU, 3 sparta, 4 mqtt_bruteforce. The binary `is_attack` field helps select
rows but never enters X. Backup slide 6 has the mapping and counts.

**Why remove duplicates before splitting?** Identical feature records in training
and testing could make evaluation misleading. This check addresses that specific
risk, not every kind of capture leakage.

**What does leakage mean?** Information that should be unavailable during training
influences the model or preparation decisions. Keeping the answer in X is direct
leakage. Using holdout variation to select features also contaminates evaluation.

**Why choose constants on training only?** The holdout must not decide which
features survive. Fit the mask on training, then reuse it unchanged for testing.

**Why no encoder or scaler?** All retained baseline features are numeric, so no
categorical encoder is needed. The team did not scale this RF baseline. The paper
describes IP encoding and Min-Max scaling, so we explicitly disclose our different
preparation rather than calling it identical.

**Why seed 42?** It is a fixed reproducibility choice, not a claim that 42 is
scientifically better. Dependency versions also affect exact numeric hashes.

**Why stratify?** It keeps similar class proportions across the split. It does
not balance class sizes or test generalization to an independent capture.

**Are the data perfectly clean or the system proven secure?** We observed zero
missing/infinite retained-feature cells and checked specific leakage risks.
Independent-network generalization and official-archive equivalence remain
unverified. Avoid broad claims about perfect cleanliness or production security.

**How does the model compare to a simple guess?** The retrospective training-majority
reference scores 72.335057% accuracy and detects no attacks. The recorded RF
scores about 99.9411%. Model/evaluation presenters cover those results. The simple
reference was added after RF, and the final integrated run remains pending.

**What is left for you?** Rehearse and present this section, obtain/readability-check
backup screenshots, help record the final integrated run, and reconcile the data
documentation after independent review and integration. Slide preparation alone
does not complete these human acceptance gates.

## Practice checklist

- [ ] Read the script once, then practice from cue words rather than memorizing.
- [ ] Record a timed run. Target 2:35–3:00 without the optional live command.
- [ ] Explain training-only feature selection without reading the slide.
- [ ] Rehearse the handoff with the next speaker and agree on your time allocation.
- [ ] Check readability on the presentation display and save genuine backup screenshots.
- [ ] Export the editable deck as PPTX from its viewer and merge the section into the team deck.
- [ ] Confirm the review-status sentence immediately before the final presentation.
- [ ] Add the actual rehearsal duration and final deck/recording links to #40.

Evidence: [Reproduction Report](https://github.com/n4stam0on/Intrusion-Interceptors-Pipeline-Capstone/wiki/Reproduction-Report),
[PR #46](https://github.com/n4stam0on/Intrusion-Interceptors-Pipeline-Capstone/pull/46),
[PR #48](https://github.com/n4stam0on/Intrusion-Interceptors-Pipeline-Capstone/pull/48).
