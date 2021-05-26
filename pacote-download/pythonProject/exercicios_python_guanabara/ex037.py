"""
037) Escreva um programa que leia um número inteiro qualquer, e peça para o usuário escolher qual será a
base de conversão:
1 para binário
2 para octal
3 para hexadecimal
"""
num = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases para conversão:
[1] Converter para BINÁRIO
[2] Converter para OCTAL
[3] Converter para HEXADECIMAL''')
opcao = int(input('Sua opção: '))
if opcao == 1:
    binario = bin(num)
    print('{} convertido para BINÁRIO é igual a {}'.format(num, binario[2:]))
elif opcao == 2:
    octal = oct(num)
    print('{} convertido para OCTAL é igual a {}'.format(num, octal[2:]))
elif opcao == 3:
    hexadecimal = hex(num)
    print('{} convertido para HEXADECIMAL é igual a {}'.format(num, hexadecimal[2:]))
else:
    print('Opção inválida! Tente novamente!')
