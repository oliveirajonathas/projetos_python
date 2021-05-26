"""
Crie um programa que leia dois valores e mostre um menu
na tela:
[1] somar
[2] multiplicar
[3] maior
[4] novos números
[5] sair do programa que
Seu programa deverá realizar a operação solicitada
em cada caso
"""
numero1 = float(input('Digite o primeiro valor: '))
numero2 = float(input('Digite o segundo valor: '))
print(20*'-=-')
opcao = int(input('O que deseja realizar?\n'
          '[1]somar\n'
          '[2]multiplicar\n'
          '[3]maior\n'
          '[4]novos número\n'
          '[5]sair do programa\n'
          'Sua opção: '))
print(20*'-=-')
while 1 <= opcao <= 5:

    if opcao == 1:
        print('A soma de {} + {} = {}'.format(numero1, numero2, numero1+numero2))
    elif opcao == 2:
        print('O produto {} x {} = {}'.format(numero1, numero2, numero1*numero2))
    elif opcao == 3:
        maior = numero1
        if numero2 > numero1:
            maior = numero2
            menor = numero1
        else:
            menor = numero2
        print('O numero {} é maior que o numero {}'.format(maior, menor))
    elif opcao == 4:
        numero1 = float(input('Digite o primeiro valor: '))
        numero2 = float(input('Digite o segundo valor: '))
    elif opcao == 5:
        break
    else:
        print('Opção inválida! Tente novamente!')
    print(20*'-=-')
    opcao = int(input('O que deseja fazer agora? '))
    print(20 * '-=-')
