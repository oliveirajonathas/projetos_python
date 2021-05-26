def leiainteiro(msg, min=0, max=1000):
    """
    Valida se a entrada é um valor do tipo INTEIRO dentro de um RANGE. Por padrão, o range está entre 0 e 1000.
    :param min: parâmetro opcional, menor valor para a entrada
    :param max: parâmetro opcional, maior valor para a entrada
    :return: retorna o valor validado
    """
    while True:
        try:
            valor = int(input(msg))
        except ValueError:
            print('\033[1;31mERRO! Valor inválido!\033[m')
        else:
            if min <= valor <= max:
                break
            else:
                print('\033[1;31mERRO! Valor inválido!\033[m')
    return valor


def leiafloat(msg, min=0, max=1000):
    """
    Valida se a entrada é um valor do tipo FLOAT dentro de um RANGE. Por padrão, o range está entre 0 e 1000.
    :param min: parâmetro opcional, menor valor para a entrada
    :param max: parâmetro opcional, maior valor para a entrada
    :return: retorna o valor validado
    """
    while True:
        try:
            valor = float(input(msg))
        except ValueError:
            print('\033[1;31mERRO! Valor inválido!\033[m')
        else:
            if min <= valor <= max:
                break
            else:
                print('\033[1;31mERRO! Valor inválido!\033[m')
    return valor