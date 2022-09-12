'''
Escreva um programa que imprima todos os números múltiplos de 5, no intervalo
fechado de 1 a 500
'''

n = range(501)
for i in n:
    if i%5 == 0:
        print(i)
