from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("PythonSSAS").getOrCreate()

df = spark.read \
    .format("com.microsoft.sqlserver.jdbc.spark") \
    .option("url", "jdbc:sqlserver://localhost:1433;databaseName=AdventureWorksDW2016CTP3") \
    .option("query", "SELECT * FROM FactInternetSales") \
    .option("user", "username") \
    .option("password", "password") \
    .load()

df.show()