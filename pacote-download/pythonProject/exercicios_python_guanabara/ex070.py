"""
Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar.
No final, mostre:

a) Qual é o total gasto na compra
b) Quantos produtos custam mais de R$1000,00
c) Qual é o nome do produto mais barato
"""
print('-=-'*20)
print('MERCADINHO CALIFE')
print('-=-'*20)
total = 0
mais_mil = 0
mais_barato = ''
menor_valor = maior_valor = 0
item = 0

while True:
    produto = str(input('Nome do Produto: ')).strip()
    preco = float(input('Preço: R$'))

    item += 1
    total += preco

    if preco > 1000:
        mais_mil += 1

    if item == 1 or preco < menor_valor:
        menor_valor = preco
        mais_barato = produto

    print(30 * '-')

    continua = 'nada'
    while continua not in 'SN':
        continua = str(input('Registrar mais um produto? S/N: ')).strip().upper()[0]
    if continua == 'N':
        break
    print(30 * '-')
print(f'Total da compra R${total:.2f}')
print(f'Temos {mais_mil} produtos custando mais de R$1000,00')
print(f'O produto mais barato: {mais_barato}')
