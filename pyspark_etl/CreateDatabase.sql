-- CREATE DATABASE IF NOT EXISTS spark_db;

\c spark_db

-- CREATE SCHEMA IF NOT EXISTS spark_schema;
SET search_path TO spark_schema;

CREATE TABLE IF NOT EXISTS soundclouduser (
    id SERIAL PRIMARY KEY,
    username TEXT,
    number_follows INTEGER,
    number_tracks INTEGER,
    link TEXT
);




