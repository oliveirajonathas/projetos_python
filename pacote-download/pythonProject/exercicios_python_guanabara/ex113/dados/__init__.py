def leiaint():
    while True:
        try:
            valor = int(input("Digite um valor inteiro: "))
        except (ValueError, TypeError, KeyboardInterrupt):
            print('\033[1;31mERRO: Você digitou um valor não válido! Tente novamente!\033[m')
        else:
            break
    return valor


def leiafloat():
    while True:
        try:
            valor = float(input("Digite um valor real: "))
        except ValueError:
            print('\033[1;31mERRO: Você digitou um valor não válido! Tente novamente!\033[m')
        except KeyboardInterrupt:
            print('\033[1;31mERRO: Você não digitou um valor. Tente novamente!\033[1m')
        else:
            break
    return valor