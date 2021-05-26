"""
Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.
"""
pesos = []
for i in range(1, 6):
    peso = float(input('Digite o {}º peso: '.format(i)))
    pesos.append(peso)
print('O menor peso lido foi {}Kg e o maior peso lido foi {}Kg'.format(min(pesos), max(pesos)))
