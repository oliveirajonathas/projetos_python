"""
Refaça o DESAFIO 051, lendo o primeiro termo e a razão
de uma PA, mostrando os 10 primeiros termos da progressão
usando a estrutura while
"""
atual = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))
print(atual, end='; ')
cont = 2

while cont <= 10:
    atual = atual + razao
    cont += 1
    print(atual, end='; ')
print('FIM')
