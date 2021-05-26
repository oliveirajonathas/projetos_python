"""
Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando usuário digitar 999, que
é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando
o flag)
"""
print('+-'*20)
print('Contador e Somador de Números Inteiros')
print('+-'*20)

cont = soma = 0

while True:
    valor = int(input('Digite um valor (Para parar, 999): '))
    if valor == 999:
        break
    cont += 1
    soma += valor
print('-'*20)
print(f'Você digitou {cont} valores e a soma entre eles é {soma}')
print('-'*20)
print('FIM DO PROGRAMA')
