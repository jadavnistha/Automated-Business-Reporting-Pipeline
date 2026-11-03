import sys
import logging
from pathlib import Path

SRC_DIR = Path(__file__).resolve().parent
sys.path.append(str(SRC_DIR))

from ingestion import ingest_file
from validation import validate_data
from transformation import transform_data
from load_to_sql import load_to_sql


# ==========================================
# PATHS
# ==========================================

PROJECT_DIR = SRC_DIR.parent

INPUT_FILE = PROJECT_DIR / "data" / "raw" / "sales_data.csv"
OUTPUT_FILE = PROJECT_DIR / "data" / "processed" / "clean_sales_data.csv"
LOG_FILE = PROJECT_DIR / "logs" / "pipeline.log"


# ==========================================
# LOGGING CONFIGURATION
# ==========================================

LOG_FILE.parent.mkdir(parents=True, exist_ok=True)

logging.basicConfig(
    filename=str(LOG_FILE),
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    force=True
)

logger = logging.getLogger(__name__)


# ==========================================
# PIPELINE
# ==========================================

def run_pipeline():

    logger.info("Pipeline started")

    print("\n==========================================")
    print("   AUTOMATED BUSINESS REPORTING PIPELINE")
    print("==========================================\n")

    try:

        # ----------------------------------
        # STEP 1: INGESTION
        # ----------------------------------

        print("STEP 1: INGESTION")
        print("------------------------------------------")

        df = ingest_file(INPUT_FILE)

        print(f"Records received: {len(df)}")

        logger.info(
            f"Ingestion completed successfully: {len(df)} records received"
        )


        # ----------------------------------
        # STEP 2: VALIDATION
        # ----------------------------------

        print("\nSTEP 2: VALIDATION")
        print("------------------------------------------")

        valid_df, invalid_df, validation_summary = validate_data(df)

        print(f"Total records: {validation_summary['total_records']}")
        print(f"Valid records: {validation_summary['valid_records']}")
        print(f"Invalid records: {validation_summary['invalid_records']}")
        print(f"Duplicate records: {validation_summary['duplicate_records']}")
        print(
            f"Records with missing values: "
            f"{validation_summary['records_with_missing_values']}"
        )
        print(f"Invalid dates: {validation_summary['invalid_dates']}")
        print(
            f"Invalid quantities: "
            f"{validation_summary['invalid_quantities']}"
        )
        print(
            f"Invalid prices: "
            f"{validation_summary['invalid_prices']}"
        )

        logger.info(
            f"Validation completed: "
            f"{validation_summary['valid_records']} valid, "
            f"{validation_summary['invalid_records']} rejected"
        )


        # ----------------------------------
        # STEP 3: TRANSFORMATION
        # ----------------------------------

        print("\nSTEP 3: TRANSFORMATION")
        print("------------------------------------------")

        processed_df = transform_data(valid_df)

        print(f"Records transformed: {len(processed_df)}")

        logger.info(
            f"Transformation completed: "
            f"{len(processed_df)} records processed"
        )


        # ----------------------------------
        # STEP 4: OUTPUT
        # ----------------------------------

        print("\nSTEP 4: OUTPUT")
        print("------------------------------------------")

        OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)

        processed_df.to_csv(
            OUTPUT_FILE,
            index=False
        )

        print(f"Processed data saved to: {OUTPUT_FILE}")

        logger.info(
            f"Processed dataset saved: {OUTPUT_FILE}"
        )


        # ----------------------------------
        # STEP 5: MYSQL LOAD
        # ----------------------------------

        load_to_sql(processed_df)

        logger.info(
            f"MySQL load completed: "
            f"{len(processed_df)} records loaded"
        )


        # ----------------------------------
        # COMPLETION
        # ----------------------------------

        print("\n==========================================")
        print("          PIPELINE COMPLETE")
        print("==========================================")

        print(f"Input records:       {len(df)}")
        print(f"Valid records:       {len(valid_df)}")
        print(f"Rejected records:    {len(invalid_df)}")
        print(f"Processed records:   {len(processed_df)}")
        print(f"Output file:         {OUTPUT_FILE}")

        print("==========================================\n")

        logger.info("Pipeline completed successfully")


    except Exception as e:

        logger.exception(
            f"Pipeline failed: {str(e)}"
        )

        print("\nERROR: Pipeline execution failed.")
        print(f"Details: {e}")

        raise


# ==========================================
# MAIN
# ==========================================

if __name__ == "__main__":
    run_pipeline()