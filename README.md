# Applied Analytics: Customer City KPIs

This beginner-friendly project loads sample customer data from a CSV file into a
SQLite database, then calculates customer count, average monthly spend, and churn
rate for a selected city.

## Project structure

```text
data/
  raw/customers_raw.csv
  db/analytics.db          # Created when you run the ETL script
src/
  etl_load_sqlite.py
  kpi_city.py
tests/
  test_kpi_city.py
```

## Run the project

Open a terminal in the project folder and activate your `.venv`. Then run:

```powershell
python -m pip install -r requirements.txt
python src\etl_load_sqlite.py
python src\kpi_city.py
pytest
```

Run the ETL script before the KPI script. The ETL reloads the table from the CSV,
so running it more than once will not add duplicate rows.

## Files

- `data/raw/customers_raw.csv` — sample customer records for four cities.
- `data/db/analytics.db` — SQLite database created by the ETL script.
- `src/etl_load_sqlite.py` — loads the CSV into the `customers_raw` table.
- `src/kpi_city.py` — calculates a city's customer, spend, and churn KPIs safely.
- `tests/test_kpi_city.py` — checks the Mumbai KPIs and SQL-injection attempt.
- `.gitignore` — excludes local environments, caches, secrets, and generated databases.
- `requirements.txt` — lists pandas for CSV loading and pytest for tests.
