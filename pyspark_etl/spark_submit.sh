docker cp ./pyspark_etl/ingest_csv_to_postgre.py spark-master:/opt/spark/work-dir/

docker exec -it spark-master mkdir /opt/spark/work-dir/jars/
docker exec -it spark-master mkdir /opt/spark/work-dir/data/

docker cp ./pyspark_etl/jars/sqljdbc42.jar spark-master:/opt/spark/work-dir/jars/
docker cp ./pyspark_etl/data/Soundcloud_User.csv spark-master:/opt/spark/work-dir/data/


docker exec spark-master /opt/spark/bin/spark-submit \
  --master spark://spark-master:7077 \
  /opt/spark/work-dir/ingest_csv_to_postgre.py