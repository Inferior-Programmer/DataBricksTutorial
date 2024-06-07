# Databricks notebook source
# MAGIC %run ../../Includes/_common

# COMMAND ----------

lesson_config = LessonConfig(name=None,
                             create_schema=True,
                             create_catalog=False,
                             requires_uc=False,
                             installing_datasets=True,
                             enable_streaming_support=False,
                             enable_ml_support = False)

DA = DBAcademyHelper(course_config=course_config,
                     lesson_config=lesson_config)
DA.reset_lesson()
DA.init()
DA.conclude_setup()

# COMMAND ----------

# TODO
my_name = "Jeremy"

# COMMAND ----------

example_df = spark.range(16)
spark.read.load(f"{DA.paths.datasets}/nyctaxi-with-zipcodes/data").write.mode("overwrite").saveAsTable("nyc_taxi")
