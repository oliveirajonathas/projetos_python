"""
Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular (largura e com-
primento) e mostre a área do terreno
"""


def calcular_area(comp, larg):
    area = comp * larg
    print(f'A área de seu terrno, de {comp}m X {larg}m é: {area:.2f} m²')


def titulo(msg):
    c = len(msg)
    print('-'*c)
    print(f'{msg:^{c}}')
    print('-'*c)


# Programa Principal
titulo('Controle de Terrenos')
comprimento = float(input('Digite o comprimento em metros: '))
largura = float(input('Digite a largura em metros: '))
calcular_area(comprimento, largura)
