from kafka import KafkaConsumer
from pyspark.sql import SparkSession
from pyspark.sql import Row
import json

# Kafka Consumer Configuration
kafka_topic = 'etl_dev_br_aptos_blocks'
kafka_servers = 'localhost:9092'  # Change to your Redpanda broker address

# Initialize Kafka Consumer
consumer = KafkaConsumer(
    kafka_topic,
    bootstrap_servers=kafka_servers,
    auto_offset_reset='earliest',
    group_id='my-group'  # Change as needed
)

# Initialize Spark Session for Delta Lake
spark = SparkSession.builder \
    .appName("DeltaLakeExample") \
    .config("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension") \
    .config("spark.sql.catalog.spark_catalog", "org.apache.spark.sql.delta.catalog.DeltaCatalog") \
    .getOrCreate()

# Path to your Delta Table
delta_table_path = '/path/to/delta/table'

# Consuming messages from Redpanda
for message in consumer:
    # Assuming the message value is a JSON string
    record = json.loads(message.value.decode('utf-8'))
    df = spark.createDataFrame([Row(**record)])
    
    # Writing to Delta Table
    df.write.format("delta").mode("append").save(delta_table_path)

    print(f"Processed message offset: {message.offset}")

# Stop the Spark session
spark.stop()
