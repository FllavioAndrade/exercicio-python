'''
Crie dois conjuntos aleatórios de 15 posições com valores aleatórios de a-z. Depois
diga quais elementos são iguais e quais são diferentes entre esses dois conjuntos.
'''

import random

lista1 = []
lista2 = []
iguais = []
iguaisNovo = []
diferentes = []
diferentesNovo = []

for i in range(15):
    lista1.append(chr(random.randint(97, 122)))

for i in range(15):
    lista2.append(chr(random.randint(97, 122)))

lista1 = sorted(lista1)
lista2 = sorted(lista2)

for i in range(97,):
    if lista1[i] not in lista2:
        diferentes.append(lista1[i])
    else:
        iguais.append(lista1[i])
iguais = sorted(iguais)

for i in range(15):
    if lista2[i] not in lista1:
        diferentes.append(lista2[i])
diferentes = sorted(diferentes)

for i in range(len(diferentes)):
    if diferentes[i] not in diferentes:
        diferentesNovo.append(diferentes[i])

print(lista1)
print(lista2)
print(iguais)
print(diferentes)
print(diferentesNovo)



