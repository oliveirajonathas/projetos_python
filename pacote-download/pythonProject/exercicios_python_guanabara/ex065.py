"""
Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os
valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar
digitando valores.
"""
continua = 1
cont = soma = maior = menor = media = 0

while continua == 1:
    valor = int(input('Digite um valor: '))
    cont += 1
    soma += valor
    if cont == 1:
        maior = menor = valor
    else:
        if valor > maior:
            maior = valor
        if valor < menor:
            menor = valor
    continua = int(input('Deseja continuar?\n'
                         '[1] SIM\n'
                         '[2] NÃO\n'
                         'Sua resposta: '))
media = soma/cont
print('A média dos valores digitados é {}. O maior deles foi {} e o menor foi {}'.format(media, maior, menor))
