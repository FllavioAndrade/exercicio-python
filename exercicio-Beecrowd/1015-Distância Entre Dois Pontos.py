'''
Leia os quatro valores correspondentes aos eixos x e y de dois pontos quaisquer no plano, p1(x1,y1) e p2(x2,y2) e calcule a distância entre eles, mostrando 4 casas decimais após a vírgula, segundo a fórmula:

(((x2-x1)**2)+((y2-y1)**2))**(1/2)

Exemplos de Entrada
1.0 7.0
5.0 9.0

Exemplos de Saída
4.4721

'''
x1, y1 = input().split()
x2, y2 = input().split()

x1 = float(x1)
y1 = float(y1)
x2 = float(x2)
y2 = float(y2)

distancia = (((x2-x1)**2)+((y2-y1)**2))**(1/2)

print(f'{distancia:.4f}')

