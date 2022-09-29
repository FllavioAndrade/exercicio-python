'''
Escreva um programa que lê uma frase do usuário e retorne em quais posições a
letra ‘a’ apareceram.
'''

frase = input('Digite uma frase: ')
qtd = len(frase)
a = 0
print('A leta "a" se encontra nas posições:')
for i in range(qtd):
    if (frase[i] == 'a'):
        print(i)
