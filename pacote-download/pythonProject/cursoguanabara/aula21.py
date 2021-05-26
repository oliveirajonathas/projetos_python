#print(int.__doc__)
#help(input)

def contador(i, f, p):
    """
    Faz uma contagem e mostra na tela
    :param i: inicio da contagem
    :param f: fim da contagem
    :param p: passo da contagem
    :return: sem retorno
    Função criadar por AUTOR
    """
    c = i
    while c <= f:
        print(f'{c}', end=' ')
        c += p
    print('FIM!')

def somar(a, b, c=0):
    s = a + b + c
    print(f'A soma vale: {s}')


def teste(b):
    #global a
    a = 8
    b += 4
    c = 2
    print(f'A dentro vale {a}')
    print(f'B dentro vale {b}')
    print(f'C dentro vale {c}')


a = 20
teste(a)
print(f'A fora vale {a}')
