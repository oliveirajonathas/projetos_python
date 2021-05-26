"""
Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar().
A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre
todos os valores PARES sorteados pela função anterior.
"""
from random import randint
from time import sleep

def sorteia(lista):
    print('Sorteando 5 valores da lista: ', end='')
    for i in range(0, 5):
        lista.append(randint(1, 10))
    for item in lista:
        print(f'{item}', end=' ')
        sleep(0.5)
    print('PRONTO!')
    print(f'Foram sorteados os números: {lista}')


def soma(lista):
    soma_par = 0
    for item in lista:
        if item % 2 == 0:
            soma_par += item
    print(f'A soma dos valores PARES é? {soma_par}')


numeros = list()
sorteia(numeros)
soma(numeros)
