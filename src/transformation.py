import pandas as pd


def transform_data(df):
    """
    Transform validated sales data into a reporting-ready format.
    """

    df = df.copy()

    # --------------------------------------------------
    # Standardize text fields
    # --------------------------------------------------

    text_columns = [
        "Product",
        "Category",
        "Region",
        "Payment_Method"
    ]

    for column in text_columns:
        df[column] = df[column].astype(str).str.strip()

    # Standardize region names
    df["Region"] = df["Region"].str.title()

    # --------------------------------------------------
    # Standardize date
    # --------------------------------------------------

    df["Order_Date"] = pd.to_datetime(
        df["Order_Date"]
    )

    # --------------------------------------------------
    # Calculate sales metrics
    # --------------------------------------------------

    df["Gross_Sales"] = (
        df["Quantity"] * df["Unit_Price"]
    )

    df["Discount_Amount"] = (
        df["Gross_Sales"] * df["Discount"]
    )

    df["Net_Sales"] = (
        df["Gross_Sales"] - df["Discount_Amount"]
    )

    # --------------------------------------------------
    # Add reporting fields
    # --------------------------------------------------

    df["Order_Month"] = (
        df["Order_Date"]
        .dt.to_period("M")
        .astype(str)
    )

    df["Order_Year"] = (
        df["Order_Date"].dt.year
    )

    # --------------------------------------------------
    # Round financial values
    # --------------------------------------------------

    financial_columns = [
        "Unit_Price",
        "Gross_Sales",
        "Discount_Amount",
        "Net_Sales"
    ]

    for column in financial_columns:
        df[column] = df[column].round(2)

    return df