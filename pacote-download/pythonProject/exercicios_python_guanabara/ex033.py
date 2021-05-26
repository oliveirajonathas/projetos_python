#Faça um programa que leia três números e mostre qual é o maior e qual é o menor
n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo número: '))
n3 = float(input('Digite o terceiro número: '))

maior = n1
menor = n2

if maior<n2:
    menor = maior
    maior = n2
    if n1<n3:
        menor = n1
    else:
        menor = n2

if maior<n3:
     menor = maior
     maior = n3
     if n1 < n2:
         menor = n1
     else:
         menor = n2

print('Maior: {} e Menor: {}'.format(maior, menor))
