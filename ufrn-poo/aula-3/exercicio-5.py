'''Para doar sangue é necessário ter entre 18 e 67 anos. Faça um programa que
pergunte a idade de uma pessoa e diga se ela pode doar sangue ou não.
'''

idade = int(input('Digite sua idade: '))


if  18 > idade <= 67:
    print(f'Sua idade é {idade}, Infelizmente você Não pode doar sangue!')
else:
    print(f'Sua idade é {idade}, você pode doar sangue!')