# Independent-Traffic Generalization Assessment

## Objective

Determine whether the MQTT-IoT-IDS2020 Bi-flow dataset
supports an independent-session or IP-grouped evaluation
of the Random Forest classifier.

## Dataset Investigation

Five scenario CSV files were inspected.

| Class | Filtered Records | Unique IP Pairs |
|---|---:|---:|
| normal | 86,008 | 17 |
| scan_A | 19,907 | 17 |
| scan_sU | 22,434 | 17 |
| sparta | 14,116 | 1 |
| mqtt_bruteforce | 14,544 | 4 |

Across all classes:
- 38 distinct source/destination IP pairs
- 17 IP pairs shared across multiple classes
- Each CSV contains 32 columns

## Session Identifier Investigation

Column names were searched for:
time, date, session, flow, capture, device, and host.

No matching column names were found.

This does not prove that no other useful grouping
information exists, but no obvious session or timestamp
identifier was identified by this inspection.

## Grouped Evaluation Limitation

The Sparta scenario contains only one IP pair.

A split that keeps IP pairs completely separate between
training and testing cannot include Sparta records in
both partitions.

Therefore, a conventional IP-pair-disjoint evaluation
cannot reliably evaluate all five classes in both
partitions using the available data.

IP pairs are also not guaranteed to represent independent
network sessions.

## Existing Model Results

The established Random Forest baseline achieved:

- Accuracy: 99.9411%
- Training records: 95,120
- Testing records: 23,781
- Features: 27
- Random state: 42

These results measure performance on the existing
stratified random test split.

They do not establish performance on independent
devices, network sessions, or capture periods.

## Conclusion

The existing Random Forest baseline remains unchanged.

Independent-traffic generalization is not established
by the current experiments.

Future evaluation should use additional capture data
or reliable session/capture identifiers when available.

The project must clearly distinguish reproducibility
and within-dataset performance from external
generalization.
