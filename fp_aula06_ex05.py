# Author: Raphael Campos Squilaro
# Project Name: FP - Multiplication table of 2, 3 and 4 with while loop

i = 2
j = 1
while i <= 4:
    print(f'Tabuada do {i}:')
    while j <= 10:
        print(f'{i} x {j} = {i * j}')
        j += 1
    print(50 * '-')
    i += 1
    j = 1
print ('Feito por Raphael Campos Squilaro :D')