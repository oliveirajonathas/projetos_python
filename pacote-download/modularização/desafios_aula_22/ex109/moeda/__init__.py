def dobro(valor, formatar=True):
    resultado = 2 * valor
    if formatar:
        resultado = moeda(resultado)
    return resultado


def metade(valor, formatar=True):
    resultado = valor/2
    if formatar:
        resultado = moeda(resultado)
    return resultado


def aumentar(valor, taxa, formatar=True):
    resultado = valor * (1 + (taxa/100))
    if formatar:
        resultado = moeda(resultado)
    return resultado


def diminuir(valor, taxa, formatar=True):
    resultado = valor * (1-(taxa/100))
    if formatar:
        resultado = moeda(resultado)
    return resultado


def moeda(valor, moeda='R$'):
    resultado = f'{moeda}{valor:.2f}'.replace('.', ',')
    return resultado
