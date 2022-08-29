'''
Leia 3 valores reais (A, B e C) e verifique se eles formam ou não um triângulo. Em caso positivo, calcule o perímetro do triângulo e apresente a mensagem:

Perimetro = XX.X

Em caso negativo, calcule a área do trapézio que tem A e B como base e C como altura, mostrando a mensagem

Area = XX.X

Entrada
6.0 4.0 2.0

Saída
Area = 10.0

Exemplos de Entrada
6.0 4.0 2.1

Exemplos de Saída
Perimetro = 12.1

'''

A, B, C = input().split()
A = float(A)
B = float(B)
C = float(C)

if ((abs(B-C) < A) & (A > (B+C))) or ((abs(A-C) < B) & (B > (A+C))) or ((abs(A-B) < C) & (C > (A+B))):
    perimetro = (A + B + C)
    print(f'Perimetro {perimetro:.1f}')
else:
    area = ((A + B) / 2)*C
    print(f'Area = {area:.1f}')

