import pandas as pd


def validate_data(df):
    """
    Validate incoming sales data against defined data-quality rules.

    Returns:
        valid_df: Records that pass validation
        invalid_df: Records that fail validation
        validation_summary: Summary of validation results
    """

    df = df.copy()

    validation_errors = []

    # --------------------------------------------------
    # 1. Check for missing required fields
    # --------------------------------------------------

    required_columns = [
        "Order_ID",
        "Order_Date",
        "Customer_ID",
        "Product",
        "Category",
        "Region",
        "Quantity",
        "Unit_Price",
        "Discount",
        "Payment_Method"
    ]

    missing_column_errors = []

    for column in required_columns:
        if column not in df.columns:
            missing_column_errors.append(column)

    if missing_column_errors:
        raise ValueError(
            f"Missing required columns: {missing_column_errors}"
        )

    # --------------------------------------------------
    # 2. Duplicate Order_ID check
    # --------------------------------------------------

    duplicate_mask = df["Order_ID"].duplicated(keep=False)

    duplicate_count = duplicate_mask.sum()

    # --------------------------------------------------
    # 3. Missing-value check
    # --------------------------------------------------

    missing_mask = df[required_columns].isnull().any(axis=1)

    missing_count = missing_mask.sum()

    # --------------------------------------------------
    # 4. Date validation
    # --------------------------------------------------

    converted_dates = pd.to_datetime(
        df["Order_Date"],
        errors="coerce"
    )

    invalid_date_mask = converted_dates.isnull()

    invalid_date_count = invalid_date_mask.sum()

    # --------------------------------------------------
    # 5. Quantity validation
    # --------------------------------------------------

    invalid_quantity_mask = df["Quantity"] <= 0

    invalid_quantity_count = invalid_quantity_mask.sum()

    # --------------------------------------------------
    # 6. Unit price validation
    # --------------------------------------------------

    invalid_price_mask = df["Unit_Price"] <= 0

    invalid_price_count = invalid_price_mask.sum()

    # --------------------------------------------------
    # 7. Discount validation
    # --------------------------------------------------

    invalid_discount_mask = (
        (df["Discount"] < 0) |
        (df["Discount"] > 1)
    )

    invalid_discount_count = invalid_discount_mask.sum()

    # --------------------------------------------------
    # 8. Region validation
    # --------------------------------------------------

    valid_regions = {
        "North",
        "South",
        "East",
        "West"
    }

    invalid_region_mask = ~df["Region"].astype(str).str.title().isin(
        valid_regions
    )

    invalid_region_count = invalid_region_mask.sum()

    # --------------------------------------------------
    # Combine validation failures
    # --------------------------------------------------

    invalid_mask = (
        duplicate_mask |
        missing_mask |
        invalid_date_mask |
        invalid_quantity_mask |
        invalid_price_mask |
        invalid_discount_mask |
        invalid_region_mask
    )

    valid_df = df.loc[~invalid_mask].copy()
    invalid_df = df.loc[invalid_mask].copy()

    # --------------------------------------------------
    # Validation summary
    # --------------------------------------------------

    validation_summary = {
        "total_records": len(df),
        "valid_records": len(valid_df),
        "invalid_records": len(invalid_df),
        "duplicate_records": int(duplicate_count),
        "records_with_missing_values": int(missing_count),
        "invalid_dates": int(invalid_date_count),
        "invalid_quantities": int(invalid_quantity_count),
        "invalid_prices": int(invalid_price_count),
        "invalid_discounts": int(invalid_discount_count),
        "invalid_regions": int(invalid_region_count)
    }

    return valid_df, invalid_df, validation_summary