'''
Faça um programa que leia três números e mostre-os em ordem decrescente.
'''

a = int(input('Digite o primeiro numero: '))
b = int(input('Digite o segundo numero: '))
c = int(input('Digite o terceiro numero: '))

lista = [a,b,c]
lista.sort(reverse=True)
print(lista)