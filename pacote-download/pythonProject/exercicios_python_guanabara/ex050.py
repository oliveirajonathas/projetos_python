"""
Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares.
Se o valor digitado for ímpar, desconsidere-o
"""
soma = 0
cont = 0
for i in range(1, 7):
    numero = int(input('Digite o {}º número: '.format(i)))
    if numero % 2 == 0:
        soma += numero
        cont += 1
print('A soma dos {} \033[40mnúmeros pares\033[m digitados é: \033[1;32m{}\033[m'.format(cont, soma))
