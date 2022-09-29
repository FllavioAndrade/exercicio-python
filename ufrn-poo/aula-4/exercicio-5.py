'''
Crie um algoritmo que receba 2 valores e imprima todos os valores pares do
intervalo fechado entre eles.
'''

x = int(input('Digite o primeiro numero do intervalo: '))
y = int(input('Digite o ultimo numero do intervalo: '))
for i in range(x,y+1):
    if(i%2 == 0):
        print(i)