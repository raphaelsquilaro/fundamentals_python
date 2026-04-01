# Author: Raphael Campos Squilaro
# Project Name: FP - Program to Calculate Area of a Land

# 1. Recebendo as entradas do usuário
# Usamos float() para permitir números decimais (ex: 10.5m)
largura = float(input("Digite a largura do terreno (metros): "))
comprimento = float(input("Digite o comprimento do terreno (metros): "))

# 2. Calculando a área (largura x comprimento)
area = largura * comprimento

# 4. Exibindo os resultados
print(f"ÁREA DO TERRENO: {area:.2f} m²")
