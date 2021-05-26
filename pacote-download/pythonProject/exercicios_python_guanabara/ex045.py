"""
Crie um programa que faça o computador jogar Jokenpô com você
"""
from random import choice
import time

computador = int(choice(['1', '2', '3']))
usuario = int(input('Qual a sua jogada?\n'
                    '[1] Pedra\n'
                    '[2] Papel\n'
                    '[3] Tesoura\n'))
jogadas = ['Pedra', 'Papel', 'Tesoura']
if 1 <= usuario <= 3:
    print('JO...')
    time.sleep(1)
    print('KEN...')
    time.sleep(1)
    print('PÔ!!!')
    time.sleep(0.5)
    print(20 * '-=-')
    print('Eu joguei {}'.format(jogadas[computador-1]))
    print('Você jogou {}'.format(jogadas[usuario-1]))
    print(20 * '-=-')
    if computador == usuario:
        print('EMPATAMOS!!!')
    elif computador == 1 and usuario == 3:
        print('GANHEI!')
    elif computador == 1 and usuario == 2:
        print('VOCÊ GANHOU!')
    elif computador == 2 and usuario == 3:
        print('VOCÊ GANHOU!')
    elif computador == 2 and usuario == 1:
        print('GANHEI!')
    elif usuario == 1 and computador == 3:
        print('VOCÊ GANHOU')
    elif usuario == 2 and computador == 3:
        print('GANHEI!')
else:
    print('Opção Inválida! Tente novamente!')
