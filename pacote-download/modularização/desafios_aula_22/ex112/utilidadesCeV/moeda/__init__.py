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


def resumo(valor=0, taxa_a=10, taxa_r=5):
    titulo('RESUMO DO VALOR')
    print(f'Preço analisado:\t{moeda(valor)}')
    print(f'Metade do preço:\t{metade(valor)}')
    print(f'Dobro do preço:\t\t{dobro(valor)}')
    print(f'{taxa_a}% de aumento:\t\t{aumentar(valor, taxa_a)}')
    print(f'{taxa_r}% de redução:\t\t{diminuir(valor, taxa_r)}')
    print('-' * 30)


def titulo(msg):
    tan = len(msg)
    print((tan + 15) * '-')
    print(f'{msg}'.center(30))
    print((tan + 15) * '-')
    return tan

