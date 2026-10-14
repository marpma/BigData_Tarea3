from pyspark.sql import SparkSession
from pyspark.sql import functions as F

spark = SparkSession.builder.appName("ProcesamientoBatchSensores").getOrCreate()
spark.sparkContext.setLogLevel("WARN")

print("=== 1. CARGA DEL CONJUNTO DE DATOS (BATCH) ===")
df = spark.read.format('csv').option('header', 'true').option('inferSchema', 'true').load('batch_data.csv')
df.show()

print("=== 2. LIMPIEZA Y TRANSFORMACIÓN ===")
df_limpio = df.na.drop()
df_transformado = df_limpio.withColumn(
    "Nivel_Riesgo",
    F.when(F.col("temperatura") > 30, "Alto").otherwise("Bajo")
)
df_transformado.show()

print("=== 3. ANÁLISIS EXPLORATORIO (EDA) Y ESTADÍSTICAS ===")
df_transformado.select("temperatura").summary().show()

df_transformado.groupBy("ubicacion") \
    .agg(
        F.round(F.avg("temperatura"), 2).alias("Temp_Promedio"),
        F.max("temperatura").alias("Temp_Maxima"),
        F.min("temperatura").alias("Temp_Minima")
    ).show()

print("=== 4. VISUALIZACIÓN DE RESULTADOS ===")
df_transformado.filter(F.col("estado") == "Alerta").show()

spark.stop()