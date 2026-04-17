#Author: Raphael Campos Squilaro
#Project: dicionary - challenge

import requests

latitude = input("Digite uma Latitude: ")
longitude = input("Digite uma Longitude: ")

url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m,wind_speed_10m&hourly=temperature_2m,relative_humidity_2m,wind_speed_10m"

resposta = requests.get(url)
dados = resposta.json()

print()
print(f"temperature_2m: {dados['current']['temperature_2m']}")
print(f"wind_speed_10m: {dados['current']['wind_speed_10m']}")