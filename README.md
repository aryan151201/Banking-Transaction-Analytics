# Banking-Transaction-Analytics
Banking transaction analysis using Python, SQL Server, and Power BI

# Banking Transaction Analytics

## Project Overview

An interactive data analytics project that examines banking transaction volumes, success rates, failed transactions, and rejected transactions using Python, SQL Server, and Power BI.

**Note:** This project uses synthetic banking transaction data for educational and portfolio purposes. It does not contain real customer or banking records.

## Tools & Technologies

- **Python:** Data generation, cleaning, and exploratory data analysis
- **Pandas:** Data manipulation and analysis
- **Microsoft SQL Server:** Data storage, SQL queries, aggregations, and joins
- **Power BI:** Interactive dashboard, KPI cards, slicers, and charts

## Key Features

- Analyzed 50,000 synthetic transaction records
- Examined transaction outcomes across SUCCESS, FAILED, and REJECTED statuses
- Compared transaction types, including NEFT and RTGS
- Analyzed transaction volumes and unsuccessful transactions by bank
- Created an interactive Power BI dashboard with date, transaction type, and status filters
- Used SQL aggregations, conditional calculations, and joins for reporting

## Key Findings

Based on the generated dataset:

- Total transactions: 50,000
- Successful transactions: 44,059 (88.12%)
- Failed transactions: 3,501 (7.00%)
- Rejected transactions: 2,440 (4.88%)

These results describe the synthetic dataset only and should not be interpreted as actual banking performance.

## Project Structure

- `data/` — Raw and processed datasets
- `python/` — Python scripts for data generation and analysis
- `sql/` — SQL queries used for analysis
- `powerbi/` — Power BI report
- `dashboard_screenshot.png` — Dashboard preview

## How to Explore

1. Review the Python scripts and sample dataset.
2. Run the SQL queries against a compatible SQL Server database after importing the dataset.
3. Open the Power BI report in Power BI Desktop and configure the data source if necessary.

## Skills Demonstrated

SQL querying, data cleaning, exploratory data analysis, KPI development, data visualization, and dashboard reporting.
