# Pyspark and Selenium on Docker
---------
**1. Selenium on Docker**

<img title="a title" alt="Alt text" src="/images/Selenium_Folder.png">

This folder contains code to run a crawler that get data from Soundcloud.com and save it into data folder. The crawler runs on Docker and data generated in a built container is mounted from container to local desktop with the docker-compose.yml .

There are steps to run app:
- <code>docker build -t crawler-img .</code>
- <code>docker run crawler-img</code>

When the contain stopped and the screen display "Crawling Successful", the data folder including Soundcloud_User.csv will exist. The file after crawling is mounted to <code>../Pyspark ETL/data/</code>

**2. Pyspark on Docker**

<img title="a title" alt="Alt text" src="/images/Spark_Folder.png">

When having had the Soundcloud_User.csv, I will do an ETL process to transform and load data to SoundCloudUser table in Azure SQL server. The origin folder has a (.env) folder containing credential infomation of SQL server (password, username,connection_string), so I have to hide it from repository.

Steps to run this app:
- Configure the essential infomation in .env file
- <code>docker build -t etl-img .</code>
- <code>docker run etl-img</code>

When all of data in Soundcloud_User.csv tranformed and loaded to database, the notification "Successful" will be displayed.

<img title="a title" alt="Alt text" src="/images/DataFile.png">
<p>
        <em style="text-align: center;">Data in SoundCloud_User.csv</em>
</p>



<img title="a title" alt="Alt text" src="/images/Data in database.png">

<em>Data in  after ETL</em>