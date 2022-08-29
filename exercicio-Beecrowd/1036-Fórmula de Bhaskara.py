'''
Leia 3 valores de ponto flutuante e efetue o cálculo das raízes da equação de Bhaskara. Se não for possível calcular as raízes, mostre a mensagem correspondente “Impossivel calcular”, caso haja uma divisão por 0 ou raiz de numero negativo.

Entrada
Leia três valores de ponto flutuante (double) A, B e C.

Saída
Se não houver possibilidade de calcular as raízes, apresente a mensagem "Impossivel calcular". Caso contrário, imprima o resultado das raízes com 5 dígitos após o ponto, com uma mensagem correspondente conforme exemplo abaixo. Imprima sempre o final de linha após cada mensagem.

Exemplo de Entrada
10.0 20.1 5.1

Exemplo de Saída
R1 = -0.29788
R2 = -1.71212

Exemplo de Entrada
0.0 20.0 5.0

Exemplo de Saída
Impossivel calcular

'''

A, B, C = input().split()
A = float(A)
B = float(B)
C = float(C)

delta = ((B**2)-(4*A*C))**0.5
if (((B**2)-(4*A*C) < 0) | (A == 0)):
    print("Impossivel calcular")
else:
    R1 = (-B + (delta)) / (2*A)
    R2 = (-B - (delta)) / (2*A)
    print(f'R1 = {R1:.5f}\nR2 = {R2:.5f}')