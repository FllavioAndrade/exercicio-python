'''
Leia 3 valores inteiros e ordene-os em ordem crescente. No final, mostre os valores em ordem crescente, uma linha em branco e em seguida, os valores na sequência como foram lidos.

Entrada
A entrada contem três números inteiros.

Saída
Imprima a saída conforme foi especificado.

Exemplos de Entrada
7 21 -14

Exemplos de Saída

-14
7
21

7
21
-14

Exemplos de Entrada
-14 21 7


Exemplos de Saída
-14
7
21

-14
21
7
'''

N1, N2, N3 = input().split()
lista1 = [N1, N2, N3]
lista2 = sorted(lista1, key=int)

for (i) in range(3):
    print(lista2[i])
print()
for (i) in range(3):
    print(lista1[i])