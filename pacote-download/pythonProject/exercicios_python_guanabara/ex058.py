"""
Melhore o jogo DESAFIO 028 onde o computador vai "pensar"
um número entre 0 e 10. Só que agora o jogador vai tentar
adivinhar até acertar, mostrando no final quantos palpites
foram necessários para vencer
"""
from random import randint
computador = randint(0, 10)
jogador = int(input('Adivinha em que número estou '
                    'pensando entre 0 e 10? '))
tentativa = 1
if computador == jogador:
    print('Parabéns! Você acertou de PRIMEIRA!')
else:
    while computador != jogador:
        tentativa += 1
        if jogador < computador:
            print('Mais! Tente novamente!')
        else:
            print('Menos! Tente novamente!')
        jogador = int(input('Seu novo palpite: '))
    print('Parabéns, finalmente você acertou depois de'
          ' {} tentativas!'.format(tentativa))
