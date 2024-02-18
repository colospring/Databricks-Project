# Databricks notebook source
# MAGIC %sql
# MAGIC select state_id as state, count(zip) as nzip
# MAGIC from uszips_delta_unmanaged
# MAGIC where state_id not in ('AS', 'GU','MP', 'PR','VI')
# MAGIC group by state
# MAGIC order by nzip

# COMMAND ----------

# MAGIC %sql
# MAGIC select state_id as state, sum(population) as population
# MAGIC from uszips_delta_unmanaged
# MAGIC where state_id not in ('AS', 'GU','MP', 'PR','VI')
# MAGIC group by state
# MAGIC order by state
