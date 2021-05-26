def quadrado_por_valor(x):
    """
    Eleva x ao quadra, usando passagem por valor
    :param x:
    :return:
    """
    print(f'Recebido o valor {x}')
    x = x * x
    print(f'Devolvido o valor {x}')
    return x


def quadrado_por_ref(lista, x):
    """
    Recebe uma lista e um valor x. Eleva x ao quadrado, e armazena-o na lista, usando passagem por referência.
    :param lista:
    :param x:
    :return:
    """
    print(f'Rcebido o valor {x}')
    x = x * x
    lista.append(x)
    print(f'Devolvido o valor {x}')
    return x


dummy = 4
print(f'dummy vale {dummy}')
print('Elevando dummy ao quadrado:')
print('por valor:')
print(quadrado_por_valor(dummy))
print(f'Após a execução de quadrado_por_valor(dummy), dummy agora vale {dummy}')
print('por referência:')
l = []
print(quadrado_por_ref(l, dummy))
print(f'Após a execução de quadrado_por_ref(l, dummy), dummy agora vale {l[0]}')
