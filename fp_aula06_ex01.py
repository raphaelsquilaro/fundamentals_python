# Author: Raphael Campos Squilaro
# Project Name: FP - Multiplication table with for loop

number = int(input('Digite um número para ver a tabuada: '))

print(f'Tabuada do {number}:')
for i in range(1, 101):
    print(f'{number} x {i} = {number * i}')

# or

for i in range(1, 101):
    resultado = number * i
    print(f'{number} x {i} = {resultado}')
