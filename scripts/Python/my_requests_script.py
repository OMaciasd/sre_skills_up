import requests
import time

url = 'http://localhost:5000'

while True:
    try:
        response = requests.get(url)
        response.raise_for_status()
        print(f"Estado de la respuesta: {response.status_code}")
    except requests.exceptions.ConnectionError as e:
        print("Estado del servidor: Error de conexión 500.")
    except requests.exceptions.HTTPError as e:
        print(f"Error HTTP: {e}")
        print("Estado del servidor: Error HTTP")
    except requests.exceptions.RequestException as e:
        print(f"Error en la solicitud: {e}")
        print("Estado del servidor: Error en la solicitud")
    time.sleep(5)
