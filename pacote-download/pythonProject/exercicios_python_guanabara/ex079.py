"""
Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso a o número já
exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem cres-
cente.
"""
valores = []  # Poderia usar: valores = list()
while True:
    novo = int(input('Digite um valor: '))  # Entrada do teclado armazenada em novo
    if novo in valores:  # Verificando se o valor de novo já existe dentro da lista
        print('Valor já consta na lista! Não registrado!')  # Se existe, não registra e mostra a mensagem
    else:
        valores.append(novo)  # Se não existe, é adicionado à lista
        print('Adicionado com sucesso!')

    print('Deseja continuar? S/N')
    # Laço de verificação se o usuário deseja continuar acrescentando valores
    while True:
        continua = str(input('Sua opção: ')).strip().upper()
        if continua in 'SN':
            break
    if continua == 'N':
        break
valores.sort()  # Coloca os valores em ordem crescente
print(valores)
