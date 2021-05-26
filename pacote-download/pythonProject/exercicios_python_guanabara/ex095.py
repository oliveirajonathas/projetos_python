"""
Aprimore o desafio 093 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do
aproveitamento de cada jogador
"""
jogador = dict()
atletas = list()
while True:
    jogador['nome'] = str(input('Nome do Jogador: ')).strip()
    partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    gols = list()
    cont = 0
    for i in range(0, partidas):
        gols.append(int(input(f'Quantos gols na partida {i}: ')))
        cont += gols[i]
    jogador['gols'] = gols[:]
    jogador['total'] = cont
    continua = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    atletas.append(jogador.copy())
    if continua in 'N':
        break
print(30*'-=')
print('{:<4}{:<20}{:<20}{:<6}'.format('cod', 'nome', 'gols', 'total'))
print(60*'-')
for k, v in enumerate(atletas):
    print(f'{k:<4}{v["nome"]:<20}{str(v["gols"]):<20}{v["total"]:<6}')

while True:
    print('-'*60)
    mostrar = int(input('Mostrar dados de qual jogador? (999 para encerrar)'))
    if mostrar <= len(atletas):
        print(f'-- LEVANTAMENTO DO JOGADOR {atletas[mostrar]["nome"]}')
        for i in range(0, len(atletas[mostrar]['gols'])):
            print(f'No jogo {i} fez {atletas[mostrar]["gols"][i]} gols')
    else:
        print(f'O jogador {mostrar} não existe! Escolha uma opção válida!')
    if mostrar == 999:
        break
