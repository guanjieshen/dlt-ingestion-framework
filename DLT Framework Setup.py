# Databricks notebook source
# MAGIC %md Instantiate Widgets

# COMMAND ----------

dbutils.widgets.removeAll()
dbutils.widgets.text("dlt_database","dlt","Database")

# COMMAND ----------

# MAGIC %md The following will create a DLT database in DBFS.

# COMMAND ----------

# MAGIC %sql 
# MAGIC CREATE DATABASE IF NOT EXISTS $dlt_database

# COMMAND ----------

# MAGIC %md The following will create a __managed__ table in DBFS.

# COMMAND ----------

# MAGIC %sql 
# MAGIC CREATE TABLE IF NOT EXISTS $dlt_database.rules (
# MAGIC   rules_id bigint GENERATED ALWAYS AS IDENTITY (START WITH 0 INCREMENT BY 1),
# MAGIC   rule_name string,
# MAGIC   rule_category string,
# MAGIC   rule_description string,
# MAGIC   rule string,
# MAGIC   created_by string,
# MAGIC   updated_by string,
# MAGIC   created_date timestamp,
# MAGIC   updated_date timestamp 
# MAGIC )  COMMENT 'This table contains generic data quality rules that can be used DLT pipelines';

# COMMAND ----------

# MAGIC %sql 
# MAGIC CREATE TABLE IF NOT EXISTS $dlt_database.ingestion_map (
# MAGIC   map_id bigint GENERATED ALWAYS AS IDENTITY (START WITH 0 INCREMENT BY 1),
# MAGIC   source_location string,
# MAGIC   source_type string,
# MAGIC   source_details STRUCT<header:boolean, delimiter: string>,
# MAGIC   destination_table string,
# MAGIC   description string,
# MAGIC   status boolean,
# MAGIC   created_by string,
# MAGIC   updated_by string,
# MAGIC   created_date timestamp,
# MAGIC   updated_date timestamp
# MAGIC ) COMMENT 'This table mapping of source locations to DLT tables';

# COMMAND ----------

# MAGIC %md Reset tables

# COMMAND ----------

# MAGIC %sql
# MAGIC DROP TABLE IF EXISTS $dlt_database.rules;
# MAGIC DROP TABLE IF EXISTS $dlt_database.ingestion_map;

# COMMAND ----------


