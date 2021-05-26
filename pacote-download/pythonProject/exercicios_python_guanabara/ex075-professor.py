"""
Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
A) Quantas vezes apareceu o valor 9
B) Em que posição foi digitado o primeiro valor 3
C) Quais foram os números pares
"""

num = (int(input('Digite um número: ')), int(input('Digite outro número: ')),int(input('Digite mais um número: ')),
       int(input('Digite o último número: ')))

if 9 in num:
    print(f'O número 9 apareceu {num.count(9)} vezes!')
else:
    print('O número 9 não foi digitado!')

if 3 in num:
    print(f'O número três apareceu na {num.index(3) + 1} posição')
else:
    print('O número 3 não foi digitado!')

pares = 0
for n in num:
    if n % 2 == 0:
        pares += 1

if pares > 0:
    print('Os número PARES digitados foram: ', end='')
    for n in num:
        if n % 2 == 0:
            print(n, end=' ')
else:
    print('Não foram digitados valores pares!')
