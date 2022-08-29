'''
Leia um valor inteiro. A seguir, calcule o menor número de notas possíveis (cédulas) no qual o valor pode ser decomposto. As notas consideradas são de 100, 50, 20, 10, 5, 2 e 1. A seguir mostre o valor lido e a relação de notas necessárias.

Entrada
O arquivo de entrada contém um valor inteiro N (0 < N < 1000000).

Saída
Imprima o valor lido e, em seguida, a quantidade mínima de notas de cada tipo necessárias, conforme o exemplo fornecido. Não esqueça de imprimir o fim de linha após cada linha, caso contrário seu programa apresentará a mensagem: “Presentation Error”.

Exemplo de Entrada
576

Exemplo de Saída
5 nota(s) de R$ 100,00
1 nota(s) de R$ 50,00
1 nota(s) de R$ 20,00
0 nota(s) de R$ 10,00
1 nota(s) de R$ 5,00
0 nota(s) de R$ 2,00
1 nota(s) de R$ 1,00
'''
cedula = int(input())
a = int(cedula/100)
cedula = cedula%100
b = int(cedula/50)
cedula = cedula%50
c = int(cedula/20)
cedula = cedula%20
d = int(cedula/10)
cedula = cedula%10
e = int(cedula/5)
cedula = cedula%5
f = int(cedula/2)
g = cedula%2
print(f'{a} nota(s) de R$ 100,00\n{b} nota(s) de R$ 50,00\n{c} nota(s) de R$ 20,00\n{d} nota(s) de R$ 10,00\n{e} nota(s) de R$ 5,00\n{f} nota(s) de R$ 2,00\n{g} nota(s) de R$ 1,00\n')

