'''
Crie um programa que calcule os descontos em um salário. Considere 3% para o
sindicato e 10% de INSS. Indique o valor pago de FGTS pela empresa (11%), mas
esse valor não é descontado do salário, pois é a empresa que paga. Os descontos de
imposto de renda estão listados abaixo.
Salário Bruto ate R$900,00 (inclusive) – Isento;
Salário Bruto de R$ 1500, 00 (inclusive) – desconto de 5%;
Salario bruto até R$ 2500,00 (Inclusive) – desconto de 10%;
Salário bruto acima de 2500 – Desconto de 20%
O programa deve mostrar cada desconto, o total de descontos e o salário líquido.

'''

salario = float(input('Digite o valor de seu salário Bruto: '))

sindicato = salario*0.03
inss = salario * 0.1
fgts = salario* 0.11
impRenda = 0
if salario > 900 and salario <= 1500:
    impRenda = salario*0.05
elif salario > 1500 and salario <= 2500:
    impRenda = salario*0.1
elif salario > 2500:
    impRenda = salario * 0.2

print(f'DESCONTOS\nSINDICATO: {sindicato}\nINSS: {inss:.2f}\nFGTS: {fgts}\n\
IMPOSTO DE RENDA:{impRenda:.2f}\n\nSALÁRIO BRUTO: {salario:.2f}\n\
SALÁRIO LIQUIDO: {(salario-inss-impRenda-sindicato):.2f}')