'''
Leia um valor de ponto flutuante com duas casas decimais. Este valor representa um valor monetário. A seguir, calcule o menor número de notas e moedas possíveis no qual o valor pode ser decomposto. As notas consideradas são de 100, 50, 20, 10, 5, 2. As moedas possíveis são de 1, 0.50, 0.25, 0.10, 0.05 e 0.01. A seguir mostre a relação de notas necessárias.

Entrada
O arquivo de entrada contém um valor de ponto flutuante N (0 ≤ N ≤ 1000000.00).

Saída
Imprima a quantidade mínima de notas e moedas necessárias para trocar o valor inicial, conforme exemplo fornecido.

Obs: Utilize ponto (.) para separar a parte decimal.

Exemplo de Entrada
576.73

Exemplo de Saída

NOTAS:
5 nota(s) de R$ 100.00
1 nota(s) de R$ 50.00
1 nota(s) de R$ 20.00
0 nota(s) de R$ 10.00
1 nota(s) de R$ 5.00
0 nota(s) de R$ 2.00
MOEDAS:
1 moeda(s) de R$ 1.00
1 moeda(s) de R$ 0.50
0 moeda(s) de R$ 0.25
2 moeda(s) de R$ 0.10
0 moeda(s) de R$ 0.05
3 moeda(s) de R$ 0.01

'''

cedula = float(input())
print("NOTAS:")
z = cedula
a = int(cedula//100)

cedula = cedula%100
b = int(cedula//50)

cedula = cedula%50
c = int(cedula//20)

cedula = cedula%20
d = int(cedula//10)

cedula = cedula%10
e = int(cedula//5)

cedula = cedula%5
f = int(cedula//2)

g = int(cedula%2)


print(f'{a} nota(s) de R$ 100.00\n{b} nota(s) de R$ 50.00\n{c} nota(s) de R$ 20.00\n{d} nota(s) de R$ 10.00\n{e} nota(s) de R$ 5.00\n{f} nota(s) de R$ 2.00')
print("MOEDAS:")
cedula = (z - int(z))*100

h = int(cedula//50)

cedula = cedula%50
i = int(cedula//25)

cedula = cedula%25
j = int(cedula//10)

cedula = cedula%10
k = int(cedula//5)

l =  int(cedula%5)

print(f'{g} moeda(s) de R$ 1.00\n{h} moeda(s) de R$ 0.50\n{i} moeda(s) de R$ 0.25\n{j} moeda(s) de R$ 0.10\n{k} moeda(s) de R$ 0.05\n{l} moeda(s) de R$ 0.01')



