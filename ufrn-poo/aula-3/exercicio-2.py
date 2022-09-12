'''
faça um programa para a leitura de três notas parciais de um aluno. A mensagem
“Aprovado”, se a média alcançada for maior ou igual a sete;A mensagem “Aprovado
com Distinção”, se a média for igual a dez;A mensagem “Reprovado” se a média for
menor de do que sete;.
'''

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
nota3 = float(input('Digite a terceira nota: '))

media = (nota1+nota2+nota3)/3

if media == 10:
    print(f'APROVADO COM DISTINÇÃO!!\nMÉDIA = {media:.2f}')

elif media >= 7:
    print(f'APROVADO!!\nMÉDIA = ({media:.2f})')
else:
    print(f'REPROVADO!!\nMÉDIA = {media:.2f}')