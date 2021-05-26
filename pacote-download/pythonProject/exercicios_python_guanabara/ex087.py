"""Aprimore o desafio anterior, mostrando no final:
a) A soma de todos os valores pares digitados
b) A soma dos valores da terceira coluna
c) O maior valor da segunda linha"""
matriz = list()
linhas = list()
for linha in range(0, 3):
    for coluna in range(0, 3):
        valor = int(input(f'Digite o da posição [{linha+1},{coluna+1}]: '))
        linhas.append(valor)
    matriz.append(linhas[:])
    linhas.clear()
print(30*'=-')

soma_par = 0
terc_col = 0
maior_valor = 0

for linha, valor in enumerate(matriz):
    for i in range(0, 3):
        print(f'[{valor[i]:^5}]', end='')
        if valor[i] % 2 == 0:
            soma_par += valor[i]
        if i == 2:  # Se estamos na TERCEIRA COLUNA
            terc_col += valor[i]
        if linha == 1:  # Se estamos na SEGUNDA LINHA
            if i == 0:
                maior_valor = valor[i]
            else:
                if valor[i] > maior_valor:
                    maior_valor = valor[i]
    print()
print(30*'=-')

print(f'A soma de todos os valores pares digitados foi {soma_par}.')
print(f'A soma dos elementos da TERCEIRA COLUNA foi {terc_col}.')
print(f'O MAIOR valor da SEGUNDA LINHA foi {maior_valor}.')
