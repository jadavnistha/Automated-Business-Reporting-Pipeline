import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta
from pathlib import Path

# Reproducibility
np.random.seed(42)
random.seed(42)

# --------------------------------------------------
# Configuration
# --------------------------------------------------

NUM_RECORDS = 1200

products = {
    "Laptop": "Electronics",
    "Smartphone": "Electronics",
    "Headphones": "Electronics",
    "Office Chair": "Furniture",
    "Desk": "Furniture",
    "Notebook": "Stationery",
    "Pen Set": "Stationery",
    "Backpack": "Accessories",
    "Monitor": "Electronics",
    "Keyboard": "Electronics"
}

regions = ["North", "South", "East", "West"]
payment_methods = ["Credit Card", "Debit Card", "UPI", "Cash"]

start_date = datetime(2026, 1, 1)

# --------------------------------------------------
# Generate clean records
# --------------------------------------------------

records = []

for i in range(NUM_RECORDS):

    product = random.choice(list(products.keys()))

    quantity = random.randint(1, 5)

    unit_price = {
        "Laptop": 65000,
        "Smartphone": 35000,
        "Headphones": 3500,
        "Office Chair": 8500,
        "Desk": 12000,
        "Notebook": 250,
        "Pen Set": 180,
        "Backpack": 1800,
        "Monitor": 15000,
        "Keyboard": 2500
    }[product]

    # Add some price variation
    unit_price = round(unit_price * random.uniform(0.9, 1.1), 2)

    discount = round(random.choice([0, 0.05, 0.10, 0.15]), 2)

    order_date = start_date + timedelta(
        days=random.randint(0, 240)
    )

    records.append({
        "Order_ID": f"ORD{i+1:05d}",
        "Order_Date": order_date.strftime("%Y-%m-%d"),
        "Customer_ID": f"CUST{random.randint(1, 350):04d}",
        "Product": product,
        "Category": products[product],
        "Region": random.choice(regions),
        "Quantity": quantity,
        "Unit_Price": unit_price,
        "Discount": discount,
        "Payment_Method": random.choice(payment_methods)
    })

df = pd.DataFrame(records)

# --------------------------------------------------
# Introduce data-quality issues
# --------------------------------------------------

# Missing Customer IDs
missing_indices = np.random.choice(
    df.index,
    size=10,
    replace=False
)

df.loc[missing_indices, "Customer_ID"] = np.nan


# Duplicate records
duplicates = df.iloc[20:25].copy()
df = pd.concat([df, duplicates], ignore_index=True)


# Invalid quantities
invalid_quantity_indices = np.random.choice(
    df.index,
    size=5,
    replace=False
)

df.loc[invalid_quantity_indices, "Quantity"] = -3


# Invalid prices
invalid_price_indices = np.random.choice(
    df.index,
    size=5,
    replace=False
)

df.loc[invalid_price_indices, "Unit_Price"] = -500


# Inconsistent region formatting
region_indices = np.random.choice(
    df.index,
    size=15,
    replace=False
)

df.loc[region_indices, "Region"] = df.loc[
    region_indices, "Region"
].str.lower()


# Missing product
missing_product_indices = np.random.choice(
    df.index,
    size=5,
    replace=False
)

df.loc[missing_product_indices, "Product"] = np.nan


# --------------------------------------------------
# Save dataset
# --------------------------------------------------

output_path = Path("data/raw/sales_data.csv")

output_path.parent.mkdir(
    parents=True,
    exist_ok=True
)

df.to_csv(output_path, index=False)

print(f"Dataset created successfully.")
print(f"Rows: {len(df)}")
print(f"Columns: {len(df.columns)}")
print(f"Saved to: {output_path}")