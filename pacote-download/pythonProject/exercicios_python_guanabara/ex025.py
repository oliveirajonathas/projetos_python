#Crie um programa que leia o nom de uma pessoa e diga se ela tem "SILVA" no nome

nome = str(input('Digite o seu nome: '))
nome = nome.upper().strip()
print('Um de seus nomes é SILVA: {}'.format('SILVA' in nome))
