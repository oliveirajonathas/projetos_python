"""Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre
um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente
obs: usar três níveis de lista (uma com tudo, uma com nomes e uma com notas)"""
materia = list()
aluno = list()
notas = list()

while True:
    nome = str(input('Nome: ')).strip().upper()
    nota1 = float(input('Nota 1: '))
    notas.append(nota1)
    nota2 = float(input('Nota 2: '))
    notas.append(nota2)
    media = (nota1 + nota2)/2
    aluno.append(nome)
    aluno.append(notas[:])
    aluno.append(media)
    materia.append(aluno[:])
    aluno.clear()
    notas.clear()

    while True:
        continua = str(input('Continua? [S/N]')).strip().upper()[0]
        if continua in 'SN':
            break
    if continua == 'N':
        break
print(20*'-')
print('{:^20}'.format('BOLETIM'))
print(20*'-')
print('NOME', 18*' ', 'MÉDIA')
for pos, item in enumerate(materia):
    print(f'{pos + 1:^4}{item[0]:.<22}{item[2]:2.1f}')
print(20*'-')

while True:
    mostrar = int(input('Deseja ver as notas de que aluno(a)? '))
    if mostrar > len(materia) or mostrar < 1 and mostrar != 999:
        print('Digite um valor válido!')
    else:
        print(f'As notas de {materia[mostrar-1][0]} foram: {materia[mostrar-1][1]}')
    if mostrar == 999:
        break

