import tempfile
import unittest
from pathlib import Path

import numpy as np
import pandas as pd

from src.preprocess_dataset import (
    EXPECTED_COLUMNS,
    SCENARIOS,
    prepare_dataset,
    write_outputs,
)


def make_row(seed: int, is_attack: int) -> dict[str, int | float | str]:
    row: dict[str, int | float | str] = {}
    for index, column in enumerate(EXPECTED_COLUMNS):
        if column == "ip_src":
            row[column] = f"10.0.{seed}.1"
        elif column == "ip_dst":
            row[column] = f"10.0.{seed}.2"
        elif column == "proto":
            row[column] = 6
        elif column == "is_attack":
            row[column] = is_attack
        elif column == "bwd_num_urg_flags":
            row[column] = 0
        else:
            row[column] = seed * 100 + index
    return row


class PreprocessingTests(unittest.TestCase):
    def create_fixture(self, directory: Path) -> None:
        for scenario in SCENARIOS:
            base = scenario.class_id * 10 + 1
            selected = [
                make_row(base + offset, scenario.selected_is_attack)
                for offset in range(3)
            ]
            duplicate = selected[0].copy()
            duplicate["ip_src"] = "192.0.2.50"
            duplicate["ip_dst"] = "192.0.2.51"
            background = make_row(
                base + 9,
                1 - scenario.selected_is_attack,
            )
            pd.DataFrame([*selected, duplicate, background]).to_csv(
                directory / scenario.filename, index=False
            )

    def test_leakage_filtering_deduplication_and_stratified_split(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            input_dir = Path(temporary)
            self.create_fixture(input_dir)
            X_train, X_test, y_train, y_test, metadata = prepare_dataset(
                input_dir, test_size=0.4, random_state=17
            )

            self.assertEqual(len(X_train) + len(X_test), 15)
            self.assertEqual(metadata["selected_rows_total"], 20)
            self.assertTrue(
                all(value == 1 for value in metadata["duplicates_removed_by_class"].values())
            )
            self.assertNotIn("ip_src", X_train.columns)
            self.assertNotIn("ip_dst", X_train.columns)
            self.assertNotIn("proto", X_train.columns)
            self.assertNotIn("is_attack", X_train.columns)
            self.assertNotIn("bwd_num_urg_flags", X_train.columns)
            self.assertEqual(set(y_train) | set(y_test), {0, 1, 2, 3, 4})

            train_rows = {tuple(row) for row in X_train.to_numpy()}
            test_rows = {tuple(row) for row in X_test.to_numpy()}
            self.assertFalse(train_rows & test_rows)

    def test_deterministic_output_round_trip(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            input_dir = Path(temporary) / "input"
            output_dir = Path(temporary) / "output"
            input_dir.mkdir()
            self.create_fixture(input_dir)

            first = prepare_dataset(input_dir, test_size=0.4, random_state=42)
            second = prepare_dataset(input_dir, test_size=0.4, random_state=42)
            for left, right in zip(first[:4], second[:4]):
                np.testing.assert_array_equal(left.to_numpy(), right.to_numpy())

            created = write_outputs(output_dir, *first, write_csv=False)
            self.assertEqual(len(created), 2)
            with np.load(created[0], allow_pickle=False) as bundle:
                np.testing.assert_array_equal(bundle["X_train"], first[0].to_numpy())
                np.testing.assert_array_equal(bundle["y_test"], first[3].to_numpy())

    def test_missing_required_column_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            input_dir = Path(temporary)
            self.create_fixture(input_dir)
            broken_path = input_dir / SCENARIOS[0].filename
            broken = pd.read_csv(broken_path).drop(columns=["fwd_num_pkts"])
            broken.to_csv(broken_path, index=False)

            with self.assertRaisesRegex(ValueError, "Schema mismatch"):
                prepare_dataset(input_dir, test_size=0.4)


if __name__ == "__main__":
    unittest.main()
