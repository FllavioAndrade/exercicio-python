'''
Faça um programa que receba três inteiros e diga qual deles é o maior e qual o
menor.
'''


a = int(input('Digite o primeiro numero: '))
b = int(input('Digite o segundo numero: '))
c = int(input('Digite o terceiro numero: '))

print(f'O maior número é o {max(a,b,c)}')
print(f'O menor número é o {min(a,b,c)}')