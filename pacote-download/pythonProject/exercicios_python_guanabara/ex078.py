"""
Faça um programa que leia 4 valores numéricos e guarde-os numa lista.
No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.
"""
valores = []
posicao_maior = []
posicao_menor = []
maior = menor = 0

for i in range(0, 5):
    valores.append(int(input(f'Digite o {i + 1}º valor: ')))
    if i == 0:
        maior = menor = valores[i]
    else:
        if valores[i] > maior:
            maior = valores[i]
        if valores[i] < menor:
            menor = valores[i]

for i in range(0, 5):
    if maior == valores[i]:
        posicao_maior.append(i)  # Lista que guarda as posições do maior valor
    if menor == valores[i]:
        posicao_menor.append(i)  # Lista que guarda as posições do menor valor

print(f'Você digitou os valores: {valores}')
print(f'O \033[1;34mMAIOR\033[m valor digitado é {maior} nas posições ', end='')
for valor in posicao_maior:
    print(f'{valor}... ', end='')
print(f'\nO \033[1;32mMENOR\033[m valor digitado é {menor} nas posições ', end='')
for valor in posicao_menor:
    print(f'{valor}... ', end='')
