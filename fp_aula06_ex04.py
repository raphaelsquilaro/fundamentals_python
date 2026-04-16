# Author: Raphael Campos Squilaro
# Project Name: FP - Fatorization of a number with while loop

number = int(input('Digite um número para fatorar: '))
fatorial = 1
i = 1
while i <= number:
    fatorial *= i # fatorial = fatorial * i
    print(f'O número {i} tem o fatorial: {fatorial}')
    i += 1
print(50*'-')
print(f'O fatorial de {number} é: {fatorial}')

number = int(input('Digite um número para fatorar: '))
fatorial = 1
while number > 0:
    fatorial = fatorial * number
    number = number - 1
    print(f'Variavel number: {number}, Variavel fatorial: {fatorial}')
print(50*'-')
print(f'O fatorial é: {fatorial}')
