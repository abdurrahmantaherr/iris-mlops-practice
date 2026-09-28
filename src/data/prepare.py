from pathlib import Path

import pandas as pd


RAW_DATA = Path("data/raw/iris.csv")
PROCESSED_DATA = Path("data/processed/iris.csv")


def prepare_data():
    df = pd.read_csv(RAW_DATA)

    PROCESSED_DATA.parent.mkdir(parents=True, exist_ok=True)

    df.to_csv(PROCESSED_DATA, index=False)

    print(f"Processed data saved to: {PROCESSED_DATA}")


if __name__ == "__main__":
    prepare_data()
