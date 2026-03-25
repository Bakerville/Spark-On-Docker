from pyspark.sql import SparkSession

class ExtractLoadFiletoDB():
    def __init__(self) -> None:
        self.masterName = None
        self.appName = None
        self.driver = None
        self.spark = None
        self.sourceMetadata = None
        self.sourceDataFrame = None
        self.DBConnection = None
        pass
    
    # Create a SparkSession
    def createSparkSession(self, masterName, appName,driverPos="./jars/sqljdbc41.jar"):
        self.spark = SparkSession.builder.master("local[1]")\
                .config("spark.jars",driverPos)\
                .config("spark.driver.extraClassPath",driverPos)\
                .config('spark.executor.extraClassPath', driverPos)\
                .appName(appName)\
                .getOrCreate()
        return None
    
    # Extract data from flat file
    def extractSourceFile(self,filePath, schema, delimiter=",", header=True):
        try:
            self.sourceDataFrame = self.spark.read.options(delimiter=delimiter)\
                                       .csv(filePath, schema=schema,header=header)
            
        except Exception as error:
            print("Caught this error: ", error)


        self.sourceMetadata = {"path": filePath, "schema": list(schema)}

        return self.sourceDataFrame
    
    # Create connection to Azure SQL Database
    def createDBConnection(self, url=None, driver="com.microsoft.sqlserver.jdbc.SQLServerDriver", username=None, password=None,format="jdbc"):

        self.DBConnection = {"url":url, "driver":driver,"format":format,\
                            "user": username, "password": password}
        return None
    
    # Ingest data from file to database
    def writeDBTable(self, tablename =None, mode="overwrite", dataframe=None):
        dataframe.write \
            .format(self.DBConnection["format"])\
            .option("driver",self.DBConnection["driver"]) \
            .option("url", self.DBConnection["url"]) \
            .option("dbtable", tablename) \
            .option("user", self.DBConnection["user"]) \
            .option("password", self.DBConnection["password"])\
            .save(mode=mode)



