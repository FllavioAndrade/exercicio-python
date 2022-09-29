'''
Crie um programa que receba dois números inteiros e positivos do usuário e calcule
o máximo divisor comum (MDC) e o mínimo múltiplo comum (MMC).
'''

def mdc(a, b):
    if b == 0:
        return a
    return mdc(b, a % b)


def mmc(a, b):
    return abs(a*b) / mdc(a, b)


a = int(input('Digite o primeiro numero: '))
b = int(input('Digite o segundo numero: '))
print(f"MMC {a} e {b} -->  {mmc(a, b)}")
print(f"MDC {a} e {b} -->  {mdc(a, b)}")
