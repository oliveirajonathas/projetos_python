"""
Crie um programa que leia uma frase qualquer e diga se ela é um palindromo, desconsiderando os espaços
obs: palindromo é a frase que é igual lida normalmente ou de trás pra frente
ex:
APOS A SOPA
A SACADA DA CASA
A TORRE DA DERROTA
O LOBO AMA O BOLO
ANOTARAM A DATA DA MARATONA
"""
frase = str(input('Digite uma frase: ')).strip().upper()
frase_sem_espaco = frase.replace(' ', '')
tamanho = len(frase_sem_espaco)
frase_normal = []
frase_invertida = []

for i in range(0, tamanho):
    letra = frase_sem_espaco[i]
    frase_normal.append(letra)

for i in range(tamanho-1, -1, -1):
    letra = frase_sem_espaco[i]
    frase_invertida.append(letra)

if frase_normal == frase_invertida:
    print('A frase "{}" é um PALINDROMO'.format(frase))
else:
    print('A frase "{}" NÃO É um PALÍNDROMO'.format(frase))
