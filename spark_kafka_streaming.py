from pyspark.sql import SparkSession
from pyspark.sql.streaming import *
from pyspark.sql.functions import explode
from pyspark.sql.functions import split

spark = SparkSession \
    .builder \
    .appName("Spark Kafka Streaming") \
    .config("spark.jars.packages", "org.apache.spark:spark-sql-kafka-0-10_2.12:3.2.1") \
    .getOrCreate()

spark.sparkContext.setLogLevel('WARN')

lines = spark \
    .readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "broker:29092") \
    .option("subscribe", "demo") \
    .load()


lines.selectExpr("CAST(value AS STRING)")
words = lines.select(explode(split(lines.value, ' ')).alias("word"))

# generate running word count
wordCount = words.groupBy("word").count()

# start running the query that prints the running counts in the console
query = wordCount \
    .writeStream \
    .outputMode("complete") \
    .format("console") \
    .start()


query.awaitTermination()
