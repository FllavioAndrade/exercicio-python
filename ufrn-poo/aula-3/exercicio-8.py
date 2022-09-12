'''
Faça um programa que gere um número aleatório, mas só imprime se for negativo
ou maior que mil
'''
import random

numero = random.randint(-2000,2000)
if numero < 0 or numero > 1000:
    print(numero)