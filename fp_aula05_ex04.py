# Author: Raphael Campos Squilaro
# Project Name: FP - Fatorization with for loop

number = int(input('Digite um número para fatorar: '))
fatorial = 1
for i in range(1, number + 1):
    fatorial *= i
    print(f'O número {i} tem o fatorial: {fatorial}')
print(f'O fatorial de {number} é: {fatorial}')
