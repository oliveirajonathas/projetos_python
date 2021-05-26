"""
Melhore o DESAFIO 061, perguntando para o usuário se ele quer
mostrar mais alguns termos. O programa encerra quando ele
disser que quer mostrar 0 termos
"""
atual = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))
print(atual, end='; ')
cont = 2

while cont <= 10:
    atual = atual + razao
    cont += 1
    print(atual, end='; ')

stop = 1
while stop != 0:
    print('\n')
    stop = int(input('Você gostaria de mostrar mais algum termo da PA? Se sim, digite a número de termos,'
                     ' se não, digite 0. Sua escolha: '))
    if stop != 0:
        for i in range(1, stop + 1):
            atual = atual + razao
            print(atual, end='; ')
print('FIM DO PROGRAMA')
