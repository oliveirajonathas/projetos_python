"""
Escreva um programa que leia um número n inteiro qualquer e mostre na tela os n primeiros elementos de
uma sequência de Fibonacci.
Ex.: 0 > 1 > 1 > 2 > 3 > 5 > 8
"""

print('-'*25)
print('Sequência de Fibonacci')
print('-'*25)

termos = int(input('Quantos termos deseja ver? '))

t1 = 0
t2 = 1
print(t1, '->', t2, '->', end='')
cont = 3

while cont <= termos:
    t3 = t1 + t2
    print(t3, '->', end='')
    t1 = t2
    t2 = t3
    cont += 1
print('FIM')
