'''
Leia a hora inicial, minuto inicial, hora final e minuto final de um jogo. A seguir calcule a duração do jogo.

Obs: O jogo tem duração mínima de um (1) minuto e duração máxima de 24 horas.

Entrada
Quatro números inteiros representando a hora de início e fim do jogo.

Saída
Mostre a seguinte mensagem: “O JOGO DUROU XXX HORA(S) E YYY MINUTO(S)” .

Exemplos de Entrada
7 8 9 10


Exemplos de Saída
O JOGO DUROU 2 HORA(S) E 2 MINUTO(S)

Exemplos de Entrada
7 7 7 7

Exemplos de Saída
O JOGO DUROU 24 HORA(S) E 0 MINUTO(S)


Exemplos de Entrada
7 10 8 9

Exemplos de Saída
O JOGO DUROU 0 HORA(S) E 59 MINUTO(S)

'''
A, B, C, D = input().split()
A = int(A)
B = int(B)
C = int(C)
D = int(D)

if (A == C):

    if (D > B):
        print(f'O JOGO DUROU 0 HORA(S) E {D - B} MINUTO(S)')

    elif (D == B):
        print(f'O JOGO DUROU 24 HORA(S) E {D - B} MINUTO(S)')
    else:
        print(f'O JOGO DUROU 23 HORA(S) E {60 + D - B} MINUTO(S)')

elif (A > C):

    if (D >= B):
        print(f'O JOGO DUROU {24 + C - A} HORA(S) E {D - B} MINUTO(S)')
    else:
        print(f'O JOGO DUROU {23 + C - A} HORA(S) E {60 + D - B} MINUTO(S)')

else:
    if D >= B:
        print(f'O JOGO DUROU {C - A} HORA(S) E {D - B} MINUTO(S)')
    else:
        if ((C - A) == 1):
            C = C - 1
    print(f'O JOGO DUROU {C - A} HORA(S) E {60 + D - B} MINUTO(S)')
