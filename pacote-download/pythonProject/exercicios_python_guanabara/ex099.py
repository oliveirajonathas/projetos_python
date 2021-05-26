"""
Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros.
Seu programa tem que analisar todos os valores e dizer qual deles é o maior
"""


def maior(*val):
    print(f'Foram passados os valores: {val[0]}')
    print(f'O maior valor é: {max(val[0])}')


valores = []
while True:
    valores.append(int(input('Digite um valor: ')))
    continua = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    while True:
        if continua not in 'NS':
            print('Opção inválida! Digite S ou N')
        else:
            break
    if continua == 'N':
        break

maior(valores)
