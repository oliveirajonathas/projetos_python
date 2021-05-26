"""Crie um programa que crie uma matriz de dimensão 3x3 e preencha com valores digitados no teclado. No final, mostre
a matriz na tela, com a formatação correta.
Formato da saída:
[1][2][3]
[4][5][6]
[7][8][9]"""

matriz = list()
linhas = list()
for linha in range(0, 3):
    for coluna in range(0, 3):
        valor = int(input(f'Digite o da posição [{linha+1},{coluna+1}]: '))
        linhas.append(valor)
    matriz.append(linhas[:])
    linhas.clear()
print(30*'=-')
for linha in matriz:
    for i in range(0, 3):
        print(f'[{linha[i]:^5}]', end='')
    print()
