'''
Escreva um programa que recebe um valor inteiro do usuário e informe se o número
é par ou ímpar.
'''

numero = int(input('Digite um número: '))
if numero%2 == 0:
    print(f'O número {numero} é PAR')
else:
    print(f'O número {numero} é IMPAR')