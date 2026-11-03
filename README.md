# 🤖  Business Reporting Pipeline

An end-to-end sales reporting solution that automates the flow from raw CSV/Excel data to a MySQL reporting database, SQL-based KPIs, and an interactive Power BI dashboard.

## Overview

Businesses often receive recurring sales files that require repetitive manual cleaning, validation, calculations, and reporting. This project demonstrates how that workflow can be automated using Python, SQL/MySQL, and Power BI.

The pipeline:

```text
Raw CSV / Excel
      ↓
Python Ingestion
      ↓
Data Validation
      ↓
Data Transformation
      ↓
Processed CSV
      ↓
MySQL Reporting Database
      ↓
SQL KPI Analysis
      ↓
Power BI Dashboard
```

## Business Problem

The raw sales data can contain issues such as:

- Duplicate orders
- Missing required values
- Invalid quantities
- Invalid prices
- Inconsistent formatting

If these records are used directly for reporting, they can affect KPI accuracy. The objective is therefore to create a repeatable process that validates and standardizes incoming data before it reaches the reporting layer.

## Key Features

- CSV and Excel file ingestion
- Automated data-quality validation
- Duplicate and missing-value detection
- Invalid quantity, price, date, and discount checks
- Text and region standardization
- Automated sales calculations
- MySQL database loading
- SQL-based business KPI generation
- Power BI interactive dashboard
- Pipeline logging and exception handling
- Environment-variable based database credentials

## Data

The sample dataset represents recurring retail/e-commerce sales transactions.

Main fields include:

| Field | Description |
|---|---|
| Order_ID | Unique order identifier |
| Order_Date | Transaction date |
| Customer_ID | Customer identifier |
| Product | Product purchased |
| Category | Product category |
| Region | Sales region |
| Quantity | Units purchased |
| Unit_Price | Price per unit |
| Discount | Discount applied |
| Payment_Method | Payment method |

The raw dataset contains **1,205 records**.

## Data Validation

The validation stage checks the incoming records before they are transformed or loaded into MySQL.

| Check | Records |
|---|---:|
| Total records | 1,205 |
| Valid records | 1,170 |
| Rejected records | 35 |
| Duplicate records | 10 |
| Missing values | 15 |
| Invalid dates | 0 |
| Invalid quantities | 5 |
| Invalid prices | 5 |
| Invalid discounts | 0 |

Formatting inconsistencies such as region capitalization are standardized during transformation rather than unnecessarily rejected.

## Data Transformation

Validated records are cleaned and enriched using Python/Pandas.

The transformation process:

- Removes unnecessary whitespace
- Standardizes region names
- Converts order dates to a consistent format
- Calculates Gross Sales
- Calculates Discount Amount
- Calculates Net Sales
- Creates Order Month
- Creates Order Year

### Calculated fields

```text
Gross Sales = Quantity × Unit Price

Discount Amount = Gross Sales × Discount

Net Sales = Gross Sales - Discount Amount
```

The resulting 1,170 records are saved to:

```text
data/processed/clean_sales_data.csv
```

## MySQL Reporting Layer

Processed data is loaded into:

```text
Database: automated_reporting
Table: sales
```

The database provides a structured layer for SQL analysis and Power BI reporting.

The table includes the original transaction fields together with calculated reporting fields such as:

```text
Gross_Sales
Discount_Amount
Net_Sales
Order_Month
Order_Year
```

## SQL Analysis

SQL is used to generate business KPIs and analyze performance by different dimensions.

Core metrics include:

- Total Sales
- Total Orders
- Total Customers
- Total Quantity
- Average Order Value
- Sales by Region
- Sales by Product
- Payment Method performance

Example KPI calculation:

```sql
SELECT
    SUM(Net_Sales) AS total_sales,
    COUNT(DISTINCT Order_ID) AS total_orders,
    COUNT(DISTINCT Customer_ID) AS total_customers,
    SUM(Quantity) AS total_quantity,
    ROUND(
        SUM(Net_Sales) / COUNT(DISTINCT Order_ID),
        2
    ) AS average_order_value
FROM sales;
```

## Key Results

The processed dataset produces:

| KPI | Result |
|---|---:|
| Total Sales | $46,645,979.89 |
| Total Orders | 1,170 |
| Total Customers | 337 |
| Total Quantity | 3,597 |
| Average Order Value | $39,868.36 |

### Regional Performance

| Region | Orders | Net Sales |
|---|---:|---:|
| South | 286 | $12,254,209.75 |
| West | 288 | $11,888,278.81 |
| North | 300 | $11,422,941.94 |
| East | 296 | $11,080,549.39 |

South has the highest net sales, while East has the lowest. Regional revenue is relatively balanced compared with the differences between individual products.

### Product Performance

| Product | Orders | Net Sales |
|---|---:|---:|
| Laptop | 309 | $18,758,962.28 |
| Smartphone | 431 | $13,979,121.95 |
| Monitor | 389 | $5,419,383.73 |
| Office Chair | 365 | $2,862,248.09 |
| Desk | 254 | $2,833,370.56 |
| Headphones | 337 | $1,095,685.35 |
| Keyboard | 366 | $845,710.04 |
| Backpack | 428 | $708,495.91 |
| Notebook | 347 | $81,212.94 |
| Pen Set | 371 | $61,789.04 |

Laptops and Smartphones are the strongest contributors to revenue. The results also show that high order volume does not necessarily mean high revenue contribution.

## Power BI Dashboard

The processed MySQL data is connected to Power BI for interactive reporting.

<img width="1206" height="670" alt="reporting_dashboard1" src="https://github.com/user-attachments/assets/89ac1e8a-a276-4c00-8c9d-f9b79637ad30" />
<img width="1212" height="679" alt="reporting_dashboard2" src="https://github.com/user-attachments/assets/9e647524-ce45-4b7c-8901-25e0808958e5" />


The dashboard includes:

- Total Sales KPI
- Total Orders KPI
- Total Customers KPI
- Total Quantity KPI
- Average Order Value
- Monthly Sales Trend
- Sales by Region
- Sales by Product
- Payment Method distribution
- Region slicer for interactive filtering

The dashboard is designed to give management a quick view of overall performance while allowing users to investigate regional and product-level results.

## Project Structure

```text
automated-business-reporting-pipeline/
│
├── data/
│   ├── raw/
│   │   └── sales_data.csv
│   └── processed/
│       └── clean_sales_data.csv
│
├── src/
│   ├── ingestion.py
│   ├── validation.py
│   ├── transformation.py
│   ├── load_to_sql.py
│   └── pipeline.py
│
├── sql/
│   ├── schema.sql
│   ├── transformations.sql
│   └── kpi_queries.sql
│
├── dashboard/
│   └── business_reporting.pbix
│
├── logs/
│   └── pipeline.log
│
├── analysis.md
├── requirements.txt
├── .gitignore
└── README.md
```

## Component Responsibilities

### `ingestion.py`
Reads supported CSV/Excel files and checks that the input file exists and uses a supported format.

### `validation.py`
Applies data-quality rules and separates valid and rejected records.

### `transformation.py`
Standardizes data and creates calculated business fields.

### `load_to_sql.py`
Connects to MySQL and loads the processed dataset into the reporting table.

### `pipeline.py`
Orchestrates the complete workflow and records pipeline activity.

### `sql/`
Contains the database schema and analytical SQL queries.

### `dashboard/`
Contains the Power BI report.

### `analysis.md`
Documents detailed findings and business recommendations separately from the implementation documentation.

## Logging and Error Handling

The pipeline uses Python logging to record important execution events in:

```text
logs/pipeline.log
```

The pipeline records events such as:

- Pipeline start
- Successful ingestion
- Validation results
- Transformation completion
- Output generation
- MySQL loading
- Successful completion
- Processing failures

Exceptions are logged so that a failed processing stage can be investigated.

## Security

Database credentials are stored using environment variables rather than being hard-coded into the source code.

Example `.env` configuration:

```text
DB_USER=root
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=3306
DB_NAME=automated_reporting
```

The `.env` file should remain excluded through `.gitignore` and must not be committed to GitHub.

## How to Run

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Configure MySQL

Create the database and table by running:

```text
sql/schema.sql
```

### 3. Configure environment variables

Create a `.env` file in the project root with the database connection details.

### 4. Add the raw dataset

Place the input file in:

```text
data/raw/sales_data.csv
```

### 5. Run the pipeline

From the project root:

```bash
python src/pipeline.py
```

The pipeline will ingest the raw file, validate the records, transform valid data, save the processed CSV, and load the results into MySQL.

### 6. Verify the database

```sql
USE automated_reporting;

SELECT COUNT(*) AS total_rows
FROM sales;
```

For the current dataset, the expected result is:

```text
1170
```

### 7. Open Power BI

Open:

```text
dashboard/business_reporting.pbix
```

Refresh the report after the MySQL data has been updated.

## Business Recommendations

Based on the analysis:

1. Maintain automated validation for recurring sales files to prevent data-quality issues from affecting reporting.
2. Closely monitor high-value products such as Laptops and Smartphones because they contribute substantially to total revenue.
3. Investigate high-volume, lower-value products for pricing, bundling, cross-selling, and inventory opportunities.
4. Monitor regional performance regularly and investigate the causes of differences between stronger and weaker regions.
5. Continue automating recurring reporting activities so analysts can spend less time on repetitive data preparation and more time on analysis.

## Future Improvements

Possible extensions include:

- Scheduled pipeline execution
- Automated failure alerts
- Data-quality monitoring dashboard
- Historical sales tracking
- Sales anomaly detection
- Forecasting
- Automated Power BI refresh
- Staging tables and transactional database loading
- Additional customer-level analysis

## Limitations

This is a portfolio-scale implementation running locally. It is designed to demonstrate the complete reporting workflow rather than serve as a production enterprise data platform.

The current implementation requires manual pipeline execution and Power BI refresh. Future versions could introduce scheduling, automated alerts, historical data management, and stronger production database controls.

## Skills Demonstrated

- Python
- Pandas
- SQL
- MySQL
- Power BI
- Data validation
- Data transformation
- ETL pipeline design
- KPI development
- Business analysis
- Reporting automation
- Logging and exception handling
- Data-quality management

## Project Outcome

This project demonstrates the complete journey from **raw operational data to business reporting**:

```text
Business Problem
      ↓
Raw Data
      ↓
Python ETL
      ↓
Data Quality Validation
      ↓
Transformation
      ↓
MySQL
      ↓
SQL Analytics
      ↓
Power BI
      ↓
Business Insights & Recommendations
```

The key objective is to demonstrate how a repetitive reporting process can be made more **structured, repeatable, reliable, and easier to analyze** using commonly used business and technology tools.
