-- ==========================================
-- Automated Business Reporting Pipeline
-- Database Schema
-- ==========================================

CREATE DATABASE IF NOT EXISTS automated_reporting;

USE automated_reporting;


-- ==========================================
-- Sales Table
-- ==========================================

DROP TABLE IF EXISTS sales;

CREATE TABLE sales (

    Order_ID VARCHAR(20) PRIMARY KEY,

    Order_Date DATE NOT NULL,

    Customer_ID VARCHAR(20) NOT NULL,

    Product VARCHAR(100) NOT NULL,

    Category VARCHAR(50) NOT NULL,

    Region VARCHAR(20) NOT NULL,

    Quantity INT NOT NULL,

    Unit_Price DECIMAL(12,2) NOT NULL,

    Discount DECIMAL(5,2) NOT NULL,

    Payment_Method VARCHAR(50) NOT NULL,

    Gross_Sales DECIMAL(14,2) NOT NULL,

    Discount_Amount DECIMAL(14,2) NOT NULL,

    Net_Sales DECIMAL(14,2) NOT NULL,

    Order_Month VARCHAR(7) NOT NULL,

    Order_Year INT NOT NULL,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

);
USE automated_reporting;

SHOW TABLES;
DESCRIBE sales;
USE automated_reporting;

SELECT COUNT(*) AS total_records
FROM sales;
SELECT *
FROM sales
LIMIT 10;
SELECT COUNT(*) FROM sales;
