"""Faça um programa que leia o nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:

a) Quantas pessoas foram cadastradas
b) Uma listagem com as pessoas mais pesadas
c) Uma listagem com as pessoas mais leves"""

grupo = list()
pessoa = list()
while True:
    pessoa.append(str(input('Nome: ')))
    pessoa.append(float(input('Peso: ')))
    grupo.append(pessoa[:])
    pessoa.clear()
    while True:
        continua = str(input('Quer continuar? [S/N]')).strip().upper()[0]
        if continua in 'SN':
            break
    if continua in 'N':
        break
print(30*'-=')
print(f'Foram cadastradas {len(grupo)} pessoas')

maior_peso = menor_peso = 0
mais_pesada = list()
mais_leve = list()

#  Verificando qual foi o MAIOR e o MENOR pesos cadastrados
for i, p in enumerate(grupo):
    if i == 0:
        maior_peso = menor_peso = p[1]
    else:
        if p[1] > maior_peso:
            maior_peso = p[1]
        elif p[1] < menor_peso:
            menor_peso = p[1]

#  Identificando as pessoas MAIS e MENOS pesadas
for i, p in enumerate(grupo):
    if p[1] == maior_peso:
        mais_pesada.append(p[0])
    elif p[1] == menor_peso:
        mais_leve.append(p[0])

print(f'As pessoas mais pesadas, com {maior_peso}Kg, foram {mais_pesada}')
print(f'As pessoas mais leves, com {menor_peso}Kg, foram {mais_leve}')

