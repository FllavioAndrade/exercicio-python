'''
 Escreva um programa que receba dez inserções do usuário e imprima a metade de
cada um deles, a soma total e a média aritmética.
'''
soma = 0
n = range(10)
for i in n:

    valor = int(input(f'Digite o {i+1}º valor: '))
    print(f'A Metade de {valor} = {valor/2}\n')
    soma = soma+valor
print(f'SOMATORIO: {soma}\nMEDIA: {soma/10}')