"""Faça um programa que ajude um jogador da MEGA SENA a criar palpites. O programa vai perguntar quantos jogos serão
gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta"""
from random import randint
from time import sleep

loteria = list()
jogo = list()
cont = 0
while True:
    qtd = int(input('Deseja gerar quantos jogos? '))
    for i in range(0, qtd):
        while cont < 6:
            valor = randint(0, 10)
            if valor not in jogo:
                jogo.append(valor)
                cont += 1
        cont = 0
        loteria.append(jogo[:])
        jogo.clear()
    if len(loteria) == qtd:
        break
print('Calculando palpites: ')
sleep(1)
for pos, jogo in enumerate(loteria):
    print(f'Jogo {pos + 1}: {jogo}')
    sleep(1)
print('Concluído! VOLTE SEMPRE!')
