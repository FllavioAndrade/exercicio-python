'''
Elabore um programa que leia dois valores numéricos reais e desconhecidos,
representados por A e B. Apresente o resultado das quatro operações aritméticas
básicas (soma, subtração, divisão e multiplicação) entre eles.
'''

x = float(input('Digite o primeiro numero: '))
y = float(input('Digite o segundo numero: '))

print(f'SOMA:{x} + {y} = {x+y}\nSUBTRAÇÃO:{x} - {y} = {x-y}\n'
      f'PRODUTO:{x} x {y} = {x*y}\nRAZÃO:{x} / {y} = {x/y}\n ')