def leiaint(msg='', min=-100, max=100):
    while True:
        valor = str(input(msg))
        if valor.isnumeric():
            valor = int(valor)
            if min <= valor <= max:
                break
            else:
                print('\033[1;31mERRO! Digite um valor válido.\033[m')
        else:
            print('\033[1;31mERRO! Digite um valor válido.\033[m')
    return valor
