"""
Faça um programa que tenha uma função chamada escreva(), que recebe um texto qualquer como parâmetro e mostre uma mensa-
gem com tamanho adaptável.
ex:
escreva('Olá, Mundo!')
saída:
----------
Olá Mundo!
----------
"""


def escreva(msg):
    tam = len(msg) + 5
    print('~'*tam)
    print(f'{msg:^{tam}}')
    print('~' * tam)


escreva('Olá, Mundo!')
escreva('Meu nome é Jonathas!!!')
