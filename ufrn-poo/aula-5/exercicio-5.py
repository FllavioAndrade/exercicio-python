'''
Faça um programa que diga quantos números negativos há em uma lista.
'''

import random
lista = []
qtd = 0;
for i in range(20):
    lista.append(random.randint(-100, 100))
tamanho = len(lista)
for i in range(tamanho):
    if lista[i] <= 0:
        qtd += 1
print (f'Na lista {lista} \ntemos {qtd} numero(s) Negativos')
