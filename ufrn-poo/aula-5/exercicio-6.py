'''
Faça um programa que una duas listas aleatórias de inteiros, com 100 entradas, e
diga quais números são primos e em que posição eles aparecem.
'''

import random
lista1 = []
lista2 = []
lista3 = []
primos = []
qtd = 0;
for i in range(100):
    lista1.append(random.randint(1, 1000))

for i in range(100):
    lista2.append(random.randint(1, 1000))

lista3 = lista1+lista2

tamanho = len(lista3)
for i in range(tamanho):
    if ((lista3[i] % 2 == 0) and (lista3[i] != 2)) or \
         ((lista3[i] % 3 == 0) and (lista3[i] != 3)) or \
         ((lista3[i] % 5 == 0) and (lista3[i] != 5)) or \
         ((lista3[i] % 7 == 0) and (lista3[i] != 7)):
        qtd +=0
    elif lista3[i] > 1:
        qtd += 1
        primos.append(lista3[i])
print (f'da lista {sorted(lista3)}\nTemos {qtd} numero(s) Primos')
print (f'{sorted(primos)}')