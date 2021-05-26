"""
Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta
de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.
"""
lista = []
posicao = 0
cont_maior = 0
cont_menor = 0

for i in range(0, 5):
    valor = int(input('Digite um valor: '))

    if i == 0:
        lista.append(valor)

    print('Novo valor: ', valor)

    # Estrutura que verifica se o valor digitado é MAIOR ou MENOR que todos, ou se é INTERMEDIÁRIO.
    for item in lista:
        if valor > item:
            cont_maior += 1  # Conta quantas vezes o valor digitado foi maior que todos os itens da lista
        if valor < item:
            cont_menor += 1  # Conta quantas vezes o valor digitado foi menor que todos os itens da lista

    if cont_maior == len(lista):
        lista.append(valor)  # Acrescenta, ao FIM da lista, se o valor for maior que todos os itens
        cont_maior = 0
        print('Inserido ao fim da lista!')
    elif cont_menor == len(lista):
        lista.insert(0, valor)  # Acrescenta, no INÍCIO da lista, se o valor for menor que todos os itens
        cont_menor = 0
        print('Valor inserido no início da lista!')
    else:
        for i in range(0, len(lista)):
            if lista[i] <= valor <= lista[i+1]:
                posicao = i + 1
        lista.insert(posicao, valor)  # Acrescenta o valor entre outros dois valores
        print(f'Valor inserido entre {lista[posicao-1]} e {lista[posicao + 1]}.')

    #print('Lista atual: ', lista)
print(lista)
