'''
Crie um algoritmo que receba 10 números do usuário e imprima o maior valor entre
eles.
'''

numero = []
for i in range(10):
    numero.append(int(input(f'Digite o {i+1}º numero: ')))
print(f'O Maior número digitado foi {max(numero)}')