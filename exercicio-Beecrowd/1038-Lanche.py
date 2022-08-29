'''
Com base na tabela abaixo, escreva um programa que leia o código de um item e a quantidade deste item. A seguir, calcule e mostre o valor da conta a pagar.

codigo        Especificacao             Preço
1             Cachorro Quente           R& 4.00
2             X-Salada                  R& 4.50
3             X-bacon                   R& 5.00
4             Torrada Simples           R& 2.00
5             Refrigerante              R& 1.50

Entrada
O arquivo de entrada contém dois valores inteiros correspondentes ao código e à quantidade de um item conforme tabela acima.

Saída
O arquivo de saída deve conter a mensagem "Total: R$ " seguido pelo valor a ser pago, com 2 casas após o ponto decimal.

Exemplo de Entrada
3 2

Exemplo de Saída
Total: R$ 10.00

Exemplo de Entrada
4 3

Exemplo de Saída
Total: R$ 6.00

'''

A, B,  = input().split()
A = int(A)
B = int(B)
preco = ["4.00", "4.50", "5.00", "2.00", "1.50"]
print(f'Total: R$ {(float(preco[A-1])*B):.2f}')