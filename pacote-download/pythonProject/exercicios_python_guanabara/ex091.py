"""
Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicioná-
rio. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.
obs.: o professor explica como colocar um dicionário em ordem na aula de exercício.
"""
from random import randint
from time import sleep
from operator import itemgetter

jogadas = list()
jogadores = dict()
print('Valores Sorteados:')
for i in range(1, 5):
    jogadores[f'jogador{i}'] = randint(1, 6)
for k, v in jogadores.items():
    print(f'O {k} tirou {v} no dado.')
    sleep(1)
print('*'*30)
print('RANKING DOS JOGADORES')

ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)

for i, v in enumerate(ranking):
    print(f'{i+1}º lugar: {v[0]} com {v[1]} pontos!')
    sleep(1)
