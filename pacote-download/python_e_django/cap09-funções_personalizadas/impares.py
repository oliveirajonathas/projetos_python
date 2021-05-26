def sao_impares(valores):
    resultado = True
    for num in valores:
        if num % 2 == 0:
            resultado = False
    return resultado


def sao_impares_lista(*lista):
    print(lista)
    resultado = True
    for num in lista:
        if num % 2 == 0:
            resultado = False
    return resultado


impares = [1, 3, 5, 7, 11]

print(sao_impares(impares))
print(sao_impares_lista(1, 3, 5, 1))
