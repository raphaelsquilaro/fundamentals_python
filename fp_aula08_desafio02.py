#Author: Raphael Campos Squilaro
#Project: dicionary - challenge

import requests

url = "https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL"

resposta = requests.get(url)
dados = resposta.json()

cotacao_dollar = float(dados['USDBRL']['bid'])

print(f"Cotação atual do Dólar: R$ {cotacao_dollar:.2f}")

entrada_usuario = input("Digite uma quantia em dólares (US$): ")
valor_em_dolar = float(entrada_usuario)

reais1 = valor_em_dolar * cotacao_dollar

print(f"US$ {valor_em_dolar:.2f} equivalem a R$ {reais1:.2f}")

# ===============================================================

cotacao_euro = float(dados['EURBRL']['bid'])

print(f"Cotação atual do Euro: R$ {cotacao_euro:.2f}")

entrada_usuario = input("Digite uma quantia em Euro (EUR$): ")
valor_em_dolar = float(entrada_usuario)

reais2 = valor_em_dolar * cotacao_euro

print(f"US$ {valor_em_dolar:.2f} equivalem a R$ {reais2:.2f}")

#=================================================================

cotacao_bitcoin = float(dados['BTCBRL']['bid'])

print(f"Cotação atual do Bitcoin: R$ {cotacao_bitcoin:.2f}")

entrada_usuario = input("Digite uma quantia em Bitcoin (BTC$): ")
valor_em_dolar = float(entrada_usuario)

reais3 = valor_em_dolar * cotacao_bitcoin

print(f"US$ {valor_em_dolar:.2f} equivalem a R$ {reais3:.2f}")