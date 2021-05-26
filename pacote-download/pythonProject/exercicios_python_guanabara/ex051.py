"""
Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros
termos dessa progressão
"""
a1 = int(input('Informe o primeiro termo da PA: '))
razao = int(input('Informe a razão da PA: '))
for i in range(0, 10):
    an = a1 + i*razao
    print(an, end=' -> ')
