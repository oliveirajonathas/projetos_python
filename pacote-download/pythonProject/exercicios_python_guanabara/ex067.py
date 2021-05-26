"""
Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O pro-
grama será interrompido quando o número solicitado for negativo
"""
print('-=-'*10)
print('Tabuada')
print('-=-'*10)

while True:
    numero = int(input('Deseja ver a tabuada de que número: '))
    if numero < 0:
        break
    print('*' * 20)
    print(f'Tabuada de {numero}')
    print('*' * 20)
    for i in range(1, 11):
        print(f'{numero} x {i} = {numero*i}')
    print('*'*20)
print('Fim do programa')
