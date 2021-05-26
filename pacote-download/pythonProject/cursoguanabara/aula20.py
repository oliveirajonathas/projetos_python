def somar(a, b):
    s = a + b
    return s


def contador(*num):
        print(f'Recebi os valores {num}')
        print(f'São, ao todo, {len(num)} números.')


def dobrar(lista):
    pos = 0
    while pos < len(lista):
        lista[pos] *= 2
        pos += 1

#  Programa principal
somar(20, 4)
somar(8, 9)
somar(b=256, a=36)
x = somar(2, 0)
print(x)

contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)
contador(1)

valores = [2, 1, 6, 4]
print(valores)


