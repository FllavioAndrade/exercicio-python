'''
Escreva um programa que receba valores do usuário. Os valores devem ser
subtraídos do primeiro valor digitado e o programa só deve parar quando o valor
acumulado chegar ou passar de zero.
'''

valor = int(input('Digite um numero: '))
while valor >= 0:
    valor -= int(input('Digite um numero: '))
