"""
Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a
ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.
OBS: Considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1
"""
titulo = 'Banco J&R'
print(20*'-=-')
print(f'{titulo:^60}')
print(20*'-=-')
while True:
    numero = int(input('Quanto deseja sacar? R$'))

    cinquenta = numero // 50
    resto_cinquenta = numero % 50

    vinte = resto_cinquenta // 20
    resto_vinte = numero % 20

    dez = resto_vinte // 10
    resto_dez = numero % 10

    print(f'''
    0{cinquenta} cédulas de R$50,00
    0{vinte} cédulas de R$20,00
    0{dez} cédulas de R$10,00
    0{resto_dez} cédulas de R$01,00  
           ''')
    print('''[1] Confirmar saque\n[2] Alterar valor? ''')

    saque = 0
    while saque < 1 or saque > 2:
        saque = int(input('Sua opção: '))

    if saque == 1:
        break
print('Pode retirar o seu dinheiro!')
