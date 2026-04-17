#Author: Raphael Campos Squilaro
#Project: dicionary

import requests

url = "https://economia.awesomeapi.com.br/last/USD-BRL"
resposta = requests.get(url)
dados = resposta.json()

valor_dolar = dados['USDBRL']['bid']

print(f"Cotação atual do dólar: {valor_dolar}")
