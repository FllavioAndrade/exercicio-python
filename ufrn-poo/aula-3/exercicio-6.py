'''
Escreva um programa que pergunte o dia, mês e ano do aniversário de uma pessoa e
diga se a data é válida ou não. Caso não seja, diga o motivo. Suponha que todos os
meses tem 31 dias.
'''


import datetime
import calendar

qtd = 0
dia = int(input('digite o dia: '))
mes = int(input('digite o mes: '))
ano = int(input('digite o ano: '))

if  dia < 1 or dia > 31:
    print("DATA INVÁLIDA!\nO MÊS TÊM 31 DIAS")
    qtd += 1
if mes < 1 or mes > 12:
    print("DATA INVÁLIDA!\nO ANO TÊM 12 MESES")
    qtd += 1

if qtd == 0:
    print(f'A Data de seu aniversário é {dia}/{mes}/{ano}\n')

    print(calendar.month(ano, mes,dia))
