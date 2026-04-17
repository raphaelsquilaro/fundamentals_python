#Author: Raphael Campos Squilaro
#Project: dicionary

import requests

cep = input("Digite seu cep: ")

url = f"https://viacep.com.br/ws/{cep}/json/"
resposta = requests.get(url)
dados = resposta.json()

print()
print()
print(f"Logradouro: {dados['logradouro']}")
print(f"Bairro: {dados['bairro']}")
print(f"Cidade: {dados['localidade']}")
print(f"UF: {dados['uf']}")