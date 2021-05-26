"""
Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o nome de um jogador e
quantos gols ele marcou.

O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.
"""


def ficha(nome='', gols=0):
    if nome == '':
        nome = '<desconhecido>'
    print(f'O jogador {nome} marcou {gols} gols.')


def lergols():
    valor = input('Número de Gols: ')
    if valor == '':
        valor = 0
    else:
        int(valor)
    return valor


jogador = str(input('Nome do jogador: ')).strip()
gol = lergols()

ficha(jogador, gol)
