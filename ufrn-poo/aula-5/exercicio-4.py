'''
Crie um programa armazene todos os números digitados pelo usuário, então
coloque-os em ordem decrescente e imprima.
'''
lista = []
qtd = 0
while True:
    lista.append(int(input(f'Digite o {qtd}º numero ou 0 (zero) para sair: ')))

    if lista[qtd] == 0:
        break
    qtd += 1
print(sorted(lista, reverse=True))