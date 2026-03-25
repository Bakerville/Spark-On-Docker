from pyspark.sql import SparkSession
from pyspark.sql.types import IntegerType, StringType, DoubleType, StructField, StructType
import logging
import os

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

schema = StructType([
        StructField("ID", IntegerType(), False),
        StructField("USERNAME", StringType(), False),
        StructField("NUMBER_FOLLOWS", StringType(), False),
        StructField("NUMBER_TRACKS", IntegerType(), False),
        StructField("LINK", StringType(), False)])

spark_master = 'spark://spark-master:7077'

hostname = os.environ["HOST"]
database = os.environ["DATABASE"]
username = os.environ["USERNAME"]
password = os.environ["PASSWORD"]

connection_string = {
    "postgres":{
        "jdbc": "jdbc:postgresql://{host}:5432/{database}"
    }
}


class IngestCSVtoDB():
    # Initialize Spark session with specified app name, master host, and driver position
    def __init__(self, app_name, master_host, driver_pos) -> None:
        self.spark = SparkSession.builder\
            .appName(app_name)\
            .master(master_host)\
            .config("spark.driver.extraClassPath", driver_pos)\
            .getOrCreate()
        logger.info("Spark session created successfully")
    
    # Extract CSV file
    def extractCSV(self, file_path, delimiter, schema):
        """Extract data from CSV file and return a DataFrame.
        Args:
            file_path (str): The path to the CSV file.
            delimiter (str): The delimiter used in the CSV file.
            schema (StructType): The schema of the DataFrame to be created.
        Returns:
            DataFrame: A Spark DataFrame containing the data from the CSV file.
        """
        try:
            if not os.path.exists(file_path):
                logger.error(f"File not found: {file_path}")
                raise FileNotFoundError(f"File not found: {file_path}")
            
            df = self.spark.read\
                .options(**{"header": "true", "delimiter": delimiter})\
                .schema(schema)\
                .csv(file_path)
            logger.info("CSV file read successfully")
            return df
        except Exception as err:
            logger.error(f"Error reading CSV file: {err}")
            raise err
    
if __name__ == "__main__":
    app_name = "IngestCSVtoDB"
    driver_pos = './jars/sqljdbc42.jar'
    file_path = "./data/Soundcloud_User.csv"

    config = {
        "app_name": app_name,
        "master_host": spark_master,
        "driver_pos": driver_pos
    }

    ingest_process = IngestCSVtoDB(**config)
    df = ingest_process.extractCSV(file_path=file_path, delimiter=",", schema=schema)

    df.show(10)
    