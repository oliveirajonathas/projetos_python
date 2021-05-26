import validacoes


def cabecalho(msg):
    tam = len(msg) + 20
    linha(msg)
    print(msg.center(tam))
    linha(msg)


def linha(msg):
    tam = len(msg) + 20
    print('-'*tam)


def menu(itens):
    for pos, val in enumerate(itens):
        print(f'\033[33m{pos + 1}\033[m - \033[34m{val}\033[m')
    opc = validacoes.leiainteiro('\033[32mSua Opção: \033[m', 1, 3)
    return opc
