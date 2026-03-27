# Author: Raphael Campos Squilaro
# Project Name: FP - Program to Create Credencial Card with User with Age +18

name = input('Digite seu nome: ')
age = int(input('Digite sua idade: '))
credits = input('Possui credencial: ')

if age >= 18 and credits == 'sim':
    print(f'Parabéns {name}, você tem acesso a credencial!')
else:
    print(f'Infelizmente {name}, você não tem acesso a credencial!')