"""
Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
A) Quantas vezes apareceu o valor 9
B) Em que posição foi digitado o primeiro valor 3
C) Quais foram os números pares
"""
valor1 = int(input('Digite o primeiro valor: '))
valor2 = int(input('Digite o segundo valor: '))
valor3 = int(input('Digite o terceiro valor: '))
valor4 = int(input('Digite o quarto valor: '))

valores = (valor1, valor2, valor3, valor4)

# Contador de noves
cont = 0
for numero in valores:
    if numero == 9:
        cont += 1
if cont > 0:
    print(f'O número 9 apareceu {cont} vezes.')
else:
    print('Não foi digitado o valor 9.')

# Localizador e contador de três
cont = 0
for numero in valores:
    if numero == 3:
        cont += 1
if cont > 0:
    print(f'O primeiro valor 3 foi digitado na {valores.index(3) + 1}ª posição.')
else:
    print('Não foi digitado o valor 3.')

# Pares
cont = 0
for numero in valores:
    if numero % 2 == 0:
        cont += 1

if cont == 0:
    print('Não foram digitados valores PARES.')
else:
    print('Os valores PARES digitados foram: ', end='')
    for numero in valores:
        if numero % 2 == 0:
            print(numero, end=' ')
