'''
Faça um programa que peça 3 lados de um triângulo. Identifique se os dados
representam um triângulo e também se o triângulo é equilátero (três lados iguais),
isósceles (dois lados iguais) ou escaleno (todos os lados diferentes).
'''

A, B, C = input('Digite os três lados do triângulo separados por espaço: ').split()
lista = [A,B,C]
lista1 = sorted(lista, key=float, reverse=True)
A = float(lista1[0])
B = float(lista1[1])
C = float(lista1[2])

if(A >= (B+C)):
    print('NAO FORMA TRIANGULO')

else:
    if (A ** 2) == (B ** 2 + C ** 2):
        print('TRIANGULO RETANGULO')

    if (A ** 2) > (B ** 2 + C ** 2):
        print('TRIANGULO OBTUSANGULO')

    if (A ** 2) < (B ** 2 + C ** 2):
        print('TRIANGULO ACUTANGULO')

    if A == B == C:
        print('TRIANGULO EQUILATERO')

    if ((A == B) and (C != (A or B))) or ((A == C) and (B != (A or C))) or ((B == C) and (C != (A or C))):
        print('TRIANGULO ISOSCELES')
