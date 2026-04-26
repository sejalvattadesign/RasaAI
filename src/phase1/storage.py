import sqlite3
from pathlib import Path

import pandas as pd


def persist_csv(df: pd.DataFrame, output_path: Path) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(output_path, index=False)


def persist_sqlite(df: pd.DataFrame, sqlite_path: Path, table_name: str) -> None:
    sqlite_path.parent.mkdir(parents=True, exist_ok=True)
    with sqlite3.connect(sqlite_path) as conn:
        df.to_sql(table_name, conn, if_exists="replace", index=False)

