import requests
import time

url = 'http://localhost:5000'

while True:
    response = requests.get(url)
    print(f"Status Code: {response.status_code}")
    time.sleep(5)  # Espera 5 segundos entre solicitudes
