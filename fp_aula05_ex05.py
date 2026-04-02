#Author: Raphael Campos Squilaro

#user write a number
#if the number is positive (> than 0), count from 1 to that number and print the count
#if the number is negative (< than 0), print that the number is negative
#if the number is zero, print that the number is zero

#Project Name: FP - Loop for with if-else

contadorp = 0 , contadorn = 0 , contadorz = 0

for i in range(10):
    digitado = int(input('Digite um número: '))
    if digitado > 0:
        contadorp = contadorp + 1 # contadorp += 1
        print(f'Contagem: {contadorp}')
    elif digitado < 0:
        contadorn = contadorn + 1 # contadorn += 1
        print(f'Contagem: {contadorn}')
    else:
        contadorz = contadorz + 1 # contadorz += 1
        print(f'Contagem: {contadorz}')     
