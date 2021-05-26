"""
Faça um mini-sistema que utiliza o Inreractive Help do Python. O usuário vai digitar o comando, e o manual vai aparecer.
Quando o usuário digitar a palavra "FIM", o programa se encerrará.

OBS: use cores
"""
from time import sleep

cores = {
    'amarelo': '\033[43m',
    'azul': '\033[44m',
    'verde': '\033[42m',
    'vermelho': '\033[41m'
}

amarelo = cores['amarelo']
azul = cores['azul']
verde = cores['verde']
vermelho = cores['vermelho']


def titulo(msg, cor):
    print(f'{cor}', end='')
    print('~' * (len(msg) + 5))
    print(f'{msg:^{len(msg) + 5}}')
    print('~' * (len(msg) + 5))
    print('\033[m', end='')


def pyhelp():
    while True:
        titulo('SISTEMA DE AJUDA PyHELP', amarelo)
        funcionalidade = input('Função ou Biblioteca: ')
        if funcionalidade.upper() == 'FIM':
            titulo('ATÉ LOGO', vermelho)
            break
        titulo(f'Acessando o manual do comando {funcionalidade}', azul)
        sleep(1)
        print(f'{verde}', end='')
        help(funcionalidade)
        print('\033[m', end='')
        sleep(1)


pyhelp()
