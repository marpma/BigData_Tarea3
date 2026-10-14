import time
from pyspark.sql import SparkSession
from pyspark.sql import functions as F

spark = SparkSession.builder.appName("ProcesamientoContinuo").getOrCreate()
spark.sparkContext.setLogLevel("WARN")

print("Monitoreando datos en tiempo real...")
try:
    while True:
        try:
            df = spark.read.format('csv').option('header', 'true').option('inferSchema', 'true').load('streaming_batch_data.csv')
            print("\n--- Estado Actualizado del Lote ---")
            df.groupBy("ubicacion").agg(
                F.count("temperatura").alias("Total_Registros"),
                F.round(F.avg("temperatura"), 2).alias("Temp_Promedio")
            ).show()
        except Exception:
            print("Esperando archivo de datos...")
        time.sleep(4)
except KeyboardInterrupt:
    spark.stop()