import time
import random

print("=== INICIANDO GENERADOR EN TIEMPO REAL ===")
with open("streaming_batch_data.csv", "w") as f:
    f.write("id_sensor,ubicacion,temperatura,humedad,estado\n")
    f.flush()

for i in range(1, 71):
    sensor_id = random.randint(101, 105)
    temperatura = round(random.uniform(21.0, 38.5), 2)
    humedad = round(random.uniform(40.0, 75.0), 2)
    estado = "Alerta" if temperatura > 32.0 else "Normal"
    
    registro = f"{sensor_id},Zona_Simulada,{temperatura},{humedad},{estado}\n"
    with open("streaming_batch_data.csv", "a") as f:
        f.write(registro)
        f.flush()
        
    print(f"[{i}/70] Enviado -> Sensor: {sensor_id} | Temp: {temperatura}°C | Estado: {estado}")
    time.sleep(2.5)

print("=== GENERACIÓN FINALIZADA ===")