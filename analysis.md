# Business Analysis

## 1. Overview

The automated business reporting pipeline processes recurring sales data and converts raw operational records into reporting-ready information.

The dataset initially contained **1,205 records**. The validation stage identified **35 records requiring rejection**, leaving **1,170 valid records** for transformation and reporting.

The analysis focuses on sales performance across regions, products, customers, and order activity.

---

## 2. Data Quality Analysis

The validation process identified several data-quality issues in the incoming dataset.

| Validation Check | Records Identified |
|---|---:|
| Total records received | 1,205 |
| Valid records | 1,170 |
| Rejected records | 35 |
| Duplicate records | 10 |
| Records with missing values | 15 |
| Invalid dates | 0 |
| Invalid quantities | 5 |
| Invalid prices | 5 |
| Invalid discounts | 0 |

The pipeline rejects records containing duplicate order IDs, missing required fields, invalid quantities, invalid prices, or other validation failures.

Formatting inconsistencies such as lowercase region values are standardized during transformation rather than rejected.

This ensures that only validated and standardized records enter the reporting layer.

---

## 3. Overall Sales Performance

The processed dataset contains:

- **1,170 orders**
- **337 customers**
- **3,597 units sold**
- **$46,645,979.89 in net sales**
- **$39,868.36 average order value**

The average order value indicates that the business generates a relatively high sales value per transaction within this dataset.

---

## 4. Regional Sales Analysis

Sales performance across the four regions was relatively balanced.

| Region | Orders | Net Sales |
|---|---:|---:|
| South | 286 | $12,254,209.75 |
| West | 288 | $11,888,278.81 |
| North | 300 | $11,422,941.94 |
| East | 296 | $11,080,549.39 |

The **South region generated the highest net sales**, while the **East region generated the lowest**.

The difference between the highest and lowest regional sales is relatively moderate, indicating that revenue is distributed across all four regions rather than being concentrated in a single market.

---

## 5. Product Performance Analysis

Product-level sales show a much stronger difference in performance.

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

The **Laptop category generated the highest sales value**, followed by Smartphones and Monitors.

There is a significant difference between order volume and revenue contribution. For example, products such as Backpacks, Notebooks, and Pen Sets have relatively high order counts but contribute considerably less revenue than products such as Laptops and Smartphones.

This indicates that order volume alone is not sufficient to evaluate product performance. Revenue contribution should also be considered.

---

## 6. Key Findings

### Finding 1 — Data quality requires automated controls

The incoming dataset contained 35 records that failed validation checks.

Without automated validation, these records could potentially affect reporting accuracy.

### Finding 2 — Regional performance is relatively balanced

No region dominates the dataset to the same extent that the top products dominate product-level sales.

South is the strongest region by net sales, while East is the weakest.

### Finding 3 — Revenue is concentrated among high-value products

Laptops and Smartphones contribute substantially more revenue than the remaining products.

This creates a clear distinction between **high-volume products** and **high-value products**.

### Finding 4 — Order volume does not necessarily indicate revenue importance

Some products have high order counts but relatively low sales value.

Therefore, product decisions should consider both transaction volume and financial contribution.

### Finding 5 — Automated reporting can reduce repetitive manual work

The pipeline converts raw files into validated, transformed, SQL-ready data and connects the processed dataset to Power BI.

This creates a repeatable reporting workflow instead of requiring the same data preparation steps to be performed manually for every reporting cycle.

---

# Recommendations

## 1. Introduce automated data-quality checks at the point of ingestion

Recurring sales files should pass through validation before being added to the reporting database.

The business should monitor:

- Duplicate order IDs
- Missing customer or product information
- Invalid quantities
- Invalid prices
- Invalid dates
- Invalid discount values

This can reduce the risk of inaccurate information reaching management reports.

---

## 2. Prioritize high-value products in performance reviews

Management should separately monitor revenue contribution and order volume.

High-value products such as Laptops and Smartphones should receive dedicated performance tracking because changes in their sales can have a larger effect on overall revenue.

---

## 3. Investigate lower-value, high-volume products

Products with relatively high order counts but low revenue contribution should be reviewed for:

- Pricing strategy
- Bundle opportunities
- Cross-selling opportunities
- Customer acquisition value
- Inventory efficiency

The objective should not necessarily be to discontinue these products, but to understand whether their high transaction volume is creating sufficient business value.

---

## 4. Monitor regional performance consistently

Regional KPIs should be reviewed regularly to identify changes in sales performance.

The business could investigate why the East region trails the other regions and determine whether differences are related to demand, product mix, pricing, or sales activity.

---

## 5. Automate recurring management reporting

The validated SQL dataset and Power BI dashboard can serve as the foundation for a recurring reporting process.

Instead of manually cleaning and preparing each reporting file, the organization can use the pipeline to standardize the process and provide management with consistent KPIs.

---

## 6. Extend the pipeline with monitoring and alerts

A future version could automatically notify analysts when:

- Validation failures exceed a threshold
- Duplicate records increase significantly
- A file is missing
- Database loading fails
- Sales fall below an expected level

This would move the solution from simple reporting automation toward operational monitoring.