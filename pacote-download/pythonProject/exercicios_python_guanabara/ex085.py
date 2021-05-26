"""Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única (duas listas
uma para pares e uma para ímpares, dentro da lista de valores), que mantenha separados os valores pares e ímpares.
No final, mostre os valores pares e ímpares em ordem crescente."""
pares = list()
impares = list()
valores = list()
for i in range(0, 7):
    valor = int(input(f'Digite o {i+1}º valor: '))
    if valor % 2 == 0:
        pares.append(valor)
    else:
        impares.append(valor)

valores.append(pares[:])
valores.append(impares[:])

print(f'Os valores \033[1;31mPARES\033[m digitados foram: {sorted(valores[0])}')
print(f'Os valores \033[1;32mÍMPARES\033[m digitados foram: {sorted(valores[1])}')
