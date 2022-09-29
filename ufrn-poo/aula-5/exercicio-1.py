'''
Escreva um programa que receba uma frase do usuário e separe por palavras.
Depois diga quantas letras tem cada palavra e quantas palavras foram escritas.
'''

frase = input('Digite uma frase: ')
qtdPalavra = frase.count(' ')
palavra = frase.split()
print(f'A frase possui {qtdPalavra+1} Palavras\n')
for i in range(qtdPalavra):
    qtdLetra = len(palavra[i])
    print(f'A palavra "{palavra[i]}" contém "{qtdLetra}" Letra(s)!')
