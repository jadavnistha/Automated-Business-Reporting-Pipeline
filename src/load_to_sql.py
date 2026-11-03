import os
import pandas as pd
from sqlalchemy import create_engine, text
from sqlalchemy.engine import URL
from sqlalchemy import create_engine, text
from dotenv import load_dotenv

load_dotenv()

DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = int(os.getenv("DB_PORT", "3306"))
DB_NAME = os.getenv("DB_NAME")


def load_to_sql(df):
    """
    Load transformed sales data into MySQL.

    Existing records with the same Order_ID are removed
    before the refreshed dataset is loaded.
    """

    connection_url = URL.create(
    drivername="mysql+pymysql",
    username=DB_USER,
    password=DB_PASSWORD,
    host=DB_HOST,
    port=DB_PORT,
    database=DB_NAME
    )


    engine = create_engine(connection_url)

    print("\nSTEP 5: MYSQL LOAD")
    print("------------------------------------------")

    df = df.copy()

    # Convert datetime to MySQL-compatible date
    df["Order_Date"] = pd.to_datetime(df["Order_Date"]).dt.date

    order_ids = df["Order_ID"].tolist()

    # Remove existing records with the same Order_ID
    if order_ids:

        placeholders = ", ".join(
            [f":id_{i}" for i in range(len(order_ids))]
        )

        delete_query = text(
            f"DELETE FROM sales "
            f"WHERE Order_ID IN ({placeholders})"
        )

        delete_params = {
            f"id_{i}": order_id
            for i, order_id in enumerate(order_ids)
        }

        with engine.begin() as connection:
            result = connection.execute(
                delete_query,
                delete_params
            )

        print(f"Existing records replaced: {result.rowcount}")

    # Insert refreshed records
    df.to_sql(
        name="sales",
        con=engine,
        if_exists="append",
        index=False
    )

    print(f"Records loaded into MySQL: {len(df)}")
    print("MySQL load completed successfully.")