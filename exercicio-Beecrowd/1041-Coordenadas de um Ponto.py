'''
Leia 2 valores com uma casa decimal (x e y), que devem representar as coordenadas de um ponto em um plano. A seguir, determine qual o quadrante ao qual pertence o ponto, ou se está sobre um dos eixos cartesianos ou na origem (x = y = 0).



Se o ponto estiver na origem, escreva a mensagem “Origem”.

Se o ponto estiver sobre um dos eixos escreva “Eixo X” ou “Eixo Y”, conforme for a situação.

Entrada
A entrada contem as coordenadas de um ponto.

Saída
A saída deve apresentar o quadrante em que o ponto se encontra.

Exemplos de Entrada
4.5 -2.2

Exemplos de Saída
Q4

Exemplos de Entrada
0.0 0.0

Exemplos de Saída
Origem
'''

N1, N2, = input().split()
N1 = float(N1)
N2 = float(N2)

if (N1 > 0.0) & (N2 > 0.0):
    print('Q1')
elif (N1 < 0.0) & (N2 > 0.0):
    print('Q1')
elif (N1 < 0.0) & (N2 < 0.0):
    print('Q3')
elif (N1 > 0.0) & (N2 < 0.0):
    print('Q4')
elif (N1 == N2 == 0.0):
    print('Origem')
elif (N1 == 0.0) & (N2 != 0.0):
    print('Eixo Y')
else:
    print('Eixo X')