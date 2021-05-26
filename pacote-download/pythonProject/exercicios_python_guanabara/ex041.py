"""
041) A confederação nacional de natação precisa de um programa que leia o ano de nascimento de um atleta
e mostre sua categoria, de acordo com a idade:
- Até 9 anos: MIRIM
- Até 14 anos: INFANTIL
- Até 19 anos: JÚNIOR
- Até 25 anos: SÊNIOR
- Acima: MASTER
"""
from datetime import date
nascimento = int(input('Qual o ano de nascimento do(a) atleta? '))
ano_atual = date.today().year
idade = ano_atual - nascimento
print('O(A) Atleta tem {} anos!'.format(idade))
if idade <= 9:
    print('Categoria: MIRIM')
elif idade <= 14:
    print('Categoria: INFANTIL')
elif idade <= 19:
    print('Categoria: JÚNIOR')
elif idade <= 25:
    print('Categoria: SÊNIOR')
else:
    print('Categoria: MASTER')
