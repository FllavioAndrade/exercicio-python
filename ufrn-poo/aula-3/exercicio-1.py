'''
Crie um programa que informe se o valor de entrada do usuário é positivo ou
negativo.
'''

valor = float(input('Digite um valor: ' ))
if valor > 0:
    print(f'{valor} é um número positivo!')
elif valor < 0:
    print(f'{valor} é um número negativo!')
else:
    print(f'{valor} é um número nulo!')