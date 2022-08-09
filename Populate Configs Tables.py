# Databricks notebook source
dbutils.widgets.removeAll()
dbutils.widgets.text("dlt_database","dlt","Database")

# COMMAND ----------

# MAGIC %md Example of adding source tables for DLT ingestion.

# COMMAND ----------

# MAGIC %sql
# MAGIC INSERT INTO
# MAGIC   $dlt_database.ingestion_map(
# MAGIC     source_location,
# MAGIC     source_type,
# MAGIC     source_details,
# MAGIC     destination_table,
# MAGIC     description,
# MAGIC     status,
# MAGIC     created_by,
# MAGIC     updated_by,
# MAGIC     created_date,
# MAGIC     updated_date
# MAGIC   )
# MAGIC VALUES
# MAGIC   (
# MAGIC     'dbfs:/mnt/guanjiestorage-delta/flightdelays',
# MAGIC     'csv',
# MAGIC     named_struct("header", 1, "delimiter", ","),
# MAGIC     "departure_delays_bronze",
# MAGIC     "Departure delays data",
# MAGIC     1,
# MAGIC     "guanjie.shen@databricks.com",
# MAGIC     "guanjie.shen@databricks.com",
# MAGIC     current_timestamp(),
# MAGIC     current_timestamp()
# MAGIC   ),
# MAGIC   (
# MAGIC     'dbfs:/mnt/guanjiestorage-delta/airports',
# MAGIC     'csv',
# MAGIC     named_struct("header", 1, "delimiter", "\t"),
# MAGIC     "airport_codes_bronze",
# MAGIC     "Airport Codes data",
# MAGIC     0,
# MAGIC     "guanjie.shen@databricks.com",
# MAGIC     "guanjie.shen@databricks.com",
# MAGIC     current_timestamp(),
# MAGIC     current_timestamp()
# MAGIC   );
# MAGIC SELECT
# MAGIC   *
# MAGIC FROM
# MAGIC   $dlt_database.ingestion_map

# COMMAND ----------

# MAGIC %sql
# MAGIC INSERT INTO
# MAGIC   $dlt_database.ingestion_map(
# MAGIC     source_location,
# MAGIC     source_type,
# MAGIC     source_details,
# MAGIC     destination_table,
# MAGIC     description,
# MAGIC     status,
# MAGIC     created_by,
# MAGIC     updated_by,
# MAGIC     created_date,
# MAGIC     updated_date
# MAGIC   )
# MAGIC VALUES
# MAGIC   (
# MAGIC     'dbfs:/mnt/guanjiestorage-delta/flightdelays',
# MAGIC     'csv',
# MAGIC     named_struct("header", 1, "delimiter", ","),
# MAGIC     "test_delays_bronze_1",
# MAGIC     "Departure delays data",
# MAGIC     1,
# MAGIC     "guanjie.shen@databricks.com",
# MAGIC     "guanjie.shen@databricks.com",
# MAGIC     current_timestamp(),
# MAGIC     current_timestamp()
# MAGIC   );
# MAGIC SELECT
# MAGIC   *
# MAGIC FROM
# MAGIC   $dlt_database.ingestion_map

# COMMAND ----------

# MAGIC %md Example of adding data quality rules as a part of the ingestion framework.
