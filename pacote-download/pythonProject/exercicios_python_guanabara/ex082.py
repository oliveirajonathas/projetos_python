"""
Crie um programa que vai ler vários números e coloca em uma lista.
Depois disso, cire duas listas extras que vão conter apenas os valores PARES e os valores ÍMPARES digitados, respectiva-
mente. Ao final, mostre o conteúdo das três listas geradas.
"""
valores = []
while True:
    valores.append(int(input('Digite um número: ')))
    while True:
        continua = str(input('Quer continuar? S/N')).strip().upper()[0]
        if continua == 'S' or continua == 'N':
            break
    if continua in 'N':
        break
print(30*'-=')
print('Valores digitados: ')
for item in valores:
    print(f'{item}...', end='')
print()

pares = []
impares = []

for item in valores:
    if item % 2 == 0:
        pares.append(item)
    else:
        impares.append(item)

print('Valores pares: ')
for item in pares:
    print(f'{item}...', end='')

print()
print('Valores ímpares: ')
for item in impares:
    print(f'{item}...', end='')
