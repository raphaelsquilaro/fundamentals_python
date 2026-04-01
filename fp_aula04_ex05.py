# Author: Raphael Campos Squilaro
# Project Name: FP - Drive license and Bafometre Test Program

idade = int(input('Digite a sua idade: '))
bebida = input('Você consumiu bebida alcoólica? (sim/não): ')

if idade >= 18 and bebida != 'sim':
    print('Você pode dirigir!')
else:
    print('Você não pode dirigir!')
