# Author: Raphael Campos Squilaro
# Project Name: FP - Program to Person have driving license or not and bafometre test

license = input('Possui carteira de motorista? (sim/não): ')
bafometro = input('Passou no resultado do bafometro? (sim/não): ')

if license == 'sim' and bafometro == 'sim':
    print('Pode dirigir!')
else:
    print('Não pode dirigir!')