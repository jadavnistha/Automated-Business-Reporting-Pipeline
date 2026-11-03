import pandas as pd
from pathlib import Path


SUPPORTED_EXTENSIONS = [".csv", ".xlsx", ".xls"]


def ingest_file(file_path):
    """
    Read a CSV or Excel business data file into a pandas DataFrame.
    """

    file_path = Path(file_path)

    if not file_path.exists():
        raise FileNotFoundError(f"Input file not found: {file_path}")

    if file_path.suffix.lower() not in SUPPORTED_EXTENSIONS:
        raise ValueError(
            f"Unsupported file format: {file_path.suffix}"
        )

    if file_path.suffix.lower() == ".csv":
        df = pd.read_csv(file_path)

    else:
        df = pd.read_excel(file_path)

    print(f"Successfully ingested: {file_path.name}")
    print(f"Records received: {len(df)}")

    return df


if __name__ == "__main__":
    input_file = "data/raw/sales_data.csv"

    df = ingest_file(input_file)

    print("\n========== INGESTION SUMMARY ==========")
    print(f"Rows: {len(df)}")
    print(f"Columns: {len(df.columns)}")
    print("\nColumns:")
    print(list(df.columns))