"""
Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com
as seguintes informações:
- Quantidade de notas
- A maior nota
- A menor nota
- A média
- A situação (opcional)
Adicione também as docstrings da função
"""


def notas(*notas, sit=False):
    """
    Função para analisar as notas e situações de vários alunos.
    :param notas: uma ou mais notas dos alunos (aceita várias)
    :param sit: valor opcional, indicando se deve ou não adicionar a situação
    :return: dicionário com várias informações sobre a situação da turma
    """
    total = len(notas)
    maior = max(notas)
    menor = min(notas)
    media = sum(notas)/total
    balanco = {
        'total': total,
        'maior': maior,
        'menor': menor,
        'media': media,
    }
    if sit:
        if media < 7:
            balanco['situacao'] = 'RUIM'
        elif 7 <= media <= 9:
            balanco['situacao'] = 'BOA'
        elif media > 9:
            balanco['situacao'] = 'EXCELENTE'
    return balanco


print(notas(2.5, 2, 4, 5, 3, sit=True))
