# Tarea 3 - Procesamiento de Datos con Apache Spark

Repositorio correspondiente a la Tarea 3 del curso de Big Data, enfocado en la implementación de procesamiento por lotes (Batch) y procesamiento en tiempo real (Streaming) utilizando Apache Spark y Python (PySpark).

## 👨‍💻 Autor

* **Nombre:** Miguel Ángel Rodríguez Pacheco

* **Institución:** Universidad Nacional Abierta y a Distancia (UNAD)

## 📂 Estructura del Repositorio

El repositorio contiene los scripts desarrollados para la práctica:

* `batch_data.csv`: Conjunto de datos base estructurado para el análisis por lotes.

* `batch_analysis.py`: Script de PySpark para la carga, limpieza, transformación y análisis exploratorio de datos (EDA) en Batch.

* `generador_lote_largo.py`: Script productor/generador que emite registros de manera progresiva para la simulación.

* `procesador_continuo.py`: Script consumidor de PySpark que procesa y muestra las métricas en tiempo real.

## ⚙️ Instrucciones de Ejecución

### 1. Procesamiento Batch (Lotes)

Ejecuta el análisis exploratorio y estadístico con el siguiente comando:

```
python3 batch_analysis.py

```

### 2. Procesamiento en Tiempo Real (Streaming)

* **Terminal 1 (Consumidor):**

  ```
  python3 procesador_continuo.py
  
  ```

* **Terminal 2 (Productor):**

  ```
  python3 generador_lote_largo.py
  
  ```