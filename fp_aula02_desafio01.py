# Author: Raphael Campos Squilaro
# Project Name: FP - Ethanol or Gasoline Cost-Effectiveness Calculator

"""
A empresa |ABC deseja melhorar seu consumo com os carros.
A empresa deseja inicialmente analisar o desempenho dos carros.

A empresa precisa saber se compensa abastecer com etanol ou gasolina

dados devem ser apresentados da seguinte forma:
nome da empresa_carro_combustível_consumo
formatados com 2 casas decimais
Gasolina - R$ 6,69 o litro
Etanol - R$ 4,61 o litro
"""

# Recebendo as entradas do usuário
nome_empresa = input("Digite o nome da empresa: ")
modelo_carro = input("Digite o modelo do carro: ")
tipo_combustivel = input("Digite o tipo de combustível (Gasolina ou Etanol): ")
consumo_km_por_litro = float(input("Digite o consumo do carro (km por litro): "))

# Preços dos combustíveis
preco_gasolina = 6.69
preco_etanol = 4.61
# Calculando o custo por km para cada combustível
custo_gasolina_por_km = preco_gasolina / consumo_km_por_litro
custo_etanol_por_km = preco_etanol / consumo_km_por_litro
# Determinando qual combustível é mais econômico
if custo_gasolina_por_km < custo_etanol_por_km:
    combustivel_mais_economico = "Gasolina"
    custo_mais_economico = custo_gasolina_por_km
else:
    combustivel_mais_economico = "Etanol"
    custo_mais_economico = custo_etanol_por_km
# Exibindo os resultados formatados
print("-" * 50)
print(f"Empresa: {nome_empresa}")
print(f"Modelo do Carro: {modelo_carro}")
print(f"Tipo de Combustível: {tipo_combustivel}")
print(f"Consumo: {consumo_km_por_litro:.2f} km/l")
print(f"Custo por km com Gasolina: R$ {custo_gasolina_por_km:.2f}")
print(f"Custo por km com Etanol: R$ {custo_etanol_por_km:.2f}")
print(f"Combustível mais econômico: {combustivel_mais_economico} (R$ {custo_mais_economico:.2f} por km)")
print("-" * 50)
