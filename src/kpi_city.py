from pathlib import Path
import sqlite3


DATABASE_PATH = (
    Path(__file__).resolve().parents[1] / "data" / "db" / "analytics.db"
)


def city_kpi(city: str) -> dict[str, str | int | float] | None:
    """Return customer count, average spend, and churn rate for one city."""
    with sqlite3.connect(DATABASE_PATH) as connection:
        connection.row_factory = sqlite3.Row
        result = connection.execute(
            """
            SELECT
                city,
                COUNT(*) AS customer_count,
                ROUND(AVG(monthly_spend), 2) AS average_monthly_spend,
                ROUND(AVG(churned) * 100.0, 2) AS churn_rate_percent
            FROM customers_raw
            WHERE city = ?
            GROUP BY city
            """,
            (city,),
        ).fetchone()

    return dict(result) if result is not None else None


if __name__ == "__main__":
    print(city_kpi("Mumbai"))
    print(city_kpi("Mumbai' OR 1=1 --"))
