from pyspark.sql import SparkSession
from pyspark.sql.functions import split, regexp_replace
from pyspark.sql import SparkSession
from pyspark.sql.functions import col

class Transform():
    def __init__(self, data, spark) -> None:
        self.DataFrame = data
        self.spark = spark

    def extract_number_follows(self, col):
        return split(col," ").getItem(0)
             
    def string_to_int(self,dataframe, column_name, new_column_name ):
        try:
            df = dataframe.withColumn(f'new_{column_name}',self.extract_number_follows(dataframe[column_name]))
            table = df.createOrReplaceTempView("temp")
            sql_query = f"SELECT *, CAST(REPLACE(new_{column_name}, ',','') as INT) as {new_column_name}\
                          FROM temp"
            return self.spark.sql(f"""{sql_query}""")

        except Exception:
           try:
               table = dataframe.createOrReplaceTempView("temp")
               sql_query = f"SELECT *, CAST({column_name} as INT) as {new_column_name}\
                          FROM temp"
               return  self.spark.sql(f"""{sql_query}""")
           except Exception as err :
               print("Something goes wrong: ", err)


    

