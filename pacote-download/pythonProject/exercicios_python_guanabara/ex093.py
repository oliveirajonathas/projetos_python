"""
Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e
quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guarda-
do em um dicionário, incluindo o total de gols feitos durante o campeonato.
"""
jogador = dict()
jogador['nome'] = str(input('Nome do Jogador: ')).strip()
partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
gols = list()
cont = 0
for i in range(0, partidas):
    gols.append(int(input(f'Quantos gols na partida {i}: ')))
    cont += gols[i]
jogador['gols'] = gols[:]
jogador['total'] = cont

print(30*'-=')
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')

print(30*'-=')
print(f'O jogador {jogador["nome"]} jogou {partidas} partidas')
for i in range(0, partidas):
    print(f'  => Na partida {i}, fez {gols[i]} gols')
print(f'Foi um total de {jogador["total"]} gols.')
