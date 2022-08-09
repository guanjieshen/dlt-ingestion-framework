# Databricks notebook source
dbutils.widgets.text('dlt_database', 'dlt')

# COMMAND ----------

def generate_dlt_tables(source):
  @dlt.table(
    name = source["destination_table"],
    comment = source["description"]
  )
  def create_ingestion_tables():    
    loc = source["source_location"]
    if source["source_type"] == "csv":
      print(source["source_location"])
      return (
        spark.read.format(source["source_type"])
          .option("delimiter", source["source_details"]["delimiter"])
          .option("header", source["source_details"]["header"])
          .load(source["source_location"])
       )

# COMMAND ----------

import dlt
from pyspark.sql.functions import *

database =dbutils.widgets.get('dlt_database')

# Get list of records to ingest into the platform
data_sources = (
  spark.read.format("delta")
    .table(f"{database}.ingestion_map")
    .where("status = 1")
    .collect()
)

for source in data_sources:
  generate_dlt_tables(source)

