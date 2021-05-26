"""
Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.
"""
from random import randint

aleatorios = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
print('Número sorteados: ', end='')

menor = maior = 0
for pos, numero in enumerate(aleatorios):
    print(numero, end=' ')
    if pos == 0:
        maior = menor = numero
    else:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero

print('')
print(f'O \033[1;32mMAIOR\033[m número sorteado foi {maior} e o \033[1;33mMENOR\033[m número sorteado foi {menor}')
print(f'O \033[1;32mMAIOR\033[m número sorteado foi {max(aleatorios)} e o \033[1;33mMENOR\033[m número sorteado foi '
      f'{min(aleatorios)}')
