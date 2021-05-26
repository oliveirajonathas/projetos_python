"""
Faça um programa que leia um número qualquer e mostre
o seu fatorial.
"""
numero = int(input('Digite um número inteiro: '))
n = 1
fatorial = 1
while n <= numero:
    fatorial = fatorial * n
    n += 1
print('{}! = {}'.format(numero, fatorial))

fatorial = 1
for i in range(1, numero+1):
    fatorial = fatorial * i
print('{}! = {}'.format(numero, fatorial))
