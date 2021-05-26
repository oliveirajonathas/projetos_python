"""
Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados em um dicionário e todos os dicioná-
rios e uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas
B) A média de idade do grupo
C) Uma lista com todas as mulheres
D) Uma lista com todas as pessoas com idade acima da média
"""
grupo = list()
pessoa = dict()

while True:
    pessoa['Nome'] = str(input('Nome: ')).strip()
    while True:
        pessoa['Sexo'] = str(input('Sexo: [M/F]')).strip().upper()[0]
        if pessoa['Sexo'] in 'MF':
            break
        print('ERRO! Por favor, digite apenas M ou F')
    pessoa['Idade'] = int(input('Idade: '))
    grupo.append(pessoa.copy())
    continua = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if continua in 'N':
        break
print(30*'-=')
print(f'Foram cadastradas {len(grupo)} pessoas.')

tot_idade = 0
for p in grupo:
    tot_idade += p['Idade']
print(f'A média de idade do grupo é: {tot_idade/len(grupo):5.1f}')

mulheres = list()
for p in grupo:
    if p['Sexo'] == 'F':
        mulheres.append(p['Nome'])
print(f'As mulheres cadastradas no grupo foram: {mulheres}')

acima_media = list()
for p in grupo:
    if p['Idade'] > (tot_idade/len(grupo)):
        acima_media.append(p['Nome'])
print(f'As pessoas com idade acima da média são: {acima_media}')
