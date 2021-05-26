"""
Faça um programa que tenha uma função chamada contador(), que recebe três parâmetros: início, fim e passo e realize a
contagem.
Seu programa tem que realizar três contagens através da função criada:
a) De 1 até 10, de 1 em 1
b) De 10 até 0, de 2 em 2
c) Uma contagem personalizada
"""
from time import sleep


def contador(inicio, fim, passo):
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}: ')
    if passo == 0:
        passo = 1
    if inicio > fim:
        passo *= -1
        for i in range(inicio, fim - 1, passo):
            print(i, end=' ')
            sleep(0.3)
    else:
        for i in range(inicio, fim + 1, passo):
            print(i, end=' ')
            sleep(0.3)
    print('FIM!')
    print('-=' * 16)


# Programa principal
print('-=' * 16)
contador(1, 10, 1)
contador(10, 0, 2)
print('Agora é a sua vez de personalizar a contagem!')
start = int(input('Início: '))
stop = int(input('Fim: '))
while True:
    step = int(input('Passo (contagem crescente ou decrescente, use passo POSITIVO): '))
    if step < 0:
        print('O passo deve ser POSITIVO! Tente novamente!')
    else:
        break
print('-=' * 16)
contador(start, stop, step)
