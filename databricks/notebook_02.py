# Databricks notebook source
# Importing necessary libraries
from pyspark.sql.functions import countDistinct

# Reading the cars table
cars = spark.table("cars")

# Getting the number of unique car types
unique_types_count = cars.select(countDistinct("Type")).collect()[0][0]

# Printing the result
print("汽车类型数为：", unique_types_count)
