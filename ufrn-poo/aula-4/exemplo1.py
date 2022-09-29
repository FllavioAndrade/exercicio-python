'''
Crie uma lista com números pares de 0 a 100 com o
comando range;
'''

n = range(0,101,2)
print(list(n))
print(len(n))


'''
Imprimir todos os pares de 1 a 10.000 usando o 
comando for;
'''

n = range(10001)
for i in n:
    if i%2 == 0:
        print(i)
'''
Crie um programa que acumula valores digitados pelo 
usuário. O usuário deve ter duas opções: 1 para digitar 
outro número ou 2 para o programa parar;
'''
valor = 1
qtd = 0

while valor == 1:
   valor  = int(input('Digite um valor: '))

