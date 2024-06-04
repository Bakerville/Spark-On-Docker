from packages.ExtractLoad import ExtractLoadFiletoDB
from packages.Transform import Transform
from dotenv import load_dotenv, dotenv_values
from pyspark.sql.types import IntegerType, StringType, DoubleType, StructField, StructType


source_schema = StructType([
        StructField("ID", IntegerType(), False),
        StructField("USERNAME", StringType(), False),
        StructField("NUMBER_FOLLOWS", StringType(), False),
        StructField("NUMBER_TRACKS", IntegerType(), False),
        StructField("LINK", StringType(), False)])
        
FILEPATH = "./data/Soundcloud_User.csv"

USERNAME = dotenv_values(".env").get("USERNAME")
HOST = dotenv_values(".env").get("HOST")
CONNECTION_STRING = dotenv_values(".env").get("CONNECTION_STRING")
PASSWORD = dotenv_values(".env").get("PASSWORD")

URL = dotenv_values(".env").get("URL")

try:

# Extract data from local and create a spark session
        IngestProcess = ExtractLoadFiletoDB()

        IngestProcess.createSparkSession(masterName="local[4]", appName="ETLSpark.com", driverPos="./jars/sqljdbc42.jar")

        IngestProcess.extractSourceFile(filePath=FILEPATH, delimiter=",", schema=source_schema)

        source = IngestProcess.sourceDataFrame

        spark = IngestProcess.spark

# Transform daa
        TransformProcess = Transform(data= source, spark=spark)

        temp = TransformProcess.string_to_int(source, "NUMBER_FOLLOWS", "DB_NUMBER_FOLLOWS")

        temp_1 = TransformProcess.string_to_int(temp, "NUMBER_TRACKS", "DB_NUMBER_TRACKS")

        temp_2 = temp_1.withColumnRenamed("db_number_follows","NumberFollows").withColumnRenamed("db_number_tracks","NumberTracks")

        destination = temp_2.select("Id","Username", "NumberFollows", "NumberTracks", "Link")

        #Load data to table in database
        IngestProcess.createDBConnection(url = URL, username=USERNAME, password=PASSWORD)

        IngestProcess.writeDBTable(tablename="[dbo].[SoundCloudUser]", dataframe=destination)

        spark.stop()

        print("Successful")
except Exception as err:
        raise ConnectionError(err)






