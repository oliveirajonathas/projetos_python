"""
Faça um programa que leia um número inteiro e diga se ele é ou não um número primo
"""
cont = 0
numero = int(input('Que número você quer analisar? '))
divisores = []
for i in range(1, 10):
    if numero % i == 0:
        cont += 1
        divisores.append(i)
if cont > 2:
    print('O número {} é divisível por {} e \033[1;31mNÃO É PRIMO\033[m!'.format(numero, divisores))
else:
    print('O número {} é divisível por {} e \033[1;32mÉ PRIMO\033[m!'.format(numero, divisores))
