"""
Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando
um laço for
"""
print('-=-'*20)
print('Este programa mostra a tabuada do número que você escolher!')
print('-=-'*20)
numero = int(input('Digite o número: '))
print('-' * 15)
print('TABUADA DE {}'.format(numero))
print('-'*15)
for i in range(1, 11):
    print('{} x {} = {}'.format(numero, i, numero*i))
print('-'*15)
