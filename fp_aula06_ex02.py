# Author: Raphael Campos Squilaro
# Project Name: FP - Multiplication table with while loop

num = int(input('Digite um número para ver a tabuada: '))
print(f'Tabuada do {num}:')
i = 1
while i <= 100:
    print(f'{num} x {i} = {num * i}')
    i += 1