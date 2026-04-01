# Author: Raphael Campos Squilaro
# Project Name: FP - User Authentication Program

usuario = 'raphael'
senha = '123456'

acesso = input('Digite seu usuário: ')
senhaD = input('Digite sua senha: ')

if usuario == acesso and senha == senhaD:
    print('Acesso Aceito')
else:
    print('Acesso Negado')
