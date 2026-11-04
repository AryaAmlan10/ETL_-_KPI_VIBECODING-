from pathlib import Path
import sqlite3

import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parents[1]
CSV_PATH = PROJECT_ROOT / "data" / "raw" / "customers_raw.csv"
DATABASE_PATH = PROJECT_ROOT / "data" / "db" / "analytics.db"


def load_data() -> None:
    """Load the customer CSV into SQLite, replacing any previous rows."""
    customers = pd.read_csv(CSV_PATH)
    DATABASE_PATH.parent.mkdir(parents=True, exist_ok=True)

    with sqlite3.connect(DATABASE_PATH) as connection:
        connection.execute(
            """
            CREATE TABLE IF NOT EXISTS customers_raw (
                customer_id INTEGER,
                city TEXT,
                monthly_spend REAL,
                churned INTEGER
            )
            """
        )
        connection.execute("DELETE FROM customers_raw")
        connection.executemany(
            """
            INSERT INTO customers_raw (customer_id, city, monthly_spend, churned)
            VALUES (?, ?, ?, ?)
            """,
            customers.itertuples(index=False, name=None),
        )

    print(f"Loaded {len(customers)} customers into {DATABASE_PATH}")


if __name__ == "__main__":
    load_data()
