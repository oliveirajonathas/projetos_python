"""
Faça um programa que leia nome e média de um aluno, guardando também a situação desse aluno em um dicionário. No final,
mostre o conteúdo da estrutura na tela.
"""
sit_aluno = dict()
sit_aluno['NOME'] = str(input('Nome: '))
sit_aluno['MEDIA'] = float(input('Média: '))
if sit_aluno['MEDIA'] < 5:
    sit_aluno['SITUACAO'] = 'REPROVADO!'
elif 5 <= sit_aluno['MEDIA'] <= 7:
    sit_aluno['SITUACAO'] = 'RECUPERAÇÃO!'
else:
    sit_aluno['SITUACAO'] = 'APROVADO!'

for k, v in sit_aluno.items():
    print(f'{k} do aluno é: {v}')
