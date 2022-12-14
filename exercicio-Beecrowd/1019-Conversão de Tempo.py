'''
Leia um valor inteiro, que é o tempo de duração em segundos de um determinado evento em uma fábrica, e informe-o expresso no formato horas:minutos:segundos.

Entrada
O arquivo de entrada contém um valor inteiro N.

Saída
Imprima o tempo lido no arquivo de entrada (segundos), convertido para horas:minutos:segundos, conforme exemplo fornecido.

Exemplo de Entrada
556

Exemplo de Saída
0:9:16

Exemplo de Entrada
140153

Exemplo de Saída
38:55:53

'''
hora = 0
segundos = int(input())
if segundos >= 3600:
    hora = segundos//3600
    segundos = segundos%3600
if segundos < 3600:
    minuto = segundos//60
    segundos = segundos%60

print(f'{hora}:{minuto}:{segundos}')