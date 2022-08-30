'''
Leia a hora inicial e a hora final de um jogo. A seguir calcule a duração do jogo, sabendo que o mesmo pode começar em um dia e terminar em outro, tendo uma duração mínima de 1 hora e máxima de 24 horas.

Entrada
A entrada contém dois valores inteiros representando a hora de início e a hora de fim do jogo.

Saída
Apresente a duração do jogo conforme exemplo abaixo.

Exemplos de Entrada
16 2

Exemplos de Saída
O JOGO DUROU 10 HORA(S)

Exemplos de Entrada
0 0

Exemplos de Saída
O JOGO DUROU 24 HORA(S)

'''

A, B, = input().split()
A = int(A)
B = int(B)

if(A == B):
    print('O JOGO DUROU 24 HORA(S)')

elif (A > B):
    print(f'O JOGO DUROU {24 + B - A} HORA(S)')
elif (B > A):
    print(f'O JOGO DUROU {B-A} HORA(S)')