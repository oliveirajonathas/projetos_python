def dobro(valor):
    resultado = 2 * valor
    return resultado


def metade(valor):
    resultado = valor/2
    return resultado


def aumentar(valor, taxa):
    resultado = valor * (1 + (taxa/100))
    return resultado


def diminuir(valor, taxa):
    resultado = valor * (1-(taxa/100))
    return resultado


def moeda(valor, moeda='R$'):
    resultado = f'{moeda}{valor:.2f}'.replace('.', ',')
    return resultado
