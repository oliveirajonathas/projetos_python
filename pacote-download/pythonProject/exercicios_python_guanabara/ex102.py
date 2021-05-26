"""
Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indica o número a calcular
e o outro chamado show, que será um valor lógico (opcional) indicando se será mostrado ou não na tela o processo de
cálculo do fatorial (por padrão, não deve mostrar)
"""


def fatorial(num, show=False):
    """
    Calcula o fatorial de um número
    :param num: O número cujo fatorial deve ser calculado
    :param show: (opcional) Mostrar ou não o cálculo
    :return: O valor do fatorial de um número num
    """
    fat = 1
    for i in range(num, 0, -1):
        fat *= i
        if show:
            print(i, end='')
            if i > 1:
                print(' X ', end='')
            else:
                print(' = ', end='')
    return fat


print(fatorial(5))
