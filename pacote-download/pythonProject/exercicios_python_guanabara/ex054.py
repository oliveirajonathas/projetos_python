"""
Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas
ainda não atingiram a maioridade e quantos já são maiores (maioridade 21 anos)
"""
from datetime import date
menor = 0
maior = 0
for i in range(1, 8):
    ano = int(input('Digite o {}º ano de nascimento: '.format(i)))
    idade = date.today().year - ano
    if idade < 21:
        menor += 1
    else:
        maior += 1
print('São {} pessoas maiores e {} pessoas menores.'.format(maior, menor))
