# datosjson.py
import json
from datetime import datetime

# Definir el nombre del archivo JSON
nombre_archivo = 'myfile.json'

try:
    # Abrir el archivo JSON en modo lectura
    with open(nombre_archivo, 'r') as json_file:
        # Cargar el contenido del archivo JSON en la variable ourjson
        ourjson = json.load(json_file)

    # Verificar si la clave 'tokens' existe y es una lista
    if 'tokens' in ourjson and isinstance(ourjson['tokens'], list):
        # Iterar a través de cada token en la lista
        for item in ourjson['tokens']:
            token_value = item.get('token')
            expiry_time_str = item.get('expiry_time')

            if token_value and expiry_time_str:
                # Convertir la cadena de tiempo de expiración a un objeto datetime
                expire_datetime = datetime.fromisoformat(expiry_time_str.replace('Z', '+00:00'))
                # Obtener la fecha y hora actual (considerando la zona horaria local)
                now = datetime.now()
                # Calcular el tiempo restante
                time_remaining = expire_datetime - now

                print(f"Token: {token_value}")
                if time_remaining.total_seconds() > 0:
                    days = time_remaining.days
                    seconds = time_remaining.seconds
                    hours = seconds // 3600
                    minutes = (seconds % 3600) // 60
                    remaining_str = f"{days} días, {hours} horas, {minutes} minutos"
                    print(f"  Expira en: {remaining_str}")
                else:
                    print("  ¡El token ha expirado!")
                print("-" * 20)
            else:
                print("Advertencia: Datos de token incompletos.")
                print("-" * 20)
    else:
        print("Advertencia: No se encontró la lista de 'tokens' en el archivo JSON.")

except FileNotFoundError:
    print(f"Error: El archivo '{nombre_archivo}' no fue encontrado en la máquina virtual.")
except json.JSONDecodeError:
    print(f"Error: El archivo '{nombre_archivo}' contiene un formato JSON inválido.")
except Exception as e:
    print(f"Ocurrió un error inesperado: {e}")