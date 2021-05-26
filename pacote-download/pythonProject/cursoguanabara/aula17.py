'''
valores = []
valores.append(5)
valores.append(9)
valores.append(4)

for pos, v in enumerate(valores):
    print(f'Na posição {pos} encontrei o valor {v}!')
print('Cheguei ao final da lista')

for cont in range(0, 5):
    valores.append(int(input(f'Digite o {cont + 1}º valor: ')))

for pos, v in enumerate(valores):
    print(f'Na posição {pos} encontrei o valor {v}!')
print('Cheguei ao final da lista')
'''
a = [2, 3, 4, 7]
b = a[:]
a[2] = 20
print(f'Lista a: {a}')
print(f'Lista b: {b}')
