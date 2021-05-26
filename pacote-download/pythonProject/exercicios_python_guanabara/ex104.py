"""Crie um programa que tenha uma função leiaInt(), que vai funcionar de forma semelhante à função input() do Python, só
que fazendo a validação para aceitar apenas um valor numérico

Ex: n = leiaInt('Digite um n')"""


def leiaint():
    while True:
        valor = str(input('Digite um valor numérico: '))
        if valor.isnumeric():
            valor = int(valor)
            break
        else:
            print('\033[1;31mERRO! Digite um número inteiro válido.\033[m')
    return valor


numero = leiaint()
print(f'Você acabou de digitar o número {numero}')
