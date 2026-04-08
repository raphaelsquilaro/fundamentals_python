# Author: Raphael Campos Squilaro
# Project Name: FP - Ethanol or Gasoline Cost-Effectiveness Calculator

gasolina_preco = 6.69
etanol_preco = 4.61

consumo_km_por_litro = float(input("Digite o consumo do carro (km por litro): "))
custo_gasolina_por_km = gasolina_preco / consumo_km_por_litro
custo_etanol_por_km = etanol_preco / consumo_km_por_litro

if custo_gasolina_por_km < custo_etanol_por_km:
    print("Gasolina é mais vantajosa para abastecer os carros.")
else:
    print("Etanol é mais vantajoso para abastecer os carros.")