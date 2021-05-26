"""
Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade) em um dicionário.
Se por acaso a CTPS for diferente de ZERO, o dicionário também receberá o ano de contratação e o salário. Calcule e
acrescente, além da idade, com quantos anos a pessoa vai se aposentar. Considere aposentadoria após 35 anos de contri-
buição idependente do sexo.
"""
from datetime import date
dados = dict()
dados['Nome'] = str(input('Nome: ')).strip()
dados['Idade'] = date.today().year - int(input('Ano de nascimento: '))
dados['CTPS'] = int(input('Número da CTPS. (0 se não tiver): '))
if dados['CTPS'] != 0:
    dados['Contratacao'] = int(input('Ano de Contratação: '))
    dados['Salario'] = float(input('Salário: R$'))
    dados['Aposentadoria'] = dados['Idade'] + (35 - (date.today().year - dados['Contratacao']))
print(30*'-=')
for k, v in dados.items():
    print(f'{k}: {v}')
