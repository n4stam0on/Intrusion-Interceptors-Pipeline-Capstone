"""Run a reproducible smoke test and basic audit on an IDS CSV dataset."""

from __future__ import annotations

import argparse
from pathlib import Path

import pandas as pd


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Load an IDS CSV and report the evidence required for the capstone proposal."
    )
    parser.add_argument("csv_path", type=Path, help="Path to a CSV file under data/raw/")
    parser.add_argument(
        "--label",
        help="Name of the target/label column. If omitted, available columns are shown.",
    )
    parser.add_argument(
        "--rows",
        type=int,
        default=100_000,
        help="Maximum rows to load for the smoke test (default: 100000)",
    )
    parser.add_argument(
        "--full",
        action="store_true",
        help="Load the complete CSV instead of limiting the smoke test to --rows",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    csv_path = args.csv_path.expanduser().resolve()

    if not csv_path.is_file():
        raise SystemExit(f"CSV file not found: {csv_path}")
    if csv_path.suffix.lower() != ".csv":
        raise SystemExit(f"Expected a .csv file, received: {csv_path.name}")
    if args.rows < 1:
        raise SystemExit("--rows must be at least 1")

    row_limit = None if args.full else args.rows
    frame = pd.read_csv(csv_path, nrows=row_limit, low_memory=False)

    print("=== Dataset loading evidence ===")
    print(f"File: {csv_path.name}")
    print(f"File size: {csv_path.stat().st_size:,} bytes")
    print(f"Rows loaded: {len(frame):,}")
    print(f"Columns: {len(frame.columns):,}")
    print(f"Mode: {'full file' if args.full else f'smoke test (up to {args.rows:,} rows)'}")

    print("\n=== Column data types ===")
    print(frame.dtypes.to_string())

    print("\n=== Missing values by column ===")
    missing = frame.isna().sum().sort_values(ascending=False)
    print(missing.to_string())

    print("\n=== Duplicate rows in loaded data ===")
    print(f"{int(frame.duplicated().sum()):,}")

    print("\n=== Label distribution ===")
    if args.label:
        if args.label not in frame.columns:
            available = ", ".join(map(str, frame.columns))
            raise SystemExit(
                f"Label column '{args.label}' was not found. Available columns: {available}"
            )
        counts = frame[args.label].value_counts(dropna=False)
        percentages = frame[args.label].value_counts(dropna=False, normalize=True) * 100
        summary = pd.DataFrame({"count": counts, "percent": percentages.round(2)})
        print(summary.to_string())
    else:
        print("No --label supplied. Choose one from these columns:")
        print("\n".join(map(str, frame.columns)))


if __name__ == "__main__":
    main()
