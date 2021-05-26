def leiadinheiro():
    while True:
        valor = str(input('Digite o preço: R$')).replace(',', '.').strip()
        if valor.isalpha() or valor == '':
            print(f'\033[1;31mERRO! "{valor}" é um preço inválido!\033[m')
        else:
            break
    return float(valor)
