from src.etl_load_sqlite import load_data
from src.kpi_city import city_kpi


def test_city_kpi_returns_expected_values() -> None:
    load_data()

    result = city_kpi("Mumbai")

    assert result == {
        "city": "Mumbai",
        "customer_count": 3,
        "average_monthly_spend": 1500.17,
        "churn_rate_percent": 33.33,
    }


def test_city_kpi_does_not_match_sql_injection_attempt() -> None:
    load_data()

    result = city_kpi("Mumbai' OR 1=1 --")

    assert result is None
