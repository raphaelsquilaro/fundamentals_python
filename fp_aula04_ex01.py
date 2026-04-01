# Author: Raphael Campos Squilaro
# Project Name: FP - User Authentication Program with Username and Password

user = 'raphael'
password = 'metallica'

access_user = input('Digite seu usuário: ')
access_password = input('Digite sua senha: ')

#and é um operador lógico que retorna True se ambas as condições forem verdadeiras

if user == access_user and password == access_password:
    print('Acesso Aceito')
