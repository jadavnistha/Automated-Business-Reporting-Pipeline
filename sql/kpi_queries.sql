USE automated_reporting;

-- ==========================================
-- 1. TOTAL SALES
-- ==========================================

SELECT
    SUM(Net_Sales) AS total_sales
FROM sales;


-- ==========================================
-- 2. TOTAL ORDERS
-- ==========================================

SELECT
    COUNT(DISTINCT Order_ID) AS total_orders
FROM sales;


-- ==========================================
-- 3. TOTAL CUSTOMERS
-- ==========================================

SELECT
    COUNT(DISTINCT Customer_ID) AS total_customers
FROM sales;


-- ==========================================
-- 4. TOTAL QUANTITY SOLD
-- ==========================================

SELECT
    SUM(Quantity) AS total_quantity
FROM sales;


-- ==========================================
-- 5. AVERAGE ORDER VALUE
-- ==========================================

SELECT
    ROUND(AVG(Net_Sales), 2) AS average_order_value
FROM sales;


-- ==========================================
-- 6. SALES BY REGION
-- ==========================================

SELECT
    Region,
    COUNT(DISTINCT Order_ID) AS total_orders,
    SUM(Net_Sales) AS total_sales
FROM sales
GROUP BY Region
ORDER BY total_sales DESC;


-- ==========================================
-- 7. SALES BY CATEGORY
-- ==========================================

SELECT
    Category,
    COUNT(DISTINCT Order_ID) AS total_orders,
    SUM(Quantity) AS units_sold,
    SUM(Net_Sales) AS total_sales
FROM sales
GROUP BY Category
ORDER BY total_sales DESC;


-- ==========================================
-- 8. SALES BY PRODUCT
-- ==========================================

SELECT
    Product,
    SUM(Quantity) AS units_sold,
    SUM(Net_Sales) AS total_sales
FROM sales
GROUP BY Product
ORDER BY total_sales DESC;


-- ==========================================
-- 9. MONTHLY SALES TREND
-- ==========================================

SELECT
    Order_Month,
    COUNT(DISTINCT Order_ID) AS total_orders,
    SUM(Net_Sales) AS total_sales
FROM sales
GROUP BY Order_Month
ORDER BY Order_Month;


-- ==========================================
-- 10. PAYMENT METHOD PERFORMANCE
-- ==========================================

SELECT
    Payment_Method,
    COUNT(DISTINCT Order_ID) AS total_orders,
    SUM(Net_Sales) AS total_sales
FROM sales
GROUP BY Payment_Method
ORDER BY total_sales DESC;