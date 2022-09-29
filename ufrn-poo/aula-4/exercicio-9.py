'''
Escreva um programa que receba valores do usuário. Os valores devem ser
subtraídos do primeiro valor digitado e o programa só deve parar quando o valor
acumulado chegar ou passar de zero.
'''

a = int(input('Digite um numero: '))
while True:
    valor = int(input('Digite um numero: '))
    if valor == a:
        break

