# Author: Raphael Campos Squilaro
# Project: IMC calculator with if-elif-else

peso = float(input("Digite seu peso (kg): "))
altura = float(input("Digite sua Altura (m): "))

imc = peso / (altura ** 2)

if(imc < 18.5):
    print("Abaixo do peso (Magreza)")
elif(imc >= 18.5 and imc < 24.9):
    print("Eutrófico (Peso Normal)")
elif(imc >= 24.9 and imc < 29.9):
    print("Sobrepeso")
elif(imc >= 29.9 and imc < 34.9):
    print("Obesidade I")
elif(imc >= 34.9 and imc < 39.9):
    print("Obesidade Grau II (Severa)")
else:
    print("Obesidade Grau III (Mórbida/Grave)")
