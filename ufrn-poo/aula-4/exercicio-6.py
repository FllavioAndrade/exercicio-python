'''

Considere a função matemática 𝑓 = ((𝑥²+1)^(0.5))
2 + 1. Escreva um algoritmo que imprima
todos os valores dessa função no intervalo fechado de -100 até 100.

'''

for i in range(-100,100):
    print(((i**2)+1)**(1/2))
    